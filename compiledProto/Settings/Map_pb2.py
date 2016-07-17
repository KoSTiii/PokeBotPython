# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Settings/Map.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Settings/Map.proto',
  package='POGOProtos.Settings',
  syntax='proto3',
  serialized_pb=_b('\n\x12Settings/Map.proto\x12\x13POGOProtos.Settings\"\x87\x02\n\x03Map\x12\x1d\n\x15pokemon_visible_range\x18\x01 \x01(\x01\x12\x1d\n\x15poke_nav_range_meters\x18\x02 \x01(\x01\x12\x1e\n\x16\x65ncounter_range_meters\x18\x03 \x01(\x01\x12+\n#get_map_objects_min_refresh_seconds\x18\x04 \x01(\x02\x12+\n#get_map_objects_max_refresh_seconds\x18\x05 \x01(\x02\x12+\n#get_map_objects_min_distance_meters\x18\x06 \x01(\x02\x12\x1b\n\x13google_maps_api_key\x18\x07 \x01(\tb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MAP = _descriptor.Descriptor(
  name='Map',
  full_name='POGOProtos.Settings.Map',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokemon_visible_range', full_name='POGOProtos.Settings.Map.pokemon_visible_range', index=0,
      number=1, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='poke_nav_range_meters', full_name='POGOProtos.Settings.Map.poke_nav_range_meters', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encounter_range_meters', full_name='POGOProtos.Settings.Map.encounter_range_meters', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_map_objects_min_refresh_seconds', full_name='POGOProtos.Settings.Map.get_map_objects_min_refresh_seconds', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_map_objects_max_refresh_seconds', full_name='POGOProtos.Settings.Map.get_map_objects_max_refresh_seconds', index=4,
      number=5, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='get_map_objects_min_distance_meters', full_name='POGOProtos.Settings.Map.get_map_objects_min_distance_meters', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='google_maps_api_key', full_name='POGOProtos.Settings.Map.google_maps_api_key', index=6,
      number=7, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  serialized_start=44,
  serialized_end=307,
)

DESCRIPTOR.message_types_by_name['Map'] = _MAP

Map = _reflection.GeneratedProtocolMessageType('Map', (_message.Message,), dict(
  DESCRIPTOR = _MAP,
  __module__ = 'Settings.Map_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Settings.Map)
  ))
_sym_db.RegisterMessage(Map)


# @@protoc_insertion_point(module_scope)
