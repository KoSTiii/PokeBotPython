# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos.Data.proto

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
from POGOProtos.Data import Player_pb2 as POGOProtos_dot_Data_dot_Player__pb2
POGOProtos_dot_Enums__pb2 = POGOProtos_dot_Data_dot_Player__pb2.POGOProtos_dot_Enums__pb2

from POGOProtos.Enums_pb2 import *
from POGOProtos.Data.Player_pb2 import *

DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos.Data.proto',
  package='POGOProtos.Data',
  syntax='proto3',
  serialized_pb=_b('\n\x15POGOProtos.Data.proto\x12\x0fPOGOProtos.Data\x1a\x16POGOProtos.Enums.proto\x1a\x1cPOGOProtos.Data.Player.proto\"Q\n\x10\x44ownloadUrlEntry\x12\x10\n\x08\x61sset_id\x18\x01 \x01(\t\x12\x0b\n\x03url\x18\x02 \x01(\t\x12\x0c\n\x04size\x18\x03 \x01(\x05\x12\x10\n\x08\x63hecksum\x18\x04 \x01(\r\"\x8b\x01\n\x0bPlayerBadge\x12/\n\nbadge_type\x18\x01 \x01(\x0e\x32\x1b.POGOProtos.Enums.BadgeType\x12\x0c\n\x04rank\x18\x02 \x01(\x05\x12\x13\n\x0bstart_value\x18\x03 \x01(\x05\x12\x11\n\tend_value\x18\x04 \x01(\x05\x12\x15\n\rcurrent_value\x18\x05 \x01(\x01\"\xe2\x03\n\nPlayerData\x12\x1d\n\x15\x63reation_timestamp_ms\x18\x01 \x01(\x03\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x0c\n\x04team\x18\x05 \x01(\x05\x12\x37\n\x0etutorial_state\x18\x07 \x03(\x0e\x32\x1f.POGOProtos.Enums.TutorialState\x12\x34\n\x06\x61vatar\x18\x08 \x01(\x0b\x32$.POGOProtos.Data.Player.PlayerAvatar\x12\x1b\n\x13max_pokemon_storage\x18\t \x01(\x05\x12\x18\n\x10max_item_storage\x18\n \x01(\x05\x12\x37\n\x0b\x64\x61ily_bonus\x18\x0b \x01(\x0b\x32\".POGOProtos.Data.Player.DailyBonus\x12=\n\x0e\x65quipped_badge\x18\x0c \x01(\x0b\x32%.POGOProtos.Data.Player.EquippedBadge\x12\x41\n\x10\x63ontact_settings\x18\r \x01(\x0b\x32\'.POGOProtos.Data.Player.ContactSettings\x12\x34\n\ncurrencies\x18\x0e \x03(\x0b\x32 .POGOProtos.Data.Player.Currency\"\x99\x01\n\x0cPokedexEntry\x12\x1c\n\x14pokedex_entry_number\x18\x01 \x01(\x05\x12\x19\n\x11times_encountered\x18\x02 \x01(\x05\x12\x16\n\x0etimes_captured\x18\x03 \x01(\x05\x12\x1e\n\x16\x65volution_stone_pieces\x18\x04 \x01(\x05\x12\x18\n\x10\x65volution_stones\x18\x05 \x01(\x05\"\xf5\x05\n\x0bPokemonData\x12\n\n\x02id\x18\x01 \x01(\x06\x12/\n\npokemon_id\x18\x02 \x01(\x0e\x32\x1b.POGOProtos.Enums.PokemonId\x12\n\n\x02\x63p\x18\x03 \x01(\x05\x12\x0f\n\x07stamina\x18\x04 \x01(\x05\x12\x13\n\x0bstamina_max\x18\x05 \x01(\x05\x12-\n\x06move_1\x18\x06 \x01(\x0e\x32\x1d.POGOProtos.Enums.PokemonMove\x12-\n\x06move_2\x18\x07 \x01(\x0e\x32\x1d.POGOProtos.Enums.PokemonMove\x12\x18\n\x10\x64\x65ployed_fort_id\x18\x08 \x01(\x05\x12\x12\n\nowner_name\x18\t \x01(\t\x12\x0e\n\x06is_egg\x18\n \x01(\x08\x12\x1c\n\x14\x65gg_km_walked_target\x18\x0b \x01(\x05\x12\x1b\n\x13\x65gg_km_walked_start\x18\x0c \x01(\x05\x12\x0e\n\x06origin\x18\x0e \x01(\x05\x12\x10\n\x08height_m\x18\x0f \x01(\x02\x12\x11\n\tweight_kg\x18\x10 \x01(\x02\x12\x19\n\x11individual_attack\x18\x11 \x01(\x05\x12\x1a\n\x12individual_defense\x18\x12 \x01(\x05\x12\x1a\n\x12individual_stamina\x18\x13 \x01(\x05\x12\x15\n\rcp_multiplier\x18\x14 \x01(\x05\x12\x10\n\x08pokeball\x18\x15 \x01(\x05\x12\x18\n\x10\x63\x61ptured_cell_id\x18\x16 \x01(\x04\x12\x18\n\x10\x62\x61ttles_attacked\x18\x17 \x01(\x05\x12\x18\n\x10\x62\x61ttles_defended\x18\x18 \x01(\x05\x12\x18\n\x10\x65gg_incubator_id\x18\x19 \x01(\x05\x12\x18\n\x10\x63reation_time_ms\x18\x1a \x01(\x04\x12\x14\n\x0cnum_upgrades\x18\x1b \x01(\x05\x12 \n\x18\x61\x64\x64itional_cp_multiplier\x18\x1c \x01(\x05\x12\x10\n\x08\x66\x61vorite\x18\x1d \x01(\x05\x12\x10\n\x08nickname\x18\x1e \x01(\t\x12\x11\n\tfrom_fort\x18\x1f \x01(\x05P\x00P\x01\x62\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Enums__pb2.DESCRIPTOR,POGOProtos_dot_Data_dot_Player__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_DOWNLOADURLENTRY = _descriptor.Descriptor(
  name='DownloadUrlEntry',
  full_name='POGOProtos.Data.DownloadUrlEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='asset_id', full_name='POGOProtos.Data.DownloadUrlEntry.asset_id', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='url', full_name='POGOProtos.Data.DownloadUrlEntry.url', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='size', full_name='POGOProtos.Data.DownloadUrlEntry.size', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='checksum', full_name='POGOProtos.Data.DownloadUrlEntry.checksum', index=3,
      number=4, type=13, cpp_type=3, label=1,
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
  serialized_start=96,
  serialized_end=177,
)


