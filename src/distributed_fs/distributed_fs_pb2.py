# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: distributed_fs.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14\x64istributed_fs.proto\"!\n\rCreateRequest\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\"\x10\n\x0e\x43reateResponse\"\r\n\x0bListRequest\"\x1d\n\x0cListResponse\x12\r\n\x05\x66iles\x18\x01 \x03(\t\"\x1f\n\x0bReadRequest\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\"3\n\x0cReadResponse\x12\x13\n\x0b\x66ilecontent\x18\x01 \x01(\t\x12\x0e\n\x06status\x18\x02 \x01(\t\"I\n\rUpdateRequest\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x13\n\x0b\x66ilecontent\x18\x02 \x01(\t\x12\x11\n\toverwrite\x18\x03 \x01(\x08\" \n\x0eUpdateResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"!\n\rDeleteRequest\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\" \n\x0e\x44\x65leteResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"\"\n\x0eRestoreRequest\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\"\x11\n\x0fRestoreResponse\"K\n\x11PermissionRequest\x12\x10\n\x08\x66ilename\x18\x01 \x01(\t\x12\x10\n\x08hostname\x18\x02 \x01(\t\x12\x12\n\npermission\x18\x03 \x01(\t\"$\n\x12PermissionResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"\x16\n\x14\x43reateNodeKeyRequest\"\'\n\x15\x43reateNodeKeyResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"\\\n\x14ReplicateFileRequest\x12\x0e\n\x06\x66ileId\x18\x01 \x01(\t\x12\x10\n\x08\x66ileName\x18\x02 \x01(\t\x12\r\n\x05owner\x18\x03 \x01(\t\x12\x13\n\x0b\x66ileContent\x18\x04 \x01(\t\"\'\n\x15ReplicateFileResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"N\n\x16ReplicateUpdateRequest\x12\x0e\n\x06\x66ileId\x18\x01 \x01(\t\x12\x13\n\x0b\x66ileContent\x18\x02 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x03 \x01(\t\")\n\x17ReplicateUpdateResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"[\n\x1aReplicatePermissionRequest\x12\x0e\n\x06\x66ileId\x18\x01 \x01(\t\x12\x15\n\rfilePublicKey\x18\x02 \x01(\t\x12\x16\n\x0e\x66ilePrivateKey\x18\x03 \x01(\t\"-\n\x1bReplicatePermissionResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"(\n\x16ReplicateDeleteRequest\x12\x0e\n\x06\x66ileId\x18\x01 \x01(\t\")\n\x17ReplicateDeleteResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"+\n\x17ReplicateRestoreRequest\x12\x10\n\x08\x66ilePath\x18\x01 \x01(\t\"\x1a\n\x18ReplicateRestoreResponse\"H\n\x10UpdateKeyRequest\x12\x10\n\x08hostname\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\x12\x11\n\tpublicKey\x18\x03 \x01(\t\"#\n\x11UpdateKeyResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\"2\n\x0f\x46ileLockRequest\x12\x0e\n\x06\x66ileId\x18\x01 \x01(\t\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\"\'\n\x10\x46ileLockResponse\x12\x13\n\x0blockGranted\x18\x01 \x01(\x08\x32\xa7\x07\n\x15\x44istributedFileSystem\x12/\n\nCreateFile\x12\x0e.CreateRequest\x1a\x0f.CreateResponse\"\x00\x12*\n\tListFiles\x12\x0c.ListRequest\x1a\r.ListResponse\"\x00\x12)\n\x08ReadFile\x12\x0c.ReadRequest\x1a\r.ReadResponse\"\x00\x12/\n\nUpdateFile\x12\x0e.UpdateRequest\x1a\x0f.UpdateResponse\"\x00\x12/\n\nDeleteFile\x12\x0e.DeleteRequest\x1a\x0f.DeleteResponse\"\x00\x12\x32\n\x0bRestoreFile\x12\x0f.RestoreRequest\x1a\x10.RestoreResponse\"\x00\x12=\n\x10GrantPermissions\x12\x12.PermissionRequest\x1a\x13.PermissionResponse\"\x00\x12\x41\n\x0e\x43reateNodeKeys\x12\x15.CreateNodeKeyRequest\x1a\x16.CreateNodeKeyResponse\"\x00\x12@\n\rReplicateFile\x12\x15.ReplicateFileRequest\x1a\x16.ReplicateFileResponse\"\x00\x12J\n\x13ReplicateUpdateFile\x12\x17.ReplicateUpdateRequest\x1a\x18.ReplicateUpdateResponse\"\x00\x12S\n\x14ReplicatePermissions\x12\x1b.ReplicatePermissionRequest\x1a\x1c.ReplicatePermissionResponse\"\x00\x12J\n\x13ReplicateDeleteFile\x12\x17.ReplicateDeleteRequest\x1a\x18.ReplicateDeleteResponse\"\x00\x12I\n\x10ReplicateRestore\x12\x18.ReplicateRestoreRequest\x1a\x19.ReplicateRestoreResponse\"\x00\x12>\n\x13UpdateNodePublicKey\x12\x11.UpdateKeyRequest\x1a\x12.UpdateKeyResponse\"\x00\x12\x34\n\x0bGetFileLock\x12\x10.FileLockRequest\x1a\x11.FileLockResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'distributed_fs_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _CREATEREQUEST._serialized_start=24
  _CREATEREQUEST._serialized_end=57
  _CREATERESPONSE._serialized_start=59
  _CREATERESPONSE._serialized_end=75
  _LISTREQUEST._serialized_start=77
  _LISTREQUEST._serialized_end=90
  _LISTRESPONSE._serialized_start=92
  _LISTRESPONSE._serialized_end=121
  _READREQUEST._serialized_start=123
  _READREQUEST._serialized_end=154
  _READRESPONSE._serialized_start=156
  _READRESPONSE._serialized_end=207
  _UPDATEREQUEST._serialized_start=209
  _UPDATEREQUEST._serialized_end=282
  _UPDATERESPONSE._serialized_start=284
  _UPDATERESPONSE._serialized_end=316
  _DELETEREQUEST._serialized_start=318
  _DELETEREQUEST._serialized_end=351
  _DELETERESPONSE._serialized_start=353
  _DELETERESPONSE._serialized_end=385
  _RESTOREREQUEST._serialized_start=387
  _RESTOREREQUEST._serialized_end=421
  _RESTORERESPONSE._serialized_start=423
  _RESTORERESPONSE._serialized_end=440
  _PERMISSIONREQUEST._serialized_start=442
  _PERMISSIONREQUEST._serialized_end=517
  _PERMISSIONRESPONSE._serialized_start=519
  _PERMISSIONRESPONSE._serialized_end=555
  _CREATENODEKEYREQUEST._serialized_start=557
  _CREATENODEKEYREQUEST._serialized_end=579
  _CREATENODEKEYRESPONSE._serialized_start=581
  _CREATENODEKEYRESPONSE._serialized_end=620
  _REPLICATEFILEREQUEST._serialized_start=622
  _REPLICATEFILEREQUEST._serialized_end=714
  _REPLICATEFILERESPONSE._serialized_start=716
  _REPLICATEFILERESPONSE._serialized_end=755
  _REPLICATEUPDATEREQUEST._serialized_start=757
  _REPLICATEUPDATEREQUEST._serialized_end=835
  _REPLICATEUPDATERESPONSE._serialized_start=837
  _REPLICATEUPDATERESPONSE._serialized_end=878
  _REPLICATEPERMISSIONREQUEST._serialized_start=880
  _REPLICATEPERMISSIONREQUEST._serialized_end=971
  _REPLICATEPERMISSIONRESPONSE._serialized_start=973
  _REPLICATEPERMISSIONRESPONSE._serialized_end=1018
  _REPLICATEDELETEREQUEST._serialized_start=1020
  _REPLICATEDELETEREQUEST._serialized_end=1060
  _REPLICATEDELETERESPONSE._serialized_start=1062
  _REPLICATEDELETERESPONSE._serialized_end=1103
  _REPLICATERESTOREREQUEST._serialized_start=1105
  _REPLICATERESTOREREQUEST._serialized_end=1148
  _REPLICATERESTORERESPONSE._serialized_start=1150
  _REPLICATERESTORERESPONSE._serialized_end=1176
  _UPDATEKEYREQUEST._serialized_start=1178
  _UPDATEKEYREQUEST._serialized_end=1250
  _UPDATEKEYRESPONSE._serialized_start=1252
  _UPDATEKEYRESPONSE._serialized_end=1287
  _FILELOCKREQUEST._serialized_start=1289
  _FILELOCKREQUEST._serialized_end=1339
  _FILELOCKRESPONSE._serialized_start=1341
  _FILELOCKRESPONSE._serialized_end=1380
  _DISTRIBUTEDFILESYSTEM._serialized_start=1383
  _DISTRIBUTEDFILESYSTEM._serialized_end=2318
# @@protoc_insertion_point(module_scope)
