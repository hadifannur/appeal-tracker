# Add protected range

Use this API to add multiple protected ranges based on  spreadsheetToken  and dimension information. You can operate on up to 5000 rows or columns.

**Notice**：Only protected rows or protected columns can be set, and protected cells cannot be set temporarily.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/protected_dimension
HTTP Method | POST
Supported app types | Custom App、Store App
Required scopes<br>**The scopes required to call this API. You can call the API with any of the scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space(drive:drive)<br>View, comment, edit, and manage Sheets(sheets:spreadsheet)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `user_access_token`  or  `tenant_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[Learn more about how to obtain and use access_token](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Query parameters

Parameter | Type | Required | Description
---|---|---|---
user_id_type | string | No | User ID type in the request, currently supports open_id and union_id | .

### Path parameters
|Parameter|Type|Required|Description|
|--|-----|--|----|
|spreadsheetToken|string|Yes|Spreadsheet token. For more information about how to obtain the token, see  [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview).| 

### Request body

**Notice**：The editors field is no longer used. Please use the users field instead. Users must contain the IDs of users with edit permission for the protected range to add. The ID type is determined by the user_id_type field.
|Parameter|Type|Required|Description|
|--|-----|--|----|
|addProtectedDimension|/|Yes|Dimension information for the protected range(s) to be added. A maximum of 50 elements are supported.| 
|&emsp;∟dimension|/|Yes|Dimension information for the protected rows and columns| 
|&emsp;&emsp;∟sheetId|string|Yes|sheetId| 
|&emsp;&emsp;∟majorDimension|string|No|Values: ROWS (default) or COLUMNS| 
|&emsp;&emsp;∟startIndex|int|Yes|Start position|
|&emsp;&emsp;∟endIndex|int|Yes|End position| 
|&emsp;∟editors|array<int64>|NO|userIDs of users who can edit the protected range| 
|&emsp;∟users|array<string>|No|IDs of users who can edit the protected range, ID type determined by user_id_type| 
|&emsp;∟lockInfo|string|No|Protected range information|

### Request body example

```json
{
    "addProtectedDimension":[
        {
            "dimension":{
                "sheetId":"string",
                "majorDimension":"COLUMNS",
                "startIndex":10,
                "endIndex":13
            },
            "users":[
                "ou_326f4b0552770f2de069deb256de5b30"
            ],
            "lockInfo":"You can edit"
        }
    ]
}
```

###  cURL Request example
```
curl --location --request POST 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/shtcngNygNfuqhxTBf588jwgWbJ/protected_dimension?user_id_type=open_id' \
--header 'Authorization: Bearer t-e346617a4acfc3a11d4ed24dca0d0c0fc8e0067e' \
--header 'Content-Type: application/json' \
--data-raw '{
    "addProtectedDimension":[
        {
            "dimension":{
                "sheetId":"Q7PlXT",
                "majorDimension":"COLUMNS",
                "startIndex":10,
                "endIndex":13
            },
            "users":[
              "ou_326f4b0552770f2de069deb256de5b30"
            ],
            "lockInfo":"You can edit"
        }
    ]
}'
```

## Response
### Response body

**Notice**：The editors field is discarded. Please use the users field instead. Users must contain the IDs of users with edit permission for the protected range to add. The ID type is determined by the user_id_type field.
|Parameter|Type|Description|
|--|-----|--|
|addProtectedDimension|array<interface>|Dimension information for the protected range(s) to be added, multiple ranges are allowed| 
|&emsp;∟dimension|Dimension information for the protected rows and columns| 
|&emsp;&emsp;∟sheetId|string|sheetId| 
|&emsp;&emsp;∟majorDimension|string|Values: ROWS (default) or COLUMNS| 
|&emsp;&emsp;∟startIndex|int||Start position|
|&emsp;&emsp;∟endIndex|int|End position| 
|&emsp;∟editors|array<int64>|UserIDs of users who can edit the protected range| 
|&emsp;∟users|array<string>|IDs of users who can edit the protected range, ID type determined by user_id_type.|
|&emsp;∟lockInfo|string|Protected range information|
|&emsp;∟protectId|string|Unique uid of the protected range, can be used to remove protection later.|

### Response body example  

```json
{
    "code": 0,
    "data": {
        "addProtectedDimension": [
            {
                "dimension": {
                    "endIndex": 0,
                    "majorDimension": "COLUMNS",
                    "sheetId": "***",
                    "startIndex": 0
                },
                "users": [
                    "ou_326f4b0552770f2de069deb256de5b30"
                ],
                "lockInfo": "***",
                "protectId": "***"
            }
        ]
    },
    "msg": "Success"
}

