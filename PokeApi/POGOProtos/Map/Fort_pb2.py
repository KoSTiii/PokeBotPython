# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos.Map.Fort.proto

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
  name='POGOProtos.Map.Fort.proto',
  package='POGOProtos.Map.Fort',
  syntax='proto3',
  serialized_pb=_b('\n\x19POGOProtos.Map.Fort.proto\x12\x13POGOProtos.Map.Fort\x1a\x16POGOProtos.Enums.proto\x1a\x1aPOGOProtos.Inventory.proto\"\xbb\x04\n\x08\x46ortData\x12\n\n\x02id\x18\x01 \x01(\t\x12\"\n\x1alast_modified_timestamp_ms\x18\x02 \x01(\x03\x12\x10\n\x08latitude\x18\x03 \x01(\x01\x12\x11\n\tlongitude\x18\x04 \x01(\x01\x12\x0f\n\x07\x65nabled\x18\x08 \x01(\x08\x12+\n\x04type\x18\t \x01(\x0e\x32\x1d.POGOProtos.Map.Fort.FortType\x12\x32\n\rowned_by_team\x18\x05 \x01(\x0e\x32\x1b.POGOProtos.Enums.TeamColor\x12\x35\n\x10guard_pokemon_id\x18\x06 \x01(\x0e\x32\x1b.POGOProtos.Enums.PokemonId\x12\x18\n\x10guard_pokemon_cp\x18\x07 \x01(\x05\x12\x12\n\ngym_points\x18\n \x01(\x03\x12\x14\n\x0cis_in_battle\x18\x0b \x01(\x08\x12&\n\x1e\x63ooldown_complete_timestamp_ms\x18\x0e \x01(\x03\x12\x31\n\x07sponsor\x18\x0f \x01(\x0e\x32 .POGOProtos.Map.Fort.FortSponsor\x12>\n\x0erendering_type\x18\x10 \x01(\x0e\x32&.POGOProtos.Map.Fort.FortRenderingType\x12\x1c\n\x14\x61\x63tive_fort_modifier\x18\x0c \x01(\x0c\x12\x34\n\tlure_info\x18\r \x01(\x0b\x32!.POGOProtos.Map.Fort.FortLureInfo\"\x8c\x01\n\x0c\x46ortLureInfo\x12\x0f\n\x07\x66ort_id\x18\x01 \x01(\t\x12\x10\n\x08unknown2\x18\x02 \x01(\x01\x12\x36\n\x11\x61\x63tive_pokemon_id\x18\x03 \x01(\x0e\x32\x1b.POGOProtos.Enums.PokemonId\x12!\n\x19lure_expires_timestamp_ms\x18\x04 \x01(\x03\"\x80\x01\n\x0c\x46ortModifier\x12-\n\x07item_id\x18\x01 \x01(\x0e\x32\x1c.POGOProtos.Inventory.ItemId\x12\x1f\n\x17\x65xpiration_timestamp_ms\x18\x02 \x01(\x03\x12 \n\x18\x64\x65ployer_player_codename\x18\x03 \x01(\t\"o\n\x0b\x46ortSummary\x12\x17\n\x0f\x66ort_summary_id\x18\x01 \x01(\x05\x12\"\n\x1alast_modified_timestamp_ms\x18\x02 \x01(\x05\x12\x10\n\x08latitude\x18\x03 \x01(\x05\x12\x11\n\tlongitude\x18\x04 \x01(\x05*3\n\x11\x46ortRenderingType\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\x11\n\rINTERNAL_TEST\x10\x01*B\n\x0b\x46ortSponsor\x12\x11\n\rUNSET_SPONSOR\x10\x00\x12\r\n\tMCDONALDS\x10\x01\x12\x11\n\rPOKEMON_STORE\x10\x02*#\n\x08\x46ortType\x12\x07\n\x03GYM\x10\x00\x12\x0e\n\nCHECKPOINT\x10\x01P\x00P\x01\x62\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Enums__pb2.DESCRIPTOR,POGOProtos_dot_Inventory__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

_FORTRENDERINGTYPE = _descriptor.EnumDescriptor(
  name='FortRenderingType',
  full_name='POGOProtos.Map.Fort.FortRenderingType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DEFAULT', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='INTERNAL_TEST', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1063,
  serialized_end=1114,
)
_sym_db.RegisterEnumDescriptor(_FORTRENDERINGTYPE)

FortRenderingType = enum_type_wrapper.EnumTypeWrapper(_FORTRENDERINGTYPE)
_FORTSPONSOR = _descriptor.EnumDescriptor(
  name='FortSponsor',
  full_name='POGOProtos.Map.Fort.FortSponsor',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='UNSET_SPONSOR', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='MCDONALDS', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='POKEMON_STORE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1116,
  serialized_end=1182,
)
_sym_db.RegisterEnumDescriptor(_FORTSPONSOR)

FortSponsor = enum_type_wrapper.EnumTypeWrapper(_FORTSPONSOR)
_FORTTYPE = _descriptor.EnumDescriptor(
  name='FortType',
  full_name='POGOProtos.Map.Fort.FortType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='GYM', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CHECKPOINT', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=1184,
  serialized_end=1219,
)
_sym_db.RegisterEnumDescriptor(_FORTTYPE)

FortType = enum_type_wrapper.EnumTypeWrapper(_FORTTYPE)
DEFAULT = 0
INTERNAL_TEST = 1
UNSET_SPONSOR = 0
MCDONALDS = 1
POKEMON_STORE = 2
GYM = 0
CHECKPOINT = 1



_FORTDATA = _descriptor.Descriptor(
  name='FortData',
  full_name='POGOProtos.Map.Fort.FortData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='POGOProtos.Map.Fort.FortData.id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_modified_timestamp_ms', full_name='POGOProtos.Map.Fort.FortData.last_modified_timestamp_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='POGOProtos.Map.Fort.FortData.latitude', index=2,
      number=3, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='POGOProtos.Map.Fort.FortData.longitude', index=3,
      number=4, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='enabled', full_name='POGOProtos.Map.Fort.FortData.enabled', index=4,
      number=8, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='POGOProtos.Map.Fort.FortData.type', index=5,
      number=9, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='owned_by_team', full_name='POGOProtos.Map.Fort.FortData.owned_by_team', index=6,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='guard_pokemon_id', full_name='POGOProtos.Map.Fort.FortData.guard_pokemon_id', index=7,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='guard_pokemon_cp', full_name='POGOProtos.Map.Fort.FortData.guard_pokemon_cp', index=8,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='gym_points', full_name='POGOProtos.Map.Fort.FortData.gym_points', index=9,
      number=10, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_in_battle', full_name='POGOProtos.Map.Fort.FortData.is_in_battle', index=10,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cooldown_complete_timestamp_ms', full_name='POGOProtos.Map.Fort.FortData.cooldown_complete_timestamp_ms', index=11,
      number=14, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='sponsor', full_name='POGOProtos.Map.Fort.FortData.sponsor', index=12,
      number=15, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rendering_type', full_name='POGOProtos.Map.Fort.FortData.rendering_type', index=13,
      number=16, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='active_fort_modifier', full_name='POGOProtos.Map.Fort.FortData.active_fort_modifier', index=14,
      number=12, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lure_info', full_name='POGOProtos.Map.Fort.FortData.lure_info', index=15,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
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
  serialized_start=103,
  serialized_end=674,
)


_FORTLUREINFO = _descriptor.Descriptor(
  name='FortLureInfo',
  full_name='POGOProtos.Map.Fort.FortLureInfo',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fort_id', full_name='POGOProtos.Map.Fort.FortLureInfo.fort_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='unknown2', full_name='POGOProtos.Map.Fort.FortLureInfo.unknown2', index=1,
      number=2, type=1, cpp_type=5, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='active_pokemon_id', full_name='POGOProtos.Map.Fort.FortLureInfo.active_pokemon_id', index=2,
      number=3, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='lure_expires_timestamp_ms', full_name='POGOProtos.Map.Fort.FortLureInfo.lure_expires_timestamp_ms', index=3,
      number=4, type=3, cpp_type=2, label=1,
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
  serialized_start=677,
  serialized_end=817,
)


_FORTMODIFIER = _descriptor.Descriptor(
  name='FortModifier',
  full_name='POGOProtos.Map.Fort.FortModifier',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='item_id', full_name='POGOProtos.Map.Fort.FortModifier.item_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='expiration_timestamp_ms', full_name='POGOProtos.Map.Fort.FortModifier.expiration_timestamp_ms', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deployer_player_codename', full_name='POGOProtos.Map.Fort.FortModifier.deployer_player_codename', index=2,
      number=3, type=9, cpp_type=9, label=1,
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
  serialized_start=820,
  serialized_end=948,
)


_FORTSUMMARY = _descriptor.Descriptor(
  name='FortSummary',
  full_name='POGOProtos.Map.Fort.FortSummary',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fort_summary_id', full_name='POGOProtos.Map.Fort.FortSummary.fort_summary_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last_modified_timestamp_ms', full_name='POGOProtos.Map.Fort.FortSummary.last_modified_timestamp_ms', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='latitude', full_name='POGOProtos.Map.Fort.FortSummary.latitude', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='longitude', full_name='POGOProtos.Map.Fort.FortSummary.longitude', index=3,
      number=4, type=5, cpp_type=1, label=1,
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
  serialized_start=950,
  serialized_end=1061,
)

_FORTDATA.fields_by_name['type'].enum_type = _FORTTYPE
_FORTDATA.fields_by_name['owned_by_team'].enum_type = POGOProtos_dot_Enums__pb2._TEAMCOLOR
_FORTDATA.fields_by_name['guard_pokemon_id'].enum_type = POGOProtos_dot_Enums__pb2._POKEMONID
_FORTDATA.fields_by_name['sponsor'].enum_type = _FORTSPONSOR
_FORTDATA.fields_by_name['rendering_type'].enum_type = _FORTRENDERINGTYPE
_FORTDATA.fields_by_name['lure_info'].message_type = _FORTLUREINFO
_FORTLUREINFO.fields_by_name['active_pokemon_id'].enum_type = POGOProtos_dot_Enums__pb2._POKEMONID
_FORTMODIFIER.fields_by_name['item_id'].enum_type = POGOProtos_dot_Inventory__pb2._ITEMID
DESCRIPTOR.message_types_by_name['FortData'] = _FORTDATA
DESCRIPTOR.message_types_by_name['FortLureInfo'] = _FORTLUREINFO
DESCRIPTOR.message_types_by_name['FortModifier'] = _FORTMODIFIER
DESCRIPTOR.message_types_by_name['FortSummary'] = _FORTSUMMARY
DESCRIPTOR.enum_types_by_name['FortRenderingType'] = _FORTRENDERINGTYPE
DESCRIPTOR.enum_types_by_name['FortSponsor'] = _FORTSPONSOR
DESCRIPTOR.enum_types_by_name['FortType'] = _FORTTYPE

FortData = _reflection.GeneratedProtocolMessageType('FortData', (_message.Message,), dict(
  DESCRIPTOR = _FORTDATA,
  __module__ = 'POGOProtos.Map.Fort_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Map.Fort.FortData)
  ))
_sym_db.RegisterMessage(FortData)

FortLureInfo = _reflection.GeneratedProtocolMessageType('FortLureInfo', (_message.Message,), dict(
  DESCRIPTOR = _FORTLUREINFO,
  __module__ = 'POGOProtos.Map.Fort_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Map.Fort.FortLureInfo)
  ))
_sym_db.RegisterMessage(FortLureInfo)

FortModifier = _reflection.GeneratedProtocolMessageType('FortModifier', (_message.Message,), dict(
  DESCRIPTOR = _FORTMODIFIER,
  __module__ = 'POGOProtos.Map.Fort_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Map.Fort.FortModifier)
  ))
_sym_db.RegisterMessage(FortModifier)

FortSummary = _reflection.GeneratedProtocolMessageType('FortSummary', (_message.Message,), dict(
  DESCRIPTOR = _FORTSUMMARY,
  __module__ = 'POGOProtos.Map.Fort_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Map.Fort.FortSummary)
  ))
_sym_db.RegisterMessage(FortSummary)


# @@protoc_insertion_point(module_scope)
