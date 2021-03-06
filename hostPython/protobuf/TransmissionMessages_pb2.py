# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: TransmissionMessages.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='TransmissionMessages.proto',
  package='',
  syntax='proto2',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\x1aTransmissionMessages.proto\"\xaf\x02\n\tIOControl\x12/\n\rtypeOfControl\x18\x01 \x02(\x0e\x32\x18.IOControl.TypeOfControl\x12\x12\n\ndigitalPin\x18\x02 \x01(\x05\x12\x11\n\tanalogPin\x18\x03 \x01(\x05\x12=\n\rcheckResponse\x18\x04 \x01(\x0e\x32\x18.IOControl.CheckResponse:\x0cSUCCESSFULLY\"S\n\rTypeOfControl\x12\x0f\n\x0b\x41NALOGWRITE\x10\x01\x12\x10\n\x0c\x44IGITALWRITE\x10\x02\x12\x0e\n\nANALOGREAD\x10\x03\x12\x0f\n\x0b\x44IGITALREAD\x10\x04\"6\n\rCheckResponse\x12\x13\n\x0fNONSUCCESSFULLY\x10\x00\x12\x10\n\x0cSUCCESSFULLY\x10\x01\":\n\x05Stats\x12\r\n\x05value\x18\x01 \x02(\x05\x12\x13\n\x0bmbedVersion\x18\x02 \x01(\x05\x12\r\n\x05\x63puId\x18\x03 \x01(\x05\"\x1a\n\x07RawData\x12\x0f\n\x07rawcomm\x18\x01 \x02(\t'
)



_IOCONTROL_TYPEOFCONTROL = _descriptor.EnumDescriptor(
  name='TypeOfControl',
  full_name='IOControl.TypeOfControl',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ANALOGWRITE', index=0, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DIGITALWRITE', index=1, number=2,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='ANALOGREAD', index=2, number=3,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='DIGITALREAD', index=3, number=4,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=195,
  serialized_end=278,
)
_sym_db.RegisterEnumDescriptor(_IOCONTROL_TYPEOFCONTROL)

_IOCONTROL_CHECKRESPONSE = _descriptor.EnumDescriptor(
  name='CheckResponse',
  full_name='IOControl.CheckResponse',
  filename=None,
  file=DESCRIPTOR,
  create_key=_descriptor._internal_create_key,
  values=[
    _descriptor.EnumValueDescriptor(
      name='NONSUCCESSFULLY', index=0, number=0,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
    _descriptor.EnumValueDescriptor(
      name='SUCCESSFULLY', index=1, number=1,
      serialized_options=None,
      type=None,
      create_key=_descriptor._internal_create_key),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=280,
  serialized_end=334,
)
_sym_db.RegisterEnumDescriptor(_IOCONTROL_CHECKRESPONSE)


_IOCONTROL = _descriptor.Descriptor(
  name='IOControl',
  full_name='IOControl',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='typeOfControl', full_name='IOControl.typeOfControl', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='digitalPin', full_name='IOControl.digitalPin', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='analogPin', full_name='IOControl.analogPin', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='checkResponse', full_name='IOControl.checkResponse', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _IOCONTROL_TYPEOFCONTROL,
    _IOCONTROL_CHECKRESPONSE,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=31,
  serialized_end=334,
)


_STATS = _descriptor.Descriptor(
  name='Stats',
  full_name='Stats',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='value', full_name='Stats.value', index=0,
      number=1, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='mbedVersion', full_name='Stats.mbedVersion', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='cpuId', full_name='Stats.cpuId', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=336,
  serialized_end=394,
)


_RAWDATA = _descriptor.Descriptor(
  name='RawData',
  full_name='RawData',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='rawcomm', full_name='RawData.rawcomm', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=396,
  serialized_end=422,
)

_IOCONTROL.fields_by_name['typeOfControl'].enum_type = _IOCONTROL_TYPEOFCONTROL
_IOCONTROL.fields_by_name['checkResponse'].enum_type = _IOCONTROL_CHECKRESPONSE
_IOCONTROL_TYPEOFCONTROL.containing_type = _IOCONTROL
_IOCONTROL_CHECKRESPONSE.containing_type = _IOCONTROL
DESCRIPTOR.message_types_by_name['IOControl'] = _IOCONTROL
DESCRIPTOR.message_types_by_name['Stats'] = _STATS
DESCRIPTOR.message_types_by_name['RawData'] = _RAWDATA
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

IOControl = _reflection.GeneratedProtocolMessageType('IOControl', (_message.Message,), {
  'DESCRIPTOR' : _IOCONTROL,
  '__module__' : 'TransmissionMessages_pb2'
  # @@protoc_insertion_point(class_scope:IOControl)
  })
_sym_db.RegisterMessage(IOControl)

Stats = _reflection.GeneratedProtocolMessageType('Stats', (_message.Message,), {
  'DESCRIPTOR' : _STATS,
  '__module__' : 'TransmissionMessages_pb2'
  # @@protoc_insertion_point(class_scope:Stats)
  })
_sym_db.RegisterMessage(Stats)

RawData = _reflection.GeneratedProtocolMessageType('RawData', (_message.Message,), {
  'DESCRIPTOR' : _RAWDATA,
  '__module__' : 'TransmissionMessages_pb2'
  # @@protoc_insertion_point(class_scope:RawData)
  })
_sym_db.RegisterMessage(RawData)


# @@protoc_insertion_point(module_scope)