_PLAYERBADGE = _descriptor.Descriptor(
  name='PlayerBadge',
  full_name='POGOProtos.Data.PlayerBadge',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='badge_type', full_name='POGOProtos.Data.PlayerBadge.badge_type', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='rank', full_name='POGOProtos.Data.PlayerBadge.rank', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='start_value', full_name='POGOProtos.Data.PlayerBadge.start_value', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end_value', full_name='POGOProtos.Data.PlayerBadge.end_value', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='current_value', full_name='POGOProtos.Data.PlayerBadge.current_value', index=4,
      number=5, type=1, cpp_type=5, label=1,
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
  serialized_start=180,
  serialized_end=319,
)


_PLAYERDATA = _descriptor.Descriptor(
  name='PlayerData',
  full_name='POGOProtos.Data.PlayerData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='creation_timestamp_ms', full_name='POGOProtos.Data.PlayerData.creation_timestamp_ms', index=0,
      number=1, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='username', full_name='POGOProtos.Data.PlayerData.username', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='team', full_name='POGOProtos.Data.PlayerData.team', index=2,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='tutorial_state', full_name='POGOProtos.Data.PlayerData.tutorial_state', index=3,
      number=7, type=14, cpp_type=8, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='avatar', full_name='POGOProtos.Data.PlayerData.avatar', index=4,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_pokemon_storage', full_name='POGOProtos.Data.PlayerData.max_pokemon_storage', index=5,
      number=9, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='max_item_storage', full_name='POGOProtos.Data.PlayerData.max_item_storage', index=6,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='daily_bonus', full_name='POGOProtos.Data.PlayerData.daily_bonus', index=7,
      number=11, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='equipped_badge', full_name='POGOProtos.Data.PlayerData.equipped_badge', index=8,
      number=12, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='contact_settings', full_name='POGOProtos.Data.PlayerData.contact_settings', index=9,
      number=13, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='currencies', full_name='POGOProtos.Data.PlayerData.currencies', index=10,
      number=14, type=11, cpp_type=10, label=3,
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
  serialized_start=322,
  serialized_end=804,
)


