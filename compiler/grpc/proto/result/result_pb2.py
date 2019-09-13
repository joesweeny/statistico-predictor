# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: compiler/grpc/proto/result/result.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from compiler.grpc.proto.competition import competition_pb2 as compiler_dot_grpc_dot_proto_dot_competition_dot_competition__pb2
from compiler.grpc.proto.round import round_pb2 as compiler_dot_grpc_dot_proto_dot_round_dot_round__pb2
from compiler.grpc.proto.season import season_pb2 as compiler_dot_grpc_dot_proto_dot_season_dot_season__pb2
from compiler.grpc.proto.team import team_pb2 as compiler_dot_grpc_dot_proto_dot_team_dot_team__pb2
from compiler.grpc.proto.venue import venue_pb2 as compiler_dot_grpc_dot_proto_dot_venue_dot_venue__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='compiler/grpc/proto/result/result.proto',
  package='result',
  syntax='proto3',
  serialized_options=_b('Z;github.com/statistico/statistico-data/internal/proto/result'),
  serialized_pb=_b('\n\'compiler/grpc/proto/result/result.proto\x12\x06result\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x31\x63ompiler/grpc/proto/competition/competition.proto\x1a%compiler/grpc/proto/round/round.proto\x1a\'compiler/grpc/proto/season/season.proto\x1a#compiler/grpc/proto/team/team.proto\x1a%compiler/grpc/proto/venue/venue.proto\"7\n\rSeasonRequest\x12\x11\n\tseason_id\x18\x01 \x01(\x03\x12\x13\n\x0b\x64\x61te_before\x18\x02 \x01(\t\"\x88\x02\n\x06Result\x12\n\n\x02id\x18\x01 \x01(\x03\x12-\n\x0b\x63ompetition\x18\x02 \x01(\x0b\x32\x18.competition.Competition\x12\x1e\n\x06season\x18\x03 \x01(\x0b\x32\x0e.season.Season\x12\x1b\n\x05round\x18\x04 \x01(\x0b\x32\x0c.round.Round\x12\x1b\n\x05venue\x18\x05 \x01(\x0b\x32\x0c.venue.Venue\x12/\n\nreferee_id\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int64Value\x12\x11\n\tdate_time\x18\x07 \x01(\x03\x12%\n\nmatch_data\x18\x08 \x01(\x0b\x32\x11.result.MatchData\"l\n\tMatchData\x12\x1d\n\thome_team\x18\x01 \x01(\x0b\x32\n.team.Team\x12\x1d\n\taway_team\x18\x02 \x01(\x0b\x32\n.team.Team\x12!\n\x05stats\x18\x03 \x01(\x0b\x32\x12.result.MatchStats\"\xfd\x06\n\nMatchStats\x12+\n\x05pitch\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x0ehome_formation\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x34\n\x0e\x61way_formation\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12/\n\nhome_score\x18\x04 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12/\n\naway_score\x18\x05 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x33\n\x0ehome_pen_score\x18\x06 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x33\n\x0e\x61way_pen_score\x18\x07 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x35\n\x0fhalf_time_score\x18\x08 \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x35\n\x0f\x66ull_time_score\x18\t \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x36\n\x10\x65xtra_time_score\x18\n \x01(\x0b\x32\x1c.google.protobuf.StringValue\x12\x39\n\x14home_league_position\x18\x0b \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x39\n\x14\x61way_league_position\x18\x0c \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12,\n\x07minutes\x18\r \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12,\n\x07seconds\x18\x0e \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12/\n\nadded_time\x18\x0f \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12/\n\nextra_time\x18\x10 \x01(\x0b\x32\x1b.google.protobuf.Int32Value\x12\x30\n\x0binjury_time\x18\x11 \x01(\x0b\x32\x1b.google.protobuf.Int32Value2Q\n\rResultService\x12@\n\x13GetResultsForSeason\x12\x15.result.SeasonRequest\x1a\x0e.result.Result\"\x00\x30\x01\x42=Z;github.com/statistico/statistico-data/internal/proto/resultb\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_wrappers__pb2.DESCRIPTOR,compiler_dot_grpc_dot_proto_dot_competition_dot_competition__pb2.DESCRIPTOR,compiler_dot_grpc_dot_proto_dot_round_dot_round__pb2.DESCRIPTOR,compiler_dot_grpc_dot_proto_dot_season_dot_season__pb2.DESCRIPTOR,compiler_dot_grpc_dot_proto_dot_team_dot_team__pb2.DESCRIPTOR,compiler_dot_grpc_dot_proto_dot_venue_dot_venue__pb2.DESCRIPTOR,])




_SEASONREQUEST = _descriptor.Descriptor(
  name='SeasonRequest',
  full_name='result.SeasonRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='season_id', full_name='result.SeasonRequest.season_id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date_before', full_name='result.SeasonRequest.date_before', index=1,
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
  serialized_start=290,
  serialized_end=345,
)


_RESULT = _descriptor.Descriptor(
  name='Result',
  full_name='result.Result',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='result.Result.id', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='competition', full_name='result.Result.competition', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='season', full_name='result.Result.season', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='round', full_name='result.Result.round', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='venue', full_name='result.Result.venue', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='referee_id', full_name='result.Result.referee_id', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='date_time', full_name='result.Result.date_time', index=6,
      number=7, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='match_data', full_name='result.Result.match_data', index=7,
      number=8, type=11, cpp_type=10, label=1,
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
  serialized_start=348,
  serialized_end=612,
)


_MATCHDATA = _descriptor.Descriptor(
  name='MatchData',
  full_name='result.MatchData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='home_team', full_name='result.MatchData.home_team', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='away_team', full_name='result.MatchData.away_team', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='stats', full_name='result.MatchData.stats', index=2,
      number=3, type=11, cpp_type=10, label=1,
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
  serialized_start=614,
  serialized_end=722,
)


_MATCHSTATS = _descriptor.Descriptor(
  name='MatchStats',
  full_name='result.MatchStats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pitch', full_name='result.MatchStats.pitch', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='home_formation', full_name='result.MatchStats.home_formation', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='away_formation', full_name='result.MatchStats.away_formation', index=2,
      number=3, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='home_score', full_name='result.MatchStats.home_score', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='away_score', full_name='result.MatchStats.away_score', index=4,
      number=5, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='home_pen_score', full_name='result.MatchStats.home_pen_score', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='away_pen_score', full_name='result.MatchStats.away_pen_score', index=6,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='half_time_score', full_name='result.MatchStats.half_time_score', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='full_time_score', full_name='result.MatchStats.full_time_score', index=8,
      number=9, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extra_time_score', full_name='result.MatchStats.extra_time_score', index=9,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='home_league_position', full_name='result.MatchStats.home_league_position', index=10,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='away_league_position', full_name='result.MatchStats.away_league_position', index=11,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minutes', full_name='result.MatchStats.minutes', index=12,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='seconds', full_name='result.MatchStats.seconds', index=13,
      number=14, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='added_time', full_name='result.MatchStats.added_time', index=14,
      number=15, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='extra_time', full_name='result.MatchStats.extra_time', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='injury_time', full_name='result.MatchStats.injury_time', index=16,
      number=17, type=11, cpp_type=10, label=1,
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
  serialized_start=725,
  serialized_end=1618,
)

_RESULT.fields_by_name['competition'].message_type = compiler_dot_grpc_dot_proto_dot_competition_dot_competition__pb2._COMPETITION
_RESULT.fields_by_name['season'].message_type = compiler_dot_grpc_dot_proto_dot_season_dot_season__pb2._SEASON
_RESULT.fields_by_name['round'].message_type = compiler_dot_grpc_dot_proto_dot_round_dot_round__pb2._ROUND
_RESULT.fields_by_name['venue'].message_type = compiler_dot_grpc_dot_proto_dot_venue_dot_venue__pb2._VENUE
_RESULT.fields_by_name['referee_id'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT64VALUE
_RESULT.fields_by_name['match_data'].message_type = _MATCHDATA
_MATCHDATA.fields_by_name['home_team'].message_type = compiler_dot_grpc_dot_proto_dot_team_dot_team__pb2._TEAM
_MATCHDATA.fields_by_name['away_team'].message_type = compiler_dot_grpc_dot_proto_dot_team_dot_team__pb2._TEAM
_MATCHDATA.fields_by_name['stats'].message_type = _MATCHSTATS
_MATCHSTATS.fields_by_name['pitch'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_MATCHSTATS.fields_by_name['home_formation'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_MATCHSTATS.fields_by_name['away_formation'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_MATCHSTATS.fields_by_name['home_score'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_MATCHSTATS.fields_by_name['away_score'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_MATCHSTATS.fields_by_name['home_pen_score'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_MATCHSTATS.fields_by_name['away_pen_score'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_MATCHSTATS.fields_by_name['half_time_score'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_MATCHSTATS.fields_by_name['full_time_score'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_MATCHSTATS.fields_by_name['extra_time_score'].message_type = google_dot_protobuf_dot_wrappers__pb2._STRINGVALUE
_MATCHSTATS.fields_by_name['home_league_position'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_MATCHSTATS.fields_by_name['away_league_position'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_MATCHSTATS.fields_by_name['minutes'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_MATCHSTATS.fields_by_name['seconds'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_MATCHSTATS.fields_by_name['added_time'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_MATCHSTATS.fields_by_name['extra_time'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
_MATCHSTATS.fields_by_name['injury_time'].message_type = google_dot_protobuf_dot_wrappers__pb2._INT32VALUE
DESCRIPTOR.message_types_by_name['SeasonRequest'] = _SEASONREQUEST
DESCRIPTOR.message_types_by_name['Result'] = _RESULT
DESCRIPTOR.message_types_by_name['MatchData'] = _MATCHDATA
DESCRIPTOR.message_types_by_name['MatchStats'] = _MATCHSTATS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SeasonRequest = _reflection.GeneratedProtocolMessageType('SeasonRequest', (_message.Message,), dict(
  DESCRIPTOR = _SEASONREQUEST,
  __module__ = 'compiler.grpc.proto.result.result_pb2'
  # @@protoc_insertion_point(class_scope:result.SeasonRequest)
  ))
_sym_db.RegisterMessage(SeasonRequest)

Result = _reflection.GeneratedProtocolMessageType('Result', (_message.Message,), dict(
  DESCRIPTOR = _RESULT,
  __module__ = 'compiler.grpc.proto.result.result_pb2'
  # @@protoc_insertion_point(class_scope:result.Result)
  ))
_sym_db.RegisterMessage(Result)

MatchData = _reflection.GeneratedProtocolMessageType('MatchData', (_message.Message,), dict(
  DESCRIPTOR = _MATCHDATA,
  __module__ = 'compiler.grpc.proto.result.result_pb2'
  # @@protoc_insertion_point(class_scope:result.MatchData)
  ))
_sym_db.RegisterMessage(MatchData)

MatchStats = _reflection.GeneratedProtocolMessageType('MatchStats', (_message.Message,), dict(
  DESCRIPTOR = _MATCHSTATS,
  __module__ = 'compiler.grpc.proto.result.result_pb2'
  # @@protoc_insertion_point(class_scope:result.MatchStats)
  ))
_sym_db.RegisterMessage(MatchStats)


DESCRIPTOR._options = None

_RESULTSERVICE = _descriptor.ServiceDescriptor(
  name='ResultService',
  full_name='result.ResultService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=1620,
  serialized_end=1701,
  methods=[
  _descriptor.MethodDescriptor(
    name='GetResultsForSeason',
    full_name='result.ResultService.GetResultsForSeason',
    index=0,
    containing_service=None,
    input_type=_SEASONREQUEST,
    output_type=_RESULT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_RESULTSERVICE)

DESCRIPTOR.services_by_name['ResultService'] = _RESULTSERVICE

# @@protoc_insertion_point(module_scope)
