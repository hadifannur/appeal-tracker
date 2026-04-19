# Create a spreadsheet

Use this API to create an online spreadsheet under the specified directory. The table title can be customized. Creating forms with content is not supported.

**Notice**：To create a spreadsheet based on a template, first obtain the `spreadsheet_token` of the template as the file token, then call the [Copy File](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file/copy) interface to create the spreadsheet.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets
HTTP Method | POST
Rate Limit | [20 per minute](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space(drive:drive)<br>View, comment, edit, and manage Sheets(sheets:spreadsheet)<br>Create spreadsheet(sheets:spreadsheet:create)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Request body

Parameter | Type | Required | Description
---|---|---|---
title | string | No | Spreadsheet title<br>**Example value**: "Sales sheet"<br>**Data validation rules**:<br>- Length range: `0` ～ `255` characters
folder_token | string | No | Folder token. You can get the folder token in two ways:<br>- URL of the folder: https://sample.feishu.cn/drive/folder/==fldbcO1UuPz8VwnpPx5a92abcef==<br>- Call the open platform interface to get it:<br>- Call the [get my space (root folder) metadata](https://open.larkoffice.com/document/ukTMukTMukTM/ugTNzUjL4UzM14CO1MTN/get-root-folder-meta) interface to get the root directory (i.e. root folder) token.<br>- Continue to call the [get list of files in folder](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file/list) interface to get the token for the folder in the root directory.<br>**Note**: To create a spreadsheet in the knowledge base, you need to call the [Create knowledge space node](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/wiki-v2/space-node/create) API and select the table (sheet) type.<br>**Example value**: "fldbcO1UuPz8VwnpPx5a92abcef"

### Request body example
```json
{
    "title": "Sales sheet",
    "folder_token": "fldbcO1UuPz8VwnpPx5a92abcef"
}
```

### cURL example

```bash
curl --location --request POST 'https://open.feishu.cn/open-apis/sheets/v3/spreadsheets' \
--header 'Authorization: Bearer u-3iqkd6KWzRLzNdXfeuCMEb' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title":"sales sheet",
    "folder_token":"fldbcO1UuPz8VwnpPx5a92abcef"
}'
```

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
spreadsheet | spreadsheet | Spreadsheet's information
title | string | Spreadsheet title
folder_token | string | Folter token, see [Overview](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/files/guide/introduction) to learn how to obtain it.
url | string | Document URL
spreadsheet_token | string | Spreadsheet token

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "spreadsheet": {
            "title": "Sales sheet",
            "folder_token": "fldbcO1UuPz8VwnpPx5a92abcef",
            "url": "https://example.feishu.cn/sheets/Iow7sNNEphp3WbtnbCscPqabcef",
            "spreadsheet_token": "Iow7sNNEphp3WbtnbCscPqabcef"
        }
    }
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
400 | 1310204 | Wrong Request Body | Check the request body parameter.
400 | 1310213 | Permission Fail | Confirm whether the current access identity has permission to read or edit spreadsheets. Please refer to the following methods to resolve this:<br>- If you are using a `tenant_access_token`, it means the current application does not have permission to read or edit spreadsheets. You need to add document permissions for the application through the cloud document webpage by navigating to the top right corner **"..."** -> **"... More"** -> **"Add applications"**.<br>**Note**: Before adding a document application, you need to ensure that the target application has at least one cloud document [API permission](https://open.larkoffice.com/document/ukTMukTMukTM/uYTM5UjL2ETO14iNxkTN/scope-list) enabled. Otherwise, you will not be able to search for the target application in the document application window.<br>![](//sf3-cn.feishucdn.com/obj/open-platform-opendoc/bb60f97ebb402475f2af1d3131d4914f_sLOzoqYRXX.png?height=1992&maxWidth=550&width=3278)<br>- If you are using a `user_access_token`, it means the current user does not have permission to read or edit spreadsheets. You need to add document permissions for the current user through the **Share** entry in the top right corner of the cloud document webpage.<br>![image.png](//sf3-cn.feishucdn.com/obj/open-platform-opendoc/caceea2ac91c170555194d7a8dc2a317_GfTRc9xLAt.png&maxWidth=550)<br>For more details on the specific steps or other methods to add permissions, refer to [Cloud Document FAQ 3](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#16c6475a).
400 | 1310235 | Retry Later | Please try again later.
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
400 | 1310226 | Excess Limit | Exceeds the limit

# Modify spreadsheet properties

This interface is used to modify the properties of the spreadsheet. Currently, modifying spreadsheet titles is supported.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token
HTTP Method | PATCH
Rate Limit | [20 per minute](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space(drive:drive)<br>View, comment, edit, and manage Sheets(sheets:spreadsheet)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Path parameters

Parameter | Type | Description
---|---|---
spreadsheet_token | string | Table token. Refer to the [Spreadsheet Overview](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview) to obtain the token.<br>**Example value**: "Iow7sNNEphp3WbtnbCscPqabcef"

### Request body

Parameter | Type | Required | Description
---|---|---|---
title | string | No | Table title. When the parameter is empty, the title will be "Untitled spreadsheet" or content corresponding to the local language environment<br>**Example value**: "Sales sheet"

### Request body example
```json
{
    "title": "Sales sheet"
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
400 | 1310251 | Invalid Parameters | Reference error message in response body
400 | 1310213 | Permission Fail | No permission
400 | 1310249 | Spreadsheet Deleted | Restore the form and try again
400 | 1310250 | Title Not Passed | Title violation, use another title
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
500 | 1315210 | Server Error | Internal service errors, please consult customer service for details

# Get spreadsheet information

This interface is used to obtain basic information for the spreadsheet, including the owner of the spreadsheet, URL links, and other related details.

## Prerequisite

Before calling this API, ensure that the current identity (either `tenant_access_token` or `user_access_token`) has been granted permissions to read or edit spreadsheets. Otherwise, the API will return HTTP 403 or 400 status codes. For more information, refer to [How to enable document permissions for applications or users](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#16c6475a).

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token
HTTP Method | GET
Rate Limit | [100 per minute](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space(drive:drive)<br>View, comment, and download all files in My Space(drive:drive:readonly)<br>View, comment, edit, and manage Sheets(sheets:spreadsheet)<br>View, comment, and export Sheets(sheets:spreadsheet:readonly)
Required field scopes | **Notice**：The response body of the API contains the following sensitive fields, and they will be returned only after corresponding scopes are added. If you do not need the fields, it is not recommended that you request the scopes.<br>Obtain user ID(contact:user.employee_id:readonly)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)

### Path parameters

Parameter | Type | Description
---|---|---
spreadsheet_token | string | Table token. Refer to the [Spreadsheet Overview](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview) to obtain the token.<br>**Example value**: "Iow7sNNEphp3WbtnbCscPqabcef"

### Query parameters

Parameter | Type | Required | Description
---|---|---|---
user_id_type | string | No | User ID categories<br>**Example value**: open_id<br>**Optional values are**:<br>- open_id：Identifies a user to an app. The same user has different Open IDs in different apps. [How to get Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid)<br>- union_id：Identifies a user to a tenant that acts as a developer. A user has the same Union ID in apps developed by the same developer, and has different Union IDs in apps developed by different developers. A developer can use Union ID to link the same user's identities in multiple apps.[How to get Union ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id)<br>- user_id：Identifies a user to a tenant. The same user has different User IDs in different tenants. In one single tenant, a user has the same User ID in all apps （including store apps）. User ID is usually used to communicate user data between different apps. [How to get User ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**Default value**: `open_id`<br>**When the value is `user_id`, the following field scopes are required**:<br>Obtain user ID(contact:user.employee_id:readonly)

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
spreadsheet | get_spreadsheet | Spreadsheet information
title | string | Spreadsheet title
owner_id | string | Spreadsheet owner
token | string | Spreadsheet token
url | string | Spreadsheet url

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "spreadsheet": {
            "title": "title",
            "owner_id": "u_48d0958ee4b2ab3eaf0b5f6c968abcef",
            "token": "Iow7sNNEphp3WbtnbCscPqabcef",
            "url": "https://example.feishu.cn/sheets/Iow7sNNEphp3WbtnbCscPqabcef"
        }
    }
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
400 | 1310251 | Invalid Parameters | Reference error message in response body
400 | 1310213 | Permission Fail | Confirm whether the current access identity has permission to read or edit spreadsheets. Please refer to the following methods to resolve this:<br>- If you are using a `tenant_access_token`, it means the current application does not have permission to read or edit spreadsheets. You need to add document permissions for the application through the cloud document webpage by navigating to the top right corner **"..."** -> **"... More"** -> **"Add applications"**.<br>**Note**: Before adding a document application, you need to ensure that the target application has at least one cloud document [API permission](https://open.larkoffice.com/document/ukTMukTMukTM/uYTM5UjL2ETO14iNxkTN/scope-list) enabled. Otherwise, you will not be able to search for the target application in the document application window.<br>![](//sf3-cn.feishucdn.com/obj/open-platform-opendoc/bb60f97ebb402475f2af1d3131d4914f_sLOzoqYRXX.png?height=1992&maxWidth=550&width=3278)<br>- If you are using a `user_access_token`, it means the current user does not have permission to read or edit spreadsheets. You need to add document permissions for the current user through the **Share** entry in the top right corner of the cloud document webpage.<br>![image.png](//sf3-cn.feishucdn.com/obj/open-platform-opendoc/caceea2ac91c170555194d7a8dc2a317_GfTRc9xLAt.png&maxWidth=550)<br>For more details on the specific steps or other methods to add permissions, refer to [Cloud Document FAQ 3](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#16c6475a).
400 | 1310249 | Spreadsheet Deleted | Restore the form and try again
500 | 1315210 | Server Error | Internal service errors, please consult customer service for details
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.
