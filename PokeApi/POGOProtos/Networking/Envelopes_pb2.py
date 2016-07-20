# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos.Networking.Envelopes.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos.Networking import Requests_pb2 as POGOProtos_dot_Networking_dot_Requests__pb2

from POGOProtos.Networking.Requests_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos.Networking.Envelopes.proto',
  package='POGOProtos.Networking.Envelopes',
  syntax='proto3',
  serialized_pb=_b('\n%POGOProtos.Networking.Envelopes.proto\x12\x1fPOGOProtos.Networking.Envelopes\x1a$POGOProtos.Networking.Requests.proto\"E\n\nAuthTicket\x12\r\n\x05start\x18\x01 \x01(\x0c\x12\x1b\n\x13\x65xpire_timestamp_ms\x18\x02 \x01(\x04\x12\x0b\n\x03\x65nd\x18\x03 \x01(\x0c\"\xa4\x04\n\x0fRequestEnvelope\x12\x13\n\x0bstatus_code\x18\x01 \x01(\x05\x12\x12\n\nrequest_id\x18\x03 \x01(\x04\x12\x39\n\x08requests\x18\x04 \x03(\x0b\x32\'.POGOProtos.Networking.Requests.Request\x12;\n\x08unknown6\x18\x06 \x01(\x0b\x32).POGOProtos.Networking.Envelopes.Unknown6\x12\x10\n\x08latitude\x18\x07 \x01(\x01\x12\x11\n\tlongitude\x18\x08 \x01(\x01\x12\x10\n\x08\x61ltitude\x18\t \x01(\x01\x12L\n\tauth_info\x18\n \x01(\x0b\x32\x39.POGOProtos.Networking.Envelopes.RequestEnvelope.AuthInfo\x12@\n\x0b\x61uth_ticket\x18\x0b \x01(\x0b\x32+.POGOProtos.Networking.Envelopes.AuthTicket\x12\x11\n\tunknown12\x18\x0c \x01(\x03\x1a\x95\x01\n\x08\x41uthInfo\x12\x10\n\x08provider\x18\x01 \x01(\t\x12L\n\x05token\x18\x02 \x01(\x0b\x32=.POGOProtos.Networking.Envelopes.RequestEnvelope.AuthInfo.JWT\x1a)\n\x03JWT\x12\x10\n\x08\x63ontents\x18\x01 \x01(\t\x12\x10\n\x08unknown2\x18\x02 \x01(\x05\"\xb0\x02\n\x10ResponseEnvelope\x12\x13\n\x0bstatus_code\x18\x01 \x01(\x05\x12\x12\n\nrequest_id\x18\x02 \x01(\x04\x12\x0f\n\x07\x61pi_url\x18\x03 \x01(\t\x12;\n\x08unknown6\x18\x06 \x01(\x0b\x32).POGOProtos.Networking.Envelopes.Unknown6\x12@\n\x0b\x61uth_ticket\x18\x07 \x01(\x0b\x32+.POGOProtos.Networking.Envelopes.AuthTicket\x12\x0f\n\x07returns\x18\x64 \x03(\x0c\x12\r\n\x05\x65rror\x18\x65 \x01(\t\x1a\x43\n\x08Unknown7\x12\x11\n\tunknown71\x18\x01 \x01(\x0c\x12\x11\n\tunknown72\x18\x02 \x01(\x03\x12\x11\n\tunknown73\x18\x03 \x01(\x0c\"\x80\x01\n\x08Unknown6\x12\x10\n\x08unknown1\x18\x01 \x01(\x05\x12\x44\n\x08unknown2\x18\x02 \x01(\x0b\x32\x32.POGOProtos.Networking.Envelopes.Unknown6.Unknown2\x1a\x1c\n\x08Unknown2\x12\x10\n\x08unknown1\x18\x01 \x01(\x0cP\x00\x62\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Networking_dot_Requests__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_AUTHTICKET = _descriptor.Descriptor(
  name='AuthTicket',
  full_name='POGOProtos.Networking.Envelopes.AuthTicket',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='POGOProtos.Networking.Envelopes.AuthTicket.start', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expire_timestamp_ms', full_name='POGOProtos.Networking.Envelopes.AuthTicket.expire_timestamp_ms', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='POGOProtos.Networking.Envelopes.AuthTicket.end', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=112,
  serialized_end=181,
)


_REQUESTENVELOPE_AUTHINFO_JWT = _descriptor.Descriptor(
  name='JWT',
  full_name='POGOProtos.Networking.Envelopes.RequestEnvelope.AuthInfo.JWT',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='contents', full_name='POGOProtos.Networking.Envelopes.RequestEnvelope.AuthInfo.JWT.contents', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown2', full_name='POGOProtos.Networking.Envelopes.RequestEnvelope.AuthInfo.JWT.unknown2', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=691,
  serialized_end=732,
)

