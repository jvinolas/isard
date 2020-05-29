// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.23.0
// 	protoc        v3.6.1
// source: pkg/proto/hyper.proto

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

type DesktopStartRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Xml string `protobuf:"bytes,1,opt,name=xml,proto3" json:"xml,omitempty"`
}

func (x *DesktopStartRequest) Reset() {
	*x = DesktopStartRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_pkg_proto_hyper_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *DesktopStartRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*DesktopStartRequest) ProtoMessage() {}

func (x *DesktopStartRequest) ProtoReflect() protoreflect.Message {
	mi := &file_pkg_proto_hyper_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use DesktopStartRequest.ProtoReflect.Descriptor instead.
func (*DesktopStartRequest) Descriptor() ([]byte, []int) {
	return file_pkg_proto_hyper_proto_rawDescGZIP(), []int{0}
}

func (x *DesktopStartRequest) GetXml() string {
	if x != nil {
		return x.Xml
	}
	return ""
}

type DesktopStartResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Xml string `protobuf:"bytes,1,opt,name=xml,proto3" json:"xml,omitempty"`
}

func (x *DesktopStartResponse) Reset() {
	*x = DesktopStartResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_pkg_proto_hyper_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *DesktopStartResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*DesktopStartResponse) ProtoMessage() {}

