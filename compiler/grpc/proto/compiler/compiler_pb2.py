# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: compiler/grpc/proto/compiler/compiler.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='compiler/grpc/proto/compiler/compiler.proto',
  package='compiler',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n+compiler/grpc/proto/compiler/compiler.proto\x12\x08\x63ompiler\"&\n\x10OverUnderRequest\x12\x12\n\nfixture_id\x18\x01 \x01(\x04\"I\n\x16OverUnderGoalsResponse\x12\x12\n\nfixture_id\x18\x01 \x01(\x04\x12\r\n\x05under\x18\x02 \x01(\x02\x12\x0c\n\x04over\x18\x03 \x01(\x02\x32t\n\x13OddsCompilerService\x12]\n\x1bGetOverUnderGoalsForFixture\x12\x1a.compiler.OverUnderRequest\x1a .compiler.OverUnderGoalsResponse\"\x00\x62\x06proto3')
)




_OVERUNDERREQUEST = _descriptor.Descriptor(
  name='OverUnderRequest',
  full_name='compiler.OverUnderRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fixture_id', full_name='compiler.OverUnderRequest.fixture_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
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
  serialized_start=57,
  serialized_end=95,
)


_OVERUNDERGOALSRESPONSE = _descriptor.Descriptor(
  name='OverUnderGoalsResponse',
  full_name='compiler.OverUnderGoalsResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fixture_id', full_name='compiler.OverUnderGoalsResponse.fixture_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='under', full_name='compiler.OverUnderGoalsResponse.under', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='over', full_name='compiler.OverUnderGoalsResponse.over', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
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
  serialized_start=97,
  serialized_end=170,
)

DESCRIPTOR.message_types_by_name['OverUnderRequest'] = _OVERUNDERREQUEST
DESCRIPTOR.message_types_by_name['OverUnderGoalsResponse'] = _OVERUNDERGOALSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

OverUnderRequest = _reflection.GeneratedProtocolMessageType('OverUnderRequest', (_message.Message,), dict(
  DESCRIPTOR = _OVERUNDERREQUEST,
  __module__ = 'compiler.grpc.proto.compiler.compiler_pb2'
  # @@protoc_insertion_point(class_scope:compiler.OverUnderRequest)
  ))
_sym_db.RegisterMessage(OverUnderRequest)

OverUnderGoalsResponse = _reflection.GeneratedProtocolMessageType('OverUnderGoalsResponse', (_message.Message,), dict(
  DESCRIPTOR = _OVERUNDERGOALSRESPONSE,
  __module__ = 'compiler.grpc.proto.compiler.compiler_pb2'
  # @@protoc_insertion_point(class_scope:compiler.OverUnderGoalsResponse)
  ))
_sym_db.RegisterMessage(OverUnderGoalsResponse)



_ODDSCOMPILERSERVICE = _descriptor.ServiceDescriptor(
  name='OddsCompilerService',
  full_name='compiler.OddsCompilerService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=172,
  serialized_end=288,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetOverUnderGoalsForFixture',
    full_name='compiler.OddsCompilerService.GetOverUnderGoalsForFixture',
    index=0,
    containing_service=None,
    input_type=_OVERUNDERREQUEST,
    output_type=_OVERUNDERGOALSRESPONSE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_ODDSCOMPILERSERVICE)

DESCRIPTOR.services_by_name['OddsCompilerService'] = _ODDSCOMPILERSERVICE

# @@protoc_insertion_point(module_scope)
