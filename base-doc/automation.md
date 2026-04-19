# List automations

This interface is used to list the automations of base

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/workflows
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
app_token | string | Base app token<br>**Example value**: "appbcbWCzen6D8dezhoCH2RpMAh"

### Query parameters

Parameter | Type | Required | Description
---|---|---|---
page_token | string | No | Page identifier. It is not filled in the first request, indicating traversal from the beginning; when there will be more groups, the new page_token will be returned at the same time, and the next traversal can use the page_token to get more groups<br>**Example value**: eVQrYzJBNDNONlk4VFZBZVlSdzlKdFJ4bVVHVExENDNKVHoxaVdiVnViQT0=
page_size | int | No | paging size<br>**Example value**: 10<br>**Default value**: `20`

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
workflows | app.workflow\[\] | Automation information
workflow_id | string | Automation id
status | string | the status of automation
title | string | the name of automation

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "workflows": [
            {
                "workflow_id": "72934597xxxx9998484",
                "status": "Enable",
                "title": "automation"
            }
        ]
    }
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
400 | 1254000 | WrongRequestJson | request body error
400 | 1254001 | WrongRequestBody | request body error
400 | 1254002 | Fail | Internal error, if you have any questions, please consult customer service.
400 | 1254003 | WrongBaseToken | app_token mistake
400 | 1254004 | WrongTableId | table_id mistake
400 | 1254010 | ReqConvError | request error
404 | 1254040 | BaseTokenNotFound | app_token doesn't exist
404 | 1254041 | TableIdNotFound | table_id doesn't exist
429 | 1254290 | TooManyRequest | Request is too fast, try again later
400 | 1254301 | OperationTypeError | Bitable does not enable advanced permissions or does not support enabling advanced permissions
400 | 1255001 | InternalError | Internal error, please contact [Technical Support] (https://applink.feishu.cn/TLJpeNdW)
400 | 1255002 | RpcError | Internal error, please contact [Technical Support] (https://applink.feishu.cn/TLJpeNdW)
400 | 1255003 | MarshalError | Serialization error, please contact [Technical Support] (https://applink.feishu.cn/TLJpeNdW) Deserialization error
400 | 1255004 | UmMarshalError | deserialization error
400 | 1255005 | ConvError | Internal error, please contact [Technical Support] (https://applink.feishu.cn/TLJpeNdW)
504 | 1255040 | Request timed out, please try again later | request timed out
400 | 1254036 | Bitable is copying, please try again later. | Copy Bitable is an asynchronous operation. This error code indicates that the current Bitable is still being copied, and the current Bitable cannot be operated during the copy. You need to wait for the copy to complete before operating.
500 | 1254200 | Something went wrong. Please contact technical support at https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952 | Internal error, please contact [Technical Support] (https://applink.feishu.cn/TLJpeNdW)

# Update Workflow status

This interface can be used to update Workflow status 

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/workflows/:workflow_id
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
app_token | string | Bitable app token<br>**Example value**: "appbcbWCzen6D8dezh"
workflow_id | string | workflow_id<br>**Example value**: "730887xxxx552638996"

### Request body

Parameter | Type | Required | Description
---|---|---|---
status | string | Yes | automated state<br>**Example value**: "Enable"

### Request body example
```json
{
    "status": "Enable"
}
```

The status of the target automation, currently only "Enable" and "Disable" are available

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
200 | 1254000 | WrongRequestJson | request body error
200 | 1254001 | WrongRequestBody | request body error
200 | 1254002 | Fail | Internal error, please contact technical support
200 | 1254003 | WrongBaseToken | app_token mistake
200 | 1254010 | ReqConvError | request error
400 | 1254036 | Bitable is copying, please try again later. | Bitable copy replicating, try again later
200 | 1254040 | BaseTokenNotFound | app_token doesn't exist
200 | 1254290 | TooManyRequest | Request is too fast, try again later
403 | 1254302 | Permission denied. | No access rights, usually caused by the table opening of advanced permissions, please add a group containing applications in the advanced permissions settings and give this group read and write permissions
200 | 1255001 | InternalError | Internal error, please contact technical support
200 | 1255002 | RpcError | Internal error, please contact technical support
200 | 1255003 | MarshalError | Serialization error, please contact technical support
200 | 1255004 | UmMarshalError | deserialization error
504 | 1255040 | Request timed out, please try again later | Try again.
