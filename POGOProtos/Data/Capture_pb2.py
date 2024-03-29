# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos.Data.Capture.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos import Enums_pb2 as POGOProtos_dot_Enums__pb2
from POGOProtos import Inventory_pb2 as POGOProtos_dot_Inventory__pb2
POGOProtos_dot_Data__pb2 = POGOProtos_dot_Inventory__pb2.POGOProtos_dot_Data__pb2
POGOProtos_dot_Enums__pb2 = POGOProtos_dot_Inventory__pb2.POGOProtos_dot_Enums__pb2
POGOProtos_dot_Data_dot_Player__pb2 = POGOProtos_dot_Inventory__pb2.POGOProtos_dot_Data_dot_Player__pb2
POGOProtos_dot_Enums__pb2 = POGOProtos_dot_Inventory__pb2.POGOProtos_dot_Enums__pb2
POGOProtos_dot_Data_dot_Player__pb2 = POGOProtos_dot_Inventory__pb2.POGOProtos_dot_Data_dot_Player__pb2
POGOProtos_dot_Enums__pb2 = POGOProtos_dot_Inventory__pb2.POGOProtos_dot_Enums__pb2
POGOProtos_dot_Enums__pb2 = POGOProtos_dot_Inventory__pb2.POGOProtos_dot_Enums__pb2

from POGOProtos.Enums_pb2 import *
from POGOProtos.Inventory_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos.Data.Capture.proto',
  package='POGOProtos.Data.Capture',
  syntax='proto3',
  serialized_pb=_b('\n\x1dPOGOProtos.Data.Capture.proto\x12\x17POGOProtos.Data.Capture\x1a\x16POGOProtos.Enums.proto\x1a\x1aPOGOProtos.Inventory.proto\"r\n\x0c\x43\x61ptureAward\x12\x35\n\ractivity_type\x18\x01 \x03(\x0e\x32\x1e.POGOProtos.Enums.ActivityType\x12\n\n\x02xp\x18\x02 \x03(\x05\x12\r\n\x05\x63\x61ndy\x18\x03 \x03(\x05\x12\x10\n\x08stardust\x18\x04 \x03(\x05\"\x88\x01\n\x12\x43\x61ptureProbability\x12\x33\n\rpokeball_type\x18\x01 \x03(\x0e\x32\x1c.POGOProtos.Inventory.ItemId\x12\x1b\n\x13\x63\x61pture_probability\x18\x02 \x03(\x02\x12 \n\x18reticle_difficulty_scale\x18\x0c \x01(\x01P\x00P\x01\x62\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Enums__pb2.DESCRIPTOR,POGOProtos_dot_Inventory__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CAPTUREAWARD = _descriptor.Descriptor(
  name='CaptureAward',
  full_name='POGOProtos.Data.Capture.CaptureAward',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='activity_type', full_name='POGOProtos.Data.Capture.CaptureAward.activity_type', index=0,
      number=1, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='xp', full_name='POGOProtos.Data.Capture.CaptureAward.xp', index=1,
      number=2, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='candy', full_name='POGOProtos.Data.Capture.CaptureAward.candy', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stardust', full_name='POGOProtos.Data.Capture.CaptureAward.stardust', index=3,
      number=4, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
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
  serialized_start=110,
  serialized_end=224,
)


_CAPTUREPROBABILITY = _descriptor.Descriptor(
  name='CaptureProbability',
  full_name='POGOProtos.Data.Capture.CaptureProbability',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokeball_type', full_name='POGOProtos.Data.Capture.CaptureProbability.pokeball_type', index=0,
      number=1, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='capture_probability', full_name='POGOProtos.Data.Capture.CaptureProbability.capture_probability', index=1,
      number=2, type=2, cpp_type=6, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='reticle_difficulty_scale', full_name='POGOProtos.Data.Capture.CaptureProbability.reticle_difficulty_scale', index=2,
      number=12, type=1, cpp_type=5, label=1,
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
  serialized_start=227,
  serialized_end=363,
)

_CAPTUREAWARD.fields_by_name['activity_type'].enum_type = POGOProtos_dot_Enums__pb2._ACTIVITYTYPE
_CAPTUREPROBABILITY.fields_by_name['pokeball_type'].enum_type = POGOProtos_dot_Inventory__pb2._ITEMID
DESCRIPTOR.message_types_by_name['CaptureAward'] = _CAPTUREAWARD
DESCRIPTOR.message_types_by_name['CaptureProbability'] = _CAPTUREPROBABILITY

CaptureAward = _reflection.GeneratedProtocolMessageType('CaptureAward', (_message.Message,), dict(
  DESCRIPTOR = _CAPTUREAWARD,
  __module__ = 'POGOProtos.Data.Capture_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Data.Capture.CaptureAward)
  ))
_sym_db.RegisterMessage(CaptureAward)

CaptureProbability = _reflection.GeneratedProtocolMessageType('CaptureProbability', (_message.Message,), dict(
  DESCRIPTOR = _CAPTUREPROBABILITY,
  __module__ = 'POGOProtos.Data.Capture_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Data.Capture.CaptureProbability)
  ))
_sym_db.RegisterMessage(CaptureProbability)


# @@protoc_insertion_point(module_scope)
