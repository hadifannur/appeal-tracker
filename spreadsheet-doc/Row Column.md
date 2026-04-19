# Add rows and columns
The interface is used to add blank rows or columns in a sheet.

## Limitations

- A single call to this interface supports adding up to 5000 rows or columns at maximum.
- This interface only supports adding rows or columns at the end of the sheet. To add rows or columns at a specified position, you need to use [insert rows or columns](https://open.larkoffice.com/document/ukTMukTMukTM/uQjMzUjL0IzM14CNyMTN).

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v2/spreadsheets/:spreadsheet_token/dimension_range
HTTP Method | POST
Supported app types | Custom App、Store App
Required scopes<br>**The scopes required to call this API. You can call the API with any of the scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space(drive:drive)<br>View, comment, edit, and manage Sheets(sheets:spreadsheet)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | When calling an API, the app needs to authenticate its identity through an access token. Refer to [Choose and obtain access tokens](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM#5aa2e490).<br>**Value format**："Bearer `access_token`"<br>Supported options are:<br>- `tenant_access_token`：<br>Call the API on behalf of the app. The range of readable and writable data is determined by the app's own [data permission range](https://open.larkoffice.com/document/home/introduction-to-scope-and-authorization/configure-app-data-permissions). Refer to [Get custom app tenant_access_token](https://open.larkoffice.com/document/ukTMukTMukTM/ukDNz4SO0MjL5QzM/auth-v3/auth/tenant_access_token_internal) or [Get store app tenant_access_token](https://open.larkoffice.com/document/ukTMukTMukTM/ukDNz4SO0MjL5QzM/auth-v3/auth/tenant_access_token). **Example value**："Bearer t-g1044qeGEDXTB6NDJOGV4JQCYDGHRBARFTGT1234"<br>- `user_access_token`：<br>Call the API on behalf of the user. The range of readable and writable data is determined by the user's data permission range. Refer to [Get user_access_token](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/authentication-management/access-token/get-user-access-token). **Example value**："Bearer u-cjz1eKCEx289x1TXEiQJqAh5171B4gDHPq00l0GE1234"
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Path parameters
|Parameter|Type|Required|Description|
|--|-----|--|----|
|spreadsheet_token|string|Yes| Spreadsheet token. For more information about how to obtain the token, see [Spreadsheet overview](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview).|
### Request body
|Parameter|Type|Required|Description|
|--|-----|--|----|
|dimension|/|Yes|Dimension information of rows and columns to add|
|&emsp;∟sheetId|string|Yes|sheetId|
|&emsp;∟majorDimension|string|Yes|The dimension to be added. Values:<br>- ROWS <br> - COLUMNS|
|&emsp;∟length|int|Yes|Number of rows and columns to add. The range is (0,5000]|
### Request body example
```json
{
  "dimension":{
       "sheetId": "2jm6f6",
        "majorDimension": "ROWS",
        "length": 8
     }
}
```
###  cURL request example
```
curl --location --request POST 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/shtcngNygNfuqhxTBf588jwgWbJ/dimension_range' \
--header 'Authorization: Bearer t-e346617a4acfc3a11d4ed24dca0d0c0fc8e0067e' \
--header 'Content-Type: application/json' \
--data-raw '{
  "dimension":{
       "sheetId": "2jm6f6",
        "majorDimension": "ROWS",
        "length": 8
     }
}'
```
## Response
### Response body
|Parameter|Type|Description|
|--|-----|--|
|addCount|int |Number of rows and columns to add|
|majorDimension|string |Insert dimension|
### Response body example 
```json
{
    "code": 0,
    "data": {
        "addCount": 1,
        "majorDimension": "ROWS"
    },
    "msg": "Success"
}

```
### Error code

For details, refer to [Server-side error codes](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN).

# Insert rows and columns

This API is used to insert empty rows or columns based on spreadsheetToken and dimension information. 

## Limitations
A single call to the interface supports the insertion of up to 5000 rows or columns.
##  Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/insert_dimension_range
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
spreadsheetToken | string | Spreadsheet token. For more information about how to obtain the token, see [Spreadsheet overview](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview) | .

###  Request body  
|Parameter|Type|Required|Description|
|--|-----|--|----|
|dimension|/|Yes|Dimension information of rows and columns to be inserted| 
|&emsp;∟sheetId|string|Yes|Sheet ID| 
|&emsp;∟majorDimension|string|No|The dimension to be inserted. Values:<br>- ROWS <br> - COLUMNS| 
|&emsp;∟startIndex|int|Yes|Start index. Counts from 0. If `startIndex` is 3, inserts empty rows or columns starting at row or column 4. Row or column 4 is included.|
|&emsp;∟endIndex|int|Yes|End index. Count from 0. If `endIndex` is 7, insert the row from the end of line 8. No more empty lines will be inserted in the 8th line. <br> Example: When `majorDimension` is` ROWS`, `startIndex` is 3, and `endIndex` is 7, blank rows are inserted in lines 4, 5, 6, and 7, for a total of 4 rows.|
|inheritStyle|string|No|Whether the inserted blank row or column inherit the cell style in the table.<br>- `BEFORE`: Inherit the style of the starting position cell<br>- `AFTER`: Inherit the style of the ending position cell Style. Empty means the demension won't inherit any style.| 

###  Request body example  
```json
{
    "dimension":{
        "sheetId":"2jm6f6",
        "majorDimension":"ROWS",
        "startIndex":3,
        "endIndex":7
    },
    "inheritStyle":"BEFORE"
}
```
### cURL Request example
```
curl --location --request POST 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/shtcngNygNfuqhxTBf588jwgWbJ/insert_dimension_range' \
--header 'Authorization: Bearer t-e346617a4acfc3a11d4ed24dca0d0c0fc8e0067e' \
--header 'Content-Type: application/json' \
--data-raw '{
    "dimension":{
        "sheetId":"2jm6f6",
        "majorDimension":"ROWS",
        "startIndex":3,
        "endIndex":7
    },
    "inheritStyle":"BEFORE"
}'
```
##  Response  

###  Response body example    

```json
{
    "code": 0,
    "msg": "Success",
    "data": {}
}
```

### Error code

For details, refer to [Server-side error codes](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN).

# Update rows and columns

This API is used to update the properties of rows and columns in a spreadsheet, including hiding rows and columns and set the height (if a row) or width (if a column) of the dimension in pixels. 

## Limitation

You can act on up to 5,000 rows and columns at once.

##  Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/dimension_range
HTTP Method | PUT
Supported app types | Custom App、Store App
Required scopes<br>**The scopes required to call this API. You can call the API with any of the scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space(drive:drive)<br>View, comment, edit, and manage Sheets(sheets:spreadsheet)

###  Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | When calling an API, the app needs to authenticate its identity through an access token. Refer to [Choose and obtain access tokens](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM#5aa2e490).<br>**Value format**："Bearer `access_token`"<br>Supported options are:<br>- `tenant_access_token`：<br>Call the API on behalf of the app. The range of readable and writable data is determined by the app's own [data permission range](https://open.larkoffice.com/document/home/introduction-to-scope-and-authorization/configure-app-data-permissions). Refer to [Get custom app tenant_access_token](https://open.larkoffice.com/document/ukTMukTMukTM/ukDNz4SO0MjL5QzM/auth-v3/auth/tenant_access_token_internal) or [Get store app tenant_access_token](https://open.larkoffice.com/document/ukTMukTMukTM/ukDNz4SO0MjL5QzM/auth-v3/auth/tenant_access_token). **Example value**："Bearer t-g1044qeGEDXTB6NDJOGV4JQCYDGHRBARFTGT1234"<br>- `user_access_token`：<br>Call the API on behalf of the user. The range of readable and writable data is determined by the user's data permission range. Refer to [Get user_access_token](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/authentication-management/access-token/get-user-access-token). **Example value**："Bearer u-cjz1eKCEx289x1TXEiQJqAh5171B4gDHPq00l0GE1234"
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Path parameters

Parameter | Type | Description
---|---|---
spreadsheetToken | string | Spreadsheet token. For more information about how to obtain the token, see [Spreadsheet overview](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview) | .

### Request body  
|Parameter|Type|Required|Description|
|--|-----|--|----|----|
|dimension|/|Yes|Dimension information of rows and columns to be updated| 
|&emsp;∟sheetId|string|Yes|sheetId|
|&emsp;∟majorDimension|string|No|The dimension to be updated. Values:<br>- ROWS <br> - COLUMNS| 
|&emsp;∟startIndex|int|Yes|Start index. Counts from 1. If `startIndex` is 3, updates empty rows or columns starting at row or column 3. Row or column 3 is included.| 
|&emsp;∟endIndex|int|Yes|End index. Count from 1. If `endIndex` is 7, update the row from the end of line 7. Row or column 7 is included. <br> Example: When `majorDimension` is` ROWS`, `startIndex` is 3, and `endIndex` is 7, rows in lines 3, 4, 5, 6, and 7 will be updated, for a total of 5 rows.| 
|dimensionProperties|/|Yes|Properties of rows or columns to be updated. Write at least one of the following parameters|
|&emsp;∟visible|bool|No|Whether to show rows or columns. Optional values are as follows:<br>- true: Show rows or columns <br>- false: Hide rows or columns| 
|&emsp;∟fixedSize|int|No|Row/Column size. The units are in seconds. When `fixedSize` is set to 0, it is equivalent to hiding the row or column. |

###  Request body example    
```json
{
    "dimension":{
        "sheetId":"2jm6f6",
        "majorDimension":"ROWS",
        "startIndex":1,
        "endIndex":3
    },
    "dimensionProperties":{
        "visible":true,
        "fixedSize":50
    }
}
```
###  cURL Request example
```BASH
curl --location --request PUT 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/shtcngNygNfuqhxTBf588jwgWbJ/dimension_range' \
--header 'Authorization: Bearer t-e346617a4acfc3a11d4ed24dca0d0c0fc8e0067e' \
--header 'Content-Type: application/json' \
--data-raw '{
    "dimension":{
        "sheetId":"2jm6f6",
        "majorDimension":"ROWS",
        "startIndex":1,
        "endIndex":3
    },
    "dimensionProperties":{
        "visible":true,
        "fixedSize":50
    }
}'
```

## Response  

###  Response body example    
```json
{
    "code": 0,
    "data": {},
    "msg": "Success"
}
```

###  Error code

For details, refer to [Server-side error codes](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN).

# Rows or columns to move

This API is used to move rows and columns. After rows and columns are moved to a target location, the rows and columns already at the target location are shifted right or down.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/move_dimension
HTTP Method | POST
Rate Limit | [100 per minute](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
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
spreadsheet_token | string | Sheet token, For details, see [Spreadsheet overview](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)<br>**Example value**: "Iow7sNNEphp3WbtnbCscPqabcef"
sheet_id | string | Sheet ID<br>**Example value**: "2jm6f6"

### Request body

Parameter | Type | Required | Description
---|---|---|---
source | dimension | No | Source location parameter
major_dimension | string | No | Row or column. values: <br>- ROWS<br>- COLUMNS<br>**Example value**: "ROWS"
start_index | int | No | Start row or column number. Counts from 0. If `startIndex` is 3, move from row or column 4. Contains the fourth row or column.<br>**Example value**: 0
end_index | int | No | End row or column number. Counts from 0. If `endIndex` is 7, move from row or column 8. The 8th row or column is contained.<br>Example: When 'majorDimension' is' ROWS', 'startIndex' is 3, and 'endIndex' is 7, the 4th, 5th, 6th, 7th and 8th rows are moved for a total of 5 rows.<br>**Example value**: 1
destination_index | int | No | Row or column number of the target location<br>**Example value**: 4

### Request body example
```json
{
    "source": {
        "major_dimension": "ROWS",
        "start_index": 0,
        "end_index": 1
    },
    "destination_index": 4
}
```

### cURL request example

```bash
curl --location --request POST 'https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/shtcnSUVpFeJ7Q2ycG1cHeSc/sheets/6e2914/move_dimension' \
--header 'Authorization: Bearer t-719d578dc63f6bd37e30cdb0394798a709070fec' \
--header 'Content-Type: application/json' \
--data-raw '{
    "source": {
        "major_dimension": "COLUMNS",
        "start_index": 1,
        "end_index": 3
    },
    "destination_index": 0
}'
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
400 | 1310211 | Wrong Sheet Id | Check the sheet_id.
400 | 1310202 | Wrong Range | Invalid range
400 | 1310229 | Wrong URL Param | Check the url parameter.
400 | 1310204 | Wrong Request Body | Check the request body parameter.
400 | 1310206 | Empty Sheet Id | Check the sheet_id
400 | 1310218 | Locked Cell | Check if the action targets a protected range.
400 | 1310213 | Permission Fail | No permission
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.
400 | 1310215 | Sheet Id Not Found | Check the sheet_id.
400 | 1310216 | Empty Value | Check the request body
400 | 1310217 | Too Many Request | Check if requests have been sent too frequently.
400 | 1310219 | Cell Excess | Check if the start or end index exceeds limit
400 | 1310235 | Retry Later | Please try again later.
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
200 | 1310234 | Marshal Error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952). | Internal service error. For more information, contact support.
400 | 1310242 | In Mix state | Doc is in cold delete state. Please wait for cold recovery and retry
400 | 1310249 | Spreadsheet Deleted | Restore the form and try again

# Delete rows or columns

This API is used to delete rows and columns based on spreadsheetToken and dimension information.

## Limitations

- You can delete up to 5,000 rows and columns at once.
- A worksheet should have a minimum of one row and one column. You cannot delete all rows or columns.

##  Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/dimension_range
HTTP Method | DELETE
Supported app types | Custom App、Store App
Required scopes<br>**The scopes required to call this API. You can call the API with any of the scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space(drive:drive)<br>View, comment, edit, and manage Sheets(sheets:spreadsheet)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | Authenticate the caller's identity through the access token. Optional values:<br>- `tenant_access_token`: Tenant authorization credential. The application acts on behalf of the tenant (i.e., a company or team) to perform corresponding operations. Example value: "Bearer t-7f1bcd13fc57d46bac21793aabcef"<br>- `user_access_token`: User authorization credential. The application acts on behalf of the user to perform corresponding operations. Example value: "Bearer u-7f1bcd13fc57d46bac21793aabcef"<br>For more information, refer to [Obtaining Access Tokens](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM).
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

###  Path parameters
|Parameter|Type|Required|Description&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;|
|--|-----|--|----|
|spreadsheetToken|string|Yes| Spreadsheet token. For details, see [Spreadsheet overview](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview).|
###  Request body
|Parameter|Type|Required|Description&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;  &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp;&nbsp;|
|--|-----|--|----|
|dimension|/|Yes|Dimension information of the rows and columns to delete. The row or column in the range [startIndex, endIndex] will be deleted|
|&emsp;∟sheetId|string|Yes|sheetId|
|&emsp;∟majorDimension|string|Yes|The dimension to be deleted. Values:<br>- ROWS <br> - COLUMNS|
|&emsp;∟startIndex|int|Yes|Start location. Start from 1. If `startIndex` is 3, the deletion starts at the 3rd row or column. Contains the third row or column.|
|&emsp;∟endIndex|int|Yes|End location. Start from 1. If `endIndex` is 7, delete until the end of the 7th row or column. Include the 7th row or column<br> Example: When `majorDimension` is `ROWS`, `startIndex` is 3, and `endIndex` is 7, delete the data in rows 3, 4, 5, 6, and 7, for a total of 5 rows.|
### Request body example
```json
{
    "dimension":{
        "sheetId":"2jm6f6",
        "majorDimension":"ROWS",
        "startIndex":3,
        "endIndex":7
    }
}
```
###  cURL Request example
```bash
curl --location --request DELETE 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/shtcngNygNfuqhxTBf588jwgWbJ/dimension_range' \
--header 'Authorization: Bearer t-e346617a4acfc3a11d4ed24dca0d0c0fc8e0067e' \
--header 'Content-Type: application/json' \
--data-raw '{
    "dimension":{
        "sheetId":"2jm6f6",
        "majorDimension":"ROWS",
        "startIndex":3,
        "endIndex":7
    }
}'
```
##  Response
### Response body
|Parameter|Type|Description|
|--|-----|--|
|delCount|int |Number of rows/columns to be deleted|
|majorDimension|string |The dimension to be deleted. Values:<br>- ROWS <br> - COLUMNS|
### Response body example
```json
{
    "code": 0,
    "data": {
        "delCount": 0,
        "majorDimension": "ROWS"
    },
    "msg": "success"
}

```
### Error code

For details, refer to [Server-side error codes](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN).
