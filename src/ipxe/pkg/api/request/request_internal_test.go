/*
 * Copyright (C) 2019 Néfix Estrada <nefixestrada@gmail.com>
 * Author: Néfix Estrada <nefixestrada@gmail.com>
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU Affero General Public License as
 * published by the Free Software Foundation, either version 3 of the
 * License, or (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU Affero General Public License for more details.
 *
 * You should have received a copy of the GNU Affero General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

package request

import (
	"crypto/tls"
	"crypto/x509"
	"io/ioutil"
	"net/http"
	"os"
	"os/exec"
	"reflect"
	"testing"
)

func prepareCerts() error {
	if err := os.Mkdir("certs", 0755); err != nil {
		return err
	}

	cmd1 := exec.Command("openssl", "genrsa", "-des3", "-passout", "pass:qwerty", "-out", "certs/ca.key", "512")
	cmd2 := exec.Command("openssl", "rsa", "-passin", "pass:qwerty", "-in", "certs/ca.key", "-out", "certs/ca.key")
	// The file is written to cert/server-cert.pem to avoid having to create a configuration file
	cmd3 := exec.Command("openssl", "req", "-x509", "-new", "-nodes", "-key", "certs/ca.key", "-sha256", "-days", "1", "-out", "certs/server-cert.pem", "-subj", "/CN=isard.domain.com")

	if err := cmd1.Run(); err != nil {
		return err
	}

	if err := cmd2.Run(); err != nil {
		return err
	}

	if err := cmd3.Run(); err != nil {
		return err
	}

	return nil
}

func TestCreateClient(t *testing.T) {
	t.Run("should work as expected", func(t *testing.T) {
		if err := prepareCerts(); err != nil {
			t.Fatalf("error creating the certificates: %v", err)
		}

		caCert, err := ioutil.ReadFile("certs/server-cert.pem")
		if err != nil {
			t.Fatalf("error preparing the test: %v", err)
		}

		rootCAs := x509.NewCertPool()
		rootCAs.AppendCertsFromPEM(caCert)

		expectedRsp := &http.Client{
			Transport: &http.Transport{
				TLSClientConfig: &tls.Config{
					RootCAs: rootCAs,
				},
			},
		}

		client, err := createClient()
		if err != nil {
			t.Errorf("unexpected error: %v", err)
		}

		if !reflect.DeepEqual(client, expectedRsp) {
			t.Errorf("expecting %+v, but got %+v", expectedRsp, client)
		}

		if err := os.RemoveAll("./certs"); err != nil {
			t.Fatalf("error finishing the test: %v", err)
		}
	})

	t.Run("there was an error reading the configuration file", func(t *testing.T) {
		initialFolder, err := os.Getwd()
		if err != nil {
			t.Fatalf("error preparing the test %v", err)
		}

		err = os.Chdir("/")
		if err != nil {
			t.Fatalf("error preparing the test %v", err)
		}

		var expectedRsp *http.Client
		expectedErr := "open config.yml: permission denied"

		client, err := createClient()
		if err.Error() != expectedErr {
			t.Errorf("expecting %s, but got %v", expectedErr, err)
		}

		if !reflect.DeepEqual(client, expectedRsp) {
			t.Errorf("expecting %v, but got %v", expectedRsp, client)
		}

		err = os.Chdir(initialFolder)
		if err != nil {
			t.Fatalf("error finishing the test %v", err)
		}
	})

	t.Run("there was an error reading the CA certificate", func(t *testing.T) {
		var expectedRsp *http.Client
		expectedErr := "open ./certs/server-cert.pem: no such file or directory"

		client, err := createClient()
		if err.Error() != expectedErr {
			t.Errorf("expecting %s, but got %v", expectedErr, err)
		}

		if !reflect.DeepEqual(client, expectedRsp) {
			t.Errorf("expecting %v, but got %v", expectedRsp, client)
		}
	})

	// Clean the generated configuration file
	err := os.Remove("config.yml")
	if err != nil {
		t.Fatalf("error finishing the tests: %v", err)
	}
}
