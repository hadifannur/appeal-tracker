# Filtering guide

Filtering refers to setting filtering conditions for specified columns within a range on a spreadsheet worksheet. This document introduces parameters and a method list related to filtering capabilities in Feishu Open Platform spreadsheets.

## Notes

- The first row within the filtering range is not included in the filter.
- Only one filtering range can be specified per worksheet.

## Filtering parameters

This section introduces the main parameters involved in filtering and their descriptions.

### Range parameter

The range parameter specifies the application scope of the filter. It supports five formats:
- sheetId: Specify the actual sheet ID to apply the filter to the entire sheet. Example: `8fe9d6`.
- sheetId!1:2: Specify the sheet ID and a range of rows to apply the filter to entire rows. Example: `8fe9d6!1:2`.
- sheetId!A:B: Specify the sheet ID and a range of columns to apply the filter to entire columns. Example: `8fe9d6!A:B`.
- sheetId!A1:B2: Specify the sheet ID and a range of cells to apply the filter to a selected area of cells. Example: `8fe9d6!A1:B2`.
- sheetId!A1:C: Specify the sheet ID, starting cell, and ending column to apply the filter up to the last row of the table. Example: `8fe9d6!A1:C`.

### Filter types

This subsection describes the main filter types and their usage.

#### Multi-Value Filtering

Multi-value filtering targets specific values. When the filter type is multiValue:
- compare_type: Not applicable
- expected: Values to display, array type with length greater than 0 and less than the number of rows in the filter range. Each value's character length must not exceed 50,000.
    ```json
    {
      "condition": {
        "filter_type": "multiValue",
        "expected": ["100", "200", "300"]
      }
    }
    ```

#### Number Filtering

Number filtering targets data that meets specific numeric conditions. When the filter type is number, compare_type parameters and their expected constraints are listed in the following table:
| compare_type enum | Description | expected array length limit |
| --------------- | ---- | --------------- |
| equal | Equals | 1 |
| notEqual | Not equal to | 1 |
| greater | Greater than | 1 |
| greaterOrEqual | Greater than or equal to | 1 |
| less | Less than | 1 |
| lessOrEqual | Less than or equal to | 1 |
| between | Between | 2 |
| notBetween | Not between | 2 |
```json
{
  "condition": {
    "filter_type": "number",
    "compare_type": "equal",
    "expected": ["100"]
  },
  "condition": {
    "filter_type": "number",
    "compare_type": "between",
    "expected": ["100", "200"]
  }
}
```

#### Text Filtering

Text filtering refers to filtering data that meets specific text conditions. When the filter type is text:

- expected: Text characters. Array type, array length is 1. The length of the text characters must not exceed 1,000.
- The compare_type parameter enums are as follows:

| compare_type Enum | Description |
    | ----------------- | ----------- |
    | beginsWith        | Begins with |
    | notBeginsWith     | Does not begin with |
    | endsWith          | Ends with |
    | notEndsWith       | Does not end with |
    | contains          | Contains |

```json
{
  "condition": {
    "filter_type": "text",
    "compare_type": "contains",
    "expected": ["Done"]
  }
}
```

#### Color Filtering

Color filtering refers to filtering data that has specific color attributes. When the filter type is color:

- expected: The hexadecimal code of the color, such as ["#ffffff"]. Array type, array length is 1.
- The compare_type parameter enums are as follows:

| compare_type Enum | Description  |
    | ----------------- | ------------ |
    | backColor         | Cell color   |
    | foreColor         | Font color   |

```json
{
  "condition": {
    "filter_type": "color",
    "compare_type": "backColor",
    "expected": ["#ffffff"]
  }
}
```

#### Clear All Filters

Clears the filter criteria of a specific column. Both compare_type and expected do not need to be filled in.

```json
{
  "condition": {
    "filter_type": "clear",
  }
}
```

## Method list

