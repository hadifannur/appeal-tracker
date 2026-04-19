# List dashboards

According to app_token, get all dashboards under app

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/dashboards
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
app_token | string | base app token<br>**Example value**: "bascng7vrxcxpig7geggXiCtadY"

### Query parameters

Parameter | Type | Required | Description
---|---|---|---
page_size | int | No | **Example value**: 10<br>**Data validation rules**:<br>- Maximum value: `500`
page_token | string | No | Page identifier. It is not filled in the first request, indicating traversal from the beginning; when there will be more groups, the new page_token will be returned at the same time, and the next traversal can use the page_token to get more groups<br>**Example value**: blknkqrP3RqUkcAW

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
dashboards | app.dashboard\[\] | Dashboard information
block_id | string | Dashboard id
name | string | Dashboard name
page_token | string | Page identifier, when has_more is true, a new page_token will also be returned. Otherwise, page_token will not be returned
has_more | boolean | Whether the response body has more parameters

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "dashboards": [
            {
                "block_id": "blknkqrP3RqUkcAW",
                "name": "dashboard1"
            }
        ],
        "page_token": "blknkqrP3RqUkcAW",
        "has_more": false
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
400 | 1254032 | InvalidRoleName | Invalid role name
400 | 1254033 | RoleNameDuplicated | Role name duplicated
404 | 1254040 | BaseTokenNotFound | AppToken not found
404 | 1254041 | TableIdNotFound | Table not found
404 | 1254042 | ViewIdNotFound | View not found
404 | 1254043 | RecordIdNotFound | RecordIdNotFound
404 | 1254044 | FieldIdNotFound | FieldIdNotFound
404 | 1254045 | FieldNameNotFound | Field name does not exist
404 | 1254047 | RoleIdNotFound | Role not found
400 | 1254048 | MemberNotFound | Member not found
404 | 1254049 | FormFieldNotFound | Form field id does not exist
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
400 | 1254110 | RoleExceedLimit | Role exceed limit, limited to 30
400 | 1254130 | TooLargeCell | TooLargeCell
429 | 1254290 | TooManyRequest | Request too fast, try again later
400 | 1254291 | Write conflict | The same data table does not support concurrent calls to the write interface, please check whether there is a concurrent call to the write interface. The writing interface includes: adding, modifying, and deleting records; adding, modifying, and deleting fields; modifying forms; modifying views, etc.
400 | 1254301 | OperationTypeError | Base does not have advanced permissions enabled or does not support enabling advanced permissions
403 | 1254302 | Permission denied. | No access rights, usually caused by the table opening of advanced permissions, please add a group containing applications in the advanced permissions settings and give this group read and write permissions
400 | 1255001 | InternalError | Internal error, have any questions can be consulting service
400 | 1255002 | RpcError | Internal error, have any questions can be consulting service
400 | 1255003 | MarshalError | Serialization failed, have any questions can be consulting service
400 | 1255004 | UmMarshalError | Deserialization failed, have any questions can be consulting service
400 | 1255005 | ConvError | Internal error, have any questions can be consulting service
504 | 1255040 | Request timed out, please try again later | Try again
400 | 1254036 | Base is copying, please try again later. | Base copy replicating, try again later
500 | 1254200 | Something went wrong. Please contact technical support at https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952 | internal error
400 | 1254011 | The page_size must be between 0 and 100. | invalid page_size

# Patch form

