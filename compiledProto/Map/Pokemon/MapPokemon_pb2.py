# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Map/Pokemon/MapPokemon.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from Enums import PokemonType_pb2 as Enums_dot_PokemonType__pb2

from Enums.PokemonType_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='Map/Pokemon/MapPokemon.proto',
  package='POGOProtos.Map.Pokemon',
  syntax='proto3',
  serialized_pb=_b('\n\x1cMap/Pokemon/MapPokemon.proto\x12\x16POGOProtos.Map.Pokemon\x1a\x17\x45nums/PokemonType.proto\"\xb4\x01\n\nMapPokemon\x12\x15\n\rspawnpoint_id\x18\x01 \x01(\t\x12\x14\n\x0c\x65ncounter_id\x18\x02 \x01(\x06\x12\x33\n\x0cpokemon_type\x18\x03 \x01(\x0e\x32\x1d.POGOProtos.Enums.PokemonType\x12\x1f\n\x17\x65xpiration_timestamp_ms\x18\x04 \x01(\x03\x12\x10\n\x08latitude\x18\x05 \x01(\x01\x12\x11\n\tlongitude\x18\x06 \x01(\x01P\x00\x62\x06proto3')
  ,
  dependencies=[Enums_dot_PokemonType__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_MAPPOKEMON = _descriptor.Descriptor(
  name='MapPokemon',
  full_name='POGOProtos.Map.Pokemon.MapPokemon',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='spawnpoint_id', full_name='POGOProtos.Map.Pokemon.MapPokemon.spawnpoint_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='encounter_id', full_name='POGOProtos.Map.Pokemon.MapPokemon.encounter_id', index=1,
      number=2, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_type', full_name='POGOProtos.Map.Pokemon.MapPokemon.pokemon_type', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expiration_timestamp_ms', full_name='POGOProtos.Map.Pokemon.MapPokemon.expiration_timestamp_ms', index=3,
      number=4, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='POGOProtos.Map.Pokemon.MapPokemon.latitude', index=4,
      number=5, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='POGOProtos.Map.Pokemon.MapPokemon.longitude', index=5,
      number=6, type=1, cpp_type=5, label=1,
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
  serialized_start=82,
  serialized_end=262,
)

_MAPPOKEMON.fields_by_name['pokemon_type'].enum_type = Enums_dot_PokemonType__pb2._POKEMONTYPE
DESCRIPTOR.message_types_by_name['MapPokemon'] = _MAPPOKEMON

MapPokemon = _reflection.GeneratedProtocolMessageType('MapPokemon', (_message.Message,), dict(
  DESCRIPTOR = _MAPPOKEMON,
  __module__ = 'Map.Pokemon.MapPokemon_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Map.Pokemon.MapPokemon)
  ))
_sym_db.RegisterMessage(MapPokemon)


# @@protoc_insertion_point(module_scope)
