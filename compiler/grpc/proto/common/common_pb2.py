# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: compiler/grpc/proto/common/common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='compiler/grpc/proto/common/common.proto',
  package='proto',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\'compiler/grpc/proto/common/common.proto\x12\x05proto\" \n\x04\x44\x61te\x12\x0b\n\x03utc\x18\x01 \x01(\x03\x12\x0b\n\x03rfc\x18\x02 \x01(\tb\x06proto3')
)




_DATE = _descriptor.Descriptor(
  name='Date',
  full_name='proto.Date',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='utc', full_name='proto.Date.utc', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='rfc', full_name='proto.Date.rfc', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=50,
  serialized_end=82,
)

DESCRIPTOR.message_types_by_name['Date'] = _DATE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Date = _reflection.GeneratedProtocolMessageType('Date', (_message.Message,), dict(
  DESCRIPTOR = _DATE,
  __module__ = 'compiler.grpc.proto.common.common_pb2'
  # @@protoc_insertion_point(class_scope:proto.Date)
  ))
_sym_db.RegisterMessage(Date)


# @@protoc_insertion_point(module_scope)
