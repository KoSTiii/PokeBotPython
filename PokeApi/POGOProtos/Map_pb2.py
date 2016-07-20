# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos.Map.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos.Map import Fort_pb2 as POGOProtos_dot_Map_dot_Fort__pb2
POGOProtos_dot_Enums__pb2 = POGOProtos_dot_Map_dot_Fort__pb2.POGOProtos_dot_Enums__pb2
POGOProtos_dot_Inventory__pb2 = POGOProtos_dot_Map_dot_Fort__pb2.POGOProtos_dot_Inventory__pb2
POGOProtos_dot_Data__pb2 = POGOProtos_dot_Map_dot_Fort__pb2.POGOProtos_dot_Data__pb2
POGOProtos_dot_Enums__pb2 = POGOProtos_dot_Map_dot_Fort__pb2.POGOProtos_dot_Enums__pb2
POGOProtos_dot_Data_dot_Player__pb2 = POGOProtos_dot_Map_dot_Fort__pb2.POGOProtos_dot_Data_dot_Player__pb2
POGOProtos_dot_Enums__pb2 = POGOProtos_dot_Map_dot_Fort__pb2.POGOProtos_dot_Enums__pb2
POGOProtos_dot_Data_dot_Player__pb2 = POGOProtos_dot_Map_dot_Fort__pb2.POGOProtos_dot_Data_dot_Player__pb2
POGOProtos_dot_Enums__pb2 = POGOProtos_dot_Map_dot_Fort__pb2.POGOProtos_dot_Enums__pb2
POGOProtos_dot_Enums__pb2 = POGOProtos_dot_Map_dot_Fort__pb2.POGOProtos_dot_Enums__pb2
from POGOProtos.Map import Pokemon_pb2 as POGOProtos_dot_Map_dot_Pokemon__pb2
POGOProtos_dot_Enums__pb2 = POGOProtos_dot_Map_dot_Pokemon__pb2.POGOProtos_dot_Enums__pb2
POGOProtos_dot_Data__pb2 = POGOProtos_dot_Map_dot_Pokemon__pb2.POGOProtos_dot_Data__pb2
POGOProtos_dot_Enums__pb2 = POGOProtos_dot_Map_dot_Pokemon__pb2.POGOProtos_dot_Enums__pb2
POGOProtos_dot_Data_dot_Player__pb2 = POGOProtos_dot_Map_dot_Pokemon__pb2.POGOProtos_dot_Data_dot_Player__pb2
POGOProtos_dot_Enums__pb2 = POGOProtos_dot_Map_dot_Pokemon__pb2.POGOProtos_dot_Enums__pb2

from POGOProtos.Map.Fort_pb2 import *
from POGOProtos.Map.Pokemon_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos.Map.proto',
  package='POGOProtos.Map',
  syntax='proto3',
  serialized_pb=_b('\n\x14POGOProtos.Map.proto\x12\x0ePOGOProtos.Map\x1a\x19POGOProtos.Map.Fort.proto\x1a\x1cPOGOProtos.Map.Pokemon.proto\"\x81\x04\n\x07MapCell\x12\x12\n\ns2_cell_id\x18\x01 \x01(\x04\x12\x1c\n\x14\x63urrent_timestamp_ms\x18\x02 \x01(\x03\x12,\n\x05\x66orts\x18\x03 \x03(\x0b\x32\x1d.POGOProtos.Map.Fort.FortData\x12\x30\n\x0cspawn_points\x18\x04 \x03(\x0b\x32\x1a.POGOProtos.Map.SpawnPoint\x12\x17\n\x0f\x64\x65leted_objects\x18\x06 \x03(\t\x12\x19\n\x11is_truncated_list\x18\x07 \x01(\x08\x12\x38\n\x0e\x66ort_summaries\x18\x08 \x03(\x0b\x32 .POGOProtos.Map.Fort.FortSummary\x12:\n\x16\x64\x65\x63imated_spawn_points\x18\t \x03(\x0b\x32\x1a.POGOProtos.Map.SpawnPoint\x12:\n\rwild_pokemons\x18\x05 \x03(\x0b\x32#.POGOProtos.Map.Pokemon.WildPokemon\x12>\n\x12\x63\x61tchable_pokemons\x18\n \x03(\x0b\x32\".POGOProtos.Map.Pokemon.MapPokemon\x12>\n\x0fnearby_pokemons\x18\x0b \x03(\x0b\x32%.POGOProtos.Map.Pokemon.NearbyPokemon\"1\n\nSpawnPoint\x12\x10\n\x08latitude\x18\x02 \x01(\x01\x12\x11\n\tlongitude\x18\x03 \x01(\x01*E\n\x10MapObjectsStatus\x12\x10\n\x0cUNSET_STATUS\x10\x00\x12\x0b\n\x07SUCCESS\x10\x01\x12\x12\n\x0eLOCATION_UNSET\x10\x02P\x00P\x01\x62\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Map_dot_Fort__pb2.DESCRIPTOR,POGOProtos_dot_Map_dot_Pokemon__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_MAPOBJECTSSTATUS = _descriptor.EnumDescriptor(
  name='MapObjectsStatus',
  full_name='POGOProtos.Map.MapObjectsStatus',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET_STATUS', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='SUCCESS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCATION_UNSET', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=664,
  serialized_end=733,
)
_sym_db.RegisterEnumDescriptor(_MAPOBJECTSSTATUS)

