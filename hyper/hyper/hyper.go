package hyper

import (
	"fmt"

	"github.com/isard-vdi/isard/hyper/env"

	"libvirt.org/libvirt-go"
)

type Interface interface {
	DesktopStart(xml string, paused bool) (string, error)
	DesktopStop(id string) error
	DesktopXMLGet(id string) (string, error)
	DesktopList() ([]libvirt.Domain, error)
	DesktopMigrateLive(id string, hypervisor string, bandwidth uint64)
	Close() error
}

type Hyper struct {
	env  *env.Env
	conn *libvirt.Connect
}

func New(env *env.Env, uri string) (*Hyper, error) {
	if uri == "" {
		uri = "qemu:///system"
	}

	conn, err := libvirt.NewConnect(uri)
	if err != nil {
		return nil, fmt.Errorf("connect to libvirt: %w", err)
	}

	return &Hyper{env, conn}, nil
}

func (h *Hyper) Close() error {
	_, err := h.conn.Close()
	return err
}