func (x *DesktopStartResponse) ProtoReflect() protoreflect.Message {
	mi := &file_pkg_proto_hyper_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use DesktopStartResponse.ProtoReflect.Descriptor instead.
func (*DesktopStartResponse) Descriptor() ([]byte, []int) {
	return file_pkg_proto_hyper_proto_rawDescGZIP(), []int{1}
}

func (x *DesktopStartResponse) GetXml() string {
	if x != nil {
		return x.Xml
	}
	return ""
}

type DesktopStopRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Id string `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
}

func (x *DesktopStopRequest) Reset() {
	*x = DesktopStopRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_pkg_proto_hyper_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *DesktopStopRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*DesktopStopRequest) ProtoMessage() {}

func (x *DesktopStopRequest) ProtoReflect() protoreflect.Message {
	mi := &file_pkg_proto_hyper_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use DesktopStopRequest.ProtoReflect.Descriptor instead.
func (*DesktopStopRequest) Descriptor() ([]byte, []int) {
	return file_pkg_proto_hyper_proto_rawDescGZIP(), []int{2}
}

func (x *DesktopStopRequest) GetId() string {
	if x != nil {
		return x.Id
	}
	return ""
}

type DesktopStopResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields
}

func (x *DesktopStopResponse) Reset() {
	*x = DesktopStopResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_pkg_proto_hyper_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *DesktopStopResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*DesktopStopResponse) ProtoMessage() {}

func (x *DesktopStopResponse) ProtoReflect() protoreflect.Message {
	mi := &file_pkg_proto_hyper_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use DesktopStopResponse.ProtoReflect.Descriptor instead.
func (*DesktopStopResponse) Descriptor() ([]byte, []int) {
	return file_pkg_proto_hyper_proto_rawDescGZIP(), []int{3}
}

type DesktopListRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields
}

func (x *DesktopListRequest) Reset() {
	*x = DesktopListRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_pkg_proto_hyper_proto_msgTypes[4]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *DesktopListRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*DesktopListRequest) ProtoMessage() {}

func (x *DesktopListRequest) ProtoReflect() protoreflect.Message {
	mi := &file_pkg_proto_hyper_proto_msgTypes[4]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use DesktopListRequest.ProtoReflect.Descriptor instead.
func (*DesktopListRequest) Descriptor() ([]byte, []int) {
	return file_pkg_proto_hyper_proto_rawDescGZIP(), []int{4}
}

type DesktopListResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Ids []string `protobuf:"bytes,1,rep,name=ids,proto3" json:"ids,omitempty"`
}

func (x *DesktopListResponse) Reset() {
	*x = DesktopListResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_pkg_proto_hyper_proto_msgTypes[5]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *DesktopListResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*DesktopListResponse) ProtoMessage() {}

func (x *DesktopListResponse) ProtoReflect() protoreflect.Message {
	mi := &file_pkg_proto_hyper_proto_msgTypes[5]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use DesktopListResponse.ProtoReflect.Descriptor instead.
func (*DesktopListResponse) Descriptor() ([]byte, []int) {
	return file_pkg_proto_hyper_proto_rawDescGZIP(), []int{5}
}

func (x *DesktopListResponse) GetIds() []string {
	if x != nil {
		return x.Ids
	}
	return nil
}

type DesktopXMLGetRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Id string `protobuf:"bytes,1,opt,name=id,proto3" json:"id,omitempty"`
}

func (x *DesktopXMLGetRequest) Reset() {
	*x = DesktopXMLGetRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_pkg_proto_hyper_proto_msgTypes[6]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *DesktopXMLGetRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*DesktopXMLGetRequest) ProtoMessage() {}

func (x *DesktopXMLGetRequest) ProtoReflect() protoreflect.Message {
	mi := &file_pkg_proto_hyper_proto_msgTypes[6]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use DesktopXMLGetRequest.ProtoReflect.Descriptor instead.
func (*DesktopXMLGetRequest) Descriptor() ([]byte, []int) {
	return file_pkg_proto_hyper_proto_rawDescGZIP(), []int{6}
}

func (x *DesktopXMLGetRequest) GetId() string {
	if x != nil {
		return x.Id
	}
	return ""
}

type DesktopXMLGetResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Xml string `protobuf:"bytes,1,opt,name=xml,proto3" json:"xml,omitempty"`
}

func (x *DesktopXMLGetResponse) Reset() {
	*x = DesktopXMLGetResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_pkg_proto_hyper_proto_msgTypes[7]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *DesktopXMLGetResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*DesktopXMLGetResponse) ProtoMessage() {}

func (x *DesktopXMLGetResponse) ProtoReflect() protoreflect.Message {
	mi := &file_pkg_proto_hyper_proto_msgTypes[7]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use DesktopXMLGetResponse.ProtoReflect.Descriptor instead.
func (*DesktopXMLGetResponse) Descriptor() ([]byte, []int) {
	return file_pkg_proto_hyper_proto_rawDescGZIP(), []int{7}
}

func (x *DesktopXMLGetResponse) GetXml() string {
	if x != nil {
		return x.Xml
	}
	return ""
}

var File_pkg_proto_hyper_proto protoreflect.FileDescriptor

var file_pkg_proto_hyper_proto_rawDesc = []byte{
	0x0a, 0x15, 0x70, 0x6b, 0x67, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2f, 0x68, 0x79, 0x70, 0x65,
	0x72, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x05, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x22, 0x27,
	0x0a, 0x13, 0x44, 0x65, 0x73, 0x6b, 0x74, 0x6f, 0x70, 0x53, 0x74, 0x61, 0x72, 0x74, 0x52, 0x65,
	0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x10, 0x0a, 0x03, 0x78, 0x6d, 0x6c, 0x18, 0x01, 0x20, 0x01,
	0x28, 0x09, 0x52, 0x03, 0x78, 0x6d, 0x6c, 0x22, 0x28, 0x0a, 0x14, 0x44, 0x65, 0x73, 0x6b, 0x74,
	0x6f, 0x70, 0x53, 0x74, 0x61, 0x72, 0x74, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12,
	0x10, 0x0a, 0x03, 0x78, 0x6d, 0x6c, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x03, 0x78, 0x6d,
	0x6c, 0x22, 0x24, 0x0a, 0x12, 0x44, 0x65, 0x73, 0x6b, 0x74, 0x6f, 0x70, 0x53, 0x74, 0x6f, 0x70,
	0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x0e, 0x0a, 0x02, 0x69, 0x64, 0x18, 0x01, 0x20,
	0x01, 0x28, 0x09, 0x52, 0x02, 0x69, 0x64, 0x22, 0x15, 0x0a, 0x13, 0x44, 0x65, 0x73, 0x6b, 0x74,
	0x6f, 0x70, 0x53, 0x74, 0x6f, 0x70, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x14,
	0x0a, 0x12, 0x44, 0x65, 0x73, 0x6b, 0x74, 0x6f, 0x70, 0x4c, 0x69, 0x73, 0x74, 0x52, 0x65, 0x71,
	0x75, 0x65, 0x73, 0x74, 0x22, 0x27, 0x0a, 0x13, 0x44, 0x65, 0x73, 0x6b, 0x74, 0x6f, 0x70, 0x4c,
	0x69, 0x73, 0x74, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x10, 0x0a, 0x03, 0x69,
	0x64, 0x73, 0x18, 0x01, 0x20, 0x03, 0x28, 0x09, 0x52, 0x03, 0x69, 0x64, 0x73, 0x22, 0x26, 0x0a,
	0x14, 0x44, 0x65, 0x73, 0x6b, 0x74, 0x6f, 0x70, 0x58, 0x4d, 0x4c, 0x47, 0x65, 0x74, 0x52, 0x65,
	0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x0e, 0x0a, 0x02, 0x69, 0x64, 0x18, 0x01, 0x20, 0x01, 0x28,
	0x09, 0x52, 0x02, 0x69, 0x64, 0x22, 0x29, 0x0a, 0x15, 0x44, 0x65, 0x73, 0x6b, 0x74, 0x6f, 0x70,
	0x58, 0x4d, 0x4c, 0x47, 0x65, 0x74, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x10,
	0x0a, 0x03, 0x78, 0x6d, 0x6c, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x52, 0x03, 0x78, 0x6d, 0x6c,
	0x32, 0xb0, 0x02, 0x0a, 0x05, 0x48, 0x79, 0x70, 0x65, 0x72, 0x12, 0x49, 0x0a, 0x0c, 0x44, 0x65,
	0x73, 0x6b, 0x74, 0x6f, 0x70, 0x53, 0x74, 0x61, 0x72, 0x74, 0x12, 0x1a, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x2e, 0x44, 0x65, 0x73, 0x6b, 0x74, 0x6f, 0x70, 0x53, 0x74, 0x61, 0x72, 0x74, 0x52,
	0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x1b, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x44,
	0x65, 0x73, 0x6b, 0x74, 0x6f, 0x70, 0x53, 0x74, 0x61, 0x72, 0x74, 0x52, 0x65, 0x73, 0x70, 0x6f,
	0x6e, 0x73, 0x65, 0x22, 0x00, 0x12, 0x46, 0x0a, 0x0b, 0x44, 0x65, 0x73, 0x6b, 0x74, 0x6f, 0x70,
	0x53, 0x74, 0x6f, 0x70, 0x12, 0x19, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x44, 0x65, 0x73,
	0x6b, 0x74, 0x6f, 0x70, 0x53, 0x74, 0x6f, 0x70, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a,
	0x1a, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x44, 0x65, 0x73, 0x6b, 0x74, 0x6f, 0x70, 0x53,
	0x74, 0x6f, 0x70, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x22, 0x00, 0x12, 0x46, 0x0a,
	0x0b, 0x44, 0x65, 0x73, 0x6b, 0x74, 0x6f, 0x70, 0x4c, 0x69, 0x73, 0x74, 0x12, 0x19, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x44, 0x65, 0x73, 0x6b, 0x74, 0x6f, 0x70, 0x4c, 0x69, 0x73, 0x74,
	0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x1a, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2e,
	0x44, 0x65, 0x73, 0x6b, 0x74, 0x6f, 0x70, 0x4c, 0x69, 0x73, 0x74, 0x52, 0x65, 0x73, 0x70, 0x6f,
	0x6e, 0x73, 0x65, 0x22, 0x00, 0x12, 0x4c, 0x0a, 0x0d, 0x44, 0x65, 0x73, 0x6b, 0x74, 0x6f, 0x70,
	0x58, 0x4d, 0x4c, 0x47, 0x65, 0x74, 0x12, 0x1b, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x44,
	0x65, 0x73, 0x6b, 0x74, 0x6f, 0x70, 0x58, 0x4d, 0x4c, 0x47, 0x65, 0x74, 0x52, 0x65, 0x71, 0x75,
	0x65, 0x73, 0x74, 0x1a, 0x1c, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x44, 0x65, 0x73, 0x6b,
	0x74, 0x6f, 0x70, 0x58, 0x4d, 0x4c, 0x47, 0x65, 0x74, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73,
	0x65, 0x22, 0x00, 0x42, 0x2c, 0x5a, 0x2a, 0x67, 0x69, 0x74, 0x68, 0x75, 0x62, 0x2e, 0x63, 0x6f,
	0x6d, 0x2f, 0x69, 0x73, 0x61, 0x72, 0x64, 0x2d, 0x76, 0x64, 0x69, 0x2f, 0x69, 0x73, 0x61, 0x72,
	0x64, 0x2f, 0x68, 0x79, 0x70, 0x65, 0x72, 0x2f, 0x70, 0x6b, 0x67, 0x2f, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_pkg_proto_hyper_proto_rawDescOnce sync.Once
	file_pkg_proto_hyper_proto_rawDescData = file_pkg_proto_hyper_proto_rawDesc
)

func file_pkg_proto_hyper_proto_rawDescGZIP() []byte {
	file_pkg_proto_hyper_proto_rawDescOnce.Do(func() {
		file_pkg_proto_hyper_proto_rawDescData = protoimpl.X.CompressGZIP(file_pkg_proto_hyper_proto_rawDescData)
	})
	return file_pkg_proto_hyper_proto_rawDescData
}

var file_pkg_proto_hyper_proto_msgTypes = make([]protoimpl.MessageInfo, 8)
var file_pkg_proto_hyper_proto_goTypes = []interface{}{
	(*DesktopStartRequest)(nil),   // 0: proto.DesktopStartRequest
	(*DesktopStartResponse)(nil),  // 1: proto.DesktopStartResponse
	(*DesktopStopRequest)(nil),    // 2: proto.DesktopStopRequest
	(*DesktopStopResponse)(nil),   // 3: proto.DesktopStopResponse
	(*DesktopListRequest)(nil),    // 4: proto.DesktopListRequest
	(*DesktopListResponse)(nil),   // 5: proto.DesktopListResponse
	(*DesktopXMLGetRequest)(nil),  // 6: proto.DesktopXMLGetRequest
	(*DesktopXMLGetResponse)(nil), // 7: proto.DesktopXMLGetResponse
}
var file_pkg_proto_hyper_proto_depIdxs = []int32{
	0, // 0: proto.Hyper.DesktopStart:input_type -> proto.DesktopStartRequest
	2, // 1: proto.Hyper.DesktopStop:input_type -> proto.DesktopStopRequest
	4, // 2: proto.Hyper.DesktopList:input_type -> proto.DesktopListRequest
	6, // 3: proto.Hyper.DesktopXMLGet:input_type -> proto.DesktopXMLGetRequest
	1, // 4: proto.Hyper.DesktopStart:output_type -> proto.DesktopStartResponse
	3, // 5: proto.Hyper.DesktopStop:output_type -> proto.DesktopStopResponse
	5, // 6: proto.Hyper.DesktopList:output_type -> proto.DesktopListResponse
	7, // 7: proto.Hyper.DesktopXMLGet:output_type -> proto.DesktopXMLGetResponse
	4, // [4:8] is the sub-list for method output_type
	0, // [0:4] is the sub-list for method input_type
	0, // [0:0] is the sub-list for extension type_name
	0, // [0:0] is the sub-list for extension extendee
	0, // [0:0] is the sub-list for field type_name
}

func init() { file_pkg_proto_hyper_proto_init() }
func file_pkg_proto_hyper_proto_init() {
	if File_pkg_proto_hyper_proto != nil {
		return
	}
	if !protoimpl.UnsafeEnabled {
		file_pkg_proto_hyper_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*DesktopStartRequest); i {
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
		file_pkg_proto_hyper_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*DesktopStartResponse); i {
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
		file_pkg_proto_hyper_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*DesktopStopRequest); i {
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
		file_pkg_proto_hyper_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*DesktopStopResponse); i {
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
		file_pkg_proto_hyper_proto_msgTypes[4].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*DesktopListRequest); i {
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
		file_pkg_proto_hyper_proto_msgTypes[5].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*DesktopListResponse); i {
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
		file_pkg_proto_hyper_proto_msgTypes[6].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*DesktopXMLGetRequest); i {
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
		file_pkg_proto_hyper_proto_msgTypes[7].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*DesktopXMLGetResponse); i {
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
			RawDescriptor: file_pkg_proto_hyper_proto_rawDesc,
			NumEnums:      0,
			NumMessages:   8,
			NumExtensions: 0,
			NumServices:   1,
		},
		GoTypes:           file_pkg_proto_hyper_proto_goTypes,
		DependencyIndexes: file_pkg_proto_hyper_proto_depIdxs,
		MessageInfos:      file_pkg_proto_hyper_proto_msgTypes,
	}.Build()
	File_pkg_proto_hyper_proto = out.File
	file_pkg_proto_hyper_proto_rawDesc = nil
	file_pkg_proto_hyper_proto_goTypes = nil
	file_pkg_proto_hyper_proto_depIdxs = nil
}

// Reference imports to suppress errors if they are not otherwise used.
var _ context.Context
var _ grpc.ClientConnInterface

// This is a compile-time assertion to ensure that this generated file
// is compatible with the grpc package it is being compiled against.
const _ = grpc.SupportPackageIsVersion6

// HyperClient is the client API for Hyper service.
//
// For semantics around ctx use and closing/ending streaming RPCs, please refer to https://godoc.org/google.golang.org/grpc#ClientConn.NewStream.
type HyperClient interface {
	DesktopStart(ctx context.Context, in *DesktopStartRequest, opts ...grpc.CallOption) (*DesktopStartResponse, error)
	DesktopStop(ctx context.Context, in *DesktopStopRequest, opts ...grpc.CallOption) (*DesktopStopResponse, error)
	DesktopList(ctx context.Context, in *DesktopListRequest, opts ...grpc.CallOption) (*DesktopListResponse, error)
	DesktopXMLGet(ctx context.Context, in *DesktopXMLGetRequest, opts ...grpc.CallOption) (*DesktopXMLGetResponse, error)
}

type hyperClient struct {
	cc grpc.ClientConnInterface
}

func NewHyperClient(cc grpc.ClientConnInterface) HyperClient {
	return &hyperClient{cc}
}

func (c *hyperClient) DesktopStart(ctx context.Context, in *DesktopStartRequest, opts ...grpc.CallOption) (*DesktopStartResponse, error) {
	out := new(DesktopStartResponse)
	err := c.cc.Invoke(ctx, "/proto.Hyper/DesktopStart", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *hyperClient) DesktopStop(ctx context.Context, in *DesktopStopRequest, opts ...grpc.CallOption) (*DesktopStopResponse, error) {
	out := new(DesktopStopResponse)
	err := c.cc.Invoke(ctx, "/proto.Hyper/DesktopStop", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *hyperClient) DesktopList(ctx context.Context, in *DesktopListRequest, opts ...grpc.CallOption) (*DesktopListResponse, error) {
	out := new(DesktopListResponse)
	err := c.cc.Invoke(ctx, "/proto.Hyper/DesktopList", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

func (c *hyperClient) DesktopXMLGet(ctx context.Context, in *DesktopXMLGetRequest, opts ...grpc.CallOption) (*DesktopXMLGetResponse, error) {
	out := new(DesktopXMLGetResponse)
	err := c.cc.Invoke(ctx, "/proto.Hyper/DesktopXMLGet", in, out, opts...)
	if err != nil {
		return nil, err
	}
	return out, nil
}

// HyperServer is the server API for Hyper service.
type HyperServer interface {
	DesktopStart(context.Context, *DesktopStartRequest) (*DesktopStartResponse, error)
	DesktopStop(context.Context, *DesktopStopRequest) (*DesktopStopResponse, error)
	DesktopList(context.Context, *DesktopListRequest) (*DesktopListResponse, error)
	DesktopXMLGet(context.Context, *DesktopXMLGetRequest) (*DesktopXMLGetResponse, error)
}

// UnimplementedHyperServer can be embedded to have forward compatible implementations.
type UnimplementedHyperServer struct {
}

func (*UnimplementedHyperServer) DesktopStart(context.Context, *DesktopStartRequest) (*DesktopStartResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method DesktopStart not implemented")
}
func (*UnimplementedHyperServer) DesktopStop(context.Context, *DesktopStopRequest) (*DesktopStopResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method DesktopStop not implemented")
}
func (*UnimplementedHyperServer) DesktopList(context.Context, *DesktopListRequest) (*DesktopListResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method DesktopList not implemented")
}
func (*UnimplementedHyperServer) DesktopXMLGet(context.Context, *DesktopXMLGetRequest) (*DesktopXMLGetResponse, error) {
	return nil, status.Errorf(codes.Unimplemented, "method DesktopXMLGet not implemented")
}

func RegisterHyperServer(s *grpc.Server, srv HyperServer) {
	s.RegisterService(&_Hyper_serviceDesc, srv)
}

func _Hyper_DesktopStart_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(DesktopStartRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(HyperServer).DesktopStart(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/proto.Hyper/DesktopStart",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(HyperServer).DesktopStart(ctx, req.(*DesktopStartRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Hyper_DesktopStop_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(DesktopStopRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(HyperServer).DesktopStop(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/proto.Hyper/DesktopStop",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(HyperServer).DesktopStop(ctx, req.(*DesktopStopRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Hyper_DesktopList_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(DesktopListRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(HyperServer).DesktopList(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/proto.Hyper/DesktopList",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(HyperServer).DesktopList(ctx, req.(*DesktopListRequest))
	}
	return interceptor(ctx, in, info, handler)
}

func _Hyper_DesktopXMLGet_Handler(srv interface{}, ctx context.Context, dec func(interface{}) error, interceptor grpc.UnaryServerInterceptor) (interface{}, error) {
	in := new(DesktopXMLGetRequest)
	if err := dec(in); err != nil {
		return nil, err
	}
	if interceptor == nil {
		return srv.(HyperServer).DesktopXMLGet(ctx, in)
	}
	info := &grpc.UnaryServerInfo{
		Server:     srv,
		FullMethod: "/proto.Hyper/DesktopXMLGet",
	}
	handler := func(ctx context.Context, req interface{}) (interface{}, error) {
		return srv.(HyperServer).DesktopXMLGet(ctx, req.(*DesktopXMLGetRequest))
	}
	return interceptor(ctx, in, info, handler)
}

var _Hyper_serviceDesc = grpc.ServiceDesc{
	ServiceName: "proto.Hyper",
	HandlerType: (*HyperServer)(nil),
	Methods: []grpc.MethodDesc{
		{
			MethodName: "DesktopStart",
			Handler:    _Hyper_DesktopStart_Handler,
		},
		{
			MethodName: "DesktopStop",
			Handler:    _Hyper_DesktopStop_Handler,
		},
		{
			MethodName: "DesktopList",
			Handler:    _Hyper_DesktopList_Handler,
		},
		{
			MethodName: "DesktopXMLGet",
			Handler:    _Hyper_DesktopXMLGet_Handler,
		},
	},
	Streams:  []grpc.StreamDesc{},
	Metadata: "pkg/proto/hyper.proto",
}