_POKEDEXENTRY = _descriptor.Descriptor(
  name='PokedexEntry',
  full_name='POGOProtos.Data.PokedexEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pokedex_entry_number', full_name='POGOProtos.Data.PokedexEntry.pokedex_entry_number', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='times_encountered', full_name='POGOProtos.Data.PokedexEntry.times_encountered', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='times_captured', full_name='POGOProtos.Data.PokedexEntry.times_captured', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='evolution_stone_pieces', full_name='POGOProtos.Data.PokedexEntry.evolution_stone_pieces', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='evolution_stones', full_name='POGOProtos.Data.PokedexEntry.evolution_stones', index=4,
      number=5, type=5, cpp_type=1, label=1,
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
  serialized_start=807,
  serialized_end=960,
)


_POKEMONDATA = _descriptor.Descriptor(
  name='PokemonData',
  full_name='POGOProtos.Data.PokemonData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='id', full_name='POGOProtos.Data.PokemonData.id', index=0,
      number=1, type=6, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokemon_id', full_name='POGOProtos.Data.PokemonData.pokemon_id', index=1,
      number=2, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cp', full_name='POGOProtos.Data.PokemonData.cp', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stamina', full_name='POGOProtos.Data.PokemonData.stamina', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stamina_max', full_name='POGOProtos.Data.PokemonData.stamina_max', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='move_1', full_name='POGOProtos.Data.PokemonData.move_1', index=5,
      number=6, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='move_2', full_name='POGOProtos.Data.PokemonData.move_2', index=6,
      number=7, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='deployed_fort_id', full_name='POGOProtos.Data.PokemonData.deployed_fort_id', index=7,
      number=8, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='owner_name', full_name='POGOProtos.Data.PokemonData.owner_name', index=8,
      number=9, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='is_egg', full_name='POGOProtos.Data.PokemonData.is_egg', index=9,
      number=10, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='egg_km_walked_target', full_name='POGOProtos.Data.PokemonData.egg_km_walked_target', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='egg_km_walked_start', full_name='POGOProtos.Data.PokemonData.egg_km_walked_start', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='origin', full_name='POGOProtos.Data.PokemonData.origin', index=12,
      number=14, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='height_m', full_name='POGOProtos.Data.PokemonData.height_m', index=13,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='weight_kg', full_name='POGOProtos.Data.PokemonData.weight_kg', index=14,
      number=16, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='individual_attack', full_name='POGOProtos.Data.PokemonData.individual_attack', index=15,
      number=17, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='individual_defense', full_name='POGOProtos.Data.PokemonData.individual_defense', index=16,
      number=18, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='individual_stamina', full_name='POGOProtos.Data.PokemonData.individual_stamina', index=17,
      number=19, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='cp_multiplier', full_name='POGOProtos.Data.PokemonData.cp_multiplier', index=18,
      number=20, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='pokeball', full_name='POGOProtos.Data.PokemonData.pokeball', index=19,
      number=21, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='captured_cell_id', full_name='POGOProtos.Data.PokemonData.captured_cell_id', index=20,
      number=22, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battles_attacked', full_name='POGOProtos.Data.PokemonData.battles_attacked', index=21,
      number=23, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='battles_defended', full_name='POGOProtos.Data.PokemonData.battles_defended', index=22,
      number=24, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='egg_incubator_id', full_name='POGOProtos.Data.PokemonData.egg_incubator_id', index=23,
      number=25, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='creation_time_ms', full_name='POGOProtos.Data.PokemonData.creation_time_ms', index=24,
      number=26, type=4, cpp_type=4, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='num_upgrades', full_name='POGOProtos.Data.PokemonData.num_upgrades', index=25,
      number=27, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='additional_cp_multiplier', full_name='POGOProtos.Data.PokemonData.additional_cp_multiplier', index=26,
      number=28, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='favorite', full_name='POGOProtos.Data.PokemonData.favorite', index=27,
      number=29, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='nickname', full_name='POGOProtos.Data.PokemonData.nickname', index=28,
      number=30, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='from_fort', full_name='POGOProtos.Data.PokemonData.from_fort', index=29,
      number=31, type=5, cpp_type=1, label=1,
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
  serialized_start=963,
  serialized_end=1720,
)

