# Create a Base App

Create a base app in user-defined folder.

**Notice**：To create a Base app based on a template, first obtain the `app_token` of the template as the file token, then call the [Copy File](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file/copy) interface to create the Base app.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps
HTTP Method | POST
Rate Limit | [20 per minute](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.**<br>Enable any scope from the list | 创建多维表格(base:app:create)<br>View, comment, edit and manage Base(bitable:app)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Request body

Parameter | Type | Required | Description
---|---|---|---
name | string | No | Base App Name<br>**Example value**: "test name"
folder_token | string | No | Base App Folder Token. The default value is empty, which means that the Base App is created at the root folder. For information on how to obtain folder_token, please refer to [How to obtain tokens related to cloud document resources](https://open.feishu.cn/document/server-docs/docs/faq?lang=en-US#e4a9bfa1)<br>**Example value**: "fldbco*****CIMltVc"
time_zone | string | No | Base App Time Zone, [More Detail](https://feishu.feishu.cn/docx/YKRndTM7VoyDqpxqqeEcd67MnEf)<br>**Example value**: "Asia/Macau"

### Request body example
```json
{
    "name":"test name",
    "folder_token": "fldbco*****CIMltVc"
}
```

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
app | app | Response data
app_token | string | Base App Token
name | string | Base App Name
folder_token | string | Base App Folder Token
url | string | Base App URL
default_table_id | string | Default table id
time_zone | string | Base App Time Zone

### Response body example
```json
{
    "code": 0,
    "data": {
        "app": {
            "app_token": "S404b*****e9PQsYDWYcNryFn0g",
            "default_table_id": "tblY2mIl0p2oumSQ",
            "folder_token": "fldbco*****CIMltVc",
            "name": "test name",
            "url": "https://example.feishu.cn/base/S404b*****e9PQsYDWYcNryFn0g",
            "time_zone":"Asia/Beijing"
        }
    },
    "msg": "success"
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
200 | 1254000 | WrongRequestJson | Request error
200 | 1254001 | WrongRequestBody | Request body error
200 | 1254002 | Fail | Internal error, have any questions can be consulting service
200 | 1254003 | WrongBaseToken | AppToken error
200 | 1254004 | WrongTableId | Table id wrong
200 | 1254005 | WrongViewId | View id wrong
200 | 1254006 | WrongRecordId | Record id wrong
200 | 1254007 | EmptyValue | Empty value
200 | 1254008 | EmptyView | Empty view
200 | 1254009 | WrongFieldId | Wrong fieldId
200 | 1254010 | ReqConvError | Request error
200 | 1254025 | InvalidCopyTypes | InvalidCopyTypes
200 | 1254030 | TooLargeResponse | TooLargeResponse
400 | 1254031 | InvalidAppName | The name length should not exceed 255.
400 | 1254036 | Base is copying, please try again later. | Base copy replicating, try again later
200 | 1254040 | BaseTokenNotFound | AppToken not found
200 | 1254041 | TableIdNotFound | Table not found
200 | 1254042 | ViewIdNotFound | View not found
200 | 1254043 | RecordIdNotFound | RecordIdNotFound
200 | 1254044 | FieldIdNotFound | FieldIdNotFound
200 | 1254060 | TextFieldConvFail | TextFieldConvFail
200 | 1254061 | NumberFieldConvFail | NumberFieldConvFail
200 | 1254062 | SingleSelectFieldConvFail | SingleSelectFieldConvFail
200 | 1254063 | MultiSelectFieldConvFail | MultiSelectFieldConvFail
200 | 1254064 | DatetimeFieldConvFail | DatetimeFieldConvFail
200 | 1254065 | CheckboxFieldConvFail | CheckboxFieldConvFail
200 | 1254066 | UserFieldConvFail | The value corresponding to the personnel field type is incorrect. The possible reasons are:<br>- The ID type specified by the user_id_type parameter does not match the type of the provided ID.<br>- An unrecognized type or structure was provided. Currently, only `id` is supported, and it must be passed as an array.<br>- An `open_id` was passed across applications. If you are passing an ID across applications, it is recommended to use `user_id`. The `open_id` obtained from different applications cannot be used interchangeably.
200 | 1254067 | LinkFieldConvFail | LinkFieldConvFail
200 | 1254100 | TableExceedLimit | TableExceedLimit, limited to 300
200 | 1254101 | ViewExceedLimit | ViewExceedLimit, limited to 200
200 | 1254102 | FileExceedLimit | FileExceedLimit
200 | 1254103 | RecordExceedLimit | RecordExceedLimit, limited to 20,000
200 | 1254104 | RecordAddOnceExceedLimit | RecordAddOnceExceedLimit, limited to 500
200 | 1254130 | TooLargeCell | TooLargeCell
200 | 1254290 | TooManyRequest | Request too fast, try again later
200 | 1254291 | Write conflict | The same data table does not support concurrent calls to the write interface, please check whether there is a concurrent call to the write interface. The writing interface includes: adding, modifying, and deleting records; adding, modifying, and deleting fields; modifying forms; modifying views, etc.
200 | 1254301 | OperationTypeError | Base does not have advanced permissions enabled or does not support enabling advanced permissions
200 | 1254304 | PermNotAllow | Advanced permissions for specific rows or columns are only available for Business and Enterprise editions
403 | 1254701 | DriveNodePermNotAllow | DriveNodePermNotAllow
404 | 1254702 | DriveNodeNotExist | DriveNodeNotExist
400 | 1254800 | InvalidParameter | Invalid Parameter, please fix it accorrding to msg and try again
200 | 1255001 | InternalError | Internal error, have any questions can be consulting service
200 | 1255002 | RpcError | Internal error, have any questions can be consulting service
200 | 1255003 | MarshalError | Serialization failed, have any questions can be consulting service
200 | 1255004 | UmMarshalError | Deserialization failed, have any questions can be consulting service
200 | 1255005 | ConvError | Internal error, have any questions can be consulting service
504 | 1255040 | Request timed out, please try again later | Try again

# Copy App

Copy a base app, you can specify to copy to a folder with permissions

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/copy
HTTP Method | POST
Rate Limit | [20 per minute](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.**<br>Enable any scope from the list | Duplicate base(base:app:copy)<br>View, comment, edit and manage Base(bitable:app)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Path parameters

Parameter | Type | Description
---|---|---
app_token | string | [Base App Token](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification#8121eebe)<br>**Example value**: "S404b*****e9PQsYDWYcNryFn0g"

### Request body

Parameter | Type | Required | Description
---|---|---|---
name | string | No | Base App Name<br>**Example value**: "test name"
folder_token | string | No | [Base App Folder Token](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#08bb5df)<br>**Example value**: "fldbco*****CIMltVc"
without_content | boolean | No | Whether to copy the Base content, take the value:<br>* true:   not copy<br>* false:    copy<br>**Example value**: false
time_zone | string | No | Base App Time Zone, [More Detail](https://feishu.feishu.cn/docx/YKRndTM7VoyDqpxqqeEcd67MnEf)<br>**Example value**: "Asia/Shanghai"

### Request body example
```json
{
    "name": "test name",
    "folder_token": "fldbco*****CIMltVc",
    "without_content": false,
    "time_zone": "Asia/Shanghai"
}
```

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
app | app | Response data
app_token | string | Base App Token
name | string | Base App Name
folder_token | string | Base App Folder Token
url | string | Base App URL
time_zone | string | Default table id

### Response body example
```json
{"code":0,
"msg":"success",
"data":{"app":{"app_token":"S404b*****e9PQsYDWYcNryFn0g",
"name":"test name",
"folder_token":"fldbco*****CIMltVc",
"url":"https://example.feishu.cn/base/S404b*****e9PQsYDWYcNryFn0g",
"time_zone":""//return default table Id only when created"}}}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
400 | 1254000 | WrongRequestJson | Request error
400 | 1254001 | WrongRequestBody | Request body error
400 | 1254002 | Fail | Internal error, have any questions can be consulting service
400 | 1254003 | WrongBaseToken | AppToken error
400 | 1254031 | InvalidAppName | App name is invalid, the length should not exceed 100 characters, and cannot contain ? / \ * : [ ]
400 | 1254036 | Base is copying, please try again later. | Base copy replicating, try again later
404 | 1254040 | BaseTokenNotFound | AppToken not found
400 | 1254290 | TooManyRequest | Request too fast, try again later
400 | 1254291 | Write conflict | The same data table does not support concurrent calls to the write interface, please check whether there is a concurrent call to the write interface. The writing interface includes: adding, modifying, and deleting records; adding, modifying, and deleting fields; modifying forms; modifying views, etc.
403 | 1254304 | PermNotAllow | Advanced permissions for specific rows or columns are only available for Business and Enterprise editions
403 | 1254701 | DriveNodePermNotAllow | Target folder has no permissions
404 | 1254702 | DriveNodeNotExist | Target folder does not exist
400 | 1254800 | InvalidParameter | Invalid Parameter, please fix it accorrding to msg and try again
500 | 1255001 | InternalError | Internal error, have any questions can be consulting service
500 | 1255002 | RpcError | Internal error, have any questions can be consulting service
500 | 1255003 | MarshalError | Serialization failed, have any questions can be consulting service
500 | 1255004 | UmMarshalError | Deserialization failed, have any questions can be consulting service
500 | 1255005 | ConvError | Internal error, have any questions can be consulting service
504 | 1255040 | Request timed out, please try again later | Try again

# Get App Information

Get App information through app_token

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token
HTTP Method | GET
Rate Limit | [20 per second](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.**<br>Enable any scope from the list | 获取多维表格信息(base:app:read)<br>View, comment, edit and manage Base(bitable:app)<br>View, comment, and export Base(bitable:app:readonly)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)

The instructions for AccessToken calling Docs API are detailed here [Docs API Overview](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN)

### Path parameters

Parameter | Type | Description
---|---|---
app_token | string | Base unique device identifier [app_token description](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification#8121eebe)<br>**Example value**: "appbcbWCzen6D8dezhoCH2RpMAh"

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
app | display_app | App information
app_token | string | AppToken information
name | string | Name
revision | int | Revison
is_advanced | boolean | IsAdvanced
time_zone | string | Base App Time Zone
formula_type | int | Document formula field type<br>Can be used in conjunction with [field API](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-field/create).<br>**Optional values are**:<br>- 1：Formula fields do not support setting types<br>- 2：Formula fields support setting types
advance_version | string | Advanced version<br>Can be used in conjunction with [role API](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-role/create).<br>**Optional values are**:<br>- v1：v1<br>- v2：v2

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "app": {
            "app_token": "appbcbWCzen6D8dezhoCH2RpMAh",
            "name": "mybase",
            "revision": 1,
            "is_advanced": false,
            "time_zone": "Asia/Beijing",
            "formula_type": 1,
            "advance_version": "v1"
        }
    }
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
200 | 1254000 | WrongRequestJson | Request error
200 | 1254001 | WrongRequestBody | Request body error
200 | 1254002 | Fail | Internal error, have any questions can be consulting service
200 | 1254003 | WrongBaseToken | AppToken error
200 | 1254004 | WrongTableId | Table id wrong
200 | 1254005 | WrongViewId | View id wrong
200 | 1254006 | WrongRecordId | Record id wrong
200 | 1254007 | EmptyValue | Empty value
200 | 1254008 | EmptyView | Empty view
200 | 1254009 | WrongFieldId | Wrong fieldId
200 | 1254010 | ReqConvError | Request error
200 | 1254030 | TooLargeResponse | TooLargeResponse
400 | 1254036 | Base is copying, please try again later. | Base copy replicating, try again later
200 | 1254040 | BaseTokenNotFound | AppToken not found
200 | 1254041 | TableIdNotFound | Table not found
200 | 1254042 | ViewIdNotFound | View not found
200 | 1254043 | RecordIdNotFound | RecordIdNotFound
200 | 1254044 | FieldIdNotFound | FieldIdNotFound
200 | 1254060 | TextFieldConvFail | TextFieldConvFail
200 | 1254061 | NumberFieldConvFail | NumberFieldConvFail
200 | 1254062 | SingleSelectFieldConvFail | SingleSelectFieldConvFail
200 | 1254063 | MultiSelectFieldConvFail | MultiSelectFieldConvFail
200 | 1254064 | DatetimeFieldConvFail | DatetimeFieldConvFail
200 | 1254065 | CheckboxFieldConvFail | CheckboxFieldConvFail
200 | 1254066 | UserFieldConvFail | The value corresponding to the personnel field type is incorrect. The possible reasons are:<br>- The ID type specified by the user_id_type parameter does not match the type of the provided ID.<br>- An unrecognized type or structure was provided. Currently, only `id` is supported, and it must be passed as an array.<br>- An `open_id` was passed across applications. If you are passing an ID across applications, it is recommended to use `user_id`. The `open_id` obtained from different applications cannot be used interchangeably.
200 | 1254067 | LinkFieldConvFail | LinkFieldConvFail
200 | 1254100 | TableExceedLimit | TableExceedLimit, limited to 300
200 | 1254101 | ViewExceedLimit | ViewExceedLimit, limited to 200
200 | 1254102 | FileExceedLimit | FileExceedLimit
200 | 1254103 | RecordExceedLimit | RecordExceedLimit, limited to 20,000
200 | 1254104 | RecordAddOnceExceedLimit | RecordAddOnceExceedLimit, limited to 500
200 | 1254130 | TooLargeCell | TooLargeCell
200 | 1254290 | TooManyRequest | Request too fast, try again later
200 | 1254291 | Write conflict | The same data table does not support concurrent calls to the write interface, please check whether there is a concurrent call to the write interface. The writing interface includes: adding, modifying, and deleting records; adding, modifying, and deleting fields; modifying forms; modifying views, etc.
200 | 1254301 | OperationTypeError | Base does not have advanced permissions enabled or does not support enabling advanced permissions
200 | 1255001 | InternalError | Internal error, have any questions can be consulting service
200 | 1255002 | RpcError | Internal error, have any questions can be consulting service
200 | 1255003 | MarshalError | Serialization failed, have any questions can be consulting service
200 | 1255004 | UmMarshalError | Deserialization failed, have any questions can be consulting service
200 | 1255005 | ConvError | Internal error, have any questions can be consulting service
504 | 1255040 | Request timed out, please try again later | Try again

# Update App Information

Update app information according to app_token

**Notice**：- Advanced permissions are not supported for Base in doc, sheet and wiki
- This API is not an atomic operation. It firstly modifies name, and then switches advanced permissions. It may be partial success

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token
HTTP Method | PUT
Rate Limit | [10 per second](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
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
app_token | string | base app token<br>**Example value**: "appbcbWCzen6D8dezhoCH2RpMAh"

### Request body

Parameter | Type | Required | Description
---|---|---|---
name | string | No | Base App Name<br>**Example value**: "new name"
is_advanced | boolean | No | Is advanced<br>**Example value**: false

You can modify the name or switch advanced permissions separately, and the parameters that are not filled in the request body will not be affected

### Request body example
```json
{
    "name": "new name",
    "is_advanced": false
}
```

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
app | display_app_v2 | App information
app_token | string | Base App Token
name | string | Base App Name
is_advanced | boolean | Advanced permissions on or off
time_zone | string | Base App Time Zone

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "app": {
            "app_token": "appbcbWCzen6D8dezhoCH2RpMAh",
            "name": "new name",
            "is_advanced": true,
            "time_zone":"Asia/Beijing"
        }
    }
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
200 | 1254000 | WrongRequestJson | Request error
200 | 1254001 | WrongRequestBody | Request body error
200 | 1254002 | Fail | Internal error, have any questions can be consulting service
200 | 1254003 | WrongBaseToken | AppToken error
200 | 1254010 | ReqConvError | Request error
200 | 1254031 | InvalidAppName | App name is invalid, the length should not exceed 100 characters, and cannot contain ? / \ * : [ ]
400 | 1254036 | Base is copying, please try again later. | Base copy replicating, try again later
200 | 1254040 | BaseTokenNotFound | AppToken not found
200 | 1254043 | RecordIdNotFound | RecordIdNotFound
200 | 1254200 | internal error | Internal error
200 | 1254290 | TooManyRequest | Request too fast, try again later
200 | 1254291 | Write conflict | The same data table does not support concurrent calls to the write interface, please check whether there is a concurrent call to the write interface. The writing interface includes: adding, modifying, and deleting records; adding, modifying, and deleting fields; modifying forms; modifying views, etc.
400 | 1254301 | OperationTypeError | Base does not have advanced permissions enabled or does not support enabling advanced permissions
403 | 1254302 | Permission denied. | No access rights, usually caused by the table opening of advanced permissions, please add a group containing applications in the advanced permissions settings and give this group read and write permissions
403 | 1254304 | The role has no permissions. | Advanced permissions for specific rows or columns are only available for Business and Enterprise editions
200 | 1255001 | InternalError | Internal error, have any questions can be consulting service
200 | 1255002 | RpcError | Internal error, have any questions can be consulting service
200 | 1255003 | MarshalError | Serialization failed, have any questions can be consulting service
200 | 1255004 | UmMarshalError | Deserialization failed, have any questions can be consulting service
504 | 1255040 | Request timed out, please try again later | Try again

## Other error code

**Error code** | **Cause**  | **Suggestion**          |
| ------- | ------- | ----------------- |
| 1254061 | The field's format is incorrect. | Make sure the parameter's format is correct.
