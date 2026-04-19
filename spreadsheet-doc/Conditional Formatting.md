# Conditional Formatting User Guide

## Scenarios

Conditional formatting is used to change the appearance of a cell based on specified conditions.

## Supported APIs

Conditional formatting currently uses 4 APIs. You can set up to 20 conditional formats for a single sheet.

1. [Get conditional formatting](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/conditionformat/condition-format-get): Obtains detailed conditional formatting information for a sheet. One operation can obtain information for up to 10 sheets.
2. [Create conditional formatting](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/conditionformat/condition-format-set): Batch sets conditional formatting. One operation can set up to 10 conditional formats.
3. [Update conditional formatting](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/conditionformat/condition-format-update): Batch updates conditional formatting. One operation can update up to 10 conditional formats.
4. [Delete conditional formatting](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/conditionformat/condition-format-delete): Deletes conditional formatting. One operation can delete up to 10 conditional formats.

## Conditional formatting restrictions

### **ranges**

The following five types of application scopes are supported:

1. sheetId: Indicates a whole sheet
2. sheetId!1:2: Indicates a whole row
3. sheetId!A:B: Indicates a whole column
4. sheetId!A1:B2: Indicates a normal range
5. sheetId!A1:C: Omits the end row to extend the range to the last row of the sheet

### **style**

The following style parameters are supported and all are optional and are not set if no value is provided. However, a style must have at least one set parameter.

1. font: bold, type: bool; italic, type: bool
2. text_decoration: type: int, values: 0: default, 1: underline, 2: strikethrough, 3: underline and strikethrough
3. fore_color: The text color, type: string
4. back_color: The background color, type: string

### **rule_type & attrs**

- rule_type, seven types in total. Four types do not require attrs parameters: ***containsBlanks (contains blanks), notContainsBlanks (does not contain blanks), duplicateValues (duplicate values), and uniqueValues (unique values)***. Three types are restricted by attrs parameters as described below: ***cellIs (limited value range), containsText (contains text content), and timePeriod (dates)***.
  - formula: string array, only required when rule_type is ***cellIs***. Two elements must be specified when operator is between or notBetween. Otherwise, one element is required. Values are specified by the user and can be numeric (**"1"**) or text (**"\"a\""**).
  - text: string, only required when rule_type is ***containsText***. Values are specified by the user.
  - timeperiod: string, only required when rule_type is ***timePeriod***. The operator must be "is", and the time_period field can be yesterday, today, tomorrow, or last7Days.
- The user can enter content of up to 1,000 characters.
- attrs parameter array, only one parameter is required in the array.

***Three rule_types are restricted by attrs parameters as follows:***

***cellIs (limited value range)***

In attrs parameter, formula is an array. Here, formula1 and formula2 indicate elements in the formula array.

| operator           | formula1 | formula2 | Remarks          |
| ------------------ | -------- | -------- | ----------- |
| equal              | Required       |          | Limited value range: is equal to    |
| notEqual              | Required       |          | Limited value range: not equal to    |
| greaterThan              | Required       |          | Limited value range: greater than    |
| greaterThanOrEqual              | Required       |          | Limited value range: greater than or equal to    |
| lessThan              | Required       |          | Limited value range: less than    |
| lessThanOrEqual              | Required       |          | Limited value range: less than or equal to    |
| between              | Required       |          | Limited value range: is between    |
| notBetween              | Required       |          | Limited value range: is not between    |
```json
{
  "condition_format": {
    "rule_type": "cellIs",
    "attrs": [
      {
        "operator": "equal",
        "formula": [
              "\"aaaaa\""  //Text must be enclosed in quotation marks ("")
        ]
      }
    ]
  },
  "condition_format": {
    "rule_type": "cellIs",
    "attrs": [
      {
        "operator": "between",
        "formula": [
              "1",
              "10"
        ]
      }
    ]
  }
}
```
***containsText (contains text content)***

| operator     | text | Remarks           |
| ------------ | ---- | ------------ |
| containsText | Required   | Contains the following content: text contains  |
| notContains | Required   | Contains the following content: text does not contain  |
| is | Required   | Contains the following content: text is  |
| beginsWith | Required   | Contains the following content: begins with |
| endsWith | Required   | Contains the following content: ends with  |
```json
{
  "condition_format": {
    "rule_type": "containsText",
    "attrs": [
      {
        "operator": "is",
        "text": "******"
      }
    ]
  }
}
```
***timePeriod (dates)***