_PLAYERBADGE.fields_by_name['badge_type'].enum_type = POGOProtos_dot_Enums__pb2._BADGETYPE
_PLAYERDATA.fields_by_name['tutorial_state'].enum_type = POGOProtos_dot_Enums__pb2._TUTORIALSTATE
_PLAYERDATA.fields_by_name['avatar'].message_type = POGOProtos_dot_Data_dot_Player__pb2._PLAYERAVATAR
_PLAYERDATA.fields_by_name['daily_bonus'].message_type = POGOProtos_dot_Data_dot_Player__pb2._DAILYBONUS
_PLAYERDATA.fields_by_name['equipped_badge'].message_type = POGOProtos_dot_Data_dot_Player__pb2._EQUIPPEDBADGE
_PLAYERDATA.fields_by_name['contact_settings'].message_type = POGOProtos_dot_Data_dot_Player__pb2._CONTACTSETTINGS
_PLAYERDATA.fields_by_name['currencies'].message_type = POGOProtos_dot_Data_dot_Player__pb2._CURRENCY
_POKEMONDATA.fields_by_name['pokemon_id'].enum_type = POGOProtos_dot_Enums__pb2._POKEMONID
_POKEMONDATA.fields_by_name['move_1'].enum_type = POGOProtos_dot_Enums__pb2._POKEMONMOVE
_POKEMONDATA.fields_by_name['move_2'].enum_type = POGOProtos_dot_Enums__pb2._POKEMONMOVE
DESCRIPTOR.message_types_by_name['DownloadUrlEntry'] = _DOWNLOADURLENTRY
DESCRIPTOR.message_types_by_name['PlayerBadge'] = _PLAYERBADGE
DESCRIPTOR.message_types_by_name['PlayerData'] = _PLAYERDATA
DESCRIPTOR.message_types_by_name['PokedexEntry'] = _POKEDEXENTRY
DESCRIPTOR.message_types_by_name['PokemonData'] = _POKEMONDATA

DownloadUrlEntry = _reflection.GeneratedProtocolMessageType('DownloadUrlEntry', (_message.Message,), dict(
  DESCRIPTOR = _DOWNLOADURLENTRY,
  __module__ = 'POGOProtos.Data_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Data.DownloadUrlEntry)
  ))
_sym_db.RegisterMessage(DownloadUrlEntry)

PlayerBadge = _reflection.GeneratedProtocolMessageType('PlayerBadge', (_message.Message,), dict(
  DESCRIPTOR = _PLAYERBADGE,
  __module__ = 'POGOProtos.Data_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Data.PlayerBadge)
  ))
_sym_db.RegisterMessage(PlayerBadge)

PlayerData = _reflection.GeneratedProtocolMessageType('PlayerData', (_message.Message,), dict(
  DESCRIPTOR = _PLAYERDATA,
  __module__ = 'POGOProtos.Data_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Data.PlayerData)
  ))
_sym_db.RegisterMessage(PlayerData)

PokedexEntry = _reflection.GeneratedProtocolMessageType('PokedexEntry', (_message.Message,), dict(
  DESCRIPTOR = _POKEDEXENTRY,
  __module__ = 'POGOProtos.Data_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Data.PokedexEntry)
  ))
_sym_db.RegisterMessage(PokedexEntry)

PokemonData = _reflection.GeneratedProtocolMessageType('PokemonData', (_message.Message,), dict(
  DESCRIPTOR = _POKEMONDATA,
  __module__ = 'POGOProtos.Data_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Data.PokemonData)
  ))
_sym_db.RegisterMessage(PokemonData)


# @@protoc_insertion_point(module_scope)
