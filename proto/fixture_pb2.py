# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: proto/fixture.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='proto/fixture.proto',
  package='statshub',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x13proto/fixture.proto\x12\x08statshub\x1a\x1egoogle/protobuf/wrappers.proto\"-\n\x07Request\x12\x11\n\tdate_from\x18\x01 \x01(\t\x12\x0f\n\x07\x64\x61te_to\x18\x02 \x01(\t\"\'\n\x0b\x43ompetition\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\"\"\n\x06Season\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\" \n\x04Team\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04name\x18\x02 \x01(\t\"\\\n\x05Venue\x12\'\n\x02id\x18\x01 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12*\n\x04name\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\"\x8d\x02\n\x07\x46ixture\x12\n\n\x02id\x18\x01 \x01(\x03\x12*\n\x0b\x63ompetition\x18\x02 \x01(\x0b\x32\x15.statshub.Competition\x12 \n\x06season\x18\x03 \x01(\x0b\x32\x10.statshub.Season\x12!\n\thome_team\x18\x04 \x01(\x0b\x32\x0e.statshub.Team\x12!\n\taway_team\x18\x05 \x01(\x0b\x32\x0e.statshub.Team\x12\x1e\n\x05venue\x18\x06 \x01(\x0b\x32\x0f.statshub.Venue\x12/\n\nreferee_id\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x11\n\tdate_time\x18\x08 \x01(\x03\x32J\n\x0e\x46ixtureService\x12\x38\n\x0cListFixtures\x12\x11.statshub.Request\x1a\x11.statshub.Fixture\"\x00\x30\x01\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,])




_REQUEST = _descriptor.Descriptor(
  name='Request',
  full_name='statshub.Request',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='date_from', full_name='statshub.Request.date_from', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date_to', full_name='statshub.Request.date_to', index=1,
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
  serialized_start=65,
  serialized_end=110,
)


_COMPETITION = _descriptor.Descriptor(
  name='Competition',
  full_name='statshub.Competition',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='statshub.Competition.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='statshub.Competition.name', index=1,
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
  serialized_start=112,
  serialized_end=151,
)


_SEASON = _descriptor.Descriptor(
  name='Season',
  full_name='statshub.Season',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='statshub.Season.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='statshub.Season.name', index=1,
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
  serialized_start=153,
  serialized_end=187,
)


_TEAM = _descriptor.Descriptor(
  name='Team',
  full_name='statshub.Team',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='statshub.Team.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='statshub.Team.name', index=1,
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
  serialized_start=189,
  serialized_end=221,
)


_VENUE = _descriptor.Descriptor(
  name='Venue',
  full_name='statshub.Venue',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='statshub.Venue.id', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name', full_name='statshub.Venue.name', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=223,
  serialized_end=315,
)


_FIXTURE = _descriptor.Descriptor(
  name='Fixture',
  full_name='statshub.Fixture',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='statshub.Fixture.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='competition', full_name='statshub.Fixture.competition', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='season', full_name='statshub.Fixture.season', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='home_team', full_name='statshub.Fixture.home_team', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='away_team', full_name='statshub.Fixture.away_team', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='venue', full_name='statshub.Fixture.venue', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='referee_id', full_name='statshub.Fixture.referee_id', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date_time', full_name='statshub.Fixture.date_time', index=7,
      number=8, type=3, cpp_type=2, label=1,
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
  serialized_start=318,
  serialized_end=587,
)

_VENUE.fields_by_name['id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_VENUE.fields_by_name['name'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_FIXTURE.fields_by_name['competition'].message_type = _COMPETITION
_FIXTURE.fields_by_name['season'].message_type = _SEASON
_FIXTURE.fields_by_name['home_team'].message_type = _TEAM
_FIXTURE.fields_by_name['away_team'].message_type = _TEAM
_FIXTURE.fields_by_name['venue'].message_type = _VENUE
_FIXTURE.fields_by_name['referee_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
DESCRIPTOR.message_types_by_name['Request'] = _REQUEST
DESCRIPTOR.message_types_by_name['Competition'] = _COMPETITION
DESCRIPTOR.message_types_by_name['Season'] = _SEASON
DESCRIPTOR.message_types_by_name['Team'] = _TEAM
DESCRIPTOR.message_types_by_name['Venue'] = _VENUE
DESCRIPTOR.message_types_by_name['Fixture'] = _FIXTURE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Request = _reflection.GeneratedProtocolMessageType('Request', (_message.Message,), dict(
  DESCRIPTOR = _REQUEST,
  __module__ = 'proto.fixture_pb2'
  # @@protoc_insertion_point(class_scope:statshub.Request)
  ))
_sym_db.RegisterMessage(Request)

Competition = _reflection.GeneratedProtocolMessageType('Competition', (_message.Message,), dict(
  DESCRIPTOR = _COMPETITION,
  __module__ = 'proto.fixture_pb2'
  # @@protoc_insertion_point(class_scope:statshub.Competition)
  ))
_sym_db.RegisterMessage(Competition)

Season = _reflection.GeneratedProtocolMessageType('Season', (_message.Message,), dict(
  DESCRIPTOR = _SEASON,
  __module__ = 'proto.fixture_pb2'
  # @@protoc_insertion_point(class_scope:statshub.Season)
  ))
_sym_db.RegisterMessage(Season)

Team = _reflection.GeneratedProtocolMessageType('Team', (_message.Message,), dict(
  DESCRIPTOR = _TEAM,
  __module__ = 'proto.fixture_pb2'
  # @@protoc_insertion_point(class_scope:statshub.Team)
  ))
_sym_db.RegisterMessage(Team)

Venue = _reflection.GeneratedProtocolMessageType('Venue', (_message.Message,), dict(
  DESCRIPTOR = _VENUE,
  __module__ = 'proto.fixture_pb2'
  # @@protoc_insertion_point(class_scope:statshub.Venue)
  ))
_sym_db.RegisterMessage(Venue)

Fixture = _reflection.GeneratedProtocolMessageType('Fixture', (_message.Message,), dict(
  DESCRIPTOR = _FIXTURE,
  __module__ = 'proto.fixture_pb2'
  # @@protoc_insertion_point(class_scope:statshub.Fixture)
  ))
_sym_db.RegisterMessage(Fixture)



_FIXTURESERVICE = _descriptor.ServiceDescriptor(
  name='FixtureService',
  full_name='statshub.FixtureService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=589,
  serialized_end=663,
  methods=[
  _descriptor.MethodDescriptor(
    name='ListFixtures',
    full_name='statshub.FixtureService.ListFixtures',
    index=0,
    containing_service=None,
    input_type=_REQUEST,
    output_type=_FIXTURE,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_FIXTURESERVICE)

DESCRIPTOR.services_by_name['FixtureService'] = _FIXTURESERVICE

# @@protoc_insertion_point(module_scope)
