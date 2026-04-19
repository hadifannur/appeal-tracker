# Application scenarios
Data verification is used to limit the data types and values input in cells. Currently, data verification is only supported for drop-down.

## 1. Drop-down
The drop-down function is a type of data verification/validity function. It provides a drop-down menu from which users choose the value of a cell. Other values cannot be input, ensuring the accuracy and correct format of the data.

The drop-down function also allows users to quickly label data. You can configure background colors for different options for a more intuitive and aesthetic display. You can also choose single option or multiple options for different scenarios. For example, the following "Gender" and "Ability" columns respectively use single option and multiple options of the drop-down list.

![image.png](//sf3-cn.feishucdn.com/obj/open-platform-opendoc/47f2dacb1ea10c5d897c0391d3d1e051_opo5xMxwpA.png?lazyload=true&width=1280&height=794)
### 1.1 Drop-down APIs
(1) [Set drop-down](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/datavalidation/set-dropdown): Sets drop-down verification rules for cells in the selected range.

(2) [Delete drop-down for specified range](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/datavalidation/delete-datavalidation): Sets drop-down verification rules for cells in the selected range.

(3) [Update drop-down verification rules](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/datavalidation/update-datavalidation): Updates the properties of specified drop-down rules.

(4) [Query drop-down rules in specified range](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/datavalidation/query-datavalidation): Queries drop-down rules in the selected range.

# Set drop-down

Use this API to set drop-down rules for cells based on spreadsheetToken, range, and drop-down properties. The range of a single operation cannot exceed 5,000 rows and 100 columns. When data already exists in the selected range, valid values are converted to options.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/dataValidation
HTTP Method | POST
Supported app types | Custom App、Store App
Required scopes<br>**The scopes required to call this API. You can call the API with any of the scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space(drive:drive)<br>View, comment, edit, and manage Sheets(sheets:spreadsheet)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `user_access_token` or `tenant_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[Learn more about how to obtain and use access_token](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Path parameters
|Parameter|Type|Required|Description|
|--|-----|--|----|
|spreadsheetToken|string|Yes|Spreadsheet token. For more information about how to obtain the token, see [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview).| 

### Request body
|Parameter|Type|Required|Description|
|--|-----|--|----|
|range|string|Yes|Query range, includes the sheetId range and cell range. Four indexing methods are supported. For details, see  [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview).| 
|dataValidationType|string|Yes|The "list" of the drop-down|
|dataValidation|||Drop-down rule properties
|&emsp;∟conditionValues|array<string>|Yes|Drop-down options, must be strings that do not include commas (,). Specify up to 500 options of up to 100 characters.|
|&emsp;∟options||No|Option properties| 
|&emsp;&emsp;∟multipleValues|bool|No|Single option: false (default), multiple options: true| 
|&emsp;&emsp;∟highlightValidData|bool|No|Whether to set color and capsule style, defaults to false when not specified|
|&emsp;&emsp;∟colors|array<string>|No|When highlightValidData is true, color must be specified. Values have one-to-one correspondence with conditionValues. Use RGB16 hex format, for example: "#fffd00".| 

### Request body example

```json
{
    "range":"yuNGtr!A2:A100",
    "dataValidationType":"list",
    "dataValidation":{
        "conditionValues":["2", "89", "3","2"],
        "options":{
            "multipleValues":true,
            "highlightValidData":true,
            "colors":["#1FB6C1", "#F006C2", "#FB16C3","#FFB6C1"]
        }
    }
}
```
###  cURL  Request example
  ```
curl --location --request POST 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/shtcngNygNfuqhxTBf588jwgWbJ/dataValidation' \
--header 'Authorization: Bearer t-5be16bd570d0437444c40d5e6b5584109e61b0b1' \
--header 'Content-Type: application/json' \
--data-raw '{
    "range":"BzY8T5!A2:A100",
    "dataValidationType":"list",
    "dataValidation":{
        "conditionValues":["2", "89", "3"],
        "options":{
            "multipleValues":true,
            "highlightValidData":true,
            "colors":["#1FB6C1", "#F006C2", "#FB16C3"]
        }
    }
}'
  ```
 ## Response

### Response body

|Parameter|Type|Required|Description|
|--|-----|--|----|
|code|int|Yes|Status code, 0 indicates success|
|msg|string|No|Status information|

### Response body example  

```json
{
    "code": 0,
    "msg": "Success"
}
```  

### Error code

For details, refer to [Server-side error codes](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN).

#  Update drop-down settings

Use this API to update drop-down properties based on spreadsheetToken, sheetId and range.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/dataValidation/:sheetId
HTTP Method | PUT
Supported app types | Custom App、Store App
Required scopes<br>**The scopes required to call this API. You can call the API with any of the scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space(drive:drive)<br>View, comment, edit, and manage Sheets(sheets:spreadsheet)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `user_access_token` or `tenant_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[Learn more about how to obtain and use access_token](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Path parameters
|Parameter|Type|Required|Description|
|--|-----|--|----|
|spreadsheetToken|string|Yes|Spreadsheet token. For more information about how to obtain the token, see [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview).| 
|sheetId|string|Yes|The unique identifier of the sheet

### Request body
|Parameter|Type|Required|Description|
|--|-----|--|----|
|ranges|array&lt;string&gt;|Yes|Update to Range Handling for Dropdown Lists. When updating a range, note that if the specified range does not currently have a dropdown list configured, the update will effectively create a new dropdown list for that range.|
|dataValidationType|string|Yes|The "list" of the drop-down|
|dataValidation|||Drop-down rule properties
|&emsp;∟conditionValues|array<string>|Yes|Drop-down options, must be strings that do not include commas (,). Specify up to 500 options of up to 100 characters.|
|&emsp;∟options||No|Option properties| 
|&emsp;&emsp;∟multipleValues|bool|No|Single option: false (default), multiple options: true| 
|&emsp;&emsp;∟highlightValidData|bool|No|Whether to set color and capsule style, defaults to false when not specified|
|&emsp;&emsp;∟colors|array<string>|No|When highlightValidData is true, color must be specified. Values have one-to-one correspondence with conditionValues. Use RGB16 hex format, for example: "#fffd00".| 

### Request body example

```json
{
    "ranges":["BzY8T5!A1:A2", "BzY8T5!B1:B1"],
    "dataValidationType":"list",
    "dataValidation":{
        "conditionValues":["1", "2", "4","2"],
        "options":{
            "multipleValues":false,
            "highlightValidData":true,
            "colors":["#1FB6C1", "#1006C2", "#FB16C3","#FFB6C1"]
        }
    }
}
```
###  cURL Request example
  ```
  curl --location --request PUT 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/shtcngNygNfuqhxTBf588jwgWbJ/dataValidation/BzY8T5' \
--header 'Authorization: Bearer t-5be16bd570d0437444c40d5e6b5584109e61b0b1' \
--header 'Content-Type: application/json' \
--data-raw '{
    "ranges":["BzY8T5!A1:A2", "BzY8T5!B1:B1"],
    "dataValidationType":"list",
    "dataValidation":{
        "conditionValues":["1", "2", "4"],
        "options":{
            "multipleValues":false,
            "highlightValidData":true,
            "colors":["#1FB6C1", "#1006C2", "#FB16C3"]
        }
    }
}'
  ```
 ## Response

### Response body

|Parameter|Type|Required|Description|
|--|-----|--|----|
|code|int|Yes|Status code, 0 indicates success|
|msg|string|No|Status information|
|data||||
|&emsp; ∟spreadsheetToken|string|Yes|The token of the spreadsheet| 
|&emsp; ∟sheetId|string|Yes|ID of the sheet| 
|&emsp;∟dataValidation|||| 
|&emsp;&emsp;∟dataValidationType|string|Yes|The "list" of the drop-down|
|&emsp;&emsp;∟conditionValues|array<string>|Yes|Drop-down options|
|&emsp;&emsp;∟options||No|Option properties| 
|&emsp;&emsp;&emsp;∟multipleValues|bool|No|Single option: false (default), multiple options: true| 
|&emsp;&emsp;&emsp;∟highlightValidData|bool|No|Whether to set color and capsule style|
|&emsp;&emsp;&emsp;∟colorValueMap|map<string,string>|No|When highlightValidData is true, the colorValueMap key has a one-to-one correspondence with conditionValues. Value is the corresponding color parameter.| 

### Response body example  

```json
{
    "code": 0,
    "data": {
        "dataValidation": {
            "conditionValues": [
                "1",
                "2",
                "4"
            ],
            "dataValidationType": "list",
            "options": {
                "colorValueMap": {
                    "1": "#1FB6C1",
                    "2": "#1006C2",
                    "4": "#FB16C3"
                },
                "highlightValidData": true,
                "multipleValues": false
            }
        },
        "sheetId": "yuNGtr",
        "spreadsheetToken": "shtbckBcolBlRfkcMVZbolMdADe"
    },
    "msg": "Success"
}
```  

### Error code

For details, refer to [Server-side error codes](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN).

# Query drop-down settings

Use this API to query drop-down settings information in a specified range based on spreadsheetToken and range. The range of a single query cannot exceed 5,000 rows and 100 columns.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/dataValidation
HTTP Method | GET
Supported app types | Custom App、Store App
Required scopes<br>**The scopes required to call this API. You can call the API with any of the scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space(drive:drive)<br>View, comment, edit, and manage Sheets(sheets:spreadsheet)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `user_access_token`  or  `tenant_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[Learn more about how to obtain and use access_token](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Path parameters
|Parameter|Type|Required|Description|
|--|-----|--|----|
|spreadsheetToken|string|Yes|Spreadsheet token. For more information about how to obtain the token, see  [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview).| 

### Query parameters
|Parameter|Type|Required|Description|
|--|-----|--|----|
|range|string|Yes|Query range, includes the sheetId range and cell range. Four indexing methods are supported. For details, see [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview).|
|dataValidationType|string|Yes|Fixed to "list", which means a drop-down list|

###  cURL Request example
```
curl --location --request GET 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/shtcngNygNfuqhxTBf588jwgWbJ/dataValidation?&range=BzY8T5!A2:A100' \
--header 'Authorization: Bearer t-5be16bd570d0437444c40d5e6b5584109e61b0b1' \
```

## Response

### Response body

|Parameter|Type|Required|Description|
|--|-----|--|----|
|code|int|Yes|Status code, 0 indicates success|
|msg|string|No|Status information|
|data||||
|&emsp; ∟spreadsheetToken|string|Yes|The token of the spreadsheet| 
|&emsp; ∟sheetId|string|Yes|ID of the sheet| 
|&emsp;∟revision|int|Yes|Version| 
|&emsp;∟dataValidations|array|No|Drop-down array, blank when no value exists| 
|&emsp;&emsp;∟ranges|array&lt;string&gt;|Yes|The ranges associated with a dropdown list are aggregated by column. For example, in the subtable with ID 4d30c6, if cells A1, A2, A4, B1, and B2 belong to the same dropdown list, the corresponding ranges for that dropdown list are: ["4d30c6!A1:A2", "4d30c6!A4:A4", "4d30c6!B1:B2"].|
|&emsp;&emsp;∟dataValidationType|string|Yes|Fixed to "list", which means a drop-down list|
|&emsp;&emsp;∟conditionValues|array<string>|Yes|Drop-down options|
|&emsp;&emsp;∟options||No|Option properties| 
|&emsp;&emsp;&emsp;∟multipleValues|bool|No|Single option: false (default), multiple options: true| 
|&emsp;&emsp;&emsp;∟highlightValidData|bool|No|Whether to set color and capsule style|
|&emsp;&emsp;&emsp;∟colorValueMap|map<string,string>|No|When highlightValidData is true, the colorValueMap key has a one-to-one correspondence with conditionValues. Value is the corresponding color parameter.| 

### Response body example  

```json
{
    "code": 0,
    "data": {
        "dataValidations": [
            {
                "conditionValues": [
                    "true",
                    "2",
                    "1",
                    "33.3333",
                    "ss"
                ],
                "dataValidationType": "list",
                "options": {
                    "colorValueMap": {
                        "1": "#b1e8fc",
                        "2": "#fed4a4",
                        "33.3333": "#f8e6ab",
                        "ss": "#a9efe6",
                        "true": "#bacefd"
                    },
                    "highlightValidData": true,
                    "multipleValues": true
                },
  				"ranges":[
        			"4d30c6!A1:A2",
        			"4d30c6!A4:A4",
        			"4d30c6!B1:B2"
        		]
            }
        ],
        "revision": 78,
        "sheetId": "4d30c6",
        "spreadsheetToken": "shtbckBcolBlRfkcMVZbolMdADe"
    },
    "msg": "Success"
}
```  

### Error code

For details, refer to [Server-side error codes](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN).

# Delete drop-down settings

Use this API to remove drop-down settings but retain option text for cells in the selected data range based on spreadsheetToken and range. A single delete range cannot include more than 5,000 cells, and each request cannot specify more than 100 ranges.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/dataValidation
HTTP Method | DELETE
Supported app types | Custom App、Store App
Required scopes<br>**The scopes required to call this API. You can call the API with any of the scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space(drive:drive)<br>View, comment, edit, and manage Sheets(sheets:spreadsheet)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `user_access_token`  or  `tenant_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[Learn more about how to obtain and use access_token](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Path parameters
|Parameter|Type|Required|Description|
|--|-----|--|----|
|spreadsheetToken|string|Yes|Spreadsheet token. For more information about how to obtain the token, see [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview).| 

### Request body
|Parameter|Type|Required|Description|
|--|-----|--|----|
|dataValidationRanges|array||Range array, each range is processed separately and cannot exceed 5,000 cells. The failure of one range does not impact other ranges. The return results give the execution results of each range.
|&emsp;∟range|string|Yes|Query range, includes the sheetId range and cell range. Four indexing methods are supported. For details, see [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview).

### Request body example

```json
{
    "dataValidationRanges":[
        {
            "range": "4d30c6!A10:C10"
        }
    ]
}
```
### cURL Request example
  ```
  curl --location --request DELETE 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/shtcngNygNfuqhxTBf588jwgWbJ/dataValidation' \
--header 'Authorization: Bearer t-ce3540c5f02ac074535f1f14d64fa90fa49621c0' \
--header 'Content-Type: application/json' \
--data-raw '{
    "dataValidationRanges":[
        {
            "range": "BzY8T5!A1:A1"
        }
    ]
}'
  ```
 ## Response

### Response body

|Parameter|Type|Required|Description|
|--|-----|--|----|
|code|int|Yes|Status code, 0 indicates success|
|msg|string|No|Status information|
|data||||
|&emsp;∟rangeResults|array|||
|&emsp;&emsp;∟range|string|Yes|The execution range, corresponds to range in the request parameters|
|&emsp;&emsp;∟msg|string|No|Result information|
|&emsp;&emsp;∟success|bool|Yes|Execution results|
|&emsp;&emsp;∟updatedCells|int|Yes|No. of cells affected|

### Response body example  

```json
{
    "code": 0,
    "data": {
        "rangeResults": [
            {
                "msg": "",
                "range": "4d30c6!A10:C10",
                "success": true,
                "updatedCells": 3
            }
        ]
    },
    "msg": "Success"
}
```  

### Error code

For details, refer to [Server-side error codes](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN).