Below is the method list for spreadsheet filtering. Here, "Store" represents applications from app stores; "Self-built" represents enterprise-built applications. For more information about application types, refer to [Application Types Introduction](https://open.larkoffice.com/document/home/app-types-introduction/overview). To understand the process of calling server APIs, refer to [Process Overview](https://open.larkoffice.com/document/uMzNwEjLzcDMx4yM3ATM/ugzNwEjL4cDMx4CO3ATM).

**Method (API)** | **Permission Requirements (any)** | **Access Tokens** | **Store** | **Self-built**
---|---|---|---|---
`POST` [Create Filter](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet-filter/create) /open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/filter | View, comment, edit, and manage all files in cloud storage(drive:drive)<br>View, comment, edit, and manage spreadsheets(sheets:spreadsheet) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**
`PUT` [Update Filter](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet-filter/update) /open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/filter | View, comment, edit, and manage all files in cloud storage(drive:drive)<br>View, comment, edit, and manage spreadsheets(sheets:spreadsheet) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**
`GET` [Get Filter](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet-filter/get) /open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/filter | View, comment, edit, and manage all files in cloud storage(drive:drive)<br>View, comment, and download all files in cloud storage(drive:drive:readonly)<br>View, comment, edit, and manage spreadsheets(sheets:spreadsheet)<br>View, comment, and export spreadsheets(sheets:spreadsheet:readonly) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**
`DELETE` [Delete Filter](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet-filter/delete) /open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/filter | View, comment, edit, and manage all files in cloud storage(drive:drive)<br>View, comment, edit, and manage spreadsheets(sheets:spreadsheet) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**

# Create a filter
For parameter values, see [Filter guide](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet-filter/filter-user-guide)
This API is used to create a filter in a sheet.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/filter
HTTP Method | POST
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
spreadsheet_token | string | Spreadsheet token<br>**Example value**: "shtcnmBA\*****yGehy8"
sheet_id | string | Sheet ID<br>**Example value**: "0b\**12"

### Request body

Parameter | Type | Required | Description
---|---|---|---
range | string | Yes | Range<br>**Example value**: "xxxxxx!C1:H14"
col | string | Yes | Column with set filter conditions<br>**Example value**: "E"
condition | condition | Yes | Filter conditions
filter_type | string | Yes | Filter type<br>**Example value**: "number"
compare_type | string | No | Comparison type<br>**Example value**: "less"
expected | string\[\] | Yes | Filter parameter<br>**Example value**: ["6"]

### Request body example
```json
{
    "range": "xxxxxx!C1:H14",
    "col": "E",
    "condition": {
        "filter_type": "number",
        "compare_type": "less",
        "expected": [
            "6"
        ]
    }
}
```

```
curl --location --request POST 'https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/shtcnSUVpFeJ7Q2yVN9/sheets/6e2914/filter' \
--header 'Authorization: Bearer t-70f073c1e09bf61ae4da4272d70dae02c345e620' \
--header 'Content-Type: application/json' \
--data-raw '{

"range": "6e2914!C1:H14",
    "col": "E",
    "condition": {
        "filter_type": "number",
        "compare_type": "less",
        "expected": ["6"]
    }
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
200 | 1310234 | Marshal Error | Internal service error. For more information, contact support.
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
400 | 1310235 | Retry Later | Please try again later.
400 | 1310236 | Wrong Filter Value | Check the filter conditions.
400 | 1310215 | Sheet Id Not Found | Check the sheet_id.
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.
400 | 1310218 | Locked Cell | Check if the action targets a protected range.
400 | 1310213 | Permission Fail | No permission
400 | 1310206 | Empty Sheet Id | Check the sheet_id
400 | 1310229 | Wrong URL Param | Check the url parameter.
400 | 1310211 | Wrong Sheet Id | Check the sheet_id.
400 | 1310242 | In Mix state | Retey Later
400 | 1310203 | Fail | Request failed
400 | 1310202 | Wrong Range | Invalid range
400 | 1310249 | Spreadsheet Deleted | Restore the form and try again

# Update a filter
For parameter values, see [Filter guide](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet-filter/filter-user-guide)
This API is used to update column filter conditions in the sheet range.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/filter
HTTP Method | PUT
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
spreadsheet_token | string | Spreadsheet token<br>**Example value**: "shtcnmBA\*****yGehy8"
sheet_id | string | Sheet ID<br>**Example value**: "0b\**12"

### Request body

Parameter | Type | Required | Description
---|---|---|---
col | string | Yes | Column with updated filter conditions<br>**Example value**: "E"
condition | condition | Yes | Filter conditions
filter_type | string | Yes | Filter type<br>**Example value**: "number"
compare_type | string | No | Comparison type<br>**Example value**: "less"
expected | string\[\] | Yes | Filter parameter<br>**Example value**: ["6"]

### Request body example
```json
{
    "col": "E",
    "condition": {
        "filter_type": "number",
        "compare_type": "less",
        "expected": [
            "6"
        ]
    }
}
```

```
curl --location --request PUT 'https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/shtcnSUVpFeJ7Q2yVN9/sheets/6e2914/filter' \
--header 'Authorization: Bearer t-719d578dc63f6bd37e30cdb0394798a709070fec' \
--header 'Content-Type: application/json' \
--data-raw '{
    "col": "G",
    "condition": {
        "filter_type": "text",
        "compare_type": "beginsWith",
        "expected": ["a"]
    }
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
200 | 1310234 | Marshal Error | Internal service error. For more information, contact support.
400 | 1310235 | Retry Later | Please try again later.
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
400 | 1310226 | Excess Limit | Exceeds the limit
400 | 1310215 | Sheet Id Not Found | Check the sheet_id.
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.
400 | 1310218 | Locked Cell | Check if the action targets a protected range.
400 | 1310213 | Permission Fail | No permission
400 | 1310206 | Empty Sheet Id | Check the sheet_id
400 | 1310229 | Wrong URL Param | Check the url parameter.
400 | 1310202 | Wrong Range | Invalid range
400 | 1310236 | Wrong Filter Value | Check the filter conditions.
400 | 1310211 | Wrong Sheet Id | Check the sheet_id.
400 | 1310242 | In Mix state | Retey Later
400 | 1310249 | Spreadsheet Deleted | Restore the form and try again

# Obtain filter

This API is used to obtain the filter details for a sheet.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/filter
HTTP Method | GET
Rate Limit | [100 per minute](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space(drive:drive)<br>View, comment, and download all files in My Space(drive:drive:readonly)<br>View, comment, edit, and manage Sheets(sheets:spreadsheet)<br>View, comment, and export Sheets(sheets:spreadsheet:readonly)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)

### Path parameters

Parameter | Type | Description
---|---|---
spreadsheet_token | string | Spreadsheet token<br>**Example value**: "shtcnmBA\*****yGehy8"
sheet_id | string | Sheet ID<br>**Example value**: "0b\**12"

```
curl --location --request GET 'https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/shtcnSUVpFeJ7QyVN9G1cHSc/sheets/6e2914/filter' \
--header 'Authorization: Bearer t-3bf3d4463b8f1956f14240c2517aa8ba2c93d8ec' \
--header 'Content-Type: application/json'
```

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
sheet_filter_info | sheet_filter_info | Filter information
range | string | Range
filtered_out_rows | int\[\] | Rows that are filtered out and hidden
filter_infos | filter_info\[\] | Sheet filter conditions
col | string | Columns with set filter conditions
conditions | condition\[\] | Filter conditions
filter_type | string | Filter type
compare_type | string | Comparison type
expected | string\[\] | Filter parameter

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "sheet_filter_info": {
            "range": "xxxxxx!A1:H14",
            "filtered_out_rows": [
                4
            ],
            "filter_infos": [
                {
                    "col": "E",
                    "conditions": [
                        {
                            "filter_type": "number",
                            "compare_type": "less",
                            "expected": [
                                "6"
                            ]
                        }
                    ]
                }
            ]
        }
    }
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
400 | 1310213 | Permission Fail | No permission
400 | 1310215 | Sheet Id Not Found | Check the sheet_id.
400 | 1310229 | Wrong URL Param | Check the url parameter.
400 | 1310226 | Excess Limit | Exceeds the limit
400 | 1310217 | Too Many Request | Check if requests have been sent too frequently.
400 | 1310235 | Retry Later | Please try again later.
400 | 1310242 | In Mix state | Retey Later
400 | 1310249 | Spreadsheet Deleted | Restore the form and try again

