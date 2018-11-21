# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: AttributeSerializer.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import GameBalance_pb2 as GameBalance__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='AttributeSerializer.proto',
  package='D3.AttributeSerializer',
  syntax='proto2',
  serialized_options=None,
  serialized_pb=_b('\n\x19\x41ttributeSerializer.proto\x12\x16\x44\x33.AttributeSerializer\x1a\x11GameBalance.proto\",\n\x0eSavedAttribute\x12\x0b\n\x03key\x18\x01 \x02(\x11\x12\r\n\x05value\x18\x02 \x02(\x11\"x\n\x0fSavedAttributes\x12)\n\tgb_handle\x18\x01 \x01(\x0b\x32\x16.D3.GameBalance.Handle\x12:\n\nattributes\x18\x02 \x03(\x0b\x32&.D3.AttributeSerializer.SavedAttribute')
  ,
  dependencies=[GameBalance__pb2.DESCRIPTOR,])




_SAVEDATTRIBUTE = _descriptor.Descriptor(
  name='SavedAttribute',
  full_name='D3.AttributeSerializer.SavedAttribute',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='D3.AttributeSerializer.SavedAttribute.key', index=0,
      number=1, type=17, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='D3.AttributeSerializer.SavedAttribute.value', index=1,
      number=2, type=17, cpp_type=1, label=2,
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=72,
  serialized_end=116,
)


_SAVEDATTRIBUTES = _descriptor.Descriptor(
  name='SavedAttributes',
  full_name='D3.AttributeSerializer.SavedAttributes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='gb_handle', full_name='D3.AttributeSerializer.SavedAttributes.gb_handle', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='attributes', full_name='D3.AttributeSerializer.SavedAttributes.attributes', index=1,
      number=2, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
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
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=118,
  serialized_end=238,
)

_SAVEDATTRIBUTES.fields_by_name['gb_handle'].message_type = GameBalance__pb2._HANDLE
_SAVEDATTRIBUTES.fields_by_name['attributes'].message_type = _SAVEDATTRIBUTE
DESCRIPTOR.message_types_by_name['SavedAttribute'] = _SAVEDATTRIBUTE
DESCRIPTOR.message_types_by_name['SavedAttributes'] = _SAVEDATTRIBUTES
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

SavedAttribute = _reflection.GeneratedProtocolMessageType('SavedAttribute', (_message.Message,), dict(
  DESCRIPTOR = _SAVEDATTRIBUTE,
  __module__ = 'AttributeSerializer_pb2'
  # @@protoc_insertion_point(class_scope:D3.AttributeSerializer.SavedAttribute)
  ))
_sym_db.RegisterMessage(SavedAttribute)

SavedAttributes = _reflection.GeneratedProtocolMessageType('SavedAttributes', (_message.Message,), dict(
  DESCRIPTOR = _SAVEDATTRIBUTES,
  __module__ = 'AttributeSerializer_pb2'
  # @@protoc_insertion_point(class_scope:D3.AttributeSerializer.SavedAttributes)
  ))
_sym_db.RegisterMessage(SavedAttributes)


# @@protoc_insertion_point(module_scope)
