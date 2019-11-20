# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: api/grpc/proto/domain_enums.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='api/grpc/proto/domain_enums.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n!api/grpc/proto/domain_enums.proto*\x8f\x01\n\x05State\x12\x11\n\rSTATE_UNKNOWN\x10\x00\x12\x16\n\x12STATE_UNIDENTIFIED\x10\x01\x12\x11\n\rSTATE_STOPPED\x10\x02\x12\x11\n\rSTATE_STARTED\x10\x03\x12\x10\n\x0cSTATE_PAUSED\x10\x04\x12\x11\n\rSTATE_DELETED\x10\x05\x12\x10\n\x0cSTATE_FAILED\x10\x06*\x9f\x01\n\x06\x41\x63tion\x12\x12\n\x0e\x41\x43TION_UNKNOWN\x10\x00\x12\x0f\n\x0b\x41\x43TION_STOP\x10\x01\x12\x10\n\x0c\x41\x43TION_START\x10\x02\x12\x10\n\x0c\x41\x43TION_PAUSE\x10\x03\x12\x11\n\rACTION_RESUME\x10\x04\x12\x11\n\rACTION_DELETE\x10\x05\x12\x11\n\rACTION_UPDATE\x10\x06\x12\x13\n\x0f\x41\x43TION_TEMPLATE\x10\x07*K\n\x06\x46ormat\x12\x10\n\x0c\x46ORMAT_QCOW2\x10\x00\x12\x0e\n\nFORMAT_RAW\x10\x01\x12\x0e\n\nFORMAT_ISO\x10\x02\x12\x0f\n\x0b\x46ORMAT_VMDK\x10\x03*?\n\x03\x42us\x12\x0b\n\x07\x42US_IDE\x10\x00\x12\x0e\n\nBUS_VIRTIO\x10\x01\x12\x0c\n\x08\x42US_SATA\x10\x02\x12\r\n\tBUS_SCSII\x10\x03*B\n\x04\x42oot\x12\x0b\n\x07\x42OOT_HD\x10\x00\x12\x0e\n\nBOOT_CDROM\x10\x01\x12\x10\n\x0c\x42OOT_NETWORK\x10\x02\x12\x0b\n\x07\x42OOT_FD\x10\x03\x62\x06proto3')
)

_STATE = _descriptor.EnumDescriptor(
  name='State',
  full_name='State',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='STATE_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATE_UNIDENTIFIED', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATE_STOPPED', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATE_STARTED', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATE_PAUSED', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATE_DELETED', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='STATE_FAILED', index=6, number=6,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=38,
  serialized_end=181,
)
_sym_db.RegisterEnumDescriptor(_STATE)

State = enum_type_wrapper.EnumTypeWrapper(_STATE)
_ACTION = _descriptor.EnumDescriptor(
  name='Action',
  full_name='Action',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ACTION_UNKNOWN', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_STOP', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_START', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_PAUSE', index=3, number=3,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_RESUME', index=4, number=4,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_DELETE', index=5, number=5,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_UPDATE', index=6, number=6,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ACTION_TEMPLATE', index=7, number=7,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=184,
  serialized_end=343,
)
_sym_db.RegisterEnumDescriptor(_ACTION)

Action = enum_type_wrapper.EnumTypeWrapper(_ACTION)
_FORMAT = _descriptor.EnumDescriptor(
  name='Format',
  full_name='Format',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='FORMAT_QCOW2', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORMAT_RAW', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORMAT_ISO', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FORMAT_VMDK', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=345,
  serialized_end=420,
)
_sym_db.RegisterEnumDescriptor(_FORMAT)

Format = enum_type_wrapper.EnumTypeWrapper(_FORMAT)
_BUS = _descriptor.EnumDescriptor(
  name='Bus',
  full_name='Bus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BUS_IDE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUS_VIRTIO', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUS_SATA', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BUS_SCSII', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=422,
  serialized_end=485,
)
_sym_db.RegisterEnumDescriptor(_BUS)

Bus = enum_type_wrapper.EnumTypeWrapper(_BUS)
_BOOT = _descriptor.EnumDescriptor(
  name='Boot',
  full_name='Boot',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='BOOT_HD', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOT_CDROM', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOT_NETWORK', index=2, number=2,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='BOOT_FD', index=3, number=3,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=487,
  serialized_end=553,
)
_sym_db.RegisterEnumDescriptor(_BOOT)

Boot = enum_type_wrapper.EnumTypeWrapper(_BOOT)
STATE_UNKNOWN = 0
STATE_UNIDENTIFIED = 1
STATE_STOPPED = 2
STATE_STARTED = 3
STATE_PAUSED = 4
STATE_DELETED = 5
STATE_FAILED = 6
ACTION_UNKNOWN = 0
ACTION_STOP = 1
ACTION_START = 2
ACTION_PAUSE = 3
ACTION_RESUME = 4
ACTION_DELETE = 5
ACTION_UPDATE = 6
ACTION_TEMPLATE = 7
FORMAT_QCOW2 = 0
FORMAT_RAW = 1
FORMAT_ISO = 2
FORMAT_VMDK = 3
BUS_IDE = 0
BUS_VIRTIO = 1
BUS_SATA = 2
BUS_SCSII = 3
BOOT_HD = 0
BOOT_CDROM = 1
BOOT_NETWORK = 2
BOOT_FD = 3


DESCRIPTOR.enum_types_by_name['State'] = _STATE
DESCRIPTOR.enum_types_by_name['Action'] = _ACTION
DESCRIPTOR.enum_types_by_name['Format'] = _FORMAT
DESCRIPTOR.enum_types_by_name['Bus'] = _BUS
DESCRIPTOR.enum_types_by_name['Boot'] = _BOOT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


# @@protoc_insertion_point(module_scope)
