# Create Connector

Create a connector, the interface only supports creating a single connector

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/connectors
HTTP Method | POST
Rate Limit | [10 per minute](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.** | View, comment, edit and manage Base(bitable:app)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Path parameters

Parameter | Type | Description
---|---|---
app_token | string | Target document token<br>**Example value**: "XrgTb4y1haKYnasu0xXb1g7lcSg"<br>**Data validation rules**:<br>- Length range: `1` ～ `100` characters

### Request body

Parameter | Type | Required | Description
---|---|---|---
target_table_id | string | No | Target table id, if filled in, create a connector based on the target table, otherwise create a new data table<br>**Example value**: "tblgOskzJO1Ls4S3"<br>**Data validation rules**:<br>- Length range: `1` ～ `20` characters
copy_from_token | string | No | The document token where the connector is to be copied, fill in together with the copy_from_table_id<br>**Example value**: "JpN3bk0WwaiM3js9VAjb6LoWcob"<br>**Data validation rules**:<br>- Length range: `1` ～ `100` characters
copy_from_table_id | string | No | The data table id corresponding to the connector to be copied, fill in together with the copy_from_token<br>**Example value**: "tbliUPLNNc0ik1wy"<br>**Data validation rules**:<br>- Length range: `1` ～ `20` characters
source_type | int | No | Data source type (this parameter only takes effect in non-replication connector scenarios)<br>**Example value**: 1<br>**Optional values are**:<br>- 1：Bitable
sync_type | int | No | Synchronization frequency (this parameter only takes effect in non-replica connector scenarios)<br>**Example value**: 1<br>**Optional values are**:<br>- 1：manual synchronization<br>- 2：timing synchronization<br>- 3：Real-time synchronization (only supported when the data source is Bitable)
field_sync_type | int | No | Field synchronization method (this parameter only takes effect in non-copy connector scenarios)<br>**Example value**: 1<br>**Optional values are**:<br>- 1：Synchronize full fields<br>- 2：Synchronize specified fields
sync_fields | string\[\] | No | List of synchronized fields, when field_sync_type = 2, need to fill in (this parameter only takes effect in non-replica connector scenarios)<br>**Example value**: ["fldpWqlcnp"]<br>**Data validation rules**:<br>- Length range: `1` ～ `500`
src_table_path | string | No | Data source path, is a json string (this parameter only takes effect in non-copy connector scenarios)<br>**Example value**: "{"token":"NafYw3iuEiKYk7k36aZcaF1Mnug","table_id":"tbljga8IeSoWw4Bk","view_id":"vewsEU9oBj"}"<br>**Data validation rules**:<br>- Length range: `1` ～ `500` characters
client_token | string | Yes | Idempotent keys, it is recommended to use the uuid algorithm to generate<br>**Example value**: "6d25a684-9558-11e9-aa94-efccd7a0659b"<br>**Data validation rules**:<br>- Length range: `1` ～ `100` characters

### Request body example
```json
{
"target_table_id": "tbljrm2jMSJdR9gf",
"source_type": 1,
"sync_type": 2,
"field_sync_type": 2,
"sync_fields": [
"fld9PBu621"
],
"src_table_path ": "{\" token\":\ "YqM2b5VJ3aAx88sXFaYbsYsyctb\",\ "table_id\":\ "tblRcDVB4WhKfxAp\",\ "view_id\":\ "vewJj1D366\"} ",
"client_token": "6d25a684-9558-11e9-aa94-efccd7a0659b"
}
```

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
connector | app.connector | Unique ID of the data table
token | string | Target document token
table_id | string | Target table id
src_table_path | string | data source path
source_type | int | data source type<br>**Optional values are**:<br>- 1：Bitable
sync_type | int | synchronization frequency<br>**Optional values are**:<br>- 1：manual synchronization<br>- 2：timing synchronization<br>- 3：real-time synchronization
field_sync_type | int | Field synchronization method<br>**Optional values are**:<br>- 1：Synchronize full fields<br>- 2：Synchronize specified fields
sync_fields | string\[\] | Synchronize field information, value only when field_sync_type = 2

### Response body example
```json
{
"Code": 0,
"Msg": "success",
"Data": {
"Connector": {
"Token": "OqfIbgJYkaECb7sECGSb9Wbqc7g",
"table_id": "tbljrm2jMSJdR9gf",
"src_table_path ": "{\" token\":\ "YqM2b5VJ3aAx88sXFaYbsYsyctb\",\ "table_id\":\ "tblRcDVB4WhKfxAp\",\ "view_id\":\ "vewJj1D366\"} ",
"source_type": 1,
"sync_type": 2,
"field_sync_type": 2,
"sync_fields": [
"fld9PBu621"
]
}
}
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
400 | 1254800 | ParamIsInvalid | Parameter error
400 | 1254900 | ConnectorNotFound | Can't find connector
400 | 1254901 | ConnectorSrcPermissionNotAllow | The user does not have permissions on the source table
400 | 1254902 | ConnectorDestPermissionNotAllow | The user does not have permissions on the target table
400 | 1254903 | ConnectorSrcBaseCannotBeDest | The source and destination tables cannot be the same
400 | 1254904 | ConnectorCountOverLimit | The number of connectors created by the user exceeds the limit
400 | 1254905 | ConnectorLackPrivilege | Users have no connector rights
400 | 1254906 | ConnectorSrcConfigErr | Source table configuration error
400 | 1254907 | ConnectorDestConfigErr | The target table is misconfigured
400 | 1254908 | ConnectorNotSupportSrcType | Data source is not supported
400 | 1254909 | ConnectorSrcFieldNotFound | The field of the source table could not be found
400 | 1254910 | ConnectorDestFieldNotFound | Field of target table not found
400 | 1254911 | ConnectorSyncTableActionForbidden | Cannot edit on synchronized table
400 | 1254912 | ConnectorLackPrimaryField | When specifying field synchronization, the index column is missing
200 | 1254000 | WrongRequestJson | request body error
200 | 1254001 | WrongRequestBody | request body error
200 | 1254002 | Fail | Internal error, please contact [Technical Support] (https://applink.feishu.cn/TLJpeNdW)
200 | 1254003 | WrongBaseToken | app_token mistake
200 | 1254004 | WrongTableId | table_id mistake
200 | 1254005 | WrongViewId | view_id mistake
200 | 1254006 | WrongRecordId | Check record_id
200 | 1254007 | EmptyValue | null value
200 | 1254008 | EmptyView | empty view
200 | 1254009 | WrongFieldId | wrong field id
200 | 1254010 | ReqConvError | request error
400 | 1254015 | Field types do not match. | Field type and value do not match
403 | 1254027 | UploadAttachNotAllowed | Attachment is not mounted, upload is prohibited
200 | 1254030 | InvalidPageToken | Illegal PageToken
400 | 1254036 | Bitable is copying, please try again later. | Copy Bitable is an asynchronous operation. This error code indicates that the current Bitable is still being copied, and the current Bitable cannot be operated during the copy. You need to wait for the copy to complete before operating.
400 | 1254037 | Invalid client token, make sure that it complies with the specification. | Illegal idempotent key
200 | 1254040 | BaseTokenNotFound | app_token doesn't exist
200 | 1254041 | TableIdNotFound | table_id doesn't exist
200 | 1254042 | ViewIdNotFound | view_id doesn't exist
200 | 1254043 | RecordIdNotFound | record_id doesn't exist
200 | 1254044 | FieldIdNotFound | field_id doesn't exist
200 | 1254045 | FieldNameNotFound | The field name does not exist. Please check whether the field name in the interface and the field name in Bitable match exactly. If it is difficult to troubleshoot, it is recommended that you call the List Fields interface to get the field name, because differences such as spaces, line breaks or special symbols may be ignored according to the UI name of the form page.
200 | 1254060 | TextFieldConvFail | Multi-line text field error
200 | 1254061 | NumberFieldConvFail | Numeric field error
200 | 1254062 | SingleSelectFieldConvFail | radio field error
200 | 1254063 | MultiSelectFieldConvFail | Multiple selection field error
200 | 1254064 | DatetimeFieldConvFail | Date field error
200 | 1254065 | CheckboxFieldConvFail | Check box field error
200 | 1254066 | UserFieldConvFail | The person field is incorrect. The reasons may be:<br>The ID type specified by the user_id_type parameter does not match the ID type passed in<br>An unrecognized type or structure is passed in. Currently, only the id parameter is supported, and an array needs to be passed in.<br>open_id passed in across apps. If passing in IDs across apps, user_id is recommended. open_id obtained by different apps cannot be cross-used<br>If you want to pass null to the person field, you can pass null.
200 | 1254067 | LinkFieldConvFail | associated field error
200 | 1254068 | URLFieldConvFail | Hyperlinke field error
200 | 1254069 | AttachFieldConvFail | Attachment field error
200 | 1254072 | Failed to convert phone field, please make sure it is correct. | Phone field error
400 | 1254074 | The parameters of Duplex Link field are invalid and need to be filled with an array of string. | Illegal format of bidirectional association field
200 | 1254100 | TableExceedLimit | The number of data tables or dashboards is exceeded. The maximum number of data tables plus dashboards in each Bitable is 100
200 | 1254101 | ViewExceedLimit | The number of views exceeds the limit, limited to 200
200 | 1254102 | FileExceedLimit | Number of files exceeded
200 | 1254103 | RecordExceedLimit | record overrun
200 | 1254104 | RecordAddOnceExceedLimit | The number of records added at a time exceeds the limit
200 | 1254105 | FieldExceedLimit | Number of fields exceeded
200 | 1254106 | AttachExceedLimit | Too many attachments
200 | 1254130 | TooLargeCell | Grid content is too large
200 | 1254290 | TooManyRequest | Request is too fast, try again later
200 | 1254291 | LockNotObtainedError | Lock grab failed
200 | 1254301 | OperationTypeError | Bitable does not enable advanced permissions or does not support enabling advanced permissions
200 | 1254303 | The attachment does not belong to this bitable. | You do not have permission to write attachments to multidimensional tables. To write attachments in Bitable, you need to call the upload material interface first, upload the attachments to the current Bitable, and then add new records.
200 | 1255001 | InternalError | Internal error, please contact [Technical Support] (https://applink.feishu.cn/TLJpeNdW)
200 | 1255002 | Something went wrong. Please contact technical support at https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952 | Internal error, please contact [Technical Support] (https://applink.feishu.cn/TLJpeNdW)
200 | 1255003 | MarshalError | serialization error
200 | 1255004 | UmMarshalError | deserialization error
200 | 1255005 | ConvError | Internal error, please contact [Technical Support] (https://applink.feishu.cn/TLJpeNdW)
400 | 1255006 | Client token conflict, please generate a new client token and try again. | Idempotent key repeatedly submitted
504 | 1255040 | Request timed out, please try again later. | request timed out
400 | 1254607 | Data not ready, please try again later | The error is generally caused by the pre-operation not being completed, or the data of this operation is too large, and the server calculation timed out. When encountering this error code, it is recommended to wait for a period of time and try again. Usually there are the following reasons:<br>- ** Frequent editing operations **: Developers' editing operations on Bitable are very frequent. It may lead to timeouts due to waiting for the pre-operation processing to complete taking too long. Bitable's underlying processing of data tables is based on the serial way of the version dimension and does not support concurrency. Therefore, such errors are prone to occur when concurrent requests are made. It is not recommended that developers make concurrent requests for a single data table.<br>- ** Batch operation load **: When developers perform batch addition, deletion and other operations in Bitable, if the data volume of the data table is very large, it may cause a single request to take too long, eventually resulting in request timed out. It is recommended that developers appropriately reduce the page_size of batch requests to reduce request time.<br>- ** Quotas and computational overhead **: Quotas are based on a single document dimension. If the reading interface involves computational logic such as formula calculation and sorting, it will consume more resources. For example, concurrent reading of multiple data tables under a document may also cause the document to block.
403 | 1254302 | Permission denied. | The calling identity lacks Bitable's advanced permissions. You need to grant advanced permissions to the calling identity:<br>- To grant advanced permissions to users, you need to add manageable permissions to the current user in the ** Share ** entry at the top right of the Bitable page.! [image.png] (//sf3-cn.feishucdn.com/obj/open-platform-opendoc/df3911b4f747d75914f35a46962d667d_dAsfLjv3QC.png?height=546&lazyload=true&maxWidth=550)<br>- To grant advanced permissions to the app, you need to add manageable permissions to the app through the top right of the Bitable page ** "..." ** - > ** "... More 」** ->**「 Add Documentation App" ** entry.<br>! [] (//sf3-cn.feishucdn.com/obj/open-platform-opendoc/22c027f63c540592d3ca8f41d48bb107_CSas7OYJBR.png?height=1994&maxWidth=550&width=3278)<br>! [image.png] (//sf3-cn.feishucdn.com/obj/open-platform-opendoc/9f3353931fafeea16a39f0eb887db175_0tjzC9P3zU.png?maxWidth=550)<br>** Attention **:<br>Before ** adding a document application **, you need to make sure that the target application has at least one Bitable [API permission] (/ssl: ttdoc/ukTMukTMukTM/uYTM5UjL2ETO14iNxkTN/scope-list). Otherwise, you will not be able to search for the target application in the document application window.<br>- You can also add users or a group containing applications in the Bitable advanced permission settings, and give this group customized permissions such as reading and writing.
403 | 1254304 | Permission denied. | The calling identity lacks advanced privileges. The calling identity needs to have manageable privileges for Bitable. For more information, refer to [How to Enable Documentation Permissions for Applications or Users] (/ssl: ttdoc/ukTMukTMukTM/uczNzUjL3czM14yN3MTN #16c6475a).
403 | 1254306 | The tenant or base owner is subject to base plan limits. | Contact the tenant administrator to apply for benefits
403 | 1254608 | Same API requests are submitted repeatedly. | Repeated update requests based on the same Bitable version are common in concurrent or very short time intervals, such as concurrent updates of a view's information to the same content. It is recommended to try again later

# List Connectors

Paging List Connectors under a Single Bitable

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/apps/:app_token/connectors
HTTP Method | GET
Rate Limit | [10 per second](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.** | View, comment, edit and manage Base(bitable:app)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)

### Path parameters

Parameter | Type | Description
---|---|---
app_token | string | The unique identifier of the target Bitable App. Different forms of Bitable have different ways of obtaining app_token:<br>- If a Bitable URL begins with ==** feishu.cn/base **==, the Bitable app_token is highlighted in the image below:<br>! [app_token] (//sf3-cn.feishucdn.com/obj/open-platform-opendoc/6916f8cfac4045ba6585b90e3afdfb0a_GxbfkJHZBa.png?height=766&lazyload=true&width=3004)<br>- If the URL of Bitable starts with ==** feishu.cn/wiki **==, you need to call the Knowledge Base related [Get Wiki Workspace Node Information] (/ssl: ttdoc/ukTMukTMukTM/uUDN04SN0QjL1QDN/wiki-v2/space/get_node) interface to get the app_token of Bitable. When the value of obj_type is'bitable ', the value of the obj_token field is the app_token of Bitable.<br>For more information, refer to [Bitable app_token Acquisition Method] (/ssl: ttdoc/ukTMukTMukTM/uUDN04SN0QjL1QDN/bit-overview #-752212c).<br>**Example value**: "XrgTb4y1haKYnasu0xXb1g7lcSg"<br>**Data validation rules**:<br>- Length range: `1` ～ `100` characters

### Query parameters

Parameter | Type | Required | Description
---|---|---|---
page_token | string | No | Page identifier. It is not filled in the first request, indicating traversal from the beginning; when there will be more groups, the new page_token will be returned at the same time, and the next traversal can use the page_token to get more groups<br>**Example value**: 12894689213120<br>**Data validation rules**:<br>- Length range: `1` ～ `100` characters
page_size | int | No | Number of connectors acquired once<br>**Example value**: 10<br>**Data validation rules**:<br>- Value range: `1` ～ `100`

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
connectors | app.connector\[\] | Connector list
token | string | Target document token
table_id | string | Target table id
src_table_path | string | data source path
source_type | int | data source type<br>**Optional values are**:<br>- 1：Bitable
sync_type | int | synchronization frequency<br>**Optional values are**:<br>- 1：manual synchronization<br>- 2：timing synchronization<br>- 3：Real-time synchronization (supported only by Bitable data sources)
field_sync_type | int | Field synchronization method<br>**Optional values are**:<br>- 1：Synchronize full fields<br>- 2：Synchronize specified fields
sync_fields | string\[\] | Synchronize field information, value only when field_sync_type = 2
has_more | boolean | Whether the response body has more parameters
total | int | Total number of connectors
page_token | string | Page identifier, when has_more is true, a new page_token will also be returned. Otherwise, page_token will not be returned

### Response body example
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "connectors": [
      {
        "token": "OqfIbgJYkaECb7sECGSb9Wbqc7g",
        "table_id": "tbljrm2jMSJdR9gf",
        "src_table_path": "{\"token\": \"YqM2b5VJ3aAx88sXFaYbsYsyctb\", \"table_id\": \"tblRcDVB4WhKfxAp\", \"view_id\": \"vewJj1D366\"}",
        "source_type": 1,
        "sync_type": 2,
        "field_sync_type": 2,
        "sync_fields": [
          "fld9PBu621"
        ]
      }
    ],
    "has_more": true,
    "total": 10,
    "page_token": "7237809899083912"
  }
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
400 | 1254800 | ParamIsInvalid | Parameter error
400 | 1254900 | ConnectorNotFound | Can't find connector
400 | 1254901 | ConnectorSrcPermissionNotAllow | The user does not have permissions on the source table
400 | 1254902 | ConnectorDestPermissionNotAllow | The user does not have permissions on the target table
400 | 1254903 | ConnectorSrcBaseCannotBeDest | The source table and the target table cannot be under the same Bitable
400 | 1254904 | ConnectorCountOverLimit | The number of connectors created by the user exceeds the limit
400 | 1254905 | ConnectorLackPrivilege | Users have no connector rights
400 | 1254906 | ConnectorSrcConfigErr | Source table configuration error
400 | 1254907 | ConnectorDestConfigErr | The target table is misconfigured
400 | 1254908 | ConnectorNotSupportSrcType | Data source is not supported
400 | 1254909 | ConnectorSrcFieldNotFound | The field of the source table could not be found
400 | 1254910 | ConnectorDestFieldNotFound | Field of target table not found
400 | 1254911 | ConnectorSyncTableActionForbidden | Cannot edit on synchronized table
400 | 1254912 | ConnectorLackPrimaryField | When specifying field synchronization, the index column is missing
200 | 1254000 | WrongRequestJson | request body error
200 | 1254001 | WrongRequestBody | request body error
200 | 1254002 | Fail | Internal error, please contact [Technical Support] (https://applink.feishu.cn/TLJpeNdW)
200 | 1254003 | WrongBaseToken | app_token mistake
200 | 1254004 | WrongTableId | table_id mistake
200 | 1254005 | WrongViewId | view_id mistake
200 | 1254006 | WrongRecordId | record_id mistake
200 | 1254007 | EmptyValue | null value
200 | 1254008 | EmptyView | empty view
200 | 1254009 | WrongFieldId | wrong field id
200 | 1254010 | ReqConvError | request error
400 | 1254015 | Field types do not match. | Field type and value do not match
403 | 1254027 | UploadAttachNotAllowed | Attachment is not mounted, upload is prohibited
200 | 1254030 | InvalidPageToken | Illegal PageToken
400 | 1254036 | Bitable is copying, please try again later. | Copy Bitable is an asynchronous operation. This error code indicates that the current Bitable is still being copied, and the current Bitable cannot be operated during the copy. You need to wait for the copy to complete before operating.
400 | 1254037 | Invalid client token, make sure that it complies with the specification. | Illegal idempotent key
200 | 1254040 | BaseTokenNotFound | app_token doesn't exist
200 | 1254041 | TableIdNotFound | table_id doesn't exist
200 | 1254042 | ViewIdNotFound | view_id doesn't exist
200 | 1254043 | RecordIdNotFound | record_id doesn't exist
200 | 1254044 | FieldIdNotFound | field_id doesn't exist
200 | 1254045 | FieldNameNotFound | The field name does not exist. Please check whether the field name in the interface and the field name in Bitable match exactly. If it is difficult to troubleshoot, it is recommended that you call the List Fields interface to get the field name, because differences such as spaces, line breaks or special symbols may be ignored according to the UI name of the form page.
200 | 1254060 | TextFieldConvFail | Multi-line text field error
200 | 1254061 | NumberFieldConvFail | Numeric field error
200 | 1254062 | SingleSelectFieldConvFail | radio field error
200 | 1254063 | MultiSelectFieldConvFail | Multiple selection field error
200 | 1254064 | DatetimeFieldConvFail | DatetimeFieldConvFail
200 | 1254065 | CheckboxFieldConvFail | Check box field error
200 | 1254066 | UserFieldConvFail | The person field is incorrect. The reasons may be:<br>The ID type specified by the user_id_type parameter does not match the ID type passed in<br>An unrecognized type or structure is passed in. Currently, only the id parameter is supported, and an array needs to be passed in.<br>open_id passed in across apps. If passing in IDs across apps, user_id is recommended. open_id obtained by different apps cannot be cross-used<br>If you want to pass null to the person field, you can pass null.
200 | 1254067 | LinkFieldConvFail | associated field error
200 | 1254068 | URLFieldConvFail | Hyperlinke field error
200 | 1254069 | AttachFieldConvFail | Attachment field error
200 | 1254072 | Failed to convert phone field, please make sure it is correct. | Phone field error
400 | 1254074 | The parameters of Duplex Link field are invalid and need to be filled with an array of string. | Illegal format of bidirectional association field
200 | 1254100 | TableExceedLimit | The number of data tables or dashboards is exceeded. The maximum number of data tables plus dashboards in each Bitable is 100
200 | 1254101 | ViewExceedLimit | The number of views exceeds the limit, limited to 200
200 | 1254102 | FileExceedLimit | Number of files exceeded
200 | 1254103 | RecordExceedLimit | record overrun
200 | 1254104 | RecordAddOnceExceedLimit | The number of records added at a time exceeds the limit
200 | 1254105 | FieldExceedLimit | Number of fields exceeded
200 | 1254106 | AttachExceedLimit | Too many attachments
200 | 1254130 | TooLargeCell | Grid content is too large
200 | 1254290 | TooManyRequest | Request is too fast, try again later
200 | 1254291 | LockNotObtainedError | Lock grab failed
200 | 1254301 | OperationTypeError | Bitable does not enable advanced permissions or does not support enabling advanced permissions
200 | 1254303 | The attachment does not belong to this bitable. | You do not have permission to write attachments to multidimensional tables. To write attachments in Bitable, you need to call the upload material interface first, upload the attachments to the current Bitable, and then add new records.
200 | 1255001 | InternalError | Internal error, please contact [Technical Support] (https://applink.feishu.cn/TLJpeNdW)
200 | 1255002 | Something went wrong. Please contact technical support at https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952 | Internal error, please contact [Technical Support] (https://applink.feishu.cn/TLJpeNdW)
200 | 1255003 | MarshalError | serialization error
200 | 1255004 | UmMarshalError | deserialization error
200 | 1255005 | ConvError | Internal error, please contact [Technical Support] (https://applink.feishu.cn/TLJpeNdW)
400 | 1255006 | Client token conflict, please generate a new client token and try again. | Idempotent key repeatedly submitted
504 | 1255040 | Request timed out, please try again later. | request timed out
400 | 1254607 | Data not ready, please try again later | The error is generally caused by the pre-operation not being completed, or the data of this operation is too large, and the server calculation timed out. When encountering this error code, it is recommended to wait for a period of time and try again. Usually there are the following reasons:<br>- ** Frequent editing operations **: Developers' editing operations on Bitable are very frequent. It may lead to timeouts due to waiting for the pre-operation processing to complete taking too long. Bitable's underlying processing of data tables is based on the serial way of the version dimension and does not support concurrency. Therefore, such errors are prone to occur when concurrent requests are made. It is not recommended that developers make concurrent requests for a single data table.<br>- ** Batch operation load **: When developers perform batch addition, deletion and other operations in Bitable, if the data volume of the data table is very large, it may cause a single request to take too long, eventually resulting in request timed out. It is recommended that developers appropriately reduce the page_size of batch requests to reduce request time.<br>- ** Quotas and computational overhead **: Quotas are based on a single document dimension. If the reading interface involves computational logic such as formula calculation and sorting, it will consume more resources. For example, concurrent reading of multiple data tables under a document may also cause the document to block.
403 | 1254302 | Permission denied. | The calling identity lacks Bitable's advanced permissions. You need to grant advanced permissions to the calling identity:<br>- To grant advanced permissions to users, you need to add manageable permissions to the current user in the ** Share ** entry at the top right of the Bitable page.! [image.png] (//sf3-cn.feishucdn.com/obj/open-platform-opendoc/df3911b4f747d75914f35a46962d667d_dAsfLjv3QC.png?height=546&lazyload=true&maxWidth=550)<br>- To grant advanced permissions to the app, you need to add manageable permissions to the app through the top right of the Bitable page ** "..." ** - > ** "... More 」** ->**「 Add Documentation App" ** entry.<br>! [] (//sf3-cn.feishucdn.com/obj/open-platform-opendoc/22c027f63c540592d3ca8f41d48bb107_CSas7OYJBR.png?height=1994&maxWidth=550&width=3278)<br>! [image.png] (//sf3-cn.feishucdn.com/obj/open-platform-opendoc/9f3353931fafeea16a39f0eb887db175_0tjzC9P3zU.png?maxWidth=550)<br>** Attention **:<br>Before ** adding a document application **, you need to make sure that the target application has at least one Bitable [API permission] (/ssl: ttdoc/ukTMukTMukTM/uYTM5UjL2ETO14iNxkTN/scope-list). Otherwise, you will not be able to search for the target application in the document application window.<br>- You can also add users or a group containing applications in the Bitable advanced permission settings, and give this group customized permissions such as reading and writing.
403 | 1254304 | Permission denied. | The calling identity lacks advanced privileges. The calling identity needs to have manageable privileges for Bitable. For more information, refer to [How to Enable Documentation Permissions for Applications or Users] (/ssl: ttdoc/ukTMukTMukTM/uczNzUjL3czM14yN3MTN #16c6475a).
403 | 1254306 | The tenant or base owner is subject to base plan limits. | Contact the tenant administrator to apply for benefits
403 | 1254608 | Same API requests are submitted repeatedly. | Repeated update requests based on the same Bitable version are common in concurrent or very short time intervals, such as concurrent updates of a view's information to the same content. It is recommended to try again later

# Delete connector

Delete multiple connectors under the same Bitable

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/apps/:app_token/connectors
HTTP Method | DELETE
Rate Limit | [10 per minute](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.** | View, comment, edit and manage Base(bitable:app)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)

### Path parameters

Parameter | Type | Description
---|---|---
app_token | string | Target document Token, the unique identifier of Bitable App. Different forms of Bitable have different ways of obtaining app_token:<br>- If a Bitable URL begins with ==** feishu.cn/base **==, the Bitable app_token is highlighted in the image below:<br>! [app_token] (//sf3-cn.feishucdn.com/obj/open-platform-opendoc/6916f8cfac4045ba6585b90e3afdfb0a_GxbfkJHZBa.png?height=766&lazyload=true&width=3004)<br>- If the URL of Bitable starts with ==** feishu.cn/wiki **==, you need to call the Knowledge Base related [Get Wiki Workspace Node Information] (/ssl: ttdoc/ukTMukTMukTM/uUDN04SN0QjL1QDN/wiki-v2/space/get_node) interface to get the app_token of Bitable. When the value of obj_type is'bitable ', the value of the obj_token field is the app_token of Bitable.<br>For more information, refer to [Bitable app_token Acquisition Method] (/ssl: ttdoc/ukTMukTMukTM/uUDN04SN0QjL1QDN/bit-overview #-752212c).<br>**Example value**: "XrgTb4y1haKYnasu0xXb1g7lcSg"<br>**Data validation rules**:<br>- Length range: `1` ～ `100` characters

### Query parameters

Parameter | Type | Required | Description
---|---|---|---
table_ids | string\[\] | No | List of target tables. The unique identifier of the Bitable data table. How to get it:<br>- You can get the "table_id" through the Bitable URL. The highlighted part of the image below is the "table_id" of the current data table.<br>- table_id can also be obtained through the [list data table] (/ssl: ttdoc/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table/list) interface<br>! [] (//sf3-cn.feishucdn.com/obj/open-platform-opendoc/18741fe2a0d3cafafaf9949b263bb57d_yD1wkOrSju.png?height=746&lazyload=true&maxWidth=700&width=2976)<br>** Data validation rules **:<br>- Length range: '0'~ '50' characters<br>**Example value**: tblgOskzJO1Ls4S3<br>**Data validation rules**:<br>- Length range: `1` ～ `20`

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
success_num | int | Number of target tables successfully configured to remove connectors
fail_table_ids | string\[\] | Remove the list of target tables where connector configuration failed
invalid_table_ids | string\[\] | List of illegal target tables without connector configuration

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "success_num": 10,
        "fail_table_ids": [
            "tbls3Ncs7P8PBU6a"
        ],
        "invalid_table_ids": [
            "tblImXQ9bL2cP6Dl"
        ]
    }
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
400 | 1254800 | ParamIsInvalid | Parameter error
400 | 1254900 | ConnectorNotFound | Can't find connector
400 | 1254901 | ConnectorSrcPermissionNotAllow | The user does not have permissions on the source table
400 | 1254902 | ConnectorDestPermissionNotAllow | The user does not have permissions on the target table
400 | 1254903 | ConnectorSrcBaseCannotBeDest | The source table and the target table cannot be under the same Bitable
400 | 1254904 | ConnectorCountOverLimit | The number of connectors created by the user exceeds the limit
400 | 1254905 | ConnectorLackPrivilege | Users have no connector rights
400 | 1254906 | ConnectorSrcConfigErr | Source table configuration error
400 | 1254907 | ConnectorDestConfigErr | The target table is misconfigured
400 | 1254908 | ConnectorNotSupportSrcType | Data source is not supported
400 | 1254909 | ConnectorSrcFieldNotFound | The field of the source table could not be found
400 | 1254910 | ConnectorDestFieldNotFound | Field of target table not found
400 | 1254911 | ConnectorSyncTableActionForbidden | Cannot edit on synchronized table
400 | 1254912 | ConnectorLackPrimaryField | When specifying field synchronization, the index column is missing
200 | 1254000 | WrongRequestJson | request body error
200 | 1254001 | WrongRequestBody | request body error
200 | 1254002 | Fail | Internal error, please contact [Technical Support] (https://applink.feishu.cn/TLJpeNdW)
200 | 1254003 | WrongBaseToken | app_token mistake
200 | 1254004 | WrongTableId | table_id mistake
200 | 1254005 | WrongViewId | view_id mistake
200 | 1254006 | WrongRecordId | Check record_id
200 | 1254007 | EmptyValue | null value
200 | 1254008 | EmptyView | empty view
200 | 1254009 | WrongFieldId | wrong field id
200 | 1254010 | ReqConvError | request error
400 | 1254015 | Field types do not match. | Field type and value do not match
403 | 1254027 | UploadAttachNotAllowed | Attachment is not mounted, upload is prohibited
200 | 1254030 | InvalidPageToken | Illegal PageToken
400 | 1254036 | Bitable is copying, please try again later. | Copy Bitable is an asynchronous operation. This error code indicates that the current Bitable is still being copied, and the current Bitable cannot be operated during the copy. You need to wait for the copy to complete before operating.
400 | 1254037 | Invalid client token, make sure that it complies with the specification. | Illegal idempotent key
200 | 1254040 | BaseTokenNotFound | app_token doesn't exist
200 | 1254041 | TableIdNotFound | table_id doesn't exist
200 | 1254042 | ViewIdNotFound | view_id doesn't exist
200 | 1254043 | RecordIdNotFound | record_id doesn't exist
200 | 1254044 | FieldIdNotFound | field_id doesn't exist
200 | 1254045 | FieldNameNotFound | The field name does not exist. Please check whether the field name in the interface and the field name in Bitable match exactly. If it is difficult to troubleshoot, it is recommended that you call the List Fields interface to get the field name, because differences such as spaces, line breaks or special symbols may be ignored according to the UI name of the form page.
200 | 1254060 | TextFieldConvFail | Multi-line text field error
200 | 1254061 | NumberFieldConvFail | Numeric field error
200 | 1254062 | SingleSelectFieldConvFail | radio field error
200 | 1254063 | MultiSelectFieldConvFail | Multiple selection field error
200 | 1254064 | DatetimeFieldConvFail | Date field error
200 | 1254065 | CheckboxFieldConvFail | Check box field error
200 | 1254066 | UserFieldConvFail | The person field is incorrect. The reasons may be:<br>The ID type specified by the user_id_type parameter does not match the ID type passed in<br>An unrecognized type or structure is passed in. Currently, only the id parameter is supported, and an array needs to be passed in.<br>open_id passed in across apps. If passing in IDs across apps, user_id is recommended. open_id obtained by different apps cannot be cross-used<br>If you want to pass null to the person field, you can pass null.
200 | 1254067 | LinkFieldConvFail | associated field error
200 | 1254068 | URLFieldConvFail | Hyperlinke field error
200 | 1254069 | AttachFieldConvFail | Attachment field error
200 | 1254072 | Failed to convert phone field, please make sure it is correct. | Phone field error
400 | 1254074 | The parameters of Duplex Link field are invalid and need to be filled with an array of string. | Illegal format of bidirectional association field
200 | 1254100 | TableExceedLimit | The number of data tables or dashboards is exceeded. The maximum number of data tables plus dashboards in each Bitable is 100
200 | 1254101 | ViewExceedLimit | The number of views exceeds the limit, limited to 200
200 | 1254102 | FileExceedLimit | Number of files exceeded
200 | 1254103 | RecordExceedLimit | record overrun
200 | 1254104 | RecordAddOnceExceedLimit | The number of records added at a time exceeds the limit
200 | 1254105 | FieldExceedLimit | Number of fields exceeded
200 | 1254106 | AttachExceedLimit | Too many attachments
200 | 1254130 | TooLargeCell | Grid content is too large
200 | 1254290 | TooManyRequest | Request is too fast, try again later
200 | 1254291 | LockNotObtainedError | Lock grab failed
200 | 1254301 | OperationTypeError | Bitable does not enable advanced permissions or does not support enabling advanced permissions
200 | 1254303 | The attachment does not belong to this bitable. | You do not have permission to write attachments to multidimensional tables. To write attachments in Bitable, you need to call the upload material interface first, upload the attachments to the current Bitable, and then add new records.
200 | 1255001 | InternalError | Internal error, please contact [Technical Support] (https://applink.feishu.cn/TLJpeNdW)
200 | 1255002 | Something went wrong. Please contact technical support at https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952 | Internal error, please contact [Technical Support] (https://applink.feishu.cn/TLJpeNdW)
200 | 1255003 | MarshalError | serialization error
200 | 1255004 | UmMarshalError | deserialization error
200 | 1255005 | ConvError | Internal error, please contact [Technical Support] (https://applink.feishu.cn/TLJpeNdW)
400 | 1255006 | Client token conflict, please generate a new client token and try again. | Idempotent key repeatedly submitted
504 | 1255040 | Request timed out, please try again later. | request timed out
400 | 1254607 | Data not ready, please try again later | The error is generally caused by the pre-operation not being completed, or the data of this operation is too large, and the server calculation timed out. When encountering this error code, it is recommended to wait for a period of time and try again. Usually there are the following reasons:<br>- ** Frequent editing operations **: Developers' editing operations on Bitable are very frequent. It may lead to timeouts due to waiting for the pre-operation processing to complete taking too long. Bitable's underlying processing of data tables is based on the serial way of the version dimension and does not support concurrency. Therefore, such errors are prone to occur when concurrent requests are made. It is not recommended that developers make concurrent requests for a single data table.<br>- ** Batch operation load **: When developers perform batch addition, deletion and other operations in Bitable, if the data volume of the data table is very large, it may cause a single request to take too long, eventually resulting in request timed out. It is recommended that developers appropriately reduce the page_size of batch requests to reduce request time.<br>- ** Quotas and computational overhead **: Quotas are based on a single document dimension. If the reading interface involves computational logic such as formula calculation and sorting, it will consume more resources. For example, concurrent reading of multiple data tables under a document may also cause the document to block.
403 | 1254302 | Permission denied. | The calling identity lacks Bitable's advanced permissions. You need to grant advanced permissions to the calling identity:<br>- To grant advanced permissions to users, you need to add manageable permissions to the current user in the ** Share ** entry at the top right of the Bitable page.! [image.png] (//sf3-cn.feishucdn.com/obj/open-platform-opendoc/df3911b4f747d75914f35a46962d667d_dAsfLjv3QC.png?height=546&lazyload=true&maxWidth=550)<br>- To grant advanced permissions to the app, you need to add manageable permissions to the app through the top right of the Bitable page ** "..." ** - > ** "... More 」** ->**「 Add Documentation App" ** entry.<br>! [] (//sf3-cn.feishucdn.com/obj/open-platform-opendoc/22c027f63c540592d3ca8f41d48bb107_CSas7OYJBR.png?height=1994&maxWidth=550&width=3278)<br>! [image.png] (//sf3-cn.feishucdn.com/obj/open-platform-opendoc/9f3353931fafeea16a39f0eb887db175_0tjzC9P3zU.png?maxWidth=550)<br>** Attention **:<br>Before ** adding a document application **, you need to make sure that the target application has at least one Bitable [API permission] (/ssl: ttdoc/ukTMukTMukTM/uYTM5UjL2ETO14iNxkTN/scope-list). Otherwise, you will not be able to search for the target application in the document application window.<br>- You can also add users or a group containing applications in the Bitable advanced permission settings, and give this group customized permissions such as reading and writing.
403 | 1254304 | Permission denied. | The calling identity lacks advanced privileges. The calling identity needs to have manageable privileges for Bitable. For more information, refer to [How to Enable Documentation Permissions for Applications or Users] (/ssl: ttdoc/ukTMukTMukTM/uczNzUjL3czM14yN3MTN #16c6475a).
403 | 1254306 | The tenant or base owner is subject to base plan limits. | Contact the tenant administrator to apply for benefits
403 | 1254608 | Same API requests are submitted repeatedly. | Repeated update requests based on the same Bitable version are common in concurrent or very short time intervals, such as concurrent updates of a view's information to the same content. It is recommended to try again later