```  

### Error code

For details, refer to [Server-side error codes](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN).

# Modify protected range

Use this API to modify a protected range based on the protected range ID. Each operation can modify up to 10 IDs.
## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/protected_range_batch_update
HTTP Method | POST
Supported app types | Custom App、Store App
Required scopes<br>**The scopes required to call this API. You can call the API with any of the scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space(drive:drive)<br>View, comment, edit, and manage Sheets(sheets:spreadsheet)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `user_access_token`  or  `tenant_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[Learn more about how to obtain and use access_token](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Path parameters
| Parameter              | Type   | Required | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                           | 
| ----------------- | ------ | ---- | ------------------------------------------------------------ | ----------- |
| spreadsheetToken  | string | Yes   | token of the  sheet , to obtain the token, see [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)| 
### Request body
| Parameter              | Type   | Required | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                           | 
| ----------------- | ------ | ---- | ------------------------------------------------------------ | ----------- |
|requests||Yes|Request
| &emsp;protectId         | string | Yes   | Protected range ID, obtained through the [Obtain sheet metadata](https://open.larkoffice.com/document/ukTMukTMukTM/uETMzUjLxEzM14SMxMTN) API                                          |
| &emsp;∟dimension         |        | No   | Row and column protection information                                                 |
| &emsp;&emsp;∟sheetId          | string | Yes   | sheetId                                                      |
| &emsp;&emsp;∟startIndex       | int    | Yes   | Protected row and column start index, starts from 1.|
| &emsp;&emsp;∟endIndex         | int    | Yes   | Protected row and column end index, starts from 1.|
| &emsp;&emsp;∟majorDimension   | string | Yes   | Protected range dimensions for the protected range ID; COLUMNS indicates protected columns and ROWS indicates protected row.| Request body   |
| &emsp;∟editors           |        | No   | Users who can edit the protected range                                         |
| &emsp;&emsp;∟addEditors       |        | No   | The list of users to add, users must have doc editing permissions.|
| &emsp;&emsp;&emsp;∟memberType | string | Yes   | User type, supports userId, openId, and unionId.|
| &emsp;&emsp;&emsp;∟memberId   | string | Yes   | User ID of the selected user type                                         |
| &emsp;&emsp;∟delEditors       |        | No   | List of users to delete                                         |
| &emsp;&emsp;&emsp;∟memberType | string | Yes   | User type, supports userId, openId, and unionId.|
| &emsp;&emsp;&emsp;∟memberId   | string | Yes   | User ID of the selected user type                                         |
| &emsp;∟lockInfo          | string | No   | Protection description                                                     |

### Request body example
```json
{
    "requests": [
        {
            "protectId": "***",
            "dimension": {
                "majorDimension": "***",
                "sheetId": "***",
                "startIndex": 0,
                "endIndex": 0
            },
            "editors": {
                "addEditors": [
                    {
                        "memberType": "userId",
                        "memberId": "****"
                    }
                ],
                "delEditors": [
                    {
                        "memberType": "userId",
                        "memberId": "****"
                    }
                ]
            },
            "lockInfo": "****"
        }
    ]
}
```
### cURL Request example
```
curl --location --request POST 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/shtcngNygNfuqhxTBf588jwgWbJ/protected_range_batch_update' \
--header 'Authorization: Bearer t-e346617a4acfc3a11d4ed24dca0d0c0fc8e0067e' \
--header 'Content-Type: application/json' \
--data-raw '{
    "requests": [
        {
            "protectId": "6947942538267541505",
            "dimension": {
                "majorDimension": "ROWS",
                "sheetId": "Q7PlXT",
                "startIndex": 2,
                "endIndex": 4
            },
            "editors": {
                "addEditors": [
                    {
                        "memberType": "userId",
                        "memberId": "667338922291111404"
                    }
                },
                "delEditors": [
                    {
                        "memberType": "userId",
                        "memberId": "667338922291122404"
                    }
                ]
            },
            "lockInfo": "1234"
        }
    ]
}'
```
## Response
### Response body
| Parameter              |Type| Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; |
| ----------------- |-----| ---------------------------------- |
|replies|array<interface>|Response|
| &emsp;∟sheetId           |string| sheet ID                          |
| &emsp;∟dimension         || Successfully modified protected row and column information             |
| &emsp;&emsp;∟sheetId          |string| sheetId                            |
| &emsp;&emsp;∟startIndex       |int| Protected row and column start index, starts from 1      .|
| &emsp;&emsp;∟endIndex         |int| Protected row and column end index, starts from 1      .|
| &emsp;&emsp;∟majorDimension   |string| Protected range dimensions                     |
| &emsp;∟editors           | Users who can edit the protected range               |
| &emsp;&emsp;∟addEditors       |array<interface>| List of successfully added users               |
| &emsp;&emsp;&emsp;∟memberType |string| User type                           |
| &emsp;&emsp;&emsp;∟memberId   |string| User ID of the selected user type               |
| &emsp;&emsp;∟delEditors       |array<interface>| List of successfully deleted users               |
| &emsp;&emsp;&emsp;∟memberType |string| User type                           |
| &emsp;&emsp;&emsp;∟memberId   |string| User ID                of the selected user type|
| &emsp;∟lockInfo          |string| Successfully modified protection description                 |
###  Response body example
```json
{
    "code": 0,
    "msg": "Success",
    "data": {
        "replies": [
            {
                "protectId": "***",
                "dimension": {
                    "sheetId": "***",
                    "startIndex": 0,
                    "endIndex": 0,
                    "majorDimension": "ROWS"
                },
                "editors": {
                    "addEditors": [
                        {
                            "memberType": "userId",
                            "memberId": "*"
                        }
                    },
                    "delEditors": []
                },
                "lockInfo": "Info11",
                "sheetId": "abb54d"
            }
        ]
    }
}
```

### Error code

For details, refer to [Server-side error codes](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN).

# Get protected range

Use this API to get detailed row and column information for a protected range based on the protected range ID. Each operation can query up to 5 IDs.

**Notice**：1. Only obtaining protected rows or columns is supported. Obtaining protected cells is not currently supported.
2. Obtaining protection ranges containing multiple ranges is not supported
## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/protected_range_batch_get
HTTP Method | GET
Supported app types | Custom App、Store App
Required scopes<br>**The scopes required to call this API. You can call the API with any of the scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space(drive:drive)<br>View, comment, edit, and manage Sheets(sheets:spreadsheet)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `user_access_token`  or  `tenant_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[Learn more about how to obtain and use access_token](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Path parameters

Parameter | Type | Description
---|---|---
spreadsheetToken | string | Spreadsheet token. For more information about how to obtain the token, see [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview) | .

### Query parameters
| Parameter             | Type   | Required | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                           | 
| ---------------- | ------ | ---- | ------------------------------------------------------------ | 
| protectIds       | string | Yes   | Protected range ID, can be obtained through the [Obtain sheet metadata](https://open.larkoffice.com/document/ukTMukTMukTM/uETMzUjLxEzM14SMxMTN) API, separate multiple IDs with comas, for example: xxxID1,xxxID2.| 
| memberType       | string | No   | Returned user type, values: userId (default), openId, or unionId| 

### cURL request example
```
curl --location --request GET 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/shtcngNygNfuqhxTBf588jwgWbJ/protected_range_batch_get?protectIds=6946456074476339204,6947648349520592923,6947942538267541505&memberType=userId' \
--header 'Authorization: Bearer t-e346617a4acfc3a11d4ed24dca0d0c0fc8e0067e' \
```

## Response  
### Response body
| Parameter                        |Type| Description                                          |
| --------------------------- |-----| --------------------------------------------- |
| protectedRanges              |array<interface>| Protected rage                                      |
| &emsp;∟protectId            |string| Protected range ID                                    |
| &emsp;∟dimension            ||  Protected range, protects the whole sheet if empty              |
| &emsp;&emsp;∟sheetId        |string| id                                    of  sheet |
| &emsp;&emsp;∟startIndex     |int| Protected row and column start index, starts from 1                 .|
| &emsp;&emsp;∟endIndex       |int| Protected row and column end index, starts from 1                 .|
| &emsp;&emsp;∟majorDimension |string| Protected range dimensions, COLUMNS indicates protected columns and ROWS indicates protected rows .|
| &emsp;∟sheetId              |string| ID of the sheet                                     |
| &emsp;∟lockInfo             |string| Protection description                                      |
| &emsp;∟editors              || User information                                      |
| &emsp;&emsp;∟users	|array<interface>|User information list|
| &emsp;&emsp;&emsp;∟memberType     |string| User type                                      |
| &emsp;&emsp;&emsp;∟memberId       |string| User ID                                        |

### Response body example

```json
{
    "code": 0,
    "msg": "Success",
    "data": {
        "protectedRanges": [
            {
                "protectId": "*****",
                "dimension": {
                    "sheetId": "***",
                    "startIndex": 0,
                    "endIndex": 0,
                    "majorDimension": "COLUMNS"
                },
                "editors": {
                    "users": [
                        {
                            "memberType": "userId",
                            "memberId": "***"
                        }
                    ]
                },
                "sheetId": "***"
            }
        ]
    }
}
```

### Error code

For details, refer to [Server-side error codes](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN).

# Delete protected range

Use this API to delete a protected range based on the protected range ID. Each operation can delete up to 10 IDs.
## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/protected_range_batch_del
HTTP Method | DELETE
Supported app types | Custom App、Store App
Required scopes<br>**The scopes required to call this API. You can call the API with any of the scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space(drive:drive)<br>View, comment, edit, and manage Sheets(sheets:spreadsheet)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | When calling an API, the app needs to authenticate its identity through an access token. Refer to [Choose and obtain access tokens](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM#5aa2e490).<br>**Value format**："Bearer `access_token`"<br>Supported options are:<br>- `tenant_access_token`：<br>Call the API on behalf of the app. The range of readable and writable data is determined by the app's own [data permission range](https://open.larkoffice.com/document/home/introduction-to-scope-and-authorization/configure-app-data-permissions). Refer to [Get custom app tenant_access_token](https://open.larkoffice.com/document/ukTMukTMukTM/ukDNz4SO0MjL5QzM/auth-v3/auth/tenant_access_token_internal) or [Get store app tenant_access_token](https://open.larkoffice.com/document/ukTMukTMukTM/ukDNz4SO0MjL5QzM/auth-v3/auth/tenant_access_token). **Example value**："Bearer t-g1044qeGEDXTB6NDJOGV4JQCYDGHRBARFTGT1234"<br>- `user_access_token`：<br>Call the API on behalf of the user. The range of readable and writable data is determined by the user's data permission range. Refer to [Get user_access_token](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/authentication-management/access-token/get-user-access-token). **Example value**："Bearer u-cjz1eKCEx289x1TXEiQJqAh5171B4gDHPq00l0GE1234"
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Path parameters
| Parameter             | Type          | Required | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                           |
| ---------------- | ------------- | ---- | ------------------------------------------------------------ | 
| spreadsheetToken | string        | Yes   |Token of the sheet, to obtain the token, see [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview).|
### Request body
| Parameter             | Type          | Required | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                           |
| ---------------- | ------------- | ---- | ------------------------------------------------------------ |
| protectIds       | array<string> | Yes   | ID of the protected range to delete, obtained through the [Obtain sheet metadata](https://open.larkoffice.com/document/ukTMukTMukTM/uETMzUjLxEzM14SMxMTN) API.|
### Request body example

```json
{
    "protectIds": ["******"]
}
```
###  cURL Request example
```
curl --location --request DELETE 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/shtcngNygNfuqhxTBf588jwgWbJ/protected_range_batch_del' \
--header 'Authorization: Bearer t-e346617a4acfc3a11d4ed24dca0d0c0fc8e0067e' \
--header 'Content-Type: application/json' \
--data-raw '{
    "protectIds": ["6947942538267541505","6946456074476339204"]
}'
```
## Response
### Response body
  | Parameter          |Type| Description                 |
| ------------- |-----| -------------------- |
| delProtectIds |array<string>| ID of successfully deleted protected range |

### Response body example
```json
{
    "code": 0,
    "msg": "Success",
    "data": {
        "delProtectIds": [
            "******"
        ]
    }
}
```

### Error code

For details, refer to [Server-side error codes](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN).
