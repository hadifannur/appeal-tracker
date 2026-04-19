# Create a table

Add a new table in Base, supporting the input of table name, view name, and fields.

## Prerequisite

Before calling this API, ensure that the current calling identity (tenant_access_token or user_access_token) has the necessary document permissions, such as edit permissions for Base. Otherwise, the API will return an HTTP 403 or 400 status code. For more information, refer to [How to Grant Document Permissions to Apps or Users](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#16c6475a).

## Usage limits

In each Base, the total number of tables and dashboards is capped at 100.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/tables
HTTP Method | POST
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
app_token | string | Unique identifier for Base [app_token parameter description](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification#8121eebe)<br>**Example value**: "appbcbWCzen6D8dezhoCH2RpMAh"<br>**Data validation rules**:<br>- Minimum length: `1` characters

### Request body

Parameter | Type | Required | Description
---|---|---|---
table | req_table | No | table
name | string | No | Name for the table.<br>Please note:<br>1. The first and last spaces in the name will be removed.<br>**Example value**: "table name"<br>**Data validation rules**:<br>- Length range: `1` ～ `100` characters
default_view_name | string | No | Name of the default table view<br>Please note:<br>1. The first and last spaces in the name will be removed.<br>2. The characters [ ] are not allowed to be included.<br>**Example value**: "Table"
fields | app.table.create_header\[\] | No | Initial fields of the data table. To learn how to fill in the fields, refer to the [Field Editing Guide](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-field/guide).<br>**Note**:<br>- If the `default_view_name` field is passed, the `fields` field must also be passed.<br>- If the `default_view_name` field is not passed, the `fields` field is optional.<br>- If neither the `default_view_name` field nor the `fields` field is passed, an empty data table containing only the index field will be created.<br>- The first field of the data table is the index field. The index field only supports the following types:<br>- 1: Multi-line text<br>- 2: Number<br>- 5: Date<br>- 13: Phone number<br>- 15: Hyperlink<br>- 20: Formula<br>- 22: Geographic location<br>**Data validation rules**:<br>- Length range: `1` ～ `300`
field_name | string | Yes | Field name<br>**Example value**: "Text"
type | int | Yes | Field type<br>**Example value**: 1<br>**Optional values are**:<br>- 1：Multiline<br>- 2：Number<br>- 3：Single option<br>- 4：Multiple options<br>- 5：Date<br>- 7：Checkbox<br>- 11：Person<br>- 13：PhoneNumber<br>- 15：Link<br>- 17：Attachment<br>- 18：One-way link<br>- 20：Formula<br>- 21：Two-way link<br>- 22：Location<br>- 23：group<br>- 1001：Date created<br>- 1002：Last modified date<br>- 1003：Created by<br>- 1004：Modified by<br>- 1005：AutoSerial
ui_type | string | No | Field Property, ref: [Field edit development guide](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-field/guide)<br>**Example value**: "Progress"<br>**Optional values are**:<br>- Text：multiline text<br>- Barcode：barcode<br>- Number：number<br>- Progress：progress<br>- Currency：currency<br>- Rating：score<br>- SingleSelect：radio<br>- MultiSelect：multiple choice<br>- DateTime：date<br>- Checkbox：checkbox<br>- User：Personnel<br>- GroupChat：group<br>- Phone：Phone number<br>- Url：Hyperlink<br>- Attachment：Attachment<br>- SingleLink：one-way association<br>- Formula：formula<br>- DuplexLink：Two-way link<br>- Location：Geographical location<br>- CreatedTime：Creation time<br>- ModifiedTime：Last update time<br>- CreatedUser：creator<br>- ModifiedUser：Modifier<br>- AutoNumber：Automatic numbering
property | app.table.field.property | No | Field description
options | app.table.field.property.option\[\] | No | Whether to disable synchronization, if true, it means that synchronization of the description content to the problem description of the form is prohibited (only valid when fields are added or modified)
name | string | No | Option name<br>**Example value**: "Red."
id | string | No | Option ID, not allowed to specify ID at creation time<br>**Example value**: "optKl35lnG"
color | int | No | Option color<br>**Example value**: 0.<br>**Data validation rules**:<br>- Value range: `0` ～ `54`
formatter | string | No | Display format of numbers and formula fields<br>**Example value**: "0."
date_formatter | string | No | The display format of the date, creation time, and last updated time fields<br>**Example value**: "Date format"
auto_fill | boolean | No | New records in the date field are automatically filled in Creation time<br>**Example value**: False
multiple | boolean | No | Multiple members are allowed to be added in the personnel field, and multiple records are allowed in one-way association and two-way association<br>**Example value**: False
table_id | string | No | The id of the associated data table in the one-way association, two-way association field<br>**Example value**: "tblsRc9GRRXKqhvW"
table_name | string | No | The name of the associated data table in the one-way association, two-way association field<br>**Example value**: ""Table2""
back_field_name | string | No | The name of the corresponding bidirectional association field in the associated data table in the bidirectional association field<br>**Example value**: ""Table1 - Bidirectional Association""
auto_serial | app.field.property.auto_serial | No | Automatic numbering type
type | string | Yes | Automatic numbering type<br>**Example value**: "auto_increment_number"<br>**Optional values are**:<br>- custom：Custom number<br>- auto_increment_number：Autoincrement number
options | app.field.property.auto_serial.options\[\] | No | List of auto-numbering rules
type | string | Yes | Optional rule item types for auto-numbering<br>**Example value**: "created_time"<br>**Optional values are**:<br>- system_number：Incremental digits, value range 1-9<br>- fixed_text：Fixed characters, maximum length: 20<br>- created_time：Creation time, supports formats "yyyyMMdd", "yyyyMM", "yyyy", "MMdd", "MM", "dd"
value | string | Yes | Values corresponding to auto-numbered optional rule item types<br>**Example value**: "YyyyMMdd"
location | app.field.property.location | No | Geolocation input method
input_type | string | Yes | Geolocation input restrictions<br>**Example value**: "not_limit"<br>**Optional values are**:<br>- only_mobile：Only allow uploads on mobile ends<br>- not_limit：Unlimited
formula_expression | string | No | Expression of formula field<br>**Example value**: "Bitable:: $table [tblNj92WQBAasdEf]. $field [fldMV60rYs] * 2"
allowed_edit_modes | allowed_edit_modes | No | Editing modes supported by the field
manual | boolean | No | Whether to allow manual entry<br>**Example value**: true
scan | boolean | No | Whether to allow mobile end entry<br>**Example value**: true
min | number(float) | No | Minimum data range for fields such as progress, score, etc<br>**Example value**: 0
max | number(float) | No | Maximum data range for fields such as progress, score, etc<br>**Example value**: 10
range_customize | boolean | No | Whether fields such as progress support custom ranges<br>**Example value**: true
currency_code | string | No | Currency<br>**Example value**: "CNY"
rating | rating | No | Relevant settings for scoring fields
symbol | string | No | Symbol display for rating fields<br>**Example value**: "star"
description | app.table.field.description | No | Field description
disable_sync | boolean | No | Whether to disable synchronization, if true, it means that synchronization of the description content to the problem description of the form is prohibited (only valid when fields are added or modified)<br>**Example value**: true<br>**Default value**: `true`
text | string | No | Field description content<br>**Example value**: "This is a field description"

### Request body example
```json
{
    "table":{
        "name":"table name",
        "default_view_name":"Grid",
        "fields":[
            {
                "field_name":"Text",
                "type":1
            }
        ]
    }
}
```

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
table_id | string | Bitable data table unique device identifier [table_id parameter description] (/ssl: ttdoc/uAjLw4CM/ukTMukTMukTM/bitable/notification #735fe883)
default_view_id | string | The id of the default table view, which is returned only if default_view_name or fields are filled in the request parameters
field_id_list | string\[\] | The id list of the initial field of the data table, which will only be returned if fields are filled in the request parameter

### Response body example
```json
{
	"Code": 0,
	"Msg": "success",
	"Data": {
		"table_id": "tblDBTWm6Es84d8c",
		"default_view_id": "vewUuKOz2R",
		"field_id_list": [
			"Fldhr2hBEA"
		]
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
200 | 1254007 | EmptyValue | Empty value
200 | 1254008 | EmptyView | Empty view
200 | 1254009 | WrongFieldId | Wrong fieldId
200 | 1254010 | ReqConvError | Request error
400 | 1254012 | NotSupportFieldOrView | Unsupported fields or views
200 | 1254013 | TableNameDuplicated | TableNameDuplicated
400 | 1254014 | FieldNameDuplicated | Field name duplicate
400 | 1254021 | EmptyViewName | View name is empty
400 | 1254022 | InvalidViewName | Invalid view name
400 | 1254029 | InvalidFieldName | Invalid field name
200 | 1254030 | TooLargeResponse | TooLargeResponse
200 | 1254036 | Base is copying, please try again later. | Base copy replicating, try again later
200 | 1254040 | BaseTokenNotFound | AppToken not found
200 | 1254041 | TableIdNotFound | Table not found
200 | 1254044 | FieldIdNotFound | FieldIdNotFound
200 | 1254060 | TextFieldConvFail | TextFieldConvFail
200 | 1254061 | NumberFieldConvFail | NumberFieldConvFail
200 | 1254062 | SingleSelectFieldConvFail | SingleSelectFieldConvFail
200 | 1254063 | MultiSelectFieldConvFail | MultiSelectFieldConvFail
200 | 1254064 | DatetimeFieldConvFail | DatetimeFieldConvFail
200 | 1254065 | CheckboxFieldConvFail | CheckboxFieldConvFail
200 | 1254066 | UserFieldConvFail | The value corresponding to the personnel field type is incorrect. The possible reasons are:<br>- The ID type specified by the user_id_type parameter does not match the type of the provided ID.<br>- An unrecognized type or structure was provided. Currently, only `id` is supported, and it must be passed as an array.<br>- An `open_id` was passed across applications. If you are passing an ID across applications, it is recommended to use `user_id`. The `open_id` obtained from different applications cannot be used interchangeably.
200 | 1254067 | LinkFieldConvFail | LinkFieldConvFail
200 | 1254100 | TableExceedLimit | TableExceedLimit, limited to 100
200 | 1254101 | ViewExceedLimit | ViewExceedLimit, limited to 200
200 | 1254130 | TooLargeCell | TooLargeCell
200 | 1254290 | TooManyRequest | Request too fast, try again later
200 | 1254291 | Write conflict | The same data table does not support concurrent calls to the write interface, please check whether there is a concurrent call to the write interface. The writing interface includes: adding, modifying, and deleting records; adding, modifying, and deleting fields; modifying forms; modifying views, etc.
200 | 1254301 | OperationTypeError | Base does not have advanced permissions enabled or does not support enabling advanced permissions
403 | 1254302 | Permission denied. | No access rights, usually caused by the table opening of advanced permissions, please add a group containing applications in the advanced permissions settings and give this group read and write permissions
400 | 1254607 | Data not ready, please try again later | Internal error, have any questions can be consulting service
200 | 1255001 | InternalError | Internal error, have any questions can be consulting service
200 | 1255002 | RpcError | Internal error, have any questions can be consulting service
200 | 1255003 | MarshalError | Serialization failed, have any questions can be consulting service
200 | 1255004 | UmMarshalError | Deserialization failed, have any questions can be consulting service
200 | 1255005 | ConvError | Internal error, have any questions can be consulting service

# Batch create table

Batch create table.

## Prerequisite

Before calling this API, ensure that the current calling identity (tenant_access_token or user_access_token) has the necessary document permissions, such as edit permissions for Base. Otherwise, the API will return an HTTP 403 or 400 status code. For more information, refer to [How to Grant Document Permissions to Apps or Users](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#16c6475a).

## Usage limits

In each Base, the total number of tables and dashboards is capped at 100.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/tables/batch_create
HTTP Method | POST
Rate Limit | [10 per second](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.** | View, comment, edit and manage Base(bitable:app)
Required field scopes | **Notice**：The response body of the API contains the following sensitive fields, and they will be returned only after corresponding scopes are added. If you do not need the fields, it is not recommended that you request the scopes.<br>Obtain user ID(contact:user.employee_id:readonly)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Path parameters

Parameter | Type | Description
---|---|---
app_token | string | Unique identifier for Base [app_token parameter description](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification#8121eebe)<br>**Example value**: "appbcbWCzen6D8dezhoCH2RpMAh"

### Query parameters

Parameter | Type | Required | Description
---|---|---|---
user_id_type | string | No | User ID categories<br>**Example value**: open_id<br>**Optional values are**:<br>- open_id：Identifies a user to an app. The same user has different Open IDs in different apps. [How to get Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid)<br>- union_id：Identifies a user to a tenant that acts as a developer. A user has the same Union ID in apps developed by the same developer, and has different Union IDs in apps developed by different developers. A developer can use Union ID to link the same user's identities in multiple apps.[How to get Union ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id)<br>- user_id：Identifies a user to a tenant. The same user has different User IDs in different tenants. In one single tenant, a user has the same User ID in all apps （including store apps）. User ID is usually used to communicate user data between different apps. [How to get User ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**Default value**: `open_id`<br>**When the value is `user_id`, the following field scopes are required**:<br>Obtain user ID(contact:user.employee_id:readonly)

### Request body

Parameter | Type | Required | Description
---|---|---|---
tables | req_table\[\] | No | tables
name | string | No | Name for the table. This field is required.<br>Please note:<br>1. The first and last spaces in the name will be removed.<br>2. If the name is empty or the same as the old name, the interface will still return success, but the name will not be changed.<br>**Example value**: "table name"<br>**Data validation rules**:<br>- Length range: `1` ～ `100` characters

### Request body example
```json
{
    "tables": [
        {
            "name": "table name"
        }
    ]
}
```

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
table_ids | string\[\] | table ids

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "table_ids": [
            "tblIovTTN2eIW2hn"
        ]
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
400 | 1254013 | TableNameDuplicated | TableNameDuplicated
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
200 | 1254100 | TableExceedLimit | TableExceedLimit, limited to 150
200 | 1254101 | ViewExceedLimit | ViewExceedLimit, limited to 200
200 | 1254102 | FileExceedLimit | FileExceedLimit
200 | 1254103 | RecordExceedLimit | RecordExceedLimit, limited to 20,000
200 | 1254104 | RecordAddOnceExceedLimit | RecordAddOnceExceedLimit, limited to 500
200 | 1254130 | TooLargeCell | TooLargeCell
200 | 1254290 | TooManyRequest | Request too fast, try again later
200 | 1254291 | Write conflict | The same data table does not support concurrent calls to the write interface, please check whether there is a concurrent call to the write interface. The writing interface includes: adding, modifying, and deleting records; adding, modifying, and deleting fields; modifying forms; modifying views, etc.
200 | 1254301 | OperationTypeError | Base does not have advanced permissions enabled or does not support enabling advanced permissions
403 | 1254302 | The role has no permissions. | The role has no permissions.
200 | 1255001 | InternalError | Internal error, have any questions can be consulting service
200 | 1255002 | RpcError | Internal error, have any questions can be consulting service
200 | 1255003 | MarshalError | Serialization failed, have any questions can be consulting service
200 | 1255004 | UmMarshalError | Deserialization failed, have any questions can be consulting service
200 | 1255005 | ConvError | Internal error, have any questions can be consulting service
504 | 1255040 | Request timed out, please try again later | Try again

# Update data table

This interface is used to update the basic information of the data table, including the name of the data table, etc.

For the first access, please refer to [Cloud Document Interface QuickStart](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN) & [Base OpenAPI Access Guide](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification) 

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/tables/:table_id
HTTP Method | PATCH
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
app_token | string | Base unique device identifier [app_token description](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification#8121eebe)<br>**Example value**: "XrgTb4y1haKYnasu0xXb1g7lcSg"<br>**Data validation rules**:<br>- Minimum length: `1` characters
table_id | string | Base data table unique device identifier [table_id description](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification#735fe883)<br>**Example value**: "tbl1TkhyTWDkSoZ3"

### Request body

Parameter | Type | Required | Description
---|---|---|---
name | string | No | The new name for the data table. <br>Please note: <br>1. The first and last spaces in the name will be removed. <br>2. If the name is empty or the same as the old name, the interface will still return success, but the name will not be changed.<br>**Example value**: "new name"<br>**Data validation rules**:<br>- Length range: `1` ～ `100` characters<br>- Regular expression: `^[^\[\]\:\\\/\?\*]+$`

### Request body example
```json
{
    "name": "new name"
}
```

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
name | string | The name of the data table

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "name": "new name"
    }
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
400 | 1254001 | WrongRequestBody | Request body error
400 | 1254002 | Fail | Internal error, have any questions can be consulting service
400 | 1254003 | WrongBaseToken | AppToken error
400 | 1254004 | WrongTableId | Table id wrong
400 | 1254013 | TableNameDuplicated | TableNameDuplicated
403 | 1254036 | Base is copying, please try again later. | Base copy replicating, try again later
404 | 1254040 | BaseTokenNotFound | AppToken not found
404 | 1254041 | TableIdNotFound | Table not found
429 | 1254290 | TooManyRequest | Request too fast, try again later
403 | 1254302 | Permission denied. | No access rights, usually caused by the table opening of advanced permissions, please add a group containing applications in the advanced permissions settings and give this group read and write permissions
500 | 1255001 | InternalError | Internal error, have any questions can be consulting service

# List all tables

According to app_token, get all tables under app.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/tables
HTTP Method | GET
Rate Limit | [20 per second](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.**<br>Enable any scope from the list | View, comment, edit and manage Base(bitable:app)<br>View, comment, and export Base(bitable:app:readonly)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)

The instructions for AccessToken calling Docs API are detailed here [Docs API Overview](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN)

### Path parameters

Parameter | Type | Description
---|---|---
app_token | string | Base unique device identifier [app_token description](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification#8121eebe)<br>**Example value**: "appbcbWCzen6D8dezhoCH2RpMAh"

### Query parameters

Parameter | Type | Required | Description
---|---|---|---
page_token | string | No | Page identifier. It is not filled in the first request, indicating traversal from the beginning; when there will be more groups, the new page_token will be returned at the same time, and the next traversal can use the page_token to get more groups<br>**Example value**: tblsRc9GRRXKqhvW
page_size | int | No | paging size<br>**Example value**: 10<br>**Default value**: `20`<br>**Data validation rules**:<br>- Maximum value: `100`

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
has_more | boolean | Whether the response body has more parameters
page_token | string | Page identifier, when has_more is true, a new page_token will also be returned. Otherwise, page_token will not be returned
total | int | Total
items | app.table\[\] | Table information
table_id | string | Table Id
revision | int | Table Revision
name | string | Table name

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "has_more": false,
        "page_token": "tblKz5D60T4JlfcT",
        "total": 1,
        "items": [
            {
                "table_id": "tblsRc9GRRXKqhvW",
                "revision": 1,
                "name": "table 1"
            }
        ]
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
400 | 1254011 | Page size must greater than 0. | Page size must greater than 0.
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
403 | 1254302 | The role has no permissions. | The role has no permissions.
200 | 1255001 | InternalError | Internal error, have any questions can be consulting service
200 | 1255002 | RpcError | Internal error, have any questions can be consulting service
200 | 1255003 | MarshalError | Serialization failed, have any questions can be consulting service
200 | 1255004 | UmMarshalError | Deserialization failed, have any questions can be consulting service
200 | 1255005 | ConvError | Internal error, have any questions can be consulting service
504 | 1255040 | Request timed out, please try again later | Try again

# Delete Table

Delete a table

For the first access, please refer to [Cloud Document Interface QuickStart](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN) & [Base OpenAPI Access Guide](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification) 

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/tables/:table_id
HTTP Method | DELETE
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
app_token | string | Base unique device identifier [app_token description](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification#8121eebe)<br>**Example value**: "appbcbWCzen6D8dezhoCH2RpMAh"<br>**Data validation rules**:<br>- Minimum length: `1` characters
table_id | string | Base data table unique device identifier [table_id description](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification#735fe883)<br>**Example value**: "tblsRc9GRRXKqhvW"

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {}
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
403 | 1254034 | The last table cannot be deleted. | The last table cannot be deleted.
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
400 | 1254607 | Data not ready, please try again later | There are usually two situations when this error occurs: 1. The last submitted modification has not been processed; 2. The data is too large and the server calculation times out; <br>This error code can be appropriately retried.
403 | 1254608 | Same API requests are submitted repeatedly. | Verify that the request parameters of this request are exactly the same as the previous one.

# Batch delete table

Batch delete table.

For the first access, please refer to [Cloud Document Interface QuickStart](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN) & [Base OpenAPI Access Guide](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification) 

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/tables/batch_delete
HTTP Method | POST
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
app_token | string | Base unique device identifier [app_token description](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification#8121eebe)<br>**Example value**: "appbcbWCzen6D8dezhoCH2RpMAh"<br>**Data validation rules**:<br>- Minimum length: `1` characters

### Request body

Parameter | Type | Required | Description
---|---|---|---
table_ids | string\[\] | No | Base data table unique device identifier,Currently supports up to 50 data tables in one operation[table_id description](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification#735fe883)<br>**Example value**: ["tbl1TkhyTWDkSoZ3"]

### Request body example
```json
{
    "table_ids": [
        "tbl1TkhyTWDkSoZ3"
    ]
}
```

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {}
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
403 | 1254034 | The last table cannot be deleted. | The last table cannot be deleted.
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
403 | 1254302 | Base role permission is missing. | No access rights, usually caused by the table opening of advanced permissions, please add a group containing applications in the advanced permissions settings and give this group read and write permissions
200 | 1255001 | InternalError | Internal error, have any questions can be consulting service
200 | 1255002 | RpcError | Internal error, have any questions can be consulting service
200 | 1255003 | MarshalError | Serialization failed, have any questions can be consulting service
200 | 1255004 | UmMarshalError | Deserialization failed, have any questions can be consulting service
200 | 1255005 | ConvError | Internal error, have any questions can be consulting service
504 | 1255040 | Request timed out, please try again later | Try again
400 | 1254607 | Data not ready, please try again later | There are usually two situations when this error occurs: 1. The last submitted modification has not been processed; 2. The data is too large and the server calculation times out; <br>This error code can be appropriately retried.
