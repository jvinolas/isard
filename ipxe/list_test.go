package isardipxe

import (
	"encoding/json"
	"errors"
	"fmt"
	"os"
	"reflect"
	"regexp"
	"testing"
)

type testWebRequest struct{}

func (testWebRequest) Get(url string) ([]byte, int, error) {
	return endpoints[url].Body, endpoints[url].Code, endpoints[url].Err
}

var endpoints map[string]endpointKey

type endpointKey struct {
	Body []byte
	Code int
	Err  error
}

var jsonEmptyList, _ = json.Marshal(&vmList{})

var listTests = []struct {
	list       *vmList
	validToken string
	endpoints  map[string]endpointKey
}{
	{
		list: &vmList{
			VMs: []*vm{
				&vm{
					ID:          "_nefix_KDE_Neon_5",
					Name:        "KDE Neon 5",
					Description: "This is a VM that's using KDE Neon 5",
				},
				&vm{
					ID:          "_nefix_Debian_9",
					Name:        "Debian 9",
					Description: "This is a VM that's using Debian 9",
				},
				&vm{
					ID:          "_nefix_Arch_Linux",
					Name:        "Arch Linux",
					Description: "This is a VM that's using Arch Linux",
				},
			},
		},
		validToken: "ShibAWD6OKjA8950vRIPUEZu848Ke0Rzp3Oxtye_V1c",
		endpoints: map[string]endpointKey{
			"https://isard.domain.com/pxe/list?tkn=ShibAWD6OKjA8950vRIPUEZu848Ke0Rzp3Oxtye_V1c": {
				Body: []byte(`{
					"vms": [
						{
							"id": "_nefix_KDE_Neon_5",
							"name": "KDE Neon 5",
							"description": "This is a VM that's using KDE Neon 5"
						},
						{
							"id": "_nefix_Debian_9",
							"name": "Debian 9",
							"description": "This is a VM that's using Debian 9"
						},
						{
							"id": "_nefix_Arch_Linux",
							"name": "Arch Linux",
							"description": "This is a VM that's using Arch Linux"
						}
					]
				}`),
				Code: 200,
				Err:  nil,
			},
			"https://isard.domain.com/pxe/list?tkn=error": {
				Body: jsonEmptyList,
				Err:  errors.New("testing error"),
			},
			"https://isard.domain.com/pxe/list?tkn=invalidtoken": {
				Body: jsonEmptyList,
				Code: 403,
				Err:  nil,
			},
			"https://isard.domain.com/pxe/list?tkn=invalidjson": {
				Body: []byte("not json!"),
				Code: 200,
				Err:  nil,
			},
		},
	},
}

func TestListVMs(t *testing.T) {
	for _, tt := range listTests {
		endpoints = tt.endpoints

		t.Run("returns the VMs list correctly", func(t *testing.T) {
			expectedRsp := tt.list

			vms, err := listVMs(testWebRequest{}, tt.validToken)
			if err != nil {
				t.Errorf("unexpected error: %v", err)
			}

			if !reflect.DeepEqual(vms, expectedRsp) {
				t.Errorf("expecting %s, but got %s", expectedRsp, vms)
			}
		})

		t.Run("there's an error reading the configuration", func(t *testing.T) {
			initialFolder, err := os.Getwd()
			if err != nil {
				t.Fatalf("error preparing the test %v", err)
			}

			err = os.Chdir("/")
			if err != nil {
				t.Fatalf("error preparing the test %v", err)
			}

			expectedRsp := &vmList{}
			expectedErr := "open config.yml: permission denied"

			vms, err := listVMs(testWebRequest{}, "this is a token")
			if err.Error() != expectedErr {
				t.Errorf("expecting %s, but got %v", expectedErr, err)
			}

			if !reflect.DeepEqual(vms, expectedRsp) {
				t.Errorf("expecting %s, but got %s", expectedRsp, vms)
			}

			err = os.Chdir(initialFolder)
			if err != nil {
				t.Fatalf("error finishing the test %v", err)
			}
		})

		t.Run("there's an error calling the API", func(t *testing.T) {
			expectedRsp := &vmList{}
			expectedErr := "testing error"

			vms, err := listVMs(testWebRequest{}, "error")
			if err.Error() != expectedErr {
				t.Errorf("expecting %s, but got %v", expectedErr, err)
			}

			if !reflect.DeepEqual(vms, expectedRsp) {
				t.Errorf("expecting %s, but got %s", expectedRsp, vms)
			}
		})

		t.Run("the code is not 200", func(t *testing.T) {
			expectedRsp := &vmList{}
			expectedErr := fmt.Sprintf("HTTP Code: %d", tt.endpoints["https://isard.domain.com/pxe/list?tkn=invalidtoken"].Code)

			vms, err := listVMs(testWebRequest{}, "invalidtoken")
			if err.Error() != expectedErr {
				t.Errorf("expecting %s, but got %v", expectedErr, err)
			}

			if !reflect.DeepEqual(vms, expectedRsp) {
				t.Errorf("expecting %s, but got %s", expectedRsp, vms)
			}
		})

		t.Run("error unmarshalling the response body", func(t *testing.T) {
			expectedRsp := &vmList{}
			expectedErr := "^invalid character '.' in literal null \\(expecting '.'\\)$"

			vms, err := listVMs(testWebRequest{}, "invalidjson")
			matched, rErr := regexp.MatchString(expectedErr, err.Error())
			if rErr != nil {
				t.Fatalf("error matching regex: %v", rErr)
			}

			if !matched {
				t.Errorf("expecting %s, but got %v", expectedErr, err)
			}

			if !reflect.DeepEqual(vms, expectedRsp) {
				t.Errorf("expecting %v, but got %v", expectedRsp, vms)
			}
		})
	}
}
