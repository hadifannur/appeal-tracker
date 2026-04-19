# Spreadsheet association user guide
## Scenarios
Spreadsheet association is used to process form, spreadsheet, and structured data. It allows you to sync structured data to spreadsheets, and sort, filter, and edit the data or plot charts based on the data.

## Lifecycle
	Four APIs are provided for spreadsheet association. A simplified lifecycle is as follows:
1. [Associate a form](https://open.larkoffice.com/document/ukTMukTMukTM/uYzM0YjL2MDN24iNzQjN) (Initialize a form and some data, and create a new spreadsheet)
2. [Set form data](https://open.larkoffice.com/document/ukTMukTMukTM/uADN0YjLwQDN24CM0QjN) (Sync data) and [Edit form header](https://open.larkoffice.com/document/ukTMukTMukTM/ugzM0YjL4MDN24COzQjN)
3. [Cancel an association](https://open.larkoffice.com/document/ukTMukTMukTM/uczM0YjL3MDN24yNzQjN) (Data sync and form header editing are no longer allowed)

## Cancel association events
You can call the API to cancel an association (used by Open Platform developers to actively cancel an association), or cancel the association on the spreadsheet page (performed by users).

![image.png](//sf3-cn.feishucdn.com/obj/open-platform-opendoc/c48d7203d77effdd6abaf1d07eb3f67e_IJrmLWJBl7.png)

To listen on association cancellation events, you can subscribe to [Document and third-party app association status change] events.

![图片名称](//sf3-cn.feishucdn.com/obj/website-img/fb4d13885d1a6ba983988094b6b750d2_2B4ehduSpf.png)

## Spreadsheet association restrictions
Forms and spreadsheets must abide by the following restrictions to ensure the integrity of form data:
1. You cannot delete header rows and columns.
2. Most actions that destroy form data are restricted (such as merging cells and local sorting).
3. You cannot delete associated sheets.
4. Association cancellation cannot be reversed.

# Associate a form

This API is used to link third-party (form) data to a spreadsheet. After association, the third-party (form) data will be synced to the spreadsheet in real time.
## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheet/v2/link_form
HTTP Method | PUT

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `user_access_token` or `tenant_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[Learn more about how to access and use access_token](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Request body

| Parameter             | Type             | Required | Description                                                         |
| ---------------- | ---------------- | ---- | ------------------------------------------------------------ | ----------- |
| title            | string           | Yes   |Spreadsheet title                                                     | Request body    |
| sheetName        | string           | Yes   | Sheet name                                                       | Request body    |
| cols             |                  | Yes   | Form header information                                                 | Request body    |
| ∟colName         | string           | Yes   | Column name                                                         | Request body    |
| ∟style           |                  | No   | Column style                                                       | Request body    |
| &emsp;∟formatter | string           | No   | Number format. For details, see the appendix [Number formats supported by sheets](https://open.larkoffice.com/document/ukTMukTMukTM/uMjM2UjLzIjN14yMyYTN) | Request body    |
| data             |                  | No   | Form data                                                     | Request body    |
| ∟values          | array<interface> | Yes   | Values to write. Only String and Number types are supported. | Request body    |

### Request body example
```json
{
    "title": "Spreadsheet title",
    "sheetName": "Sheet name",
    "cols": [
        {
            "colName": "string",
            "style": {
                "formatter": "@"
            }
        },
        {
            "colName": "string",
            "style": {
                "formatter": "0"
            }
        }
    ],
    "data": {
        "values": [
            [
                "https://www.xxx.com",
                123
            ]
        ]
    }
}
```
###  cURL request example
```
curl --location --request PUT 'https://open.feishu.cn/open-apis/sheet/v2/link_form' \
--header 'Authorization: Bearer t-5be16bd570d0437444c40d5e6b5584109e61b0b1' \
--header 'Content-Type: application/json' \
--data-raw '{
    "title": "Spreadsheet title",
    "sheetName": "Sheet name",
    "cols": [
        {
            "colName": "string",
            "style": {
                "formatter": "@"
            }
        },
        {
            "colName": "string",
            "style": {
                "formatter": "0"
            }
        }
    ],
    "data": {
        "values": [
            [
                "https://www.xxx.com",
                123
            ]
        ]
    }
}'
```
## Response
### Response body

| Parameter    |Type| Description                   |
| ------- |-----| ---------------------- |
| token   |string| Document token              |
| url     |string| Document URL               |
| sheetId |string| Spreadsheet sheetId |
| cols    |array<string>| Mapping of column names and IDs   |
| rowIds  |array<string>| Row ID                   |
  ### Response body example
```json
{
    "token": "shtcnxxx",
    "url": "https://xxx", //Document URL
    "sheetId": "sheetId",
    "cols": [
        {
            "colId": "id1",
            "colName": "name1"
        },
        {
            "colId": "id2",
            "colName": "name2"
        }
    ],
    "rowIds": [
        "rowId1",
        "rowId2"
    ],
    "code": 0,
    "msg": "Success"
}
```
### Error code

For details, refer to [Server-side error codes](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN).

# Cancel form association

This API is used to cancel the association between QR Master data and form content. The form data will no longer be synced to the spreadsheet.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheet/v2/spreadsheets/:spreadsheetToken/link_form
HTTP Method | DELETE
Required scopes<br>**The scopes required to call this API. You can call the API with any of the scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space<br>View, comment, edit, and manage Sheets

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `user_access_token` or `tenant_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[Learn more about how to access and use access_token](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Path parameters
| Parameter             | Type   | Required | Description                                                         |
| ---------------- | ------ | ---- | ------------------------------------------------------------ | 
| spreadsheetToken | string | Yes   | Spreadsheet token. For more information about how to obtain the token, see [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview). |
### Request body

| Parameter             | Type   | Required | Description                                                         |
| ---------------- | ------ | ---- | ------------------------------------------------------------ | 
| sheetId          | string | Yes   | Sheet ID. For details, see [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview). |
### Request body example
```json
{
  "sheetId": "string"
}
```
###  cURL request example
```
curl --location --request DELETE 'https://open.feishu.cn/open-apis/sheet/v2/spreadsheets/shtcnRRLTFmAY1s4Vkgkovts88b/link_form' \
--header 'Authorization: Bearer t-5be16bd570d0437444c40d5e6b5584109e61b0b1' \
--header 'Content-Type: application/json' \
--data-raw '{
  "sheetId": "9HvX8j"
}'
```
## Response
### Response body example
```json
{
  "code": 0,
  "msg": "Success"
}
```

# Set form data

This API is used to sync data to a spreadsheet based on row and column IDs.
## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheet/v2/spreadsheets/:spreadsheetToken/form_data
HTTP Method | POST
Required scopes<br>**The scopes required to call this API. You can call the API with any of the scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space<br>View, comment, edit, and manage Sheets

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `user_access_token` or `tenant_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[Learn more about how to access and use access_token](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Request body
values is a 2D array of N rows and M columns (N is less than or equal to 100).

When rowIds is not empty, rowIds.length must be equal to N to update spreadsheet data. When rowIds is empty, N new rows of data are inserted into the spreadsheet.

cols.length must be equal to M.

| Parameter             | Type             | Required | Description                                                         | Source        |
| ---------------- | ---------------- | ---- | ------------------------------------------------------------ | ----------- |
| sheetId   | string           | Yes   | Sheet ID associated with the spreadsheet                              | Request body    |
| rowIds | array<string> | No | Row ID | Request body |
| cols             |                  | Yes   | Form header information                                                 | Request body    |
| ∟colId      | string           | Yes   | Column ID                                                     | Request body    |
| ∟style           |                  | No   | Column style                                                       | Request body    |
| &emsp;∟formatter | string           | No   | Number format. For details, see the appendix [Number formats supported by sheets](https://open.larkoffice.com/document/ukTMukTMukTM/uMjM2UjLzIjN14yMyYTN) | Request body    |
| data             |                  | No   | Form data                                                     | Request body    |
| ∟values          | array<interface> | No   | Values to write. For information about how to write hyperlinks, emails, and @mention users, see the appendix [Data types supported by sheets](https://open.larkoffice.com/document/ukTMukTMukTM/ugjN1UjL4YTN14CO2UTN) | Request body    |

### Request body example
```json
{
	"sheetId":"abcd",
	"rowIds": ["rowId1"],
    "cols": [
        {
            "colId": "colId1",
            "style": {
                "formatter": "@"
            }
        },
        {
            "colId": "colId2",
            "style": {
                "formatter": "0"
            }
        }
    ],
    "data": {
        "values": [
            [
                "http://www.xx.com",
                123
            ]
        ]
    }
}
```
###  cURL request example
```
curl --location --request POST 'https://open.feishu.cn/open-apis/sheet/v2/spreadsheets/shtcnRRLTFmAY1s4Vkgkovts88b/form_data' \
--header 'Authorization: Bearer t-5be16bd570d0437444c40d5e6b5584109e61b0b1' \
--header 'Content-Type: application/json' \
--data-raw '{
	"sheetId":"9HvX8j",
	"rowIds": ["HIy9zHmi"],
    "cols": [
        {
            "colId": "QrsPhAxY",
            "style": {
                "formatter": "@"
            }
        },
        {
            "colId": "VunXL6If",
            "style": {
                "formatter": "0"
            }
        }
    ],
    "data": {
        "values": [
            [
                "http://www.xx.com",
                123
            ]
        ]
    }
}'
```
## Response
### Response body
  | Parameter   | Type | Description                 |
| ------ |-----| -------------------- |
| rowIds |array<string>| IDs of rows to update or add   |
| colIds |array<string> | All column IDs of the spreadsheet associated with the form |

### Response body example
```json
{
	"data":{
          "rowIds": ["rowId1"], 
          "colIds": ["colId1","colId2"]
	  }

"code": 0,
    "msg": "Success"
}
```
### Error code

For details, refer to [Server-side error codes](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN).

# Modify form header

This API is to modify the form header.
## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheet/v2/spreadsheets/:spreadsheetToken/form_header
HTTP Method | POST
Required scopes<br>**The scopes required to call this API. You can call the API with any of the scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space<br>View, comment, edit, and manage Sheets

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `user_access_token` or `tenant_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[Learn more about how to access and use access_token](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Request body
| Parameter             | Type          | Required | Description                                                         |
| ---------------- | ------------- | ---- | ------------------------------------------------------------ |
| editType         | string        | Yes   | Modification type. add: add a form header; update: modify a form header; delete: delete a form header; query: query a form header |
| sheetId          | string | Yes   | Sheet ID. For details, see [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview).|
| addCols          |               | No   | Add header information                                                 |
| ∟colName         | string        | Yes   | Column name                                                         |
| ∟style           |               | No   | Column style                                                       |
| &emsp;∟formatter | string           | No   | Number format. For details, see the appendix [Number formats supported by sheets](https://open.larkoffice.com/document/ukTMukTMukTM/uMjM2UjLzIjN14yMyYTN). | Request body    |
| delColIds        | array<string> | No   | List of column IDs to delete                                                 |
| updateCols       |               | No   | Updated header information                                                 |
| ∟colId           | string        | Yes   | Column ID                                                         |
| ∟colName         | string        | No   | Column name                                                         |
| ∟style           |               | No   | Column style                                                       |
| &emsp;∟formatter | string           | No   | Number format. For details, see the appendix [Number formats supported by sheets](https://open.larkoffice.com/document/ukTMukTMukTM/uMjM2UjLzIjN14yMyYTN). |
### Request body example
```json
{
    "editType": "string",
    "sheetId": "string",
    "addCols": [
        {
            "colName": "string",
            "style": {}
        },
        {
            "colName": "string",
            "style": {}
        }
    ],
    "delColIds": [
        "string",
        "string",
        "string"
    ],
    "updateCols": [
        {
            "colId": "string",
            "colName": "string",
            "style": {}
        },
        {
            "colId": "string",
            "colName": "string",
            "style": {}
        }
    ]
}
```
###  cURL request example
```
curl --location --request POST 'https://open.feishu.cn/open-apis/sheet/v2/spreadsheets/shtcnRRLTFmAY1s4Vkgkovts88b/form_header' \
--header 'Authorization: Bearer t-5be16bd570d0437444c40d5e6b5584109e61b0b1' \
--header 'Content-Type: application/json' \
--data-raw '{
    "editType": "add",
    "sheetId": "9HvX8j",
    "addCols": [
        {
            "colName": "asdf",
            "style": {
                "formatter": "@"
            }
        },
        {
            "colName": "ghjkl",
            "style": {}
        }
    ],
    "delColIds": [
        "QrsPhAxY"
    ],
    "updateCols": [
        {
            "colId": "VunXL6If",
            "colName": "strgscving",
            "style": {}
        }
    ]
}'
```
## Response
### Response body
  | Parameter     | Description     |
| -------- | -------- |
| editType | Edit type |
| colId    | Column ID     |
| colName  | Column name     |
| rowIds   | Row ID     |
### Response body example
```json
{
    "data"{
        "editType": "add",
        "cols": [
            {
                "colId": "id1",
                "colName": "name1"
            },
            {
                "colId": "id2",
                "colName": "name2"
            }
        ]
    },
    "code": 0,
    "msg": "Success"
}
```
### Error code

For details, refer to [Server-side error codes](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN).