| operator | timePeriod | Remarks       |
| -------- | ---------- | -------- |
| is       | yesterday  | Date is: yesterday   |
| is       | today  | Date is: today   |
| is       | tomorrow   | Date is: tomorrow   |
| Is       | last7Days  | Date is: within the last 7 days |
```json
{
  "condition_format": {
    "rule_type": "timePeriod",
    "attrs": [
      {
        "operator": "is",
        "time_period": "today"
      }
    ]
  }
}
```

# Create conditional formatting

Use this API to create new conditional formatting. Each conditional formatting setting operation returns success or failed. Parameter verification information is returned for failed operations.

## Usage limits

- A maximum of 10 conditional formats can be created per API call.
- A maximum of 20 conditional formats can be created in a single sheet.
## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/condition_formats/batch_create
HTTP Method | POST
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
spreadsheet_token | string | Spreadsheet token. Learn more in [Spreadsheet Overview](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview).<br>- Spreadsheet URL: https://sample.feishu.cn/sheets/==Iow7sNNEphp3WbtnbCscPqabcef==<br>- Call [List Files in Folder](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file/list)<br>**Example**: "Iow7sNNEphp3WbtnbCscPqabcef"

### Request body
| Parameter                            |Type|Required| Description                                       |
| ----------------------------- |-----|----| ---------------------------------------- |
|sheet_condition_formats|array<interface>|Yes|Spreadsheet conditional formatting information|
|&emsp;∟sheet_id                      |string|Yes|id                                  of  sheet|
|&emsp;∟condition_format              ||Yes| Detailed information for a conditional formatting                              |
|&emsp;&emsp;∟ranges                 |array<string>| | Conditional formatting application scope, supported values: sheetId (for a whole sheet); sheetId!1:2 (for a whole row); sheetId!A:B (for a whole column); sheetId!A1:B2 (for a normal range); sheetId!A1:C (apply to the last row). The application scope cannot exceed the total rows and columns of a spreadsheet, and the sheetId must be consistent with the sheetId in the parameters.|
&emsp;&emsp;∟rule_type              |string| Yes| Conditional formatting rule type, supports seven rule types: ***containsBlanks (contains blanks), notContainsBlanks (does not contain blanks), duplicateValues (duplicate values), uniqueValues (unique values), cellIs (limited value range), containsText (contains text content), timePeriod (dates)***                                 |
|&emsp;&emsp;∟attrs                  || Yes|Specific property information for the corresponding rule_type, see [Conditional Formatting User Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/conditionformat/condition-format-guide) for details|
|&emsp;&emsp;&emsp;∟operator|string| No|Operational approach|
|&emsp;&emsp;&emsp;∟time_period|string| No|Time range|
|&emsp;&emsp;&emsp;∟formula|array<string>| No|Format|
|&emsp;&emsp;&emsp;∟text|string| No|Text|
|&emsp;&emsp;∟style                  ||No| Conditional formatting style, only supports the following styles. Style parameters are all optional, but you cannot set an empty style .|
|&emsp;&emsp; &emsp;∟font            || No| Font style                                     |
|&emsp;&emsp; &emsp;&emsp;∟bold     |bool| No| Bold                                       |
|&emsp;&emsp;&emsp; &emsp;∟italic   |bool| No| Italics                                       |
|&emsp;&emsp; &emsp;∟text_decoration |int| No| Text decoration , 0: default, 1: underline, 2: strikethrough , 3: underline and strikethrough        |
|&emsp;&emsp; &emsp;∟fore_color      |string| No| Text color                                     |
|&emsp;&emsp; &emsp;∟back_color      |string| No| Background color                                     |

### Request body example

```json
{
    "sheet_condition_formats": [
        {
            "sheet_id": "40a7b0",
            "condition_format": {
                "ranges": [
                    "40a7b0!C3:C3"
                ],
                "rule_type": "timePeriod",
                "attrs": [
                    {
                        "operator": "is",
                        "time_period": "today", //Required when rule_type is timePeriod.
                        "formula": [], //Required when rule_type is cellIs.
                        "text": "" //Required when rule_type is containsText.
                    }
                ],
                "style": {
                    "font": {
                        "bold": true,
                        "italic": true
                    },
                    "fore_color": "#faf1d1",
                    "back_color": "#d9f5d6",
                    "text_decoration": 3
                }
            }
        }
    ]
}
```
###  cURL Request example
```bash
curl --location --request POST 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/shtcngNygNfuqhxTBf588jwgWbJ/condition_formats/batch_create' \
--header 'Authorization: Bearer t-e346617a4acfc3a11d4ed24dca0d0c0fc8e0067e' \
--header 'Content-Type: application/json' \
--data-raw '{
    "sheet_condition_formats": [
        {
            "sheet_id": "Q7PlXT",
            "condition_format": {
                "ranges": [
                    "Q7PlXT!C3:D9"
                ],
                "rule_type": "uniqueValues",
                "style": {
                    "font": {
                        "bold": true,
                        "italic": true
                    },
                    "fore_color": "#faf1d1",
                    "back_color": "#d9f5d6",
                    "text_decoration": 3
                }
            }
        }
    ]
}'
```
## Response
### Response body
| Parameter       | Type|Description                           |
| -------- |-----| ---------------------------- |
|responses|array<interface>|Response|
| &emsp;∟sheet_id |string | Sheet ID                     |
| &emsp;∟cf_id    |string| Successfully set conditional formatting id                  |
| &emsp;∟res_code |int| Conditional formatting setting status code, 0 indicates success and a non-0 value indicates failure       |
| &emsp;∟res_msg  |string| Status information returned for conditional formatting settings, empty indicates success and any content indicates the cause of failure |

