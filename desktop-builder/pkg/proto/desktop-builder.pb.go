// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.23.0
// 	protoc        v3.6.1
// source: pkg/proto/desktop-builder.proto

package proto

import (
	context "context"
	proto "github.com/golang/protobuf/proto"
	grpc "google.golang.org/grpc"
	codes "google.golang.org/grpc/codes"
	status "google.golang.org/grpc/status"
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

// This is a compile-time assertion that a sufficiently up-to-date version
// of the legacy proto package is being used.
const _ = proto.ProtoPackageIsVersion4

type XMLGetRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Id string `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
	// WARN: This is going to be removed in the future
	Template string `protobuf:"bytes,2,opt,name=template,proto3" json:"template,omitempty"`
}

func (x *XMLGetRequest) Reset() {
	*x = XMLGetRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_pkg_proto_desktop_builder_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *XMLGetRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*XMLGetRequest) ProtoMessage() {}

func (x *XMLGetRequest) ProtoReflect() protoreflect.Message {
	mi := &file_pkg_proto_desktop_builder_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use XMLGetRequest.ProtoReflect.Descriptor instead.
func (*XMLGetRequest) Descriptor() ([]byte, []int) {
	return file_pkg_proto_desktop_builder_proto_rawDescGZIP(), []int{0}
}

func (x *XMLGetRequest) GetId() string {
	if x != nil {
		return x.Id
	}
	return ""
}

func (x *XMLGetRequest) GetTemplate() string {
	if x != nil {
		return x.Template
	}
	return ""
}

type XMLGetResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Xml string `protobuf:"bytes,1,opt,name=xml,proto3" json:"xml,omitempty"`
}

func (x *XMLGetResponse) Reset() {
	*x = XMLGetResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_pkg_proto_desktop_builder_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *XMLGetResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*XMLGetResponse) ProtoMessage() {}

func (x *XMLGetResponse) ProtoReflect() protoreflect.Message {
	mi := &file_pkg_proto_desktop_builder_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use XMLGetResponse.ProtoReflect.Descriptor instead.
func (*XMLGetResponse) Descriptor() ([]byte, []int) {
	return file_pkg_proto_desktop_builder_proto_rawDescGZIP(), []int{1}
}

func (x *XMLGetResponse) GetXml() string {
	if x != nil {
		return x.Xml
	}
	return ""
}

type ViewerGetRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Xml string `protobuf:"bytes,1,opt,name=xml,proto3" json:"xml,omitempty"`
}

func (x *ViewerGetRequest) Reset() {
	*x = ViewerGetRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_pkg_proto_desktop_builder_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ViewerGetRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ViewerGetRequest) ProtoMessage() {}

func (x *ViewerGetRequest) ProtoReflect() protoreflect.Message {
	mi := &file_pkg_proto_desktop_builder_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ViewerGetRequest.ProtoReflect.Descriptor instead.
func (*ViewerGetRequest) Descriptor() ([]byte, []int) {
	return file_pkg_proto_desktop_builder_proto_rawDescGZIP(), []int{2}
}

func (x *ViewerGetRequest) GetXml() string {
	if x != nil {
		return x.Xml
	}
	return ""
}

type ViewerGetResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Spice []*ViewerGetResponse_Spice `protobuf:"bytes,2,rep,name=spice,proto3" json:"spice,omitempty"`
	Vnc   []*ViewerGetResponse_Vnc   `protobuf:"bytes,3,rep,name=vnc,proto3" json:"vnc,omitempty"`
}

func (x *ViewerGetResponse) Reset() {
	*x = ViewerGetResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_pkg_proto_desktop_builder_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ViewerGetResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ViewerGetResponse) ProtoMessage() {}

func (x *ViewerGetResponse) ProtoReflect() protoreflect.Message {
	mi := &file_pkg_proto_desktop_builder_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ViewerGetResponse.ProtoReflect.Descriptor instead.
func (*ViewerGetResponse) Descriptor() ([]byte, []int) {
	return file_pkg_proto_desktop_builder_proto_rawDescGZIP(), []int{3}
}

func (x *ViewerGetResponse) GetSpice() []*ViewerGetResponse_Spice {
	if x != nil {
		return x.Spice
	}
	return nil
}

func (x *ViewerGetResponse) GetVnc() []*ViewerGetResponse_Vnc {
	if x != nil {
		return x.Vnc
	}
	return nil
}

type ViewerGetResponse_Spice struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Pwd          string `protobuf:"bytes,1,opt,name=pwd,proto3" json:"pwd,omitempty"`
	SpicePort    int32  `protobuf:"varint,2,opt,name=spice_port,json=spicePort,proto3" json:"spice_port,omitempty"`
	SpiceTlsPort int32  `protobuf:"varint,3,opt,name=spice_tls_port,json=spiceTlsPort,proto3" json:"spice_tls_port,omitempty"`
}

func (x *ViewerGetResponse_Spice) Reset() {
	*x = ViewerGetResponse_Spice{}
	if protoimpl.UnsafeEnabled {
		mi := &file_pkg_proto_desktop_builder_proto_msgTypes[4]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ViewerGetResponse_Spice) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ViewerGetResponse_Spice) ProtoMessage() {}

func (x *ViewerGetResponse_Spice) ProtoReflect() protoreflect.Message {
	mi := &file_pkg_proto_desktop_builder_proto_msgTypes[4]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ViewerGetResponse_Spice.ProtoReflect.Descriptor instead.
func (*ViewerGetResponse_Spice) Descriptor() ([]byte, []int) {
	return file_pkg_proto_desktop_builder_proto_rawDescGZIP(), []int{3, 0}
}

func (x *ViewerGetResponse_Spice) GetPwd() string {
	if x != nil {
		return x.Pwd
	}
	return ""
}

func (x *ViewerGetResponse_Spice) GetSpicePort() int32 {
	if x != nil {
		return x.SpicePort
	}
	return 0
}

func (x *ViewerGetResponse_Spice) GetSpiceTlsPort() int32 {
	if x != nil {
		return x.SpiceTlsPort
	}
	return 0
}

type ViewerGetResponse_Vnc struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Pwd              string `protobuf:"bytes,1,opt,name=pwd,proto3" json:"pwd,omitempty"`
	VncPort          int32  `protobuf:"varint,2,opt,name=vnc_port,json=vncPort,proto3" json:"vnc_port,omitempty"`
	VncWebsocketPort int32  `protobuf:"varint,4,opt,name=vnc_websocket_port,json=vncWebsocketPort,proto3" json:"vnc_websocket_port,omitempty"`
}

func (x *ViewerGetResponse_Vnc) Reset() {
	*x = ViewerGetResponse_Vnc{}
	if protoimpl.UnsafeEnabled {
		mi := &file_pkg_proto_desktop_builder_proto_msgTypes[5]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ViewerGetResponse_Vnc) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ViewerGetResponse_Vnc) ProtoMessage() {}

func (x *ViewerGetResponse_Vnc) ProtoReflect() protoreflect.Message {
	mi := &file_pkg_proto_desktop_builder_proto_msgTypes[5]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ViewerGetResponse_Vnc.ProtoReflect.Descriptor instead.
func (*ViewerGetResponse_Vnc) Descriptor() ([]byte, []int) {
	return file_pkg_proto_desktop_builder_proto_rawDescGZIP(), []int{3, 1}
}

func (x *ViewerGetResponse_Vnc) GetPwd() string {
	if x != nil {
		return x.Pwd
	}
	return ""
}

func (x *ViewerGetResponse_Vnc) GetVncPort() int32 {
	if x != nil {
		return x.VncPort
	}
	return 0
}

func (x *ViewerGetResponse_Vnc) GetVncWebsocketPort() int32 {
	if x != nil {
		return x.VncWebsocketPort
	}
	return 0
}

var File_pkg_proto_desktop_builder_proto protoreflect.FileDescriptor

var file_pkg_proto_desktop_builder_proto_rawDesc = []byte{
	0x0a, 0x1f, 0x70, 0x6b, 0x67, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2f, 0x64, 0x65, 0x73, 0x6b,
	0x74, 0x6f, 0x70, 0x2d, 0x62, 0x75, 0x69, 0x6c, 0x64, 0x65, 0x72, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x12, 0x05, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0x3b, 0x0a, 0x0d, 0x58, 0x4d, 0x4c, 0x47,
	0x65, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x0e, 0x0a, 0x02, 0x69, 0x64, 0x18,
	0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x02, 0x69, 0x64, 0x12, 0x1a, 0x0a, 0x08, 0x74, 0x65, 0x6d,
	0x70, 0x6c, 0x61, 0x74, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x52, 0x08, 0x74, 0x65, 0x6d,
	0x70, 0x6c, 0x61, 0x74, 0x65, 0x22, 0x22, 0x0a, 0x0e, 0x58, 0x4d, 0x4c, 0x47, 0x65, 0x74, 0x52,
	0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x10, 0x0a, 0x03, 0x78, 0x6d, 0x6c, 0x18, 0x01,
	0x20, 0x01, 0x28, 0x09, 0x52, 0x03, 0x78, 0x6d, 0x6c, 0x22, 0x24, 0x0a, 0x10, 0x56, 0x69, 0x65,
	0x77, 0x65, 0x72, 0x47, 0x65, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x10, 0x0a,
	0x03, 0x78, 0x6d, 0x6c, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x03, 0x78, 0x6d, 0x6c, 0x22,
	0xbb, 0x02, 0x0a, 0x11, 0x56, 0x69, 0x65, 0x77, 0x65, 0x72, 0x47, 0x65, 0x74, 0x52, 0x65, 0x73,
	0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x34, 0x0a, 0x05, 0x73, 0x70, 0x69, 0x63, 0x65, 0x18, 0x02,
	0x20, 0x03, 0x28, 0x0b, 0x32, 0x1e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x56, 0x69, 0x65,
	0x77, 0x65, 0x72, 0x47, 0x65, 0x74, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x2e, 0x53,
	0x70, 0x69, 0x63, 0x65, 0x52, 0x05, 0x73, 0x70, 0x69, 0x63, 0x65, 0x12, 0x2e, 0x0a, 0x03, 0x76,
	0x6e, 0x63, 0x18, 0x03, 0x20, 0x03, 0x28, 0x0b, 0x32, 0x1c, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x2e, 0x56, 0x69, 0x65, 0x77, 0x65, 0x72, 0x47, 0x65, 0x74, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e,
	0x73, 0x65, 0x2e, 0x56, 0x6e, 0x63, 0x52, 0x03, 0x76, 0x6e, 0x63, 0x1a, 0x5e, 0x0a, 0x05, 0x53,
	0x70, 0x69, 0x63, 0x65, 0x12, 0x10, 0x0a, 0x03, 0x70, 0x77, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28,
	0x09, 0x52, 0x03, 0x70, 0x77, 0x64, 0x12, 0x1d, 0x0a, 0x0a, 0x73, 0x70, 0x69, 0x63, 0x65, 0x5f,
	0x70, 0x6f, 0x72, 0x74, 0x18, 0x02, 0x20, 0x01, 0x28, 0x05, 0x52, 0x09, 0x73, 0x70, 0x69, 0x63,
	0x65, 0x50, 0x6f, 0x72, 0x74, 0x12, 0x24, 0x0a, 0x0e, 0x73, 0x70, 0x69, 0x63, 0x65, 0x5f, 0x74,
	0x6c, 0x73, 0x5f, 0x70, 0x6f, 0x72, 0x74, 0x18, 0x03, 0x20, 0x01, 0x28, 0x05, 0x52, 0x0c, 0x73,
	0x70, 0x69, 0x63, 0x65, 0x54, 0x6c, 0x73, 0x50, 0x6f, 0x72, 0x74, 0x1a, 0x60, 0x0a, 0x03, 0x56,
	0x6e, 0x63, 0x12, 0x10, 0x0a, 0x03, 0x70, 0x77, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52,
	0x03, 0x70, 0x77, 0x64, 0x12, 0x19, 0x0a, 0x08, 0x76, 0x6e, 0x63, 0x5f, 0x70, 0x6f, 0x72, 0x74,
	0x18, 0x02, 0x20, 0x01, 0x28, 0x05, 0x52, 0x07, 0x76, 0x6e, 0x63, 0x50, 0x6f, 0x72, 0x74, 0x12,
	0x2c, 0x0a, 0x12, 0x76, 0x6e, 0x63, 0x5f, 0x77, 0x65, 0x62, 0x73, 0x6f, 0x63, 0x6b, 0x65, 0x74,
	0x5f, 0x70, 0x6f, 0x72, 0x74, 0x18, 0x04, 0x20, 0x01, 0x28, 0x05, 0x52, 0x10, 0x76, 0x6e, 0x63,
	0x57, 0x65, 0x62, 0x73, 0x6f, 0x63, 0x6b, 0x65, 0x74, 0x50, 0x6f, 0x72, 0x74, 0x32, 0x8b, 0x01,
	0x0a, 0x0e, 0x44, 0x65, 0x73, 0x6b, 0x74, 0x6f, 0x70, 0x42, 0x75, 0x69, 0x6c, 0x64, 0x65, 0x72,
	0x12, 0x37, 0x0a, 0x06, 0x58, 0x4d, 0x4c, 0x47, 0x65, 0x74, 0x12, 0x14, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x2e, 0x58, 0x4d, 0x4c, 0x47, 0x65, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74,
	0x1a, 0x15, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x58, 0x4d, 0x4c, 0x47, 0x65, 0x74, 0x52,
	0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x00, 0x12, 0x40, 0x0a, 0x09, 0x56, 0x69, 0x65,
	0x77, 0x65, 0x72, 0x47, 0x65, 0x74, 0x12, 0x17, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x56,
	0x69, 0x65, 0x77, 0x65, 0x72, 0x47, 0x65, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a,
	0x18, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x56, 0x69, 0x65, 0x77, 0x65, 0x72, 0x47, 0x65,
	0x74, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x00, 0x42, 0x36, 0x5a, 0x34, 0x67,
	0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f, 0x6d, 0x2f, 0x69, 0x73, 0x61, 0x72, 0x64, 0x2d,
	0x76, 0x64, 0x69, 0x2f, 0x69, 0x73, 0x61, 0x72, 0x64, 0x2f, 0x64, 0x65, 0x73, 0x6b, 0x74, 0x6f,
	0x70, 0x2d, 0x62, 0x75, 0x69, 0x6c, 0x64, 0x65, 0x72, 0x2f, 0x70, 0x6b, 0x67, 0x2f, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_pkg_proto_desktop_builder_proto_rawDescOnce sync.Once
	file_pkg_proto_desktop_builder_proto_rawDescData = file_pkg_proto_desktop_builder_proto_rawDesc
)

func file_pkg_proto_desktop_builder_proto_rawDescGZIP() []byte {
	file_pkg_proto_desktop_builder_proto_rawDescOnce.Do(func() {
		file_pkg_proto_desktop_builder_proto_rawDescData = protoimpl.X.CompressGZIP(file_pkg_proto_desktop_builder_proto_rawDescData)
	})
	return file_pkg_proto_desktop_builder_proto_rawDescData
}

var file_pkg_proto_desktop_builder_proto_msgTypes = make([]protoimpl.MessageInfo, 6)
var file_pkg_proto_desktop_builder_proto_goTypes = []interface{}{
	(*XMLGetRequest)(nil),           // 0: proto.XMLGetRequest
	(*XMLGetResponse)(nil),          // 1: proto.XMLGetResponse
	(*ViewerGetRequest)(nil),        // 2: proto.ViewerGetRequest
	(*ViewerGetResponse)(nil),       // 3: proto.ViewerGetResponse
	(*ViewerGetResponse_Spice)(nil), // 4: proto.ViewerGetResponse.Spice
	(*ViewerGetResponse_Vnc)(nil),   // 5: proto.ViewerGetResponse.Vnc
}
var file_pkg_proto_desktop_builder_proto_depIdxs = []int32{
	4, // 0: proto.ViewerGetResponse.spice:type_name -> proto.ViewerGetResponse.Spice
	5, // 1: proto.ViewerGetResponse.vnc:type_name -> proto.ViewerGetResponse.Vnc
	0, // 2: proto.DesktopBuilder.XMLGet:input_type -> proto.XMLGetRequest
	2, // 3: proto.DesktopBuilder.ViewerGet:input_type -> proto.ViewerGetRequest
	1, // 4: proto.DesktopBuilder.XMLGet:output_type -> proto.XMLGetResponse
	3, // 5: proto.DesktopBuilder.ViewerGet:output_type -> proto.ViewerGetResponse
	4, // [4:6] is the sub-list for method output_type
	2, // [2:4] is the sub-list for method input_type
	2, // [2:2] is the sub-list for extension type_name
	2, // [2:2] is the sub-list for extension extendee
	0, // [0:2] is the sub-list for field type_name
}

func init() { file_pkg_proto_desktop_builder_proto_init() }
func file_pkg_proto_desktop_builder_proto_init() {
	if File_pkg_proto_desktop_builder_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_pkg_proto_desktop_builder_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*XMLGetRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_pkg_proto_desktop_builder_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*XMLGetResponse); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_pkg_proto_desktop_builder_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ViewerGetRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_pkg_proto_desktop_builder_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ViewerGetResponse); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_pkg_proto_desktop_builder_proto_msgTypes[4].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ViewerGetResponse_Spice); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_pkg_proto_desktop_builder_proto_msgTypes[5].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ViewerGetResponse_Vnc); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_pkg_proto_desktop_builder_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   6,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_pkg_proto_desktop_builder_proto_goTypes,
		DependencyIndexes: file_pkg_proto_desktop_builder_proto_depIdxs,
		MessageInfos:      file_pkg_proto_desktop_builder_proto_msgTypes,
	}.Build()
	File_pkg_proto_desktop_builder_proto = out.File
	file_pkg_proto_desktop_builder_proto_rawDesc = nil
	file_pkg_proto_desktop_builder_proto_goTypes = nil
	file_pkg_proto_desktop_builder_proto_depIdxs = nil
}

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConnInterface

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion6

// DesktopBuilderClient is the client API for DesktopBuilder service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://godoc.org/google.golang.org/grpc#ClientConn.NewStream.
type DesktopBuilderClient interface {
	XMLGet(ctx context.Context, in *XMLGetRequest, opts ...grpc.CallOption) (*XMLGetResponse, error)
	ViewerGet(ctx context.Context, in *ViewerGetRequest, opts ...grpc.CallOption) (*ViewerGetResponse, error)
}

type desktopBuilderClient struct {
	cc grpc.ClientConnInterface
}

func NewDesktopBuilderClient(cc grpc.ClientConnInterface) DesktopBuilderClient {
	return &desktopBuilderClient{cc}
}

func (c *desktopBuilderClient) XMLGet(ctx context.Context, in *XMLGetRequest, opts ...grpc.CallOption) (*XMLGetResponse, error) {
	out := new(XMLGetResponse)
	err := c.cc.Invoke(ctx, "/proto.DesktopBuilder/XMLGet", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *desktopBuilderClient) ViewerGet(ctx context.Context, in *ViewerGetRequest, opts ...grpc.CallOption) (*ViewerGetResponse, error) {
	out := new(ViewerGetResponse)
	err := c.cc.Invoke(ctx, "/proto.DesktopBuilder/ViewerGet", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// DesktopBuilderServer is the server API for DesktopBuilder service.
type DesktopBuilderServer interface {
	XMLGet(context.Context, *XMLGetRequest) (*XMLGetResponse, error)
	ViewerGet(context.Context, *ViewerGetRequest) (*ViewerGetResponse, error)
}

// UnimplementedDesktopBuilderServer can be embedded to have forward compatible implementations.
type UnimplementedDesktopBuilderServer struct {
}

func (*UnimplementedDesktopBuilderServer) XMLGet(context.Context, *XMLGetRequest) (*XMLGetResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method XMLGet not implemented")
}
func (*UnimplementedDesktopBuilderServer) ViewerGet(context.Context, *ViewerGetRequest) (*ViewerGetResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method ViewerGet not implemented")
}

func RegisterDesktopBuilderServer(s *grpc.Server, srv DesktopBuilderServer) {
	s.RegisterService(&_DesktopBuilder_serviceDesc, srv)
}

func _DesktopBuilder_XMLGet_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(XMLGetRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DesktopBuilderServer).XMLGet(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/proto.DesktopBuilder/XMLGet",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DesktopBuilderServer).XMLGet(ctx, req.(*XMLGetRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _DesktopBuilder_ViewerGet_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(ViewerGetRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(DesktopBuilderServer).ViewerGet(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/proto.DesktopBuilder/ViewerGet",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(DesktopBuilderServer).ViewerGet(ctx, req.(*ViewerGetRequest))
	}
	return interceptor(ctx, in, info, handler)
}

var _DesktopBuilder_serviceDesc = grpc.ServiceDesc{
	ServiceName: "proto.DesktopBuilder",
	HandlerType: (*DesktopBuilderServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "XMLGet",
			Handler:    _DesktopBuilder_XMLGet_Handler,
		},
		{
			MethodName: "ViewerGet",
			Handler:    _DesktopBuilder_ViewerGet_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "pkg/proto/desktop-builder.proto",
}
