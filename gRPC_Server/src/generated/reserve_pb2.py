# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/messages/information/reserve.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)protos/messages/information/reserve.proto\x12\x0binformation\"S\n\x0eReserveRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x03 \x01(\t\x12\x10\n\x08\x64\x61tetime\x18\x04 \x01(\t\"!\n\x0fReserveResponse\x12\x0e\n\x06status\x18\x01 \x01(\x08\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'protos.messages.information.reserve_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_RESERVEREQUEST']._serialized_start=58
  _globals['_RESERVEREQUEST']._serialized_end=141
  _globals['_RESERVERESPONSE']._serialized_start=143
  _globals['_RESERVERESPONSE']._serialized_end=176
# @@protoc_insertion_point(module_scope)