# Delete a filter

This API is used to delete the filter of a sheet.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/filter
HTTP Method | DELETE
Rate Limit | [100 per minute](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space(drive:drive)<br>View, comment, edit, and manage Sheets(sheets:spreadsheet)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)

### Path parameters

Parameter | Type | Description
---|---|---
spreadsheet_token | string | Spreadsheet token<br>**Example value**: "shtcnmBA\*****yGehy8"
sheet_id | string | Sheet ID<br>**Example value**: "0b\**12"

```
curl --location --request DELETE 'https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/shtcnSUVpFeJ7Q2yVN/sheets/6e2914/filter' \
--header 'Authorization: Bearer t-70f073c1e09bf61ae4da4272d70dae02c345e620' \
--header 'Content-Type: application/json'
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
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
400 | 1310235 | Retry Later | Please try again later.
400 | 1310217 | Too Many Request | Check if requests have been sent too frequently.
400 | 1310218 | Locked Cell | Check if the action targets a protected range.
400 | 1310206 | Empty Sheet Id | Check the sheet_id
400 | 1310229 | Wrong URL Param | Check the url parameter.
400 | 1310211 | Wrong Sheet Id | Check the sheet_id.
400 | 1310242 | In Mix state | Retey Later
400 | 1310213 | Permission Fail | No permission
400 | 1310215 | Sheet Id Not Found | Check the sheet_id.
400 | 1310249 | Spreadsheet Deleted | Restore the form and try again
400 | 1310236 | Wrong Filter Value | Check the filter conditions.
