# New view

Add a view to the data table

## Use restrictions

The maximum number of views supported is 200, including public views, locked views, and personal views. Therefore, the number of views that individuals see in Bitable may only be partial views.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/tables/:table_id/views
HTTP Method | POST
Rate Limit | [10 per second](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.** | View, comment, edit and manage Base(bitable:app)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

The instructions for AccessToken calling Docs API are detailed here [Docs API Overview](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN)

### Path parameters

Parameter | Type | Description
---|---|---
app_token | string | Base app token<br>**Example value**: "AppbcbWCzen6D8dezhoCH2RpMAh"<br>**Data validation rules**:<br>- Minimum length: `1` characters
table_id | string | Table id<br>**Example value**: "TblsRc9GRRXKqhvW"

### Request body

Parameter | Type | Required | Description
---|---|---|---
view_name | string | Yes | View name<br>**Example value**: "Gantt View 1"
view_type | string | No | View type<br>**Example value**: "gantt"<br>**Optional values are**:<br>- grid：Grid view<br>- kanban：Kanban view<br>- gallery：Gallery view<br>- gantt：Gantt view<br>- form：Form view

### Request body example
```json
{
    "view_name": "Gantt View 1",
    "view_type": "gantt"
}
```

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
view | app.table.view | View
view_id | string | View Id
view_name | string | View name
view_type | string | View type

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "view": {
            "view_id": "vewTpR1urY",
            "view_name": "Gantt View 1",
            "view_type": "gantt"
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
200 | 1254016 | InvalidSort | invalid sort
200 | 1254018 | InvalidFilter | The filter parameter is incorrect. Please refer to [Record filter development guide](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/record-filter-guide) for information on how to fill in the filter parameter.
200 | 1254019 | InvalidViewType | Invalid view type
200 | 1254020 | ViewNameDuplicated | Duplicate view name
200 | 1254021 | EmptyViewName | View name is empty
200 | 1254022 | InvalidViewName | Invalid view name
200 | 1254030 | TooLargeResponse | TooLargeResponse
400 | 1254036 | Base is copying, please try again later. | Base copy replicating, try again later
200 | 1254040 | BaseTokenNotFound | AppToken not found
200 | 1254041 | TableIdNotFound | Table not found
200 | 1254042 | ViewIdNotFound | View not found
200 | 1254043 | RecordIdNotFound | RecordIdNotFound
200 | 1254044 | FieldIdNotFound | FieldIdNotFound
200 | 1254045 | FieldNameNotFound | Field name does not exist
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
403 | 1254302 | RolePermNotAllow | The role has no permissions.
403 | 1254304 | PermNotAllow | The role has no permissions.
403 | 1254306 | The tenant or base owner is subject to base plan limits. | The number of resources subscribed by the tenant or base administrator reaches the limit, please contact the tenant or base administrator to upgrade the version
200 | 1255001 | InternalError | Internal error, have any questions can be consulting service
200 | 1255002 | RpcError | Internal error, have any questions can be consulting service
200 | 1255003 | MarshalError | Serialization failed, have any questions can be consulting service
200 | 1255004 | UmMarshalError | Deserialization failed, have any questions can be consulting service
200 | 1255005 | ConvError | Internal error, have any questions can be consulting service
504 | 1255040 | Request timed out, please try again later | Try again
400 | 1254607 | Data not ready, please try again later | There are usually two situations when this error occurs: 1. The last submitted modification has not been processed; 2. The data is too large and the server calculation times out; <br>This error code can be appropriately retried.
403 | 1254608 | ReqRecommited | Same API requests are submitted repeatedly.

# Update view

This interface is used to incrementally modify view information.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/tables/:table_id/views/:view_id
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
app_token | string | Base app token<br>**Example value**: "Bascng7vrxcxpig7geggXiCtadY"<br>**Data validation rules**:<br>- Minimum length: `1` characters
table_id | string | Table ID<br>**Example value**: "tblsRc9GRRXKqhvW"
view_id | string | View ID<br>**Example value**: "vewTpR1urY"

### Request body

Parameter | Type | Required | Description
---|---|---|---
view_name | string | No | View name<br>**Example value**: "Grid"
property | app.table.view.property | No | View properties
filter_info | app.table.view.property.filter_info | No | Filter conditions
conjunction | string | Yes | Relationship of Multiple Filter Criteria<br>**Example value**: "and"<br>**Optional values are**:<br>- and：And<br>- or：Or<br>**Default value**: `and`
conditions | app.table.view.property.filter_info.condition\[\] | Yes | Filter Criteria<br>**Data validation rules**:<br>- Maximum length: `50`
field_id | string | Yes | Field unique ID for filtering<br>**Example value**: "fldVioU**1"
operator | string | Yes | Type of filter operation<br>**Example value**: "is"<br>**Optional values are**:<br>- is：Equal to<br>- isNot：Does not equal<br>- contains：Include<br>- doesNotContain：Not included<br>- isEmpty：Is empty<br>- isNotEmpty：Not empty<br>- isGreater：Greater than<br>- isGreaterEqual：Greater than or equal to<br>- isLess：Less than<br>- isLessEqual：Less than or equal to<br>**Default value**: `is`
value | string | No | Filter value<br>**Example value**: "["optbdVH***", "optrpd3***"]"
hidden_fields | string\[\] | No | List of hidden field IDs<br>**Example value**: ["fldVioU**2"]<br>**Data validation rules**:<br>- Maximum length: `300`
hierarchy_config | app.table.view.property.hierarchy_config | No | Table view hierarchy settings
field_id | string | No | Hierarchy's associated column id<br>**Example value**: "fldTca**hb"

### Request body example
```json
{
    "view_name": "grid",
    "property": {
        "filter_info": {
            "conditions": [
                {
                    "field_id": "fldpTw2262",
                    "operator": "isGreater",
                    "value": "[\"ExactDate\",\"1642672432000\"]"
                }
            ],
            "conjunction": "and"
        },
        "hidden_fields": null
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
view | app.table.view | View information
view_id | string | View Id
view_name | string | View name
view_type | string | View type
property | app.table.view.property | View properties
filter_info | app.table.view.property.filter_info | Filter conditions
conjunction | string | Relationship of Multiple Filter Criteria<br>**Optional values are**:<br>- and：And<br>- or：Or
conditions | app.table.view.property.filter_info.condition\[\] | Filter Criteria
field_id | string | Field unique ID for filtering
operator | string | Type of filter operation<br>**Optional values are**:<br>- is：Equal to<br>- isNot：Does not equal<br>- contains：Include<br>- doesNotContain：Not included<br>- isEmpty：Is empty<br>- isNotEmpty：Not empty<br>- isGreater：Greater than<br>- isGreaterEqual：Greater than or equal to<br>- isLess：Less than<br>- isLessEqual：Less than or equal to
value | string | Filter value
condition_id | string | Unique ID of filter condition
field_type | int | Field type for filtering <br>1: Multiline<br>2: Number<br>3: Single option<br>4: Multiple options<br>5: Date<br>7: Checkbox<br>11: Person<br>13: PhoneNumber<br>15: Link<br>17: Attachment<br>18: One-way link<br>19: LOOKUP<br>20: Formula<br>21: Two-way link<br>22: Location<br>23: GroupChat<br>1001: Date created<br>1002: Last modified date <br>1003: Created by<br>1004: Modified by<br>1005: AutoSerial
condition_omitted | boolean | Is the filter condition default?
hidden_fields | string\[\] | List of hidden field IDs
hierarchy_config | app.table.view.property.hierarchy_config | Table view hierarchy settings
field_id | string | Hierarchy's associated column id

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "view": {
            "view_id": "vewsOleexJ",
            "view_name": "grid",
            "view_type": "grid",
            "property": {
                "filter_info": {
                    "condition_omitted": null,
                    "conditions": [
                        {
                            "condition_id": "conuKMQNNg",
                            "field_id": "fldVioU**1",
                            "field_type": 1,
                            "operator": "is",
                            "value": "[\"text content\"]"
                        }
                    ],
                    "conjunction": "and"
                },
                "hidden_fields": null
            }
        }
    }
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
400 | 1254000 | WrongRequestJson | Request error
400 | 1254001 | WrongRequestBody | Request body error
400 | 1254002 | Fail | Internal error, have any questions can be consulting service
400 | 1254003 | WrongBaseToken | AppToken error
400 | 1254004 | WrongTableId | Table id wrong
400 | 1254005 | WrongViewId | View id wrong
400 | 1254006 | WrongRecordId | Record id wrong
400 | 1254007 | EmptyValue | Empty value
400 | 1254008 | EmptyView | Empty view
400 | 1254009 | WrongFieldId | Wrong fieldId
400 | 1254010 | ReqConvError | Request error
400 | 1254012 | UnsupportedFieldType | UnsupportedFieldType
400 | 1254016 | InvalidSort | invalid sort
400 | 1254018 | InvalidFilter | The filter parameter is incorrect. Please refer to [Record filter development guide](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/record-filter-guide) for information on how to fill in the filter parameter.
400 | 1254019 | InvalidViewType | Invalid view type
400 | 1254020 | ViewNameDuplicated | Duplicate view name
400 | 1254021 | EmptyViewName | View name is empty
400 | 1254022 | InvalidViewName | Invalid view name
400 | 1254030 | TooLargeResponse | TooLargeResponse
400 | 1254032 | The role name is invalid, please modify it. | Invalid role name
400 | 1254033 | The role name is duplicated, please modify it. | Role name duplicated
400 | 1254036 | Base is copying, please try again later. | Base copy replicating, try again later
404 | 1254040 | BaseTokenNotFound | AppToken not found
404 | 1254041 | TableIdNotFound | Table not found
404 | 1254042 | ViewIdNotFound | View not found
404 | 1254043 | RecordIdNotFound | RecordIdNotFound
404 | 1254044 | FieldIdNotFound | FieldIdNotFound
404 | 1254045 | FieldNameNotFound | Field name does not exist
404 | 1254047 | Role id is not found. | Role not found
400 | 1254048 | MemberNotFound | Member not found
404 | 1254049 | Form field is not found. | Form field id does not exist
400 | 1254060 | TextFieldConvFail | TextFieldConvFail
400 | 1254061 | NumberFieldConvFail | NumberFieldConvFail
400 | 1254062 | SingleSelectFieldConvFail | SingleSelectFieldConvFail
400 | 1254063 | MultiSelectFieldConvFail | MultiSelectFieldConvFail
400 | 1254064 | DatetimeFieldConvFail | DatetimeFieldConvFail
400 | 1254065 | CheckboxFieldConvFail | CheckboxFieldConvFail
400 | 1254066 | UserFieldConvFail | The value corresponding to the personnel field type is incorrect. The possible reasons are:<br>- The ID type specified by the user_id_type parameter does not match the type of the provided ID.<br>- An unrecognized type or structure was provided. Currently, only `id` is supported, and it must be passed as an array.<br>- An `open_id` was passed across applications. If you are passing an ID across applications, it is recommended to use `user_id`. The `open_id` obtained from different applications cannot be used interchangeably.
400 | 1254067 | LinkFieldConvFail | LinkFieldConvFail
400 | 1254100 | TableExceedLimit | TableExceedLimit, limited to 300
400 | 1254101 | ViewExceedLimit | ViewExceedLimit, limited to 200
400 | 1254103 | RecordExceedLimit | RecordExceedLimit, limited to 20,000
400 | 1254104 | RecordAddOnceExceedLimit | RecordAddOnceExceedLimit, limited to 500
400 | 1254110 | Role exceeds limit | Role exceed limit, limited to 30
400 | 1254130 | TooLargeCell | TooLargeCell
429 | 1254290 | TooManyRequest | Request too fast, try again later
400 | 1254291 | Write conflict | The same data table does not support concurrent calls to the write interface, please check whether there is a concurrent call to the write interface. The writing interface includes: adding, modifying, and deleting records; adding, modifying, and deleting fields; modifying forms; modifying views, etc.
400 | 1254301 | OperationTypeError | Base does not have advanced permissions enabled or does not support enabling advanced permissions
403 | 1254302 | Permission denied. | No access rights, usually caused by the table opening of advanced permissions, please add a group containing applications in the advanced permissions settings and give this group read and write permissions
403 | 1254306 | InternalError | Internal error, have any questions can be consulting service
500 | 1255001 | RpcError | Internal error, have any questions can be consulting service
500 | 1255002 | MarshalError | Serialization failed, have any questions can be consulting service
500 | 1255003 | UmMarshalError | Deserialization failed, have any questions can be consulting service
500 | 1255004 | ConvError | Internal error, have any questions can be consulting service
500 | 1255005 | Request timed out, please try again later | Try again
504 | 1255040 | Request timed out, please try again later. | There are usually two situations when this error occurs: 1. The last submitted modification has not been processed; 2. The data is too large and the server calculation times out; <br>This error code can be appropriately retried.
400 | 1254607 | Data not ready, please try again later | There are usually two situations when this error occurs: 1. The last submitted modification has not been processed; 2. The data is too large and the server calculation times out; This error code can be appropriately retried.
403 | 1254608 | Same API requests are submitted repeatedly. | Same API requests are submitted repeatedly.

# List view

Get all views of the data table based on app_token and table_id

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/tables/:table_id/views
HTTP Method | GET
Rate Limit | [20 per second](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.**<br>Enable any scope from the list | View, comment, edit and manage Base(bitable:app)<br>View, comment, and export Base(bitable:app:readonly)
Required field scopes | **Notice**：The response body of the API contains the following sensitive fields, and they will be returned only after corresponding scopes are added. If you do not need the fields, it is not recommended that you request the scopes.<br>Obtain user ID(contact:user.employee_id:readonly)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)

The instructions for AccessToken calling Docs API are detailed here [Docs API Overview](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN)

### Path parameters

Parameter | Type | Description
---|---|---
app_token | string | Base app token<br>**Example value**: "AppbcbWCzen6D8dezhoCH2RpMAh"<br>**Data validation rules**:<br>- Minimum length: `1` characters
table_id | string | Table id<br>**Example value**: "TblsRc9GRRXKqhvW"

### Query parameters

Parameter | Type | Required | Description
---|---|---|---
page_size | int | No | **Example value**: 10<br>**Data validation rules**:<br>- Maximum value: `100`
page_token | string | No | Page identifier. It is not filled in the first request, indicating traversal from the beginning; when there will be more groups, the new page_token will be returned at the same time, and the next traversal can use the page_token to get more groups<br>**Example value**: VIVWTpR1urY
user_id_type | string | No | User ID categories<br>**Example value**: open_id<br>**Optional values are**:<br>- open_id：Identifies a user to an app. The same user has different Open IDs in different apps. [How to get Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid)<br>- union_id：Identifies a user to a tenant that acts as a developer. A user has the same Union ID in apps developed by the same developer, and has different Union IDs in apps developed by different developers. A developer can use Union ID to link the same user's identities in multiple apps.[How to get Union ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id)<br>- user_id：Identifies a user to a tenant. The same user has different User IDs in different tenants. In one single tenant, a user has the same User ID in all apps （including store apps）. User ID is usually used to communicate user data between different apps. [How to get User ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**Default value**: `open_id`<br>**When the value is `user_id`, the following field scopes are required**:<br>Obtain user ID(contact:user.employee_id:readonly)

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
items | app.table.view\[\] | View information
view_id | string | View Id
view_name | string | View name
view_type | string | View type
view_public_level | string | View public class Public, Locked, Private<br>**Optional values are**:<br>- Public：Public view<br>- Locked：Lock view<br>- Private：Personal view
view_private_owner_id | string | The owner_id, id type and user_id_type parameters of the personal view are consistent
page_token | string | Page identifier, when has_more is true, a new page_token will also be returned. Otherwise, page_token will not be returned
has_more | boolean | Whether the response body has more parameters
total | int | Total

### Response body example
```json
{
	"code": 0,
	"msg": "success",
	"data": {
		"has_more": false,
		"items": [{
				"view_id": "vewqtI3f2u",
				"view_name": "Public grid",
				"view_public_level": "Public",
				"view_type": "grid"
			},
			{
				"view_id": "vew5Ys1Y1B",
				"view_name": "Private grid",
				"view_private_owner_id": "ou_fe4e2a0c10f41fb85620eb4b71d11182",
				"view_public_level": "Private",
				"view_type": "grid"
			}
		],
		"page_token": "vew5Ys1Y1B",
		"total": 2
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
200 | 1254016 | InvalidSort | invalid sort
200 | 1254018 | InvalidFilter | The filter parameter is incorrect. Please refer to [Record filter development guide](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/record-filter-guide) for information on how to fill in the filter parameter.
200 | 1254019 | InvalidViewType | Invalid view type
200 | 1254020 | ViewNameDuplicated | Duplicate view name
200 | 1254021 | EmptyViewName | View name is empty
200 | 1254022 | InvalidViewName | Invalid view name
200 | 1254030 | TooLargeResponse | TooLargeResponse
400 | 1254036 | Base is copying, please try again later. | Base copy replicating, try again later
200 | 1254040 | BaseTokenNotFound | AppToken not found
200 | 1254041 | TableIdNotFound | Table not found
200 | 1254042 | ViewIdNotFound | View not found
200 | 1254043 | RecordIdNotFound | RecordIdNotFound
200 | 1254044 | FieldIdNotFound | FieldIdNotFound
200 | 1254045 | FieldNameNotFound | Field name does not exist
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
403 | 1254302 | Permission denied. | No access rights, usually caused by the table opening of advanced permissions, please add a group containing applications in the advanced permissions settings and give this group read and write permissions
200 | 1255001 | InternalError | Internal error, have any questions can be consulting service
200 | 1255002 | RpcError | Internal error, have any questions can be consulting service
200 | 1255003 | MarshalError | Serialization failed, have any questions can be consulting service
200 | 1255004 | UmMarshalError | Deserialization failed, have any questions can be consulting service
200 | 1255005 | ConvError | Internal error, have any questions can be consulting service
504 | 1255040 | Request timed out, please try again later | Try again
400 | 1254607 | Data not ready, please try again later | There are usually two situations when this error occurs: 1. The last submitted modification has not been processed; 2. The data is too large and the server calculation times out; <br>This error code can be appropriately retried.

# Get view

This interface gets existing views based on view_id.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/tables/:table_id/views/:view_id
HTTP Method | GET
Rate Limit | [20 per second](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.**<br>Enable any scope from the list | View, comment, edit and manage Base(bitable:app)<br>View, comment, and export Base(bitable:app:readonly)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)

### Path parameters

Parameter | Type | Description
---|---|---
app_token | string | Base app token<br>**Example value**: "bascnCMII2ORej2RItqpZZUNMIe"<br>**Data validation rules**:<br>- Minimum length: `1` characters
table_id | string | Table ID<br>**Example value**: "tblsRc9GRRXKqhvW"
view_id | string | View ID<br>**Example value**: "vewTpR1urY"

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
view | app.table.view | View information
view_id | string | View Id
view_name | string | View name
view_type | string | View type
property | app.table.view.property | View properties
filter_info | app.table.view.property.filter_info | Filter conditions
conjunction | string | Relationship of Multiple Filter Criteria<br>**Optional values are**:<br>- and：And<br>- or：Or
conditions | app.table.view.property.filter_info.condition\[\] | Filter Criteria
field_id | string | Field unique ID for filtering
operator | string | Type of filter operation<br>**Optional values are**:<br>- is：Equal to<br>- isNot：Does not equal<br>- contains：Include<br>- doesNotContain：Not included<br>- isEmpty：Is empty<br>- isNotEmpty：Not empty<br>- isGreater：Greater than<br>- isGreaterEqual：Greater than or equal to<br>- isLess：Less than<br>- isLessEqual：Less than or equal to
value | string | Filter value
condition_id | string | Unique ID of filter condition
field_type | int | Field type for filtering <br>1: Multiline<br>2: Number<br>3: Single option<br>4: Multiple options<br>5: Date<br>7: Checkbox<br>11: Person<br>13: PhoneNumber<br>15: Link<br>17: Attachment<br>18: One-way link<br>19: LOOKUP<br>20: Formula<br>21: Two-way link<br>22: Location<br>23: GroupChat<br>1001: Date created<br>1002: Last modified date <br>1003: Created by<br>1004: Modified by<br>1005: AutoSerial
condition_omitted | boolean | Is the filter condition default?
hidden_fields | string\[\] | List of hidden field IDs
hierarchy_config | app.table.view.property.hierarchy_config | Table view hierarchy settings
field_id | string | Hierarchy's associated column id

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "view": {
            "view_id": "vewsOleexJ",
            "view_name": "grid",
            "view_type": "grid",
            "property": {
                "filter_info": {
                    "condition_omitted": null,
                    "conditions": [
                        {
                            "condition_id": "conuKMQNNg",
                            "field_id": "fldVioUai1",
                            "field_type": 1,
                            "operator": "is",
                            "value": "[\"text content\"]"
                        }
                    ],
                    "conjunction": "and"
                },
                "hidden_fields": null
            }
        }
    }
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
400 | 1254000 | WrongRequestJson | Request error
400 | 1254001 | WrongRequestBody | Request body error
400 | 1254002 | Fail | Internal error, have any questions can be consulting service
400 | 1254003 | WrongBaseToken | AppToken error
400 | 1254004 | WrongTableId | Table id wrong
400 | 1254005 | WrongViewId | View id wrong
400 | 1254006 | WrongRecordId | Record id wrong
400 | 1254007 | EmptyValue | Empty value
400 | 1254008 | EmptyView | Empty view
400 | 1254009 | WrongFieldId | Wrong fieldId
400 | 1254010 | ReqConvError | Request error
400 | 1254016 | InvalidSort | invalid sort
400 | 1254018 | InvalidFilter | The filter parameter is incorrect. Please refer to [Record filter development guide](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/record-filter-guide) for information on how to fill in the filter parameter.
400 | 1254019 | InvalidViewType | Invalid view type
400 | 1254020 | ViewNameDuplicated | Duplicate view name
400 | 1254021 | EmptyViewName | View name is empty
400 | 1254022 | InvalidViewName | Invalid view name
400 | 1254030 | TooLargeResponse | TooLargeResponse
400 | 1254032 | The role name is invalid, please modify it. | Invalid role name
400 | 1254033 | The role name is duplicated, please modify it. | Role name duplicated
400 | 1254036 | Base is copying, please try again later. | Base copy replicating, try again later
404 | 1254040 | BaseTokenNotFound | AppToken not found
404 | 1254041 | TableIdNotFound | Table not found
404 | 1254042 | ViewIdNotFound | View not found
404 | 1254043 | RecordIdNotFound | RecordIdNotFound
404 | 1254044 | FieldIdNotFound | FieldIdNotFound
404 | 1254045 | FieldNameNotFound | Field name does not exist
404 | 1254047 | Role id is not found. | Role not found
400 | 1254048 | MemberNotFound | Member not found
404 | 1254049 | Form field is not found. | Form field id does not exist
400 | 1254060 | TextFieldConvFail | TextFieldConvFail
400 | 1254061 | NumberFieldConvFail | NumberFieldConvFail
400 | 1254062 | SingleSelectFieldConvFail | SingleSelectFieldConvFail
400 | 1254063 | MultiSelectFieldConvFail | MultiSelectFieldConvFail
400 | 1254064 | DatetimeFieldConvFail | DatetimeFieldConvFail
400 | 1254065 | CheckboxFieldConvFail | CheckboxFieldConvFail
400 | 1254066 | UserFieldConvFail | The value corresponding to the personnel field type is incorrect. The possible reasons are:<br>- The ID type specified by the user_id_type parameter does not match the type of the provided ID.<br>- An unrecognized type or structure was provided. Currently, only `id` is supported, and it must be passed as an array.<br>- An `open_id` was passed across applications. If you are passing an ID across applications, it is recommended to use `user_id`. The `open_id` obtained from different applications cannot be used interchangeably.
400 | 1254067 | LinkFieldConvFail | LinkFieldConvFail
400 | 1254100 | TableExceedLimit | TableExceedLimit, limited to 300
400 | 1254101 | ViewExceedLimit | ViewExceedLimit, limited to 200
400 | 1254103 | RecordExceedLimit | RecordExceedLimit, limited to 20,000
400 | 1254104 | RecordAddOnceExceedLimit | RecordAddOnceExceedLimit, limited to 500
400 | 1254110 | Role exceeds limit | Role exceed limit, limited to 30
400 | 1254130 | TooLargeCell | TooLargeCell
429 | 1254290 | TooManyRequest | Request too fast, try again later
400 | 1254291 | Write conflict | The same data table does not support concurrent calls to the write interface, please check whether there is a concurrent call to the write interface. The writing interface includes: adding, modifying, and deleting records; adding, modifying, and deleting fields; modifying forms; modifying views, etc.
400 | 1254301 | OperationTypeError | Base does not have advanced permissions enabled or does not support enabling advanced permissions
403 | 1254302 | Permission denied. | No access rights, usually caused by the table opening of advanced permissions, please add a group containing applications in the advanced permissions settings and give this group read and write permissions
500 | 1255001 | InternalError | Internal error, have any questions can be consulting service
500 | 1255002 | RpcError | Internal error, have any questions can be consulting service
500 | 1255003 | MarshalError | Serialization failed, have any questions can be consulting service
500 | 1255004 | UmMarshalError | Deserialization failed, have any questions can be consulting service
500 | 1255005 | ConvError | Internal error, have any questions can be consulting service
504 | 1255040 | Request timed out, please try again later | Try again
400 | 1254607 | Data not ready, please try again later. | There are usually two situations when this error occurs: 1. The last submitted modification has not been processed; 2. The data is too large and the server calculation times out; <br>This error code can be appropriately retried.

# Delete view

Delete views from data tables

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/tables/:table_id/views/:view_id
HTTP Method | DELETE
Rate Limit | [10 per second](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.** | View, comment, edit and manage Base(bitable:app)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)

The instructions for AccessToken calling Docs API are detailed here [Docs API Overview](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN)

### Path parameters

Parameter | Type | Description
---|---|---
app_token | string | Base app token<br>**Example value**: "AppbcbWCzen6D8dezhoCH2RpMAh"
table_id | string | Table id<br>**Example value**: "TblsRc9GRRXKqhvW"
view_id | string | View Id<br>**Example value**: "VIVWTpR1urY"

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
200 | 1254016 | InvalidSort | invalid sort
200 | 1254018 | InvalidFilter | The filter parameter is incorrect. Please refer to [Record filter development guide](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/record-filter-guide) for information on how to fill in the filter parameter.
200 | 1254019 | InvalidViewType | Invalid view type
200 | 1254020 | ViewNameDuplicated | Duplicate view name
200 | 1254021 | EmptyViewName | View name is empty
200 | 1254022 | InvalidViewName | Invalid view name
200 | 1254023 | LastViewDeleteForbidden | LastViewDeleteForbidden
200 | 1254030 | TooLargeResponse | TooLargeResponse
400 | 1254036 | Base is copying, please try again later. | Base copy replicating, try again later
200 | 1254040 | BaseTokenNotFound | AppToken not found
200 | 1254041 | TableIdNotFound | Table not found
200 | 1254042 | ViewIdNotFound | View not found
200 | 1254043 | RecordIdNotFound | RecordIdNotFound
200 | 1254044 | FieldIdNotFound | FieldIdNotFound
200 | 1254045 | FieldNameNotFound | Field name does not exist
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
403 | 1254302 | RolePermNotAllow | The role has no permissions.
403 | 1254304 | PermNotAllow | The role has no permissions.
200 | 1255001 | InternalError | Internal error, have any questions can be consulting service
200 | 1255002 | RpcError | Internal error, have any questions can be consulting service
200 | 1255003 | MarshalError | Serialization failed, have any questions can be consulting service
200 | 1255004 | UmMarshalError | Deserialization failed, have any questions can be consulting service
200 | 1255005 | ConvError | Internal error, have any questions can be consulting service
504 | 1255040 | Request timed out, please try again later | Try again
400 | 1254607 | Data not ready, please try again later | There are usually two situations when this error occurs: 1. The last submitted modification has not been processed; 2. The data is too large and the server calculation times out; <br>This error code can be appropriately retried.
403 | 1254608 | ReqRecommited | Same API requests are submitted repeatedly.