#### res_code description

res_code | res_msg | Description
---|---|---
90230 | unknown rule_type | `rule_type` parameter error. The spreadsheet supports the following rule types:<br>- containsBlanks: Blank<br>- notContainsBlanks: Not blank<br>- duplicateValues: Duplicate values<br>- uniqueValues: Unique values<br>- cellIs: Specific value range<br>- containsText: Contains content<br>- timePeriod: Date<br>Refer to [rule_type and attributes attrs](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/conditionformat/condition-format-guide#6de1dc32) to learn how to choose and fill in `rule_type`.

### Response body example

```json
{
    "code": 0,
    "msg": "Success",
    "data": {
        "responses": [
            {
                "cf_id": "1gJelvenW9",
                "res_code": 0,
                "res_msg": "success",
                "sheet_id": "40a7b0"
            }
        ]
    }
}
```

### Error code

For details, refer to [Server-side error codes](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN).

# Update conditional formatting

Use this API to update an existing conditional formatting. You can update up to 10 conditional formats at once. Each conditional formatting update operation returns success or failed. Parameter verification information is returned for failed operations.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/condition_formats/batch_update
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
| spreadsheetToken  |string| Yes   | Token of the sheet, to obtain the token see the [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview) | 
### Request body
| Parameter                            |Type|Required| Description                                       |
| ----------------------------- |-----|----| ---------------------------------------- |
|sheet_condition_formats||Yes|Spreadsheet conditional formatting information|
| &emsp;∟sheet_id                      |string|Yes| Sheet ID                                 |
| &emsp;∟condition_format              ||Yes| Detailed information for a conditional formatting                              |
| &emsp;&emsp;∟cf_id                  |string|Yes|ID of the conditional formatting to update, the system checks that this ID actually exists                    |
| &emsp;&emsp;∟ranges                 |array<string>| Yes| Conditional formatting application scope, supported values: sheetId (for a whole sheet); sheetId!1:2 (for a whole row); sheetId!A:B (for a whole column); sheetId!A1:B2 (for a normal range); sheetId!A1:C (apply to the last row). The application scope cannot exceed the total rows and columns of a spreadsheet, and the sheetId must be consistent with the sheetId in the parameters. |
| &emsp;&emsp;∟rule_type              |string|Yes|Conditional formatting rule type, supports seven rule types: ***containsBlanks (contains blanks), notContainsBlanks (does not contain blanks), duplicateValues (duplicate values), uniqueValues (unique values), cellIs (limited value range), containsText (contains text content), timePeriod (dates)***                                 |
| &emsp;&emsp;∟attrs                  || Yes| Specific property information for the corresponding rule_type, see  [Conditional Formatting Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/conditionformat/condition-format-guide)  for details|
|&emsp;&emsp;&emsp;∟operator|string| No|Operational approach|
|&emsp;&emsp;&emsp;∟time_period|string| No|Time range|
|&emsp;&emsp;&emsp;∟formula|array<string>| No|Format|
|&emsp;&emsp;&emsp;∟text|string| No|Text|
| &emsp;&emsp;∟style                  ||No| Conditional formatting style, only supports the following styles. Style parameters are all optional, but you cannot set an empty style.|
| &emsp;&emsp; &emsp;∟font            || No| Font style                                     |
| &emsp;&emsp; &emsp; &emsp;∟bold     |bool| No| Bold                                       |
| &emsp;&emsp; &emsp; &emsp;∟italic   |bool| No| Italics                                       |
| &emsp;&emsp; &emsp;∟text_decoration |int|No|Text decoration, 0: default, 1: underline, 2: strikethrough, 3 , : underline and strikethrough        |
| &emsp;&emsp; &emsp;∟fore_color      |string| No| Text color                                     |
| &emsp;&emsp; &emsp;∟back_color      |string| No| Background color                                     |

### Request body example

```json
{
    "sheet_condition_formats": [
        {
            "sheet_id": "40a7b0",
            "condition_format": {
                "cf_id": "r9sYuhgAl6",
                "rule_type": "timePeriod",
                "attrs": [
                    {
                        "operator": "is",
                        "time_period": "today", //Required when ruleType is timePeriod
                        "formula": [], //Required when ruleType is cellIs
                        "text": "" //Required when ruleType is containsText
                    }
                ],
                "ranges": [
                    "40a7b0!C3:C3"
                ],
                "style": {
                    "font": {
                        "bold": true,
                        "italic": true
                    },
                    "fore_color": "#faf1d1",
                    "back_color": "#d9f5d6",
                    "text_decoration": 3
                }
            }
        }
    ]
}
```
###  cURL Request example
```
curl --location --request POST 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/shtcngNygNfuqhxTBf588jwgWbJ/condition_formats/batch_update' \
--header 'Authorization: Bearer t-e346617a4acfc3a11d4ed24dca0d0c0fc8e0067e' \
--header 'Content-Type: application/json' \
--data-raw '{
    "sheet_condition_formats": [
        {
            "sheet_id": "Q7PlXT",
            "condition_format": {
                "cf_id": "BlG0MpOkHn",
                "rule_type": "uniqueValues",
                "ranges": [
                    "Q7PlXT!C3:D9"
                ],
                "style": {
                    "font": {
                        "bold": true,
                        "italic": true
                    },
                    "fore_color": "#faf1f2",
                    "back_color": "#46f5d6",
                    "text_decoration": 2
                }
            }
        }
    ]
}'
```
## Response
### Response body
| Parameter       |Type| Description                           |
| -------- |-----| ---------------------------- |
|responses|array<interface>|Response|
| &emsp;∟sheet_id |string |Sheet ID                     |
| &emsp;∟cf_id    |string| ID                     of the conditional formatting to update|
| &emsp;∟res_code |int| Conditional formatting update status code, 0 indicates success and a non-0 value indicates failure       |
| &emsp;∟res_msg  |string| Status information returned for conditional formatting update, empty indicates success and any content indicates the cause of failure |

### Response body example

```json
{
    "code": 0,
    "msg": "Success",
    "data": {
        "responses": [
            {
                "cf_id": "1gJelvenW9",
                "res_code": 0,
                "res_msg": "success",
                "sheet_id": "40a7b0"
            }
        ]
    }
}
```
### Error code

For details, refer to [Server-side error codes](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN).

# Get conditional formatting

Use this API to get detailed conditional formatting based on a sheetId. Each operation can query up to 10 sheetIds.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/condition_formats
HTTP Method | GET
Supported app types | Custom App、Store App
Required scopes<br>**The scopes required to call this API. You can call the API with any of the scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space(drive:drive)<br>View, comment, and download all files in My Space(drive:drive:readonly)<br>View, comment, edit, and manage Sheets(sheets:spreadsheet)<br>View, comment, and export Sheets(sheets:spreadsheet:readonly)

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
| sheet_ids       |array<string>|Yes   | Sheet ID, can be obtained through the [Obtain sheet metadata](https://open.larkoffice.com/document/ukTMukTMukTM/uETMzUjLxEzM14SMxMTN) API, separate multiple IDs with commas, for example: xxxID1,xxxID2 | 
###  cURL Request example
```
curl --location --request GET 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/shtcngNygNfuqhxTBf588jwgWbJ/condition_formats?sheet_ids=Q7PlXT' \
--header 'Authorization: Bearer t-e346617a4acfc3a11d4ed24dca0d0c0fc8e0067e' \
```
## Response  
### Response body
| Parameter                            |Type| Description                                       |
| ----------------------------- |-----| ---------------------------------------- |
|sheet_condition_formats|array<interface>|Spreadsheet conditional formatting information|
| &emsp;∟sheet_id                      |string|Sheet ID                                 |
| &emsp;∟condition_format              || Detailed information for a conditional formatting                              |
| &emsp;&emsp;∟cf_id                  |string| Conditional formatting ID                                  |
| &emsp;&emsp;∟ranges                 |array<string>| Conditional formatting application scope, supported values: sheetId (for a whole sheet); sheetId!1:2 (for a whole row); sheetId!A:B (for a whole column); sheetId!A1:B2 (for a normal range); sheetId!A1:C (apply to the last row). The application scope cannot exceed the total rows and columns of a spreadsheet, and the sheetId must be consistent with the sheetId in the parameters. |
| &emsp;&emsp;∟rule_type              |string| Conditional formatting rule type, supports seven rule types: ***containsBlanks (contains blanks), notContainsBlanks (does not contain blanks), duplicateValues (duplicate values), uniqueValues (unique values), cellIs (limited value range), containsText (contains text content), timePeriod (dates)***                                  |
| &emsp;&emsp;∟attrs                  ||Specific property information for the corresponding rule_type, see [Conditional Formatting User Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/conditionformat/condition-format-guide)                         for details|
| &emsp;&emsp;∟style                  || Conditional formatting style, only supports the following styles                           |
| &emsp;&emsp; &emsp;∟font            || Font style                                     |
| &emsp;&emsp;  &emsp;&emsp; ∟bold     |bool| Bold                                       |
| &emsp;&emsp; &emsp; &emsp;∟italic   |bool| Italics                                       |
| &emsp;&emsp; &emsp;∟text_decoration |int| Text decoration,  0: default, 1: underline, 2: strikethrough , 3: underline and strikethrough        |
| &emsp;&emsp; &emsp;∟fore_color      |string| Text color                                     |
| &emsp;&emsp; &emsp;∟back_color      |string| Background color                                     |
### Response body example

```json
{
    "code": 0,
    "msg": "Success"，
    "data": {
        "sheet_condition_formats": [
            {
                "condition_format": {
                    "cf_id": "r9sYuhgAl6",
                    "ranges": [
                        "uEnW3A!C4:C4"
                    ],
                    "rule_type": "timePeriod",
                    "attrs": [
                        {
                            "operator": "is",
                            "time_period": "today"
                        }
                    ],
                    "style": {
                        "back_color": "#d9f5d6",
                        "font": {
                            "bold": true,
                            "italic": false
                        },
                        "fore_color": "#faf1d1",
                        "text_decoration": 3
                    }
                },
                "sheet_id": "uEnW3A"
            }
        ]
    }
}
```
### Error code

For details, refer to [Server-side error codes](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN).

# Delete conditional formatting

Use this API to delete an existing conditional formatting. You can delete up to 10 conditional formats at once. Each conditional formatting deletion operation returns success or failed. Parameter verification information is returned for failed operations.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/condition_formats/batch_delete
HTTP Method | DELETE
Supported app types | Custom App、Store App
Required scopes<br>**The scopes required to call this API. You can call the API with any of the scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space(drive:drive)<br>View, comment, edit, and manage Sheets(sheets:spreadsheet)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `user_access_token`  or  `tenant_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[Learn more about how to obtain and use access_token](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Path parameters
| Parameter             | Type          | Required | Description&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;                           |
| ---------------- | ------------- | ---- | ------------------------------------------------------------ | 
| spreadsheetToken | string        | Yes   | token of the  sheet , to obtain the token see the [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)|
### Request body
| Parameter       |Type| Description       |
| -------- |-----| -------- |
|sheet_cf_ids| |Spreadsheet conditional formatting ID|
| &emsp;∟sheet_id |string| sheet ID |
| &emsp;∟cf_id    |string| Conditional formatting ID   |
### Request body example
```json
{
    "sheet_cf_ids": [
        {
            "sheet_id": "40a7b0",
            "cf_id": "6hP6Dj6gsd"
        }
    ]
}
```
###  cURL Request example
```
curl --location --request DELETE 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/shtcngNygNfuqhxTBf588jwgWbJ/condition_formats/batch_delete' \
--header 'Authorization: Bearer t-e346617a4acfc3a11d4ed24dca0d0c0fc8e0067e' \
--header 'Content-Type: application/json' \
--data-raw '{
    "sheet_cf_ids": [
        {
            "sheet_id": "Q7PlXT",
            "cf_id": "KjRm0JyS1P"
        }
    ]
}'
```
## Response
### Response body
| Parameter       |Type| Description                           |
| -------- |-----| ---------------------------- |
|responses|array<interface>|Response|
| &emsp;∟sheet_id |string | sheet ID                     |
| &emsp;∟cf_id    |string| Conditional formatting ID                       |
| &emsp;∟res_code |int| Conditional formatting deletion status code, 0 indicates success and a non-0 value indicates failure       |
| &emsp;∟res_msg  |string| Status information returned for conditional formatting deletion, empty indicates success and any content indicates the cause of failure |
### Response body example
```json
{
    "code": 0,
    "data": {
        "responses": [
            {
                "cf_id": "6hP6Dj6gsd",
                "res_code": 555554047,
                "res_msg": "cfId not exist",
                "sheet_id": "40a7b0"
            }
        ]
    },
    "msg": "Success"
}
```
### Error code

For details, refer to [Server-side error codes](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN).