_REQUESTENVELOPE_AUTHINFO = _descriptor.Descriptor(
  name='AuthInfo',
  full_name='POGOProtos.Networking.Envelopes.RequestEnvelope.AuthInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='provider', full_name='POGOProtos.Networking.Envelopes.RequestEnvelope.AuthInfo.provider', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='token', full_name='POGOProtos.Networking.Envelopes.RequestEnvelope.AuthInfo.token', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_REQUESTENVELOPE_AUTHINFO_JWT, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=583,
  serialized_end=732,
)

_REQUESTENVELOPE = _descriptor.Descriptor(
  name='RequestEnvelope',
  full_name='POGOProtos.Networking.Envelopes.RequestEnvelope',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status_code', full_name='POGOProtos.Networking.Envelopes.RequestEnvelope.status_code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='request_id', full_name='POGOProtos.Networking.Envelopes.RequestEnvelope.request_id', index=1,
      number=3, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='requests', full_name='POGOProtos.Networking.Envelopes.RequestEnvelope.requests', index=2,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown6', full_name='POGOProtos.Networking.Envelopes.RequestEnvelope.unknown6', index=3,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='POGOProtos.Networking.Envelopes.RequestEnvelope.latitude', index=4,
      number=7, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='POGOProtos.Networking.Envelopes.RequestEnvelope.longitude', index=5,
      number=8, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='altitude', full_name='POGOProtos.Networking.Envelopes.RequestEnvelope.altitude', index=6,
      number=9, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auth_info', full_name='POGOProtos.Networking.Envelopes.RequestEnvelope.auth_info', index=7,
      number=10, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auth_ticket', full_name='POGOProtos.Networking.Envelopes.RequestEnvelope.auth_ticket', index=8,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown12', full_name='POGOProtos.Networking.Envelopes.RequestEnvelope.unknown12', index=9,
      number=12, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_REQUESTENVELOPE_AUTHINFO, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=184,
  serialized_end=732,
)


_RESPONSEENVELOPE_UNKNOWN7 = _descriptor.Descriptor(
  name='Unknown7',
  full_name='POGOProtos.Networking.Envelopes.ResponseEnvelope.Unknown7',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unknown71', full_name='POGOProtos.Networking.Envelopes.ResponseEnvelope.Unknown7.unknown71', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown72', full_name='POGOProtos.Networking.Envelopes.ResponseEnvelope.Unknown7.unknown72', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown73', full_name='POGOProtos.Networking.Envelopes.ResponseEnvelope.Unknown7.unknown73', index=2,
      number=3, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=972,
  serialized_end=1039,
)

_RESPONSEENVELOPE = _descriptor.Descriptor(
  name='ResponseEnvelope',
  full_name='POGOProtos.Networking.Envelopes.ResponseEnvelope',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='status_code', full_name='POGOProtos.Networking.Envelopes.ResponseEnvelope.status_code', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='request_id', full_name='POGOProtos.Networking.Envelopes.ResponseEnvelope.request_id', index=1,
      number=2, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='api_url', full_name='POGOProtos.Networking.Envelopes.ResponseEnvelope.api_url', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown6', full_name='POGOProtos.Networking.Envelopes.ResponseEnvelope.unknown6', index=3,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='auth_ticket', full_name='POGOProtos.Networking.Envelopes.ResponseEnvelope.auth_ticket', index=4,
      number=7, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='returns', full_name='POGOProtos.Networking.Envelopes.ResponseEnvelope.returns', index=5,
      number=100, type=12, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='error', full_name='POGOProtos.Networking.Envelopes.ResponseEnvelope.error', index=6,
      number=101, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_RESPONSEENVELOPE_UNKNOWN7, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=735,
  serialized_end=1039,
)


_UNKNOWN6_UNKNOWN2 = _descriptor.Descriptor(
  name='Unknown2',
  full_name='POGOProtos.Networking.Envelopes.Unknown6.Unknown2',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unknown1', full_name='POGOProtos.Networking.Envelopes.Unknown6.Unknown2.unknown1', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1142,
  serialized_end=1170,
)

_UNKNOWN6 = _descriptor.Descriptor(
  name='Unknown6',
  full_name='POGOProtos.Networking.Envelopes.Unknown6',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='unknown1', full_name='POGOProtos.Networking.Envelopes.Unknown6.unknown1', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown2', full_name='POGOProtos.Networking.Envelopes.Unknown6.unknown2', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_UNKNOWN6_UNKNOWN2, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=1042,
  serialized_end=1170,
)