Update a form

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/tables/:table_id/forms/:form_id
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
app_token | string | Base unique device identifier [app_token description](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification#8121eebe)<br>**Example value**: "bascnv1jIEppJdTCn3jOosabcef"
table_id | string | table id<br>**Example value**: "tblz8nadEUdxNMt5"
form_id | string | form id<br>**Example value**: "vew6oMbAa4"

### Request body

Parameter | Type | Required | Description
---|---|---|---
name | string | No | Form name<br>**Example value**: "Form"
description | string | No | Form description<br>**Example value**: "Form description"
shared | boolean | No | Whether to enable sharing<br>**Example value**: True
shared_limit | string | No | Share scope restrictions<br>**Example value**: "tenant_editable"<br>**Optional values are**:<br>- off：Only invited people can fill in<br>- tenant_editable：People who get the link within the organization can fill in<br>- anyone_editable：People who get the link on the Internet can fill in
submit_limit_once | boolean | No | Fill in the number of times limit once<br>**Example value**: True

### Request body example
```json
{"name":"Form",
"description":"Form description",
"shared":True,
"shared_limit":"tenant_editable",
"submit_limit_once":True}
```

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
form | app.table.form | Form description
name | string | Form name
description | string | Form description
shared | boolean | Whether to enable sharing
shared_url | string | Share URL
shared_limit | string | Share scope restrictions<br>**Optional values are**:<br>- off：Only invited people can fill in<br>- tenant_editable：People who get the link within the organization can fill in<br>- anyone_editable：People who get the link on the Internet can fill in
submit_limit_once | boolean | Fill in the number of times limit once

### Response body example
```json
{"code":0,
"msg":"success",
"data":{"form":{"name":"Form",
"description":"Form description",
"shared":True,
"shared_url":"https://example.feishu.cn/share/base/shrcnCy1KAlpahNotmhRn1abcde (The update API does not support this parameter)",
"shared_limit":"tenant_editable",
"submit_limit_once":True}}}
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
400 | 1254018 | InvalidFilter | invalid filter
400 | 1254019 | InvalidViewType | Invalid view type
400 | 1254020 | ViewNameDuplicated | Duplicate view name
400 | 1254021 | EmptyViewName | View name is empty
400 | 1254022 | InvalidViewName | Invalid view name
400 | 1254030 | TooLargeResponse | TooLargeResponse
404 | 1254040 | BaseTokenNotFound | AppToken not found
404 | 1254041 | TableIdNotFound | Table not found
404 | 1254042 | ViewIdNotFound | View not found
404 | 1254043 | RecordIdNotFound | RecordIdNotFound
404 | 1254044 | FieldIdNotFound | FieldIdNotFound
404 | 1254045 | FieldNameNotFound | Field name does not exist
404 | 1254049 | FormFieldNotFound | Form field id does not exist
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
400 | 1254130 | TooLargeCell | TooLargeCell
429 | 1254290 | TooManyRequest | Request too fast, try again later
400 | 1254291 | Write conflict | The same data table does not support concurrent calls to the write interface, please check whether there is a concurrent call to the write interface. The writing interface includes: adding, modifying, and deleting records; adding, modifying, and deleting fields; modifying forms; modifying views, etc.
400 | 1254301 | OperationTypeError | Base does not have advanced permissions enabled or does not support enabling advanced permissions
403 | 1254302 | Permission denied. | No access rights, usually caused by the table opening of advanced permissions, please add a group containing applications in the advanced permissions settings and give this group read and write permissions
400 | 1255001 | InternalError | Internal error, have any questions can be consulting service
400 | 1255002 | RpcError | Internal error, have any questions can be consulting service
400 | 1255003 | MarshalError | Serialization failed, have any questions can be consulting service
400 | 1255004 | UmMarshalError | Deserialization failed, have any questions can be consulting service
400 | 1255005 | ConvError | Internal error, have any questions can be consulting service
504 | 1255040 | Request timed out, please try again later | Try again
400 | 1254036 | Base is copying, please try again later. | Base copy replicating, try again later
500 | 1254200 | InternalError | Something went wrong. Please contact technical support at https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952
403 | 1254608 | Same API requests are submitted repeatedly. | Same API requests are submitted repeatedly.
403 | 1254305 | PermControl | Requests may be restricted by permissions such as tenant switches, wiki space, etc.
400 | 1254607 | Data not ready, please try again later | There are usually two situations when this error occurs: <br>1. The last submitted modification has not been processed; <br>2. The data is too large and the server calculation times out; This error code can be appropriately retried.
403 | 1254304 | You are not authorized to perform this operation. | Advanced permissions for specific rows or columns are only available for Business and Enterprise editions

# List form

Give form according to app_token, table_id and form_id

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/tables/:table_id/forms/:form_id
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
app_token | string | base app token<br>**Example value**: "bascnv1jIEppJdTCn3jOosabcef"
table_id | string | table id<br>**Example value**: "tblz8nadEUdxNMt5"
form_id | string | form id<br>**Example value**: "vew6oMbAa4"

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
form | app.table.form | Form information
name | string | Form name
description | string | Form description
shared | boolean | Whether to enable sharing
shared_url | string | Share URL
shared_limit | string | Share scope restrictions<br>**Optional values are**:<br>- off：Only invited people can fill in<br>- tenant_editable：People who get the link within the organization can fill in<br>- anyone_editable：People who get the link on the Internet can fill in
submit_limit_once | boolean | Fill in the number of times limit once

### Response body example
```json
{"code":0,
"msg":"success",
"data":{"form":{"name":"Form",
"description":"Form description",
"shared":True,
"shared_url":"https://example.feishu.cn/share/base/shrcnCy1KAlpahNotmhRn1abcde (The update API does not support this parameter)",
"shared_limit":"tenant_editable",
"submit_limit_once":True}}}
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
400 | 1254032 | InvalidRoleName | Invalid role name
400 | 1254033 | RoleNameDuplicated | Role name duplicated
404 | 1254040 | BaseTokenNotFound | AppToken not found
404 | 1254041 | TableIdNotFound | Table not found
404 | 1254042 | ViewIdNotFound | View not found
404 | 1254043 | RecordIdNotFound | RecordIdNotFound
404 | 1254044 | FieldIdNotFound | FieldIdNotFound
404 | 1254045 | FieldNameNotFound | Field name does not exist
404 | 1254047 | RoleIdNotFound | Role not found
400 | 1254048 | MemberNotFound | Member not found
404 | 1254049 | FormFieldNotFound | Form field id does not exist
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
400 | 1254110 | RoleExceedLimit | Role exceed limit, limited to 30
400 | 1254130 | TooLargeCell | TooLargeCell
429 | 1254290 | TooManyRequest | Request too fast, try again later
400 | 1254291 | Write conflict | The same data table does not support concurrent calls to the write interface, please check whether there is a concurrent call to the write interface. The writing interface includes: adding, modifying, and deleting records; adding, modifying, and deleting fields; modifying forms; modifying views, etc.
400 | 1254301 | OperationTypeError | Base does not have advanced permissions enabled or does not support enabling advanced permissions
403 | 1254302 | Permission denied. | No access rights, usually caused by the table opening of advanced permissions, please add a group containing applications in the advanced permissions settings and give this group read and write permissions
400 | 1255001 | InternalError | Internal error, have any questions can be consulting service
400 | 1255002 | RpcError | Internal error, have any questions can be consulting service
400 | 1255003 | MarshalError | Serialization failed, have any questions can be consulting service
400 | 1255004 | UmMarshalError | Deserialization failed, have any questions can be consulting service
400 | 1255005 | ConvError | Internal error, have any questions can be consulting service
504 | 1255040 | Request timed out, please try again later | Try again
400 | 1254036 | Base is copying, please try again later. | Base copy replicating, try again later
500 | 1254200 | InternalError | Something went wrong. Please contact technical support at https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952
403 | 1254304 | You are not authorized to perform this operation. | Advanced permissions for specific rows or columns are only available for Business and Enterprise editions

# Patch form field

Update a form field

**Notice**：A form view is a Bitable view type. Each form has a unique identifier form_id, the view_id of the current view.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/tables/:table_id/forms/:form_id/fields/:field_id
HTTP Method | PATCH
Rate Limit | [10 per second](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.**<br>Enable any scope from the list | 更新表单数据(base:form:update)<br>View, comment, edit and manage Base(bitable:app)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Path parameters

Parameter | Type | Description
---|---|---
app_token | string | Base unique device identifier [app_token description](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification#8121eebe)<br>**Example value**: "bascnCMII2ORej2RItqpZZUNMIe"
table_id | string | table id<br>**Example value**: "tblsRc9GRRXKqhvW"
form_id | string | form id<br>**Example value**: "vewTpR1urY"
field_id | string | field id<br>**Example value**: "fldjX7dUj5"

### Request body

Parameter | Type | Required | Description
---|---|---|---
pre_field_id | string | No | The previous form field ID is used to support adjusting the order of form fields, and the position is determined by the field_id of the previous form field; if the pre_field_id is an empty string, it means that it should be ranked first<br>**Example value**: "fldjX7dUj5"
title | string | No | Form field title<br>**Example value**: "Multiline text"
description | string | No | Form field description<br>**Example value**: "Multiline text description"
required | boolean | No | Required<br>**Example value**: true
visible | boolean | No | Visible<br>**Example value**: true, when the value is false , other fields are not allowed to be updated.
rich_description | app_rich_description_segment\[\] | No | Rich Text Description<br>**Data validation rules**:<br>- Length range: `1` ～ `500`
segment_type | string | Yes | element type<br>**Example value**: "text"<br>**Optional values are**:<br>- text：plain text<br>- url：link<br>**Data validation rules**:<br>- Length range: `1` ～ `100` characters
text | string | Yes | Text value<br>**Example value**: "这是一个开放性问题"<br>**Data validation rules**:<br>- Length range: `1` ～ `1000` characters
link | string | No | link<br>**Example value**: "https://open.larkoffice.com/"<br>**Data validation rules**:<br>- Length range: `1` ～ `1000` characters

### Request body example
```json
{"pre_field_id":"fldjX7dUj5",
"title":"Multiline text",
"description":"Multiline text description",
"required":true,
"visible":true, when the value is false , other fields are not allowed to be updated.,
"rich_description":[{
    "segment_type": "text",
    "text": "这是一个开放性问题",
    "link": "https://open.larkoffice.com/"
}]}
```

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
fields | app_table_form_patched_field | Updated field value
pre_field_id | string | Previous form question ID
title | string | form problem
description | string | Problem description
required | boolean | Is it required?
visible | boolean | Is it visible?
rich_description | app_rich_description_segment\[\] | Rich Text Description
segment_type | string | element type<br>**Optional values are**:<br>- text：plain text<br>- url：link
text | string | Text value
link | string | link

### Response body example
```json
{"code":0,
"msg":"success",
"data":{"fields":{"pre_field_id":"FLD1241A13B",
"title":"Please choose your preferred option",
"description":"This is an open question",
"required":True,
"visible":True,
"rich_description":[{
    "segment_type": "text",
    "text": "这是一个开放性问题",
    "link": "https://open.larkoffice.com/"
}]}}}
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
400 | 1254012 | NotSupportFieldOrView | The field type is not supported.
400 | 1254016 | InvalidSort | invalid sort
400 | 1254018 | InvalidFilter | The filter parameter is incorrect. Please refer to [Record filter development guide](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/record-filter-guide) for information on how to fill in the filter parameter.
400 | 1254019 | InvalidViewType | Invalid view type
400 | 1254020 | ViewNameDuplicated | Duplicate view name
400 | 1254021 | EmptyViewName | View name is empty
400 | 1254022 | InvalidViewName | Invalid view name
400 | 1254030 | TooLargeResponse | TooLargeResponse
400 | 1254036 | Base is copying, please try again later. | Base copy replicating, try again later
404 | 1254040 | BaseTokenNotFound | AppToken not found
404 | 1254041 | TableIdNotFound | Table not found
404 | 1254042 | ViewIdNotFound | View not found
404 | 1254043 | RecordIdNotFound | RecordIdNotFound
404 | 1254044 | FieldIdNotFound | FieldIdNotFound
404 | 1254045 | FieldNameNotFound | Field name does not exist
404 | 1254049 | FormFieldNotFound | Form field id does not exist
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
400 | 1254102 | FileExceedLimit | FileExceedLimit
400 | 1254103 | RecordExceedLimit | RecordExceedLimit, limited to 20,000
400 | 1254104 | RecordAddOnceExceedLimit | RecordAddOnceExceedLimit, limited to 500
400 | 1254130 | TooLargeCell | TooLargeCell
429 | 1254290 | TooManyRequest | Request too fast, try again later
400 | 1254291 | Write conflict | The same data table does not support concurrent calls to the write interface, please check whether there is a concurrent call to the write interface. The writing interface includes: adding, modifying, and deleting records; adding, modifying, and deleting fields; modifying forms; modifying views, etc.
400 | 1254301 | OperationTypeError | Base does not have advanced permissions enabled or does not support enabling advanced permissions
403 | 1254302 | Permission denied. | No access rights, usually caused by the table opening of advanced permissions, please add a group containing applications in the advanced permissions settings and give this group read and write permissions
400 | 1255001 | InternalError | Internal error, have any questions can be consulting service
400 | 1255002 | RpcError | Internal error, have any questions can be consulting service
400 | 1255003 | MarshalError | Serialization failed, have any questions can be consulting service
400 | 1255004 | UmMarshalError | Deserialization failed, have any questions can be consulting service
400 | 1255005 | ConvError | Internal error, have any questions can be consulting service
504 | 1255040 | Request timed out, please try again later | Try again

# List form fields

Give all form fields according to app_token, table_id and form_id

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/tables/:table_id/forms/:form_id/fields
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
app_token | string | Base unique device identifier [app_token description](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification#8121eebe)<br>**Example value**: "appbcbWCzen6D8dezhoCH2RpMAh"
table_id | string | table id<br>**Example value**: "tblsRc9GRRXKqhvW"
form_id | string | form id<br>**Example value**: "vewTpR1urY"

### Query parameters

Parameter | Type | Required | Description
---|---|---|---
page_size | int | No | **Example value**: 10<br>**Data validation rules**:<br>- Maximum value: `100`
page_token | string | No | Page identifier. It is not filled in the first request, indicating traversal from the beginning; when there will be more groups, the new page_token will be returned at the same time, and the next traversal can use the page_token to get more groups<br>**Example value**: vewTpR1urY

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
items | app.table.form.field\[\] | Form field information
field_id | string | Form field id
title | string | Form field title
description | string | Form field description
required | boolean | Required
visible | boolean | Visible
page_token | string | Page identifier, when has_more is true, a new page_token will also be returned. Otherwise, page_token will not be returned
has_more | boolean | Whether the response body has more parameters
total | int | Total

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "items": [
            {
                "field_id": "fldjX7dUj5",
                "title": "Multiline text",
                "description": "Multiline text description",
                "required": true,
                "visible": true
            }
        ],
        "page_token": "fld1lAbHh7",
        "has_more": true,
        "total": 1
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
400 | 1254036 | Base is copying, please try again later. | Base copy replicating, try again later
404 | 1254040 | BaseTokenNotFound | AppToken not found
404 | 1254041 | TableIdNotFound | Table not found
404 | 1254042 | ViewIdNotFound | View not found
404 | 1254043 | RecordIdNotFound | RecordIdNotFound
404 | 1254044 | FieldIdNotFound | FieldIdNotFound
404 | 1254045 | FieldNameNotFound | Field name does not exist
404 | 1254049 | FormFieldNotFound | Form field id does not exist
400 | 1254060 | TextFieldConvFail | TextFieldConvFail
400 | 1254061 | NumberFieldConvFail | NumberFieldConvFail
400 | 1254062 | SingleSelectFieldConvFail | SingleSelectFieldConvFail
400 | 1254063 | MultiSelectFieldConvFail | MultiSelectFieldConvFail
400 | 1254064 | DatetimeFieldConvFail | DatetimeFieldConvFail
400 | 1254065 | CheckboxFieldConvFail | CheckboxFieldConvFail
200 | 1254066 | UserFieldConvFail | The value corresponding to the personnel field type is incorrect. The possible reasons are:<br>- The ID type specified by the user_id_type parameter does not match the type of the provided ID.<br>- An unrecognized type or structure was provided. Currently, only `id` is supported, and it must be passed as an array.<br>- An `open_id` was passed across applications. If you are passing an ID across applications, it is recommended to use `user_id`. The `open_id` obtained from different applications cannot be used interchangeably.
400 | 1254067 | LinkFieldConvFail | LinkFieldConvFail
400 | 1254100 | TableExceedLimit | TableExceedLimit, limited to 300
400 | 1254101 | ViewExceedLimit | ViewExceedLimit, limited to 200
400 | 1254102 | FileExceedLimit | FileExceedLimit
400 | 1254103 | RecordExceedLimit | RecordExceedLimit, limited to 20,000
400 | 1254104 | RecordAddOnceExceedLimit | RecordAddOnceExceedLimit, limited to 500
400 | 1254130 | TooLargeCell | TooLargeCell
400 | 1254200 | InternalError | Something went wrong. Please contact technical support at https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952
429 | 1254290 | TooManyRequest | Request too fast, try again later
400 | 1254291 | Write conflict | The same data table does not support concurrent calls to the write interface, please check whether there is a concurrent call to the write interface. The writing interface includes: adding, modifying, and deleting records; adding, modifying, and deleting fields; modifying forms; modifying views, etc.
400 | 1254301 | OperationTypeError | Base does not have advanced permissions enabled or does not support enabling advanced permissions
403 | 1254302 | Permission denied. | No access rights, usually caused by the table opening of advanced permissions, please add a group containing applications in the advanced permissions settings and give this group read and write permissions
400 | 1255001 | InternalError | Internal error, have any questions can be consulting service
400 | 1255002 | RpcError | Internal error, have any questions can be consulting service
400 | 1255003 | MarshalError | Serialization failed, have any questions can be consulting service
400 | 1255004 | UmMarshalError | Deserialization failed, have any questions can be consulting service
400 | 1255005 | ConvError | Internal error, have any questions can be consulting service
504 | 1255040 | Request timed out, please try again later | Try again

