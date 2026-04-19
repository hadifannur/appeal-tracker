# Insert data
Add several rows above the designated range in a spreadsheet worksheet and populate them with data.

## Usage restrictions

- Each write operation must not exceed 5,000 rows and 100 columns. 
- Each cell should not exceed 50,000 characters. It's recommended to keep each cell under 40,000 characters due to additional control characters added by the server.
## Prerequisite

Before calling this API, ensure that the current identity (either `tenant_access_token` or `user_access_token`) has been granted permissions to read or edit spreadsheets. Otherwise, the API will return HTTP 403 or 400 status codes. For more information, refer to [How to enable document permissions for applications or users](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#16c6475a).
##  Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/values_prepend
HTTP Method | POST
Supported app types | Custom App、Store App
Required scopes<br>**The scopes required to call this API. You can call the API with any of the scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space(drive:drive)<br>View, comment, edit, and manage Sheets(sheets:spreadsheet)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | Authenticate the caller's identity through the access token. Optional values:<br>- `tenant_access_token`: Tenant authorization credential. The application acts on behalf of the tenant (i.e., a company or team) to perform corresponding operations. Example value: "Bearer t-7f1bcd13fc57d46bac21793aabcef"<br>- `user_access_token`: User authorization credential. The application acts on behalf of the user to perform corresponding operations. Example value: "Bearer u-7f1bcd13fc57d46bac21793aabcef"<br>For more information, refer to [Obtaining Access Tokens](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM).
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

###  Path parameters

Parameter | Type | Description
---|---|---
spreadsheetToken | string | The token for the spreadsheet can be obtained in two ways. For more information, refer to the [Spreadsheet Overview](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview).<br>- Spreadsheet URL: https://sample.feishu.cn/sheets/==Iow7sNNEphp3WbtnbCscPqabcef==<br>- Call [Get List of Files in Folder](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file/list)

###  Request body

Parameter | Type | Required | Description
---|---|---|---
valueRange | / | Yes | Specify the range and the data to be inserted into the worksheet.
range | string | Yes | The range for inserting data should be formatted as `<sheetId>!<start>:<end>`. Here:<br>- `sheetId` is the ID of the worksheet obtained through [Get Sheet](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet/query).<br>- `<start>:<end>` specifies the range of cells in the worksheet, where numbers represent row indices and letters represent column indices. For example, `A2:B2` represents columns A to B in the second row of the worksheet. `range` supports four formats; for more details, refer to [Spreadsheet Overview](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview).<br>**Note**: The specified `range` must cover an area equal to or greater than the area occupied by the inserted data.<br>**Example**: `8fe9d6!A2:B2`. This example indicates adding a row above the second row of the worksheet with ID `8fe9d6` and inserting data into columns A and B of the new row.
values | array<array<interface>> | Yes | The data to be inserted can include formulas, hyperlinks, email addresses, and @mentions. For more information on supported data types for writing in spreadsheets, please refer to [Supported Data Types for Spreadsheet Writing](https://open.larkoffice.com/document/ukTMukTMukTM/ugjN1UjL4YTN14CO2UTN).

### Request body example
```json
{
  "valueRange": {
    "range": "Q7PlXT!C6:F9",
    "values": [
      [
        "string",
        1,
        "http://www.xx.com"
      ]
    ]
  }
}
```

### cURL Request example
```
curl --location --request POST 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/shtcngNygNfuqhxTBf588jwgWbJ/values_prepend' \
--header 'Authorization: Bearer t-e346617a4acfc3a11d4ed24dca0d0c0fc8e0067e' \
--header 'Content-Type: application/json' \
--data-raw '{
"valueRange":{
  "range": "Q7PlXT!C6:F9",
  "values": [
    [
      "a",1,"http://www.xx.com",12
    ],
    [
      "b",2,8,"me@HelloWorld.com"
    ],
    [
      "c",3,2,6
    ],
    [
      "d",4,6,"@Jack"
    ]
  ]
  }
}'
```

##  Response
### Response body
  |Parameter|Type|Description|
|--|-----|--|
|spreadsheetToken|string|Spreadsheet token|
|tableRange|string|Range to write|
|revision|int|Version number of sheet |
|updates||Range and number of rows and columns for data insertion|
|&emsp;∟spreadsheetToken|string|Spreadsheet token|
|&emsp;∟updatedRange|string|Range to write|
|&emsp;∟updatedRows|int|Number of rows to write|
|&emsp;∟updatedColumns|int|Number of columns to write|
|&emsp;∟updatedCells|int|Total cells to write|
|&emsp;∟revision|int|Version number of sheet |
###  Response body example  
```json
{
  "code": 0,
  "data": {
    "revision": 18,
    "spreadsheetToken": "GQJHsEgcoh2qDHtSxeKcJCabcef",
    "tableRange": "6e5ed3!A1:C1",
    "updates": {
      "revision": 18,
      "spreadsheetToken": "GQJHsEgcoh2qDHtSxeKcJCabcef",
      "updatedCells": 3,
      "updatedColumns": 3,
      "updatedRange": "6e5ed3!A1:C1",
      "updatedRows": 1
    }
  },
  "msg": "success"
}
```
### Error code

For details, refer to [Server-side error codes](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN).

# Append data

Append data into empty positions within the specified range in a spreadsheet worksheet. For example, if the range parameter `range` is `6e5ed3!A1:B2`, this interface will sequentially search for empty cells starting from A1, A2, A3... until it finds the first empty cell to write the data into.

## Usage restrictions
- Each write operation must not exceed 5,000 rows and 100 columns.
- Each cell should not exceed 50,000 characters. It's recommended to keep each cell under 40,000 characters due to additional control characters added by the server.

## Prerequisite

Before calling this API, ensure that the current identity (either `tenant_access_token` or `user_access_token`) has been granted permissions to read or edit spreadsheets. Otherwise, the API will return HTTP 403 or 400 status codes. For more information, refer to [How to enable document permissions for applications or users](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#16c6475a).

##  Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/values_append
HTTP Method | POST
Supported app types | Custom App、Store App
Required scopes<br>**The scopes required to call this API. You can call the API with any of the scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space(drive:drive)<br>View, comment, edit, and manage Sheets(sheets:spreadsheet)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | Authenticate the caller's identity through the access token. Optional values:<br>- `tenant_access_token`: Tenant authorization credential. The application acts on behalf of the tenant (i.e., a company or team) to perform corresponding operations. Example value: "Bearer t-7f1bcd13fc57d46bac21793aabcef"<br>- `user_access_token`: User authorization credential. The application acts on behalf of the user to perform corresponding operations. Example value: "Bearer u-7f1bcd13fc57d46bac21793aabcef"<br>For more information, refer to [Obtaining Access Tokens](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM).
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

###  Path parameters

Parameter | Type | Description
---|---|---
spreadsheetToken | string | The token for the spreadsheet can be obtained in two ways. For more information, refer to the [Spreadsheet Overview](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview).<br>- Spreadsheet URL: https://sample.feishu.cn/sheets/==Iow7sNNEphp3WbtnbCscPqabcef==<br>- Call [Get List of Files in Folder](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file/list)

### Query parameters  
|Parameter|Type|Required|Description|
|--|-----|--|----|
|insertDataOption|string|No|Specifies the method of appending data, with the default value being OVERWRITE, meaning if the number of empty rows is less than the number of rows to be appended, existing data will be overwritten. Optional values include: <br>- OVERWRITE: Existing data will be overwritten if the number of empty rows is less than the number of rows to be appended. <br>- INSERT_ROWS: Sufficient rows will be inserted before appending the data.| 

### Request body 

Parameter | Type | Required | Description
---|---|---|---
valueRange | object | Yes | Specify the range and the data to be appended into the worksheet.
range | string | Yes | The range for appending data should be formatted as `<sheetId>!<start>:<end>`. Here:<br>- `sheetId` is the ID of the worksheet obtained through [Get Sheet](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet/query).<br>- `<start>:<end>` specifies the range of cells in the worksheet, where numbers represent row indices and letters represent column indices. For example, `A2:B2` represents columns A to B in the second row of the worksheet. `range` supports four formats; for more details, refer to [Spreadsheet Overview](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview).<br>**Note**: The specified `range` must cover an area equal to or greater than the area occupied by the appended data.<br>**Example**: `8fe9d6!A2:B2`. This example indicates adding a row above the second row of the worksheet with ID `8fe9d6` and appending data into columns A and B of the new row.
values | array<array<interface>> | Yes | The data to be appended can include formulas, hyperlinks, email addresses, and @mentions. For more information on supported data types for writing in spreadsheets, please refer to [Supported Data Types for Spreadsheet Writing](https://open.larkoffice.com/document/ukTMukTMukTM/ugjN1UjL4YTN14CO2UTN).

###  Request body example  
```json
{
  "valueRange": {
    "range": "string",
    "values": [
      [
        "string",
        1,
        "https://open.feishu.cn"
      ]
    ]
  }
}
```

### cURL Request example
```
curl --location --request POST 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/shtcngNygNfuqhxTBf588jwgWbJ/values_append?insertDataOption=OVERWRITE' \
--header 'Authorization: Bearer t-e346617a4acfc3a11d4ed24dca0d0c0fc8e0067e' \
--header 'Content-Type: application/json' \
--data-raw '{
  "valueRange": {
    "range": "Q7PlXT!A1:B4",
    "values": [
      [
        "===",
        "https://open.feishu.cn"
      ],
      [
        "Hello",
        "https://open.feishu.cn"
      ],
      [
        "World",
        "https://open.feishu.cn"
      ],
      [
        "===",
        "https://open.feishu.cn"
      ]
    ]
  }
}'
```

##  Response  
### Response body
|Parameter|Type|Description|
|--|-----|--|
|spreadsheetToken|string|Spreadsheet token|
|tableRange|string|Range to write|
|revision|int|Version number of sheet | 
|updates||Range and number of rows and columns for data insertion|
|&emsp;∟spreadsheetToken|string|Spreadsheet token|
|&emsp;∟updatedRange|string|Range to write|
|&emsp;∟updatedRows|int|Number of rows to write|
|&emsp;∟updatedColumns|int|Number of columns to write|
|&emsp;∟updatedCells|int|Total cells to write|
|&emsp;∟revision|int|Version number of sheet |

###  Response body example  
```json
{
  "code": 0,
  "msg": "Success",
  "data": {
    "revision": 0,
    "spreadsheetToken": "***",
    "tableRange": "***",
    "updates": {
      "spreadsheetToken": "***",
      "updatedRange": "***",
      "updatedRows": 0,
      "updatedColumns": 0,
      "updatedCells": 0,
      "revision": 0
    }
  }
}
```
### Error code

For details, refer to [Server-side error codes](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN).

# Write a image

This API is used to write an image to the specified cell based on the spreadsheetToken and range.

##  Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/values_image
HTTP Method | POST
Supported app types | Custom App、Store App
Required scopes<br>**The scopes required to call this API. You can call the API with any of the scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space(drive:drive)<br>View, comment, edit, and manage Sheets(sheets:spreadsheet)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `user_access_token`  or  `tenant_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[Learn more about how to obtain and use access_token](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

###  Path parameters

Parameter | Type | Description
---|---|---
spreadsheetToken | string | The token for the spreadsheet can be obtained in two ways. For more information, refer to the [Spreadsheet Overview](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview).<br>- Spreadsheet URL: https://sample.feishu.cn/sheets/==Iow7sNNEphp3WbtnbCscPqabcef==<br>- Call [Get List of Files in Folder](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file/list)

###  Request body
|Parameter|Type|Required|Description|
|--|-----|--|----|
|range|string|Yes|Query range  range=<sheetId>!<Start cell>:<End cell> For example: xxxx!A1:D5.For details, see [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview). This parameter is limited to one cell here, such as: : xxxx!A1:A1.|
|image|array<byte>|Yes|Binary data stream of the image to write.   "PNG",  "JPEG",  "JPG",  "GIF",  "BMP",  "JFIF",  "EXIF",  "TIFF",  "BPG", and  "HEIC"  formats are supported.|
|name|string|Yes|The name of the image to be written.<br>**Note**: This parameter must include a suffix, such as `test.png`. Supported suffixes are: "PNG", "JPEG", "JPG", "GIF", "BMP", "JFIF", "EXIF", "TIFF", "BPG", "HEIC". Case insensitive.|
### Request body example
```json
{ 
    "range": "string", 
    "image": [123,32,42,23],
    "name": "xxx.png"
}
```
### cURL Request example
```
curl --location --request POST 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/shtcngNygNfuqhxTBf588jwgWbJ/values_image' \
--header 'Authorization: Bearer t-e346617a4acfc3a11d4ed24dca0d0c0fc8e0067e' \
--header 'Content-Type: application/json' \
--data-raw '{ 
    "range": "Q7PlXT!H7:H7",
    "image": [137,80,78,71,13,10,26,10,0,0,0,13,73,72,68,82,0,0,0,2,0,0,0,1,1,0,0,0,0,220,89,66,39,0,0,0,2,116,82,78,83,0,0,118,147,205,56,0,0,0,10,73,68,65,84,8,215,99,104,0,0,0,130,0,129,221,67,106,244,0,0,0,0,73,69,78,68,174,66,96,130],
    "name": "test.png"
}'
```
### Example of getting image binary stream using Python

```python
def uploadImage():
    with open("./07.png", "rb") as f:
        url = "https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/X5assEfmnhepJtthAr4bY9Dlcxb/values_image"
        fb = f.read()
        misssing_padding = 4 - len(fb) % 4
        if misssing_padding:
            fb += b'=' * misssing_padding
        fb = base64.b64encode(fb).decode('utf-8')
        data = {
            "range": "CKu2Rq!A3:A3",
            "image": fb,
            "name": "a.png",
        }
        rsp = requests.post(url, data=json.dumps(data), headers={"Authorization": "Bearer 1nDxwUe_x5aGdZTDrefV5Xwk2hTt10BzMq20kk000Axr",
                                                                 "Content-Type": "application/json"})
        print(rsp.json())
```
##  Response
### Response body
  |Parameter|Type|Description|
|--|-----|--|
|spreadsheetToken|string |spreadsheet   token |
|revision|int|revision of spreadsheet|
|updateRange|string|updated range|
### Response body example

```json
{
    "code": 0,
    "data": {
        "revision": int,
        "spreadsheetToken": "string",
        "updateRange": "string"
    },
    "msg": "success"
}
```
### Error code

For details, refer to [Server-side error codes](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN).

# Write a image

This API is used to write an image to the specified cell based on the spreadsheetToken and range.

##  Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/values_image
HTTP Method | POST
Supported app types | Custom App、Store App
Required scopes<br>**The scopes required to call this API. You can call the API with any of the scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space(drive:drive)<br>View, comment, edit, and manage Sheets(sheets:spreadsheet)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `user_access_token`  or  `tenant_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[Learn more about how to obtain and use access_token](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

###  Path parameters

Parameter | Type | Description
---|---|---
spreadsheetToken | string | The token for the spreadsheet can be obtained in two ways. For more information, refer to the [Spreadsheet Overview](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview).<br>- Spreadsheet URL: https://sample.feishu.cn/sheets/==Iow7sNNEphp3WbtnbCscPqabcef==<br>- Call [Get List of Files in Folder](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file/list)

###  Request body
|Parameter|Type|Required|Description|
|--|-----|--|----|
|range|string|Yes|Query range  range=<sheetId>!<Start cell>:<End cell> For example: xxxx!A1:D5.For details, see [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview). This parameter is limited to one cell here, such as: : xxxx!A1:A1.|
|image|array<byte>|Yes|Binary data stream of the image to write.   "PNG",  "JPEG",  "JPG",  "GIF",  "BMP",  "JFIF",  "EXIF",  "TIFF",  "BPG", and  "HEIC"  formats are supported.|
|name|string|Yes|The name of the image to be written.<br>**Note**: This parameter must include a suffix, such as `test.png`. Supported suffixes are: "PNG", "JPEG", "JPG", "GIF", "BMP", "JFIF", "EXIF", "TIFF", "BPG", "HEIC". Case insensitive.|
### Request body example
```json
{ 
    "range": "string", 
    "image": [123,32,42,23],
    "name": "xxx.png"
}
```
### cURL Request example
```
curl --location --request POST 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/shtcngNygNfuqhxTBf588jwgWbJ/values_image' \
--header 'Authorization: Bearer t-e346617a4acfc3a11d4ed24dca0d0c0fc8e0067e' \
--header 'Content-Type: application/json' \
--data-raw '{ 
    "range": "Q7PlXT!H7:H7",
    "image": [137,80,78,71,13,10,26,10,0,0,0,13,73,72,68,82,0,0,0,2,0,0,0,1,1,0,0,0,0,220,89,66,39,0,0,0,2,116,82,78,83,0,0,118,147,205,56,0,0,0,10,73,68,65,84,8,215,99,104,0,0,0,130,0,129,221,67,106,244,0,0,0,0,73,69,78,68,174,66,96,130],
    "name": "test.png"
}'
```
### Example of getting image binary stream using Python

```python
def uploadImage():
    with open("./07.png", "rb") as f:
        url = "https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/X5assEfmnhepJtthAr4bY9Dlcxb/values_image"
        fb = f.read()
        misssing_padding = 4 - len(fb) % 4
        if misssing_padding:
            fb += b'=' * misssing_padding
        fb = base64.b64encode(fb).decode('utf-8')
        data = {
            "range": "CKu2Rq!A3:A3",
            "image": fb,
            "name": "a.png",
        }
        rsp = requests.post(url, data=json.dumps(data), headers={"Authorization": "Bearer 1nDxwUe_x5aGdZTDrefV5Xwk2hTt10BzMq20kk000Axr",
                                                                 "Content-Type": "application/json"})
        print(rsp.json())
```
##  Response
### Response body
  |Parameter|Type|Description|
|--|-----|--|
|spreadsheetToken|string |spreadsheet   token |
|revision|int|revision of spreadsheet|
|updateRange|string|updated range|
### Response body example

```json
{
    "code": 0,
    "data": {
        "revision": int,
        "spreadsheetToken": "string",
        "updateRange": "string"
    },
    "msg": "success"
}
```
### Error code

For details, refer to [Server-side error codes](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN).

# Read a single range

Retrieve data from a specific range in a spreadsheet.

## Usage restrictions

- The maximum limit for data returned by this interface is 10 MB.
- This interface does not support retrieving results from cross-sheet references and array formulas.

## Prerequisite

Before calling this API, ensure that the current identity (either `tenant_access_token` or `user_access_token`) has been granted permissions to read or edit spreadsheets. Otherwise, the API will return HTTP 403 or 400 status codes. For more information, refer to [How to enable document permissions for applications or users](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#16c6475a).
##  Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/values/:range
HTTP Method | GET
Supported app types | Custom App、Store App
Required scopes<br>**The scopes required to call this API. You can call the API with any of the scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space(drive:drive)<br>View, comment, and download all files in My Space(drive:drive:readonly)<br>View, comment, edit, and manage Sheets(sheets:spreadsheet)<br>View, comment, and export Sheets(sheets:spreadsheet:readonly)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | Authenticate the caller's identity through the access token. Optional values:<br>- `tenant_access_token`: Tenant authorization credential. The application acts on behalf of the tenant (i.e., a company or team) to perform corresponding operations. Example value: "Bearer t-7f1bcd13fc57d46bac21793aabcef"<br>- `user_access_token`: User authorization credential. The application acts on behalf of the user to perform corresponding operations. Example value: "Bearer t-7f1bcd13fc57d46bac21793aabcef"<br>For more information, refer to [Obtaining Access Tokens](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM).
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

###  Path parameters
|Parameter|Type|Required|Description|
|--|-----|--|----|
|spreadsheetToken|string|Yes|Spreadsheet token. For details, see [Overview](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview).|
|range|string|Yes|Query range, includes the sheetId range and cell range. For details, see [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview) . If a range of the form <sheetId>!<start cell>:<end column> is used in range, only 100 columns of data are supported.| 

###  Query parameters  
Obtaining calculation results of cross-table references and array formulas is not supported.

Name | Type | Required | Description
---|---|---|---
valueRenderOption | string | No | Specifies the format of the cell data. The optional values are as follows. When the parameter is absent, the default behavior is to not perform formula calculations and return the formula itself; numerical values are not formatted.<br>- valueRenderOption=ToString: Returns the value as plain text (excluding numerical types)<br>- valueRenderOption=FormattedValue: Computes and formats the cell<br>- valueRenderOption=Formula: Returns the formula itself when the cell contains a formula<br>- valueRenderOption=UnformattedValue: Computes but does not format the cell
dateTimeRenderOption | string | No | Specifies the format of cell data that is of date, time, or date-time type.<br>- When the parameter is absent, the default is to return a floating-point value where the integer part represents the number of days since December 30, 1899; the fractional part represents the portion of the day. For example, for January 1, 1900, at 12:00 PM, the default return is 2.5. Here, 2 indicates that January 1, 1900, is 2 days after December 30, 1899; 0.5 indicates that 12:00 PM is half of the 24 hours, i.e., 12/24=0.5.<br>- When the parameter is FormattedString, the interface calculates and formats the data of date, time, or date-time type and returns the formatted string, but does not format the numbers. For more details, refer to [Spreadsheet FAQs](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/guide/sheets-faq).
user_id_type | string | No | When the cell contains elements involving user information, such as @user, this parameter can specify the type of user ID returned. The default is `lark_id`, it is recommended to choose `open_id` or `union_id`. For more information, refer to [User Identity Overview](https://open.larkoffice.com/document/home/user-identity-introduction/introduction). Optional values:<br>- `open_id`: Identifies a user within a specific application. The same user has different Open IDs in different applications. Learn more: [How to Obtain Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid)<br>- `union_id`: Identifies a user under a specific application developer. The same user has the same Union ID in applications under the same developer and different Union IDs in applications under different developers. With Union ID, developers can link the identity of the same user across multiple applications. Learn more: [How to Obtain Union ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id)

###  cURL request example
```bash
curl --location --request GET 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/XUMasQlMYhOnMbt5htXc96h0nOg/values/Q7PlXT!A1:B2?valueRenderOption=ToString&dateTimeRenderOption=FormattedString' \
--header 'Authorization: Bearer t-ce3540c5f02ac074535f1f14d64fa90fa49621c0'
```
##  Response
### Response body 
|Parameter|Type|Description|
|--|-----|--|
|revision|Int |Version number of sheet |
|spreadsheetToken|string | Spreadsheet token. For details, see [Overview](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview).|
|valueRange||Value and range|
|&emsp;∟majorDimension|string|Insert dimension|
|&emsp;∟range|string|Range of returned data. When empty, this indicates there is no data in the query range.|
|&emsp;∟revision|int|Version number of sheet |
|&emsp;∟values|array<interface>|Values obtained by the query|

###  Response body example  
```json
{
    "code": 0,
    "data": {
        "revision": 7,
        "spreadsheetToken": "XUMasQlMYhOnMbt5htXc96h0nOg",
        "valueRange": {
            "majorDimension": "ROWS",
            "range": "Q7PlXT!A1:B2",
            "revision": 7,
            "values": [
                [
                    "Cell A1",
                    "Cell B1"
                ],
                [
                    "Cell A2",
                    "Cell B2"
                ]
            ]
        }
    },
    "msg": "success"
}
```
### Error code

For details, refer to [Server-side error codes](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN).

# Read multiple ranges

This API is used to read the values in multiple ranges based on spreadsheetToken and range.

## Usage restrictions

- The maximum data limit returned by this interface is 10 MB.
- This interface does not support retrieving the results of cross-sheet references and array formulas.

## Prerequisite

Before calling this API, ensure that the current identity (either `tenant_access_token` or `user_access_token`) has been granted permissions to read or edit spreadsheets. Otherwise, the API will return HTTP 403 or 400 status codes. For more information, refer to [How to enable document permissions for applications or users](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#16c6475a).
##  Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/values_batch_get
HTTP Method | GET
Supported app types | Custom App、Store App
Required scopes<br>**The scopes required to call this API. You can call the API with any of the scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space(drive:drive)<br>View, comment, and download all files in My Space(drive:drive:readonly)<br>View, comment, edit, and manage Sheets(sheets:spreadsheet)<br>View, comment, and export Sheets(sheets:spreadsheet:readonly)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | Authenticate the caller's identity through the access token. Optional values:<br>- `tenant_access_token`: Tenant authorization credential. The application acts on behalf of the tenant (i.e., a company or team) to perform corresponding operations. Example value: "Bearer t-7f1bcd13fc57d46bac21793aabcef"<br>- `user_access_token`: User authorization credential. The application acts on behalf of the user to perform corresponding operations. Example value: "Bearer u-7f1bcd13fc57d46bac21793aabcef"<br>For more information, refer to [Obtaining Access Tokens](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM).
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

###  Path parameters

Parameter | Type | Description
---|---|---
spreadsheetToken | string | The token for the spreadsheet can be obtained in two ways. For more information, refer to the [Spreadsheet Overview](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview).<br>- Spreadsheet URL: https://sample.feishu.cn/sheets/==Iow7sNNEphp3WbtnbCscPqabcef==<br>- Call [Get List of Files in Folder](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file/list)

###  Query parameters  

| Parameter                 | Type   | Required | Description                                                         |
| -------------------- | ------ | ---- | ------------------------------------------------------------ |
| ranges               | string | Yes   | Multiple query ranges, range separated by commas, such as range1,range2. ⁣Here, range includes the sheetId range and cell range. Four indexing methods are supported. For details, see  [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview) . If a range of the form <sheetId>!<start cell>:<end column> is used in the range, only 100 columns of data are supported|
| valueRenderOption    | string | No   | valueRenderOption=ToString can return plain text values; valueRenderOption=FormattedValue calculates and formats cells; valueRenderOption=Formula returns the formula body when cells contain formulas; valueRenderOption=UnformattedValue calculates but doesn't format cells.|
| dateTimeRenderOption  | string | No   | dateTimeRenderOption=FormattedString calculates and formats the date and time according to the specified format, but doesn't format the number. It returns the formatted string. For details, see [Sheets FAQs](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/guide/sheets-faq) .|
| user_id_type | string | No | Returned user ID type, values: open_id or union_id|

###  cURL request example
```
curl --location --request GET 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/shtcngNygNfuqhxTBf588jwgWbJ/values_batch_get?ranges=Q7PlXT!A2:B6,0b6377!B1:C8&valueRenderOption=ToString&dateTimeRenderOption=FormattedString' \
--header 'Authorization: Bearer t-e346617a4acfc3a11d4ed24dca0d0c0fc8e0067e' \
```
##  Response  

### Response body
|Parameter|Type|Description|
|--|-----|--|
|revision|int |Version number of sheet |
|spreadsheetToken|string | Spreadsheet token. For details, see [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview).|
|totalCells|int|Total cells read|
|valueRanges|array<interface>|Value and range|
|&emsp;∟majorDimension|string|Insert dimension|
|&emsp;∟range|string|Range of returned data. When empty, this indicates there is no data in the query range.|
|&emsp;∟revision|int|Version number of sheet |
|&emsp;∟values|array<interface>|Values obtained by the query|

###  Response body example    
```json
{
  "code": 0,
  "data": {
    "revision": 0,
    "spreadsheetToken": "***",
    "totalCells": 0,
    "valueRanges": [
      {
        "majorDimension": "ROWS",
        "range": "range1",
        "revision": 0,
        "values": [
          [
            "***"
          ]
        ]
      },
      {
        "majorDimension": "ROWS",
        "range": "range2",
        "revision": 0,
        "values": [
          [
            "***"
          ]
        ]
      }
    ]
  },
  "msg": "Success"
}
```  

### Error code

For details, refer to [Server-side error codes](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN).

# Write data to a single range

This API is used to write data to a single range based on spreadsheetToken and range. Any data in the range will be overwritten.
## Usage restrictions

- You can write up to 5,000 rows and 100 columns of data.
- A single cell can't exceed 50,000 characters.
## Prerequisite

Before calling this API, ensure that the current identity (either `tenant_access_token` or `user_access_token`) has been granted permissions to read or edit spreadsheets. Otherwise, the API will return HTTP 403 or 400 status codes. For more information, refer to [How to enable document permissions for applications or users](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#16c6475a).
##  Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/values
HTTP Method | PUT
Supported app types | Custom App、Store App
Required scopes<br>**The scopes required to call this API. You can call the API with any of the scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space(drive:drive)<br>View, comment, edit, and manage Sheets(sheets:spreadsheet)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `user_access_token`  or  `tenant_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[Learn more about how to obtain and use access_token](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

###  Path parameters
|Parameter|Type|Required|Description|
|--|-----|--|----|
|spreadsheetToken|string|Yes| Spreadsheet token. For more information about how to obtain the token, see [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)| URL PATH.|
###  Request body
|Parameter|Type|Required|Description|
|--|-----|--|----|
|valueRange||Yes|Value and range|
|&emsp;∟range|string|Yes|Range to update, includes the sheetId range and cell range. Four indexing methods are supported. For details, see [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview). The range indicated by range needs to be greater than or equal to the range occupied by values.|
|&emsp;∟values|array<array<interface>>|Yes|Values to write. To write formulas, hyperlinks, emails, and @mention users, see the appendix [Data types that can be written to sheet](https://open.larkoffice.com/document/ukTMukTMukTM/ugjN1UjL4YTN14CO2UTN).|
### Request body example
```json
{
"valueRange":{
    "range": "Q7PlXT!A1:C1",
    "values": [
      [
        "string", 1 ,"http://www.xx.com"
      ]
    ]
    }
}
```

###  cURL Request example
```
curl --location --request PUT 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/shtcngNygNfuqhxTBf588jwgWbJ/values' \
--header 'Authorization: Bearer t-e346617a4acfc3a11d4ed24dca0d0c0fc8e0067e' \
--header 'Content-Type: application/json' \
--data-raw '{
"valueRange":{
    "range": "Q7PlXT!A1:B2",
    "values": [
      [
        "Hello", 1
      ],
      [
        "World", 1
      ]
    ]
    }
}'
```

##  Response
### Response body
  |Parameter|Type|Description|
|--|-----|--|
|spreadsheetToken|string |spreadsheet   token |
|updatedRange|string |Range to write|
|updatedRows|int|Number of rows to write|
|updatedColumns|int|Number of columns to write|
|updatedCells|int|Total cells to write|
|revision|int|Version number of sheet |
###  Response body example  
```json
{
    "code": 0,
    "data": {
        "revision": 0,
        "spreadsheetToken": "***",
        "updatedCells": 0,
        "updatedColumns": 0,
        "updatedRange": "***",
        "updatedRows": 0
    },
    "msg": "Success"
}

```
### Error code

For details, refer to [Server-side error codes](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN).

# Write data to multiple ranges

This API is used to write data to multiple ranges based on spreadsheetToken and range. Any data in the ranges will be overwritten. You can write up to 5,000 rows and 100 columns of data. A single cell can't exceed 50,000 characters.
## Prerequisite

Before calling this API, ensure that the current identity (either `tenant_access_token` or `user_access_token`) has been granted permissions to read or edit spreadsheets. Otherwise, the API will return HTTP 403 or 400 status codes. For more information, refer to [How to enable document permissions for applications or users](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#16c6475a).
##  Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/values_batch_update
HTTP Method | POST
Supported app types | Custom App、Store App
Required scopes<br>**The scopes required to call this API. You can call the API with any of the scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space(drive:drive)<br>View, comment, edit, and manage Sheets(sheets:spreadsheet)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `user_access_token`  or  `tenant_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[Learn more about how to obtain and use access_token](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

###  Path parameters
|Parameter|Type|Required|Description|
|--|-----|--|----|
|spreadsheetToken|string|Yes| Spreadsheet token. For more information about how to obtain the token, see [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)| URL PATH.|
###  Request body
|Parameter|Type|Required|Description|
|--|-----|--|----|
|valueRanges||Yes|Multiple ranges to update|
|&emsp;∟range|string|Yes|Ranges to update, includes the sheetId ranges and cell ranges. Four indexing methods are supported. For details, see [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview). The range indicated by range needs to be greater than or equal to the range occupied by values.|
|&emsp;∟values|array<array<interface>>|Yes|Values to write. To write formulas, hyperlinks, emails, and @mention users, see the appendix [Data types that can be written to sheet ](https://open.larkoffice.com/document/ukTMukTMukTM/ugjN1UjL4YTN14CO2UTN).|
### Request body example
```json
{
  "valueRanges": [
    {
      "range": "range1",
      "values": [
        [
          "string1", 1, "http://www.xx.com"
        ]
      ]
    },
    {
      "range": "range2",
      "values": [
        [
          "string2", 2, "http://www.xx.com"
        ]
      ]
    }
  ]
}
```
### cURL Request example
```
curl --location --request POST 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/shtcngNygNfuqhxTBf588jwgWbJ/values_batch_update' \
--header 'Authorization: Bearer t-e346617a4acfc3a11d4ed24dca0d0c0fc8e0067e' \
--header 'Content-Type: application/json' \
--data-raw '{
  "valueRanges": [
    {
      "range": "Q7PlXT!A6:B9",
      "values": [
        [
          6,1
        ],
        [
          6,1
        ],
        [
          6,1
        ],
        [
          6,1
        ]
      ]
    },
    {
      "range": "BzY8T5!A1:C2",
      "values": [
        [
          "Hello", 2, "https://www.xx.com"
        ],
        [
          "World", 2, "https://www.xx.com"
        ]
      ]
    }
  ]
}'
```
##  Response
### Response body
|Parameter|Type|Description|
|--|-----|--|
|responses|array<interface>|Response|
|&emsp;∟spreadsheetToken|string |spreadsheet   token|
|&emsp;∟updatedRange|string |Range to write|
|&emsp;∟updatedRows|int|Number of rows to write|
|&emsp;∟updatedColumns|int|Number of columns to write|
|&emsp;∟updatedCells|int|Total cells to write|
|revision|int|Version number of sheet |
|spreadsheetToken|string |spreadsheet   token|
### Response body example
```json
{
    "code": 0,
    "data": {
        "responses": [
            {
                "spreadsheetToken": "***",
                "updatedCells": 0,
                "updatedColumns": 0,
                "updatedRange": "***",
                "updatedRows": 0
            },
            {
                "spreadsheetToken": "***",
                "updatedCells": 0,
                "updatedColumns": 0,
                "updatedRange": "***",
                "updatedRows": 0
            }
        ],
        "revision": 0,
        "spreadsheetToken": "***"
    },
    "msg": "Success"
}

```

### Error code

For details, refer to [Server-side error codes](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN).

# Supported data types for writing
This document introduces the data types supported by the V2 version interface for writing.

## Version description
The V2 version interface refers to the interface whose HTTP URL contains the `v2` identifier. For example, the URL `/sheets/v2/spreadsheets/:spreadsheet_token/dimension_range` of [Add rows and columns](https://open.larkoffice.com/document/ukTMukTMukTM/uUjMzUjL1IzM14SNyMTN) contains `v2`, indicating that this interface is a V2 version interface.

## String

```
"string"
```

## Number

```
123
```
## Date

1. Call the [Set cell style](https://open.larkoffice.com/document/ukTMukTMukTM/ukjMzUjL5IzM14SOyMTN) interface to set the cell to date format, and the request body example is as follows:

```json
{
  "appendStyle": {
    "range": "vJFUIq!A1:A10",
    "style": {
      "formatter": "yyyy/MM/dd"
    }
  }
}
```

2. Call the [Write data to a single range](https://open.larkoffice.com/document/ukTMukTMukTM/uAjMzUjLwIzM14CMyMTN) interface to write floating-point data, and the request body example is as follows:

```json
{
  "valueRanges": [
    {
      "range": "vJFUIq!A1:A10",
      "values": [
        [
          0
        ],
        [
          1
        ],
        [
          2
        ],
        [
          42101
        ]
      ]
    }
  ]
}
```

The integer part is the number of days since December 30, 1899; the decimal part is the proportion of the time within 24 hours. As shown in the above example, the date is displayed as shown in the figure below after writing:

![image.png](//sf3-cn.feishucdn.com/obj/open-platform-opendoc/c598f964ca602b69dd3ed11bdfb40885_dZM5cD74rz.png?height=442&lazyload=true&maxWidth=200&width=219)

## Link

### Link without text

```
"http://www.dd.com"
```

### Link with text

```json
{
    "text": "text",
    "link": "http://www.dd.com",
    "type": "url"
}
```

## Email

```
"aaa@aa.com"
```

## @Person
When writing the @Person type, it will be processed asynchronously.

- @Person only supports @users within the same tenant.
- Using this type, a single request supports @up to 50 people simultaneously.

| Field               | Description                                                                                         |
|--------------------|----------------------------------------------------------------------------------------------|
| notify             | Whether to send Feishu messages, users without read permissions will not receive Feishu messages                                           |
| grantReadPermission| Whether to grant read permission to the user (this field is only supported in independent tables); only available when the document sharing permission is owned                 |
| textType           | Specifies the content passed in the `text` field, optional `email`, `openId`, `unionId`                                |
| text               | Information of the person to @, specified by `textType`                                                         |

```json
{
    "type": "mention",
    "text": "aaa@aa.com",
    "textType": "email",
    "notify": true,
    "grantReadPermission": true
}
```

## Formula

The text field is the corresponding formula, and cross-table reference formulas (IMPORTRANGE) are not supported for now.

```json
{
    "type": "formula",
    "text": "=A1"
}
```

## @Document

textType: fixed as fileToken

text: document token

objType: document type, optional sheet, doc, slide, Base, mindnote

```json
{
    "type": "mention",
    "textType": "fileToken",
    "text": "shtxxxx",
    "objType": "sheet"
}
```

## Dropdown list

Values are arrays, which can be filled with bool, string, number types. String-type data cannot contain ",". Before using, you need to use the [Set dropdown list](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/datavalidation/set-dropdown) interface to set the dropdown list.

```json
{
    "type": "multipleValue",
    "values": [
        1,
        "test"
    ]
}
```

## Local style

### segmentStyle

bold: whether to bold

Italic: whether toitalic

strikeThrough: whether to strikethrough

underline: whether to underline

foreColor: font color, 16-bit RGB color

fontSize: font size, minimum size 9, maximum size 36

```json
{
    "bold": true,
    "italic": true,
    "strikeThrough": true,
    "underline": true,
    "foreColor": "#ff00ff",
    "fontSize": 30
}
```

### Write data with local style

#### String

```json
{
    "text": "string",
    "type": "text",
    "segmentStyle": {
        "bold": true,
        "italic": true,
        "strikeThrough": true,
        "underline": true,
        "foreColor": "#ff00ff",
        "fontSize": 20
    }
}
```

#### Number

Local style is not supported

#### Link

Supports writing different styles to different strings within the link. The foreColor field is not effective, fixed as blue; the underline field is not effective, fixed with underline;

```json
{
    "text": "text",
    "link": "http://www.dd.com",
    "type": "url",
    "texts": [
        {
            "text": "te",
            "segmentStyle": {
                "bold": true,
                "italic": true,
                "strikeThrough": true,
                "underline": true,
                "foreColor": "#ffffff",
                "fontSize": 20
            }
        },
        {
            "text": "xt",
            "segmentStyle": {
                "bold": true,
                "italic": false,
                "strikeThrough": true,
                "underline": true,
                "foreColor": "#ffffff",
                "fontSize": 10
            }
        }
    ]
}
```

#### Email

Supports writing different styles to different strings within the email. The foreColor field is not effective, fixed as blue; the underline field is not effective, fixed with underline;

```json
{
    "type": "url",
    "text": "aa@bytedance.com",
    "texts": [
        {
            "text": "aa",
            "segmentStyle": {
                "bold": true,
                "italic": true,
                "strikeThrough": true,
                "underline": true,
                "foreColor": "#ffffff",
                "fontSize": 20
            }
        },
        {
            "text": "@bytedance.com",
            "segmentStyle": {
                "bold": true,
                "italic": false,
                "strikeThrough": true,
                "underline": true,
                "foreColor": "#ffffff",
                "fontSize": 10
            }
        }
    ]
}
```

#### @Person
When writing the @Person type, it will be processed asynchronously.

- @Person only supports @users within the same tenant.
- Using this type, a single request supports @up to 50 people simultaneously.

| Field               | Description                                                                                         |
|--------------------|----------------------------------------------------------------------------------------------|
| notify             | Whether to send Feishu messages, users without read permissions will not receive Feishu messages                                           |
| grantReadPermission| Whether to grant read permission to the user (this field is only supported in independent tables); only available when the document sharing permission is owned                 |
| textType           | Specifies the content passed in the `text` field, optional `email`, `openId`, `unionId`                                |
| text               | Information of the person to @, specified by `textType`                                                         |
| segmentStyle       | Only supports setting local style for the whole; the foreColor field is not effective, fixed as blue                                                         |

```json
{
    "type": "mention",
    "text": "aaa@aa.com",
    "textType": "email",
    "notify": true,
    "grantReadPermission": true,
    "segmentStyle": {
        "bold": true,
        "italic": true,
        "strikeThrough": true,
        "underline": true,
        "foreColor": "#ff00ff",
        "fontSize": 30
    }
}
```

#### @Document

textType: fixed as fileToken

text: document token

objType: document type, optional sheet, doc, slide, Base, mindnote

The foreColor field is not effective, fixed as blue;

```json
{
    "type": "mention",
    "textType": "fileToken",
    "text": "shtxxxx",
    "objType": "sheet",
    "segmentStyle": {
        "bold": true,
        "italic": true,
        "strikeThrough": true,
        "underline": true,
        "foreColor": "#ff00ff",
        "fontSize": 30
    }
}
```

#### Dropdown list

Local style is not supported.

# Number formats supported
|Value|	 Description         | Example           | 
|  --------- | --------- | --------------- | 
||	Basic|
@|Plain text|text
0|Number|1024
#,##0|Number (Comma style)|1,024
#,##0.00|Number (Comma style with decimal point)|1,024.56
0%|Percent|10%
0.00%|Percent (with decimal point) |10.24%
0.00E+00|Scientific notation|1.02E+03
¥#,##0|CNY|¥1,024
¥#,##0.00|CNY (with decimal point)|¥1,024.56
$#,##0|USD|$1,024
$#,##0.00|USD (with decimal point)|$1,024.56
yyyy/MM/dd|Date|2017/08/10
yyyy-MM-dd|Date|2017-08-10
HH:mm:ss|Time|23:24:25
yyyy/MM/dd HH:mm:ss|Date and time|2017/08/10 23:24:25

