package grpc

import (
	"context"
	"errors"

	"github.com/isard-vdi/isard/common/pkg/grpc"
	"github.com/isard-vdi/isard/hyper/hyper"
	"github.com/isard-vdi/isard/hyper/pkg/proto"

	"google.golang.org/grpc/codes"
	"google.golang.org/grpc/status"
	"libvirt.org/libvirt-go"
)

func (h *HyperServer) DesktopStart(ctx context.Context, req *proto.DesktopStartRequest) (*proto.DesktopStartResponse, error) {
	if err := grpc.Required(grpc.RequiredParams{
		"xml": req.Xml,
	}); err != nil {
		return nil, err
	}

	desktop, err := h.hyper.Start(req.Xml, &hyper.StartOptions{})
	if err != nil {
		var e libvirt.Error
		if errors.As(err, &e) {
			switch e.Code {
			case libvirt.ERR_XML_ERROR:
				return nil, status.Errorf(codes.InvalidArgument, "start desktop: invalid XML: %s", e.Message)
			}
		}

		return nil, status.Errorf(codes.Unknown, "start desktop: %v", err)
	}
	defer desktop.Free()

	xml, err := h.hyper.XMLGet(desktop)
	if err != nil {
		return nil, status.Error(codes.Unknown, err.Error())
	}

	return &proto.DesktopStartResponse{
		Xml: xml,
	}, nil
}