MapObjectsStatus = enum_type_wrapper.EnumTypeWrapper(_MAPOBJECTSSTATUS)
UNSET_STATUS = 0
SUCCESS = 1
LOCATION_UNSET = 2



_MAPCELL = _descriptor.Descriptor(
  name='MapCell',
  full_name='POGOProtos.Map.MapCell',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='s2_cell_id', full_name='POGOProtos.Map.MapCell.s2_cell_id', index=0,
      number=1, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_timestamp_ms', full_name='POGOProtos.Map.MapCell.current_timestamp_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='forts', full_name='POGOProtos.Map.MapCell.forts', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='spawn_points', full_name='POGOProtos.Map.MapCell.spawn_points', index=3,
      number=4, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deleted_objects', full_name='POGOProtos.Map.MapCell.deleted_objects', index=4,
      number=6, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_truncated_list', full_name='POGOProtos.Map.MapCell.is_truncated_list', index=5,
      number=7, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fort_summaries', full_name='POGOProtos.Map.MapCell.fort_summaries', index=6,
      number=8, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='decimated_spawn_points', full_name='POGOProtos.Map.MapCell.decimated_spawn_points', index=7,
      number=9, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='wild_pokemons', full_name='POGOProtos.Map.MapCell.wild_pokemons', index=8,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='catchable_pokemons', full_name='POGOProtos.Map.MapCell.catchable_pokemons', index=9,
      number=10, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nearby_pokemons', full_name='POGOProtos.Map.MapCell.nearby_pokemons', index=10,
      number=11, type=11, cpp_type=10, label=3,
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
  serialized_start=98,
  serialized_end=611,
)


_SPAWNPOINT = _descriptor.Descriptor(
  name='SpawnPoint',
  full_name='POGOProtos.Map.SpawnPoint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='latitude', full_name='POGOProtos.Map.SpawnPoint.latitude', index=0,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='POGOProtos.Map.SpawnPoint.longitude', index=1,
      number=3, type=1, cpp_type=5, label=1,
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
  serialized_start=613,
  serialized_end=662,
)

_MAPCELL.fields_by_name['forts'].message_type = POGOProtos_dot_Map_dot_Fort__pb2._FORTDATA
_MAPCELL.fields_by_name['spawn_points'].message_type = _SPAWNPOINT
_MAPCELL.fields_by_name['fort_summaries'].message_type = POGOProtos_dot_Map_dot_Fort__pb2._FORTSUMMARY
_MAPCELL.fields_by_name['decimated_spawn_points'].message_type = _SPAWNPOINT
_MAPCELL.fields_by_name['wild_pokemons'].message_type = POGOProtos_dot_Map_dot_Pokemon__pb2._WILDPOKEMON
_MAPCELL.fields_by_name['catchable_pokemons'].message_type = POGOProtos_dot_Map_dot_Pokemon__pb2._MAPPOKEMON
_MAPCELL.fields_by_name['nearby_pokemons'].message_type = POGOProtos_dot_Map_dot_Pokemon__pb2._NEARBYPOKEMON
DESCRIPTOR.message_types_by_name['MapCell'] = _MAPCELL
DESCRIPTOR.message_types_by_name['SpawnPoint'] = _SPAWNPOINT
DESCRIPTOR.enum_types_by_name['MapObjectsStatus'] = _MAPOBJECTSSTATUS

MapCell = _reflection.GeneratedProtocolMessageType('MapCell', (_message.Message,), dict(
  DESCRIPTOR = _MAPCELL,
  __module__ = 'POGOProtos.Map_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Map.MapCell)
  ))
_sym_db.RegisterMessage(MapCell)

SpawnPoint = _reflection.GeneratedProtocolMessageType('SpawnPoint', (_message.Message,), dict(
  DESCRIPTOR = _SPAWNPOINT,
  __module__ = 'POGOProtos.Map_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Map.SpawnPoint)
  ))
_sym_db.RegisterMessage(SpawnPoint)


# @@protoc_insertion_point(module_scope)