_REQUESTENVELOPE_AUTHINFO_JWT.containing_type = _REQUESTENVELOPE_AUTHINFO
_REQUESTENVELOPE_AUTHINFO.fields_by_name['token'].message_type = _REQUESTENVELOPE_AUTHINFO_JWT
_REQUESTENVELOPE_AUTHINFO.containing_type = _REQUESTENVELOPE
_REQUESTENVELOPE.fields_by_name['requests'].message_type = POGOProtos_dot_Networking_dot_Requests__pb2._REQUEST
_REQUESTENVELOPE.fields_by_name['unknown6'].message_type = _UNKNOWN6
_REQUESTENVELOPE.fields_by_name['auth_info'].message_type = _REQUESTENVELOPE_AUTHINFO
_REQUESTENVELOPE.fields_by_name['auth_ticket'].message_type = _AUTHTICKET
_RESPONSEENVELOPE_UNKNOWN7.containing_type = _RESPONSEENVELOPE
_RESPONSEENVELOPE.fields_by_name['unknown6'].message_type = _UNKNOWN6
_RESPONSEENVELOPE.fields_by_name['auth_ticket'].message_type = _AUTHTICKET
_UNKNOWN6_UNKNOWN2.containing_type = _UNKNOWN6
_UNKNOWN6.fields_by_name['unknown2'].message_type = _UNKNOWN6_UNKNOWN2
DESCRIPTOR.message_types_by_name['AuthTicket'] = _AUTHTICKET
DESCRIPTOR.message_types_by_name['RequestEnvelope'] = _REQUESTENVELOPE
DESCRIPTOR.message_types_by_name['ResponseEnvelope'] = _RESPONSEENVELOPE
DESCRIPTOR.message_types_by_name['Unknown6'] = _UNKNOWN6

AuthTicket = _reflection.GeneratedProtocolMessageType('AuthTicket', (_message.Message,), dict(
  DESCRIPTOR = _AUTHTICKET,
  __module__ = 'POGOProtos.Networking.Envelopes_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Envelopes.AuthTicket)
  ))
_sym_db.RegisterMessage(AuthTicket)

RequestEnvelope = _reflection.GeneratedProtocolMessageType('RequestEnvelope', (_message.Message,), dict(

  AuthInfo = _reflection.GeneratedProtocolMessageType('AuthInfo', (_message.Message,), dict(

    JWT = _reflection.GeneratedProtocolMessageType('JWT', (_message.Message,), dict(
      DESCRIPTOR = _REQUESTENVELOPE_AUTHINFO_JWT,
      __module__ = 'POGOProtos.Networking.Envelopes_pb2'
      # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Envelopes.RequestEnvelope.AuthInfo.JWT)
      ))
    ,
    DESCRIPTOR = _REQUESTENVELOPE_AUTHINFO,
    __module__ = 'POGOProtos.Networking.Envelopes_pb2'
    # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Envelopes.RequestEnvelope.AuthInfo)
    ))
  ,
  DESCRIPTOR = _REQUESTENVELOPE,
  __module__ = 'POGOProtos.Networking.Envelopes_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Envelopes.RequestEnvelope)
  ))
_sym_db.RegisterMessage(RequestEnvelope)
_sym_db.RegisterMessage(RequestEnvelope.AuthInfo)
_sym_db.RegisterMessage(RequestEnvelope.AuthInfo.JWT)

ResponseEnvelope = _reflection.GeneratedProtocolMessageType('ResponseEnvelope', (_message.Message,), dict(

  Unknown7 = _reflection.GeneratedProtocolMessageType('Unknown7', (_message.Message,), dict(
    DESCRIPTOR = _RESPONSEENVELOPE_UNKNOWN7,
    __module__ = 'POGOProtos.Networking.Envelopes_pb2'
    # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Envelopes.ResponseEnvelope.Unknown7)
    ))
  ,
  DESCRIPTOR = _RESPONSEENVELOPE,
  __module__ = 'POGOProtos.Networking.Envelopes_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Envelopes.ResponseEnvelope)
  ))
_sym_db.RegisterMessage(ResponseEnvelope)
_sym_db.RegisterMessage(ResponseEnvelope.Unknown7)

Unknown6 = _reflection.GeneratedProtocolMessageType('Unknown6', (_message.Message,), dict(

  Unknown2 = _reflection.GeneratedProtocolMessageType('Unknown2', (_message.Message,), dict(
    DESCRIPTOR = _UNKNOWN6_UNKNOWN2,
    __module__ = 'POGOProtos.Networking.Envelopes_pb2'
    # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Envelopes.Unknown6.Unknown2)
    ))
  ,
  DESCRIPTOR = _UNKNOWN6,
  __module__ = 'POGOProtos.Networking.Envelopes_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Networking.Envelopes.Unknown6)
  ))
_sym_db.RegisterMessage(Unknown6)
_sym_db.RegisterMessage(Unknown6.Unknown2)


# @@protoc_insertion_point(module_scope)
