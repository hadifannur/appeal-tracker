# Create filter view
For range settings, see: [User guide for using filter conditions in the filter view](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet-filter_view-condition/filter-view-condition-user-guide)
This API is used to create a filter view based on passed in parameters. The ID and name fields are optional and default values are generated if none are provided. The range field is required. IDs are 10 characters long and composed of numbers and upper and lowercase English letters. Names can't exceed 100 characters. A single sheet can have up to 150 filter views.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/filter_views
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
spreadsheet_token | string | Spreadsheet token<br>**Example value**: "shtcnmBA*****yGehy8"
sheet_id | string | Sheet ID<br>**Example value**: "0b**12"

### Request body

Parameter | Type | Required | Description
---|---|---|---
filter_view_id | string | No | Filter view ID<br>**Example value**: "pH9hbVcCXA"
filter_view_name | string | No | Filter view name<br>**Example value**: "Filter view 1"
range | string | No | Filter view range<br>**Example value**: "0b**12!C1:H14"

### Request body example
```json
{
    "filter_view_id": "pH9hbVcCXA",
    "filter_view_name": "Filter view 1",
    "range": "0b**12!C1:H14"
}
```

```
curl --location --request POST 'https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/shtcnspY6YDVPxWjhG09Qxxxxxx/sheets/phwh0X/filter_views' \
--header 'Authorization: Bearer t-2602ac1d050a2a308ab8a98639d25cbaaaf26c9f' \
--header 'Content-Type: application/json' \
--data-raw '{

"range": "phwh0X!C1:H14"
}'
```

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
filter_view | filter_view | ID, name, and range of the created filter view
filter_view_id | string | Filter view ID
filter_view_name | string | Filter view name
range | string | Filter view range

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "filter_view": {
            "filter_view_id": "pH9hbVcCXA",
            "filter_view_name": "Filter view 1",
            "range": "0b**12!C1:H14"
        }
    }
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
400 | 1310217 | Too Many Request | Check if requests have been sent too frequently.
400 | 1310235 | Retry Later | Please try again later.
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.
400 | 1310215 | Sheet Id Not Found | Check the sheet_id.
400 | 1310223 | Col Id Not Found | Column ID not found. It may have been entered incorrectly or exceed the spreadsheet's column range.
400 | 1310213 | Permission Fail | No permission
400 | 1310204 | Wrong Request Body | Check the request body parameter.
400 | 1310229 | Wrong URL Param | Check the url parameter.
400 | 1310202 | Wrong Range | Invalid range
400 | 1310226 | Excess Limit | Exceeds the limit
400 | 1310211 | Wrong Sheet Id | Check the sheet_id.
400 | 1310232 | Wrong Style | Invalid style, such as color or font
400 | 1310218 | Locked Cell | Check if the action targets a protected range.
400 | 1310237 | Wrong Filter View Id | Invalid filter view ID
400 | 1310238 | Exist Filter View Id | This filter view ID already exists.
400 | 1310239 | Wrong Filter View Name | Invalid filter view name
400 | 1310240 | Exist Filter View Name | This filter view name already exists.
400 | 1310241 | Filter View Excess | The number of filter views exceeds the limit.
400 | 1310242 | In Mix state | Retey Later
400 | 1310249 | Spreadsheet Deleted | Restore the form and try again

# Update filter view
For range settings, see: [User guide for using filter conditions in the filter view](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet-filter_view-condition/filter-view-condition-user-guide)
This API is used to update the filter view name or range. The name can't exceed 100 characters and must be unique within the sheet. The range can't exceed the maximum range of the sheet.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/filter_views/:filter_view_id
HTTP Method | PATCH
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
spreadsheet_token | string | Spreadsheet token<br>**Example value**: "shtcnmBA*****yGehy8"
sheet_id | string | Sheet ID<br>**Example value**: "0b**12"
filter_view_id | string | Filter view ID<br>**Example value**: "pH9hbVcCXA"

### Request body

Parameter | Type | Required | Description
---|---|---|---
filter_view_name | string | No | Filter view name<br>**Example value**: "Filter view 1"
range | string | No | Filter view range<br>**Example value**: "0b**12!C1:H14"

### Request body example
```json
{
    "filter_view_name": "Filter view 1",
    "range": "0b**12!C1:H14"
}
```

```
curl --location --request PATCH 'https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/shtcnspY6YDVPxWjhG09Qxxxxxx/sheets/phwh0X/filter_views/1234567890' \
--header 'Authorization: Bearer t-2602ac1d050a2a308ab8a98639d25cbaaaf26c9f' \
--header 'Content-Type: application/json' \
--data-raw '{

"range": "phwh0X!C1:J20"
}'
```

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
filter_view | filter_view | Updated filter view ID, name, and range
filter_view_id | string | Filter view ID
filter_view_name | string | Filter view name
range | string | Filter view range

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "filter_view": {
            "filter_view_id": "pH9hbVcCXA",
            "filter_view_name": "Filter view 1",
            "range": "0b**12!C1:H14"
        }
    }
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
400 | 1310211 | Wrong Sheet Id | Check the sheet_id.
400 | 1310232 | Wrong Style | Invalid style, such as color or font
400 | 1310237 | Wrong Filter View Id | Invalid filter view ID
400 | 1310239 | Wrong Filter View Name | Invalid filter view name
400 | 1310240 | Exist Filter View Name | This filter view name already exists.
400 | 1310202 | Wrong Range | Invalid range
400 | 1310229 | Wrong URL Param | Check the url parameter.
400 | 1310204 | Wrong Request Body | Check the request body parameter.
400 | 1310213 | Permission Fail | No permission
400 | 1310218 | Locked Cell | Check if the action targets a protected range.
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.
400 | 1310215 | Sheet Id Not Found | Check the sheet_id.
400 | 1310217 | Too Many Request | Check if requests have been sent too frequently.
400 | 1310235 | Retry Later | Please try again later.
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
400 | 1310242 | In Mix state | Retey Later
400 | 1310249 | Spreadsheet Deleted | Restore the form and try again

# Query filter view

This API is used to query the basic information of all filter views in a sheet, including their IDs, names, and ranges.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/filter_views/query
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
spreadsheet_token | string | Spreadsheet token<br>**Example value**: "shtcnmBA*****yGehy8"
sheet_id | string | Sheet ID<br>**Example value**: "0b**12"

```
curl --location --request GET 'https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/shtcnspY6YDVPxWjhG09Qxxxxxx/sheets/phwh0X/filter_views/query' \
--header 'Authorization: Bearer t-2602ac1d050a2a308ab8a98639d25cbaaaf26c9f' \
--header 'Content-Type: application/json'
```

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
items | filter_view\[\] | Information of all filter views in a sheet, including IDs, names, and ranges
filter_view_id | string | Filter view ID
filter_view_name | string | Filter view name
range | string | Filter view range

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "items": [
            {
                "filter_view_id": "pH9hbVcCXA",
                "filter_view_name": "Filter view 1",
                "range": "0b**12!C1:H14"
            }
        ]
    }
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
400 | 1310211 | Wrong Sheet Id | Check the sheet_id.
400 | 1310237 | Wrong Filter View Id | Invalid filter view ID
400 | 1310202 | Wrong Range | Invalid range
400 | 1310229 | Wrong URL Param | Check the url parameter.
400 | 1310213 | Permission Fail | No permission
400 | 1310218 | Locked Cell | Check if the action targets a protected range.
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.
400 | 1310215 | Sheet Id Not Found | Check the sheet_id.
400 | 1310217 | Too Many Request | Check if requests have been sent too frequently.
400 | 1310235 | Retry Later | Please try again later.
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
400 | 1310242 | In Mix state | Retey Later
400 | 1310249 | Spreadsheet Deleted | Restore the form and try again

# Obtain filter view

This API is used to obtain the name and range of a specified filter view ID.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/filter_views/:filter_view_id
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
spreadsheet_token | string | Spreadsheet token<br>**Example value**: "shtcnmBA*****yGehy8"
sheet_id | string | Sheet ID<br>**Example value**: "0b**12"
filter_view_id | string | Filter view ID<br>**Example value**: "pH9hbVcCXA"

```
curl --location --request GET 'https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/shtcnspY6YDVPxWjhG09Qxxxxxx/sheets/phwh0X/filter_views/1234567890' \
--header 'Authorization: Bearer t-2602ac1d050a2a308ab8a98639d25cbaaaf26c9f' \
--header 'Content-Type: application/json'
```

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
filter_view | filter_view | Filter view information, including ID, name, and range
filter_view_id | string | Filter view ID
filter_view_name | string | Filter view name
range | string | Filter view range

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "filter_view": {
            "filter_view_id": "pH9hbVcCXA",
            "filter_view_name": "Filter view 1",
            "range": "0b**12!C1:H14"
        }
    }
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
400 | 1310229 | Wrong URL Param | Check the url parameter.
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.
400 | 1310215 | Sheet Id Not Found | Check the sheet_id.
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
400 | 1310217 | Too Many Request | Check if requests have been sent too frequently.
400 | 1310235 | Retry Later | Please try again later.
400 | 1310213 | Permission Fail | No permission
400 | 1310202 | Wrong Range | Invalid range
400 | 1310237 | Wrong Filter View Id | Invalid filter view ID
400 | 1310242 | In Mix state | Retey Later
400 | 1310249 | Spreadsheet Deleted | Restore the form and try again

# Delete filter view

This API is used to delete the filter view corresponding to the specified ID.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/filter_views/:filter_view_id
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
spreadsheet_token | string | Spreadsheet token<br>**Example value**: "shtcnmBA*****yGehy8"
sheet_id | string | Sheet ID<br>**Example value**: "0b**12"
filter_view_id | string | Filter view ID<br>**Example value**: "pH9hbVcCXA"

```
curl --location --request DELETE 'https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/shtcnspY6YDVPxWjhG09Qxxxxxx/sheets/phwh0X/filter_views/123456789a' \
--header 'Authorization: Bearer t-2602ac1d050a2a308ab8a98639d25cbaaaf26c9f' \
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
400 | 1310237 | Wrong Filter View Id | Invalid filter view ID
400 | 1310229 | Wrong URL Param | Check the url parameter.
400 | 1310213 | Permission Fail | No permission
400 | 1310218 | Locked Cell | Check if the action targets a protected range.
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.
400 | 1310215 | Sheet Id Not Found | Check the sheet_id.
400 | 1310217 | Too Many Request | Check if requests have been sent too frequently.
400 | 1310235 | Retry Later | Please try again later.
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
400 | 1310242 | In Mix state | Retey Later
400 | 1310249 | Spreadsheet Deleted | Restore the form and try again

# User guide for using filter conditions in the filter view

## Scenarios

Applies filter conditions to a column in the filter area to display specific data.

## Supported APIs

Five APIs are provided for filter conditions in filter views. A single filter view has only one range. The first row in a range is not filtered. You can set filter conditions for each column in the range.

1. [Obtain filter conditions](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet-filter_view-condition/get): Obtains the filter conditions of a specified column in the filter view.
2. [Create filter conditions](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet-filter_view-condition/create): Creates filter conditions for a specified column in the filter view.
3. [Update filter conditions](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet-filter_view-condition/update): Updates filter conditions of a specified column in the filter view.
4. [Delete filter conditions](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet-filter_view-condition/delete): Deletes filter conditions of a specified column in the filter view.
5. [Query filter conditions](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet-filter_view-condition/query): Queries all filter conditions in the filter view.

## Filter parameter
### **filter_view_id**
What is a filter_view_id?
A filter_view_id is the unique identifier of a filter view. It is obtained as follows:
1. Use the [Obtain filter view](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet-filter_view/get) API.
2. Open the filter view and find the ID in the link:
![image.png](//sf3-cn.feishucdn.com/obj/open-platform-opendoc/d70575214389a7ebec394427787771aa_3D0OWqknnU.png?lazyload=true&width=1148&height=74)

### **range**

The following five types of application scopes are supported (see [Overview](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview) for details):

1. sheetId: Indicates a whole spreadsheet
2. sheetId!1:2: Indicates a whole row
3. sheetId!A:B: Indicates a whole column
4. sheetId!A1:B2: Indicates a normal range
5. sheetId!A1:C: Omits the end row to extend the range to the last row of the spreadsheet

### **condition_id**

Column letters in the range.

### **filter_type**

Four filter_types are supported. Each filter_type must have a comparison type (compare_type) and value (expected).

1. hiddenValue: Hidden value filter
2. number: Numerical filter
3. text: Text filter
4. color: Color filter

***hiddenValue***

Value to hide

compare_type: Left blank

Expected: The value to be hidden, an array with a length greater than 0 and less than the number of rows in the range. A single value can't exceed 50,000 characters.
```json
{
    "filter_type": "hiddenValue",
    "expected": ["100", "200", "300"]
}
```
***number***

Numerical filter

| compare_type   | expected length | Notes        |
| -------------- | ----------- | --------- |
| equal          | 1           | Numerical filter: is equal to   |
| notEqual       | 1           | Numerical filter: is not equal to  |
| greater        | 1           | Numerical filter: greater than   |
| greaterOrEqual | 1           | Numerical filter: greater than or equal to |
| less           | 1           | Numerical filter: less than   |
| lessOrEqual    | 1           | Numerical filter: less than or equal to |
| between        | 2           | Numerical filter: is between   |
| notBetween     | 2           | Numerical filter: is not between  |
```json
{
    "filter_type": "number",
    "compare_type": "between",
    "expected": ["100", "200"]
}
```
***text***

Text filter
Text length can't exceed 1,000 characters

| compare_type     | expected length | Notes        |
| ---------------- | ----------- | --------- |
| beginsWith       | 1           | Text filter: text starts with  |
| notBeginsWith | 1           | Text filter: text starts without |
| endsWith         | 1           | Text filter: text ends with  |
| notEndsWith   | 1           | Text filter: text ends without |
| contains         | 1           | Text filter: text contains   |
| notContains   | 1           | Text filter: text does not contain  |
```json
{
    "filter_type": "text",
    "compare_type": "contains",
    "expected": ["abc"]
}
```
***color***

Color filter

| compare_type     | expected length | Notes        |
| ------------ | ----------- | ---------- |
| backColor    | 1           | Color filter: cell color |
| foreColor    | 1           | Color filter: text color  |
```json
{
    "filter_type": "color",
    "compare_type": "backColor",
    "expected": ["#ffffff"]
}
```
# Create a filter condition
For filter conditions, see [User guide for using filter conditions in the filter view](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet-filter_view-condition/filter-view-condition-user-guide)
This API is used to create filter conditions for a column in the range of a filter view.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/filter_views/:filter_view_id/conditions
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
spreadsheet_token | string | Spreadsheet token<br>**Example value**: "shtcnmBA*****yGehy8"
sheet_id | string | Sheet ID<br>**Example value**: "0b**12"
filter_view_id | string | Filter view ID<br>**Example value**: "pH9hbVcCXA"

### Request body

Parameter | Type | Required | Description
---|---|---|---
condition_id | string | No | Set filter condition column, using a letter designation<br>**Example value**: "E"
filter_type | string | No | Filter type<br>**Example value**: "number"
compare_type | string | No | Comparison type<br>**Example value**: "less"
expected | string\[\] | No | Filter parameter<br>**Example value**: ["6"]

### Request body example
```json
{
    "condition_id": "E",
    "filter_type": "number",
    "compare_type": "less",
    "expected": [
        "6"
    ]
}
```

```
curl --location --request POST 'https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/shtcnspY6YDVPxWjhG09Qxxxxxx/sheets/phwh0X/filter_views/1234567890/conditions' \
--header 'Authorization: Bearer t-40cdeb051222f889f4229de856517992260aa850' \
--header 'Content-Type: application/json' \
--data-raw '{
    "condition_id": "G",
    "filter_type": "text",
    "compare_type": "beginsWith",
    "expected": [
        "a"
    ]
}'
```

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
condition | filter_view_condition | Created filter condition
condition_id | string | Set filter condition column, using a letter designation
filter_type | string | Filter type
compare_type | string | Comparison type
expected | string\[\] | Filter parameter

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "condition": {
            "condition_id": "E",
            "filter_type": "number",
            "compare_type": "less",
            "expected": [
                "6"
            ]
        }
    }
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
400 | 1310211 | Wrong Sheet Id | Check the sheet_id.
400 | 1310237 | Wrong Filter View Id | Invalid filter view ID
400 | 1310236 | Wrong Filter Value | Check the filter conditions.
400 | 1310202 | Wrong Range | Invalid range
400 | 1310229 | Wrong URL Param | Check the url parameter.
400 | 1310204 | Wrong Request Body | Check the request body parameter.
400 | 1310213 | Permission Fail | No permission
400 | 1310218 | Locked Cell | Check if the action targets a protected range.
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.
400 | 1310215 | Sheet Id Not Found | Check the sheet_id.
400 | 1310223 | Col Id Not Found | Column ID not found. It may have been entered incorrectly or exceed the spreadsheet's column range.
400 | 1310217 | Too Many Request | Check if requests have been sent too frequently.
400 | 1310235 | Retry Later | Please try again later.
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
400 | 1310242 | In Mix state | Retey Later
400 | 1310232 | Wrong Style | Invalid style, such as color or font
400 | 1310249 | Spreadsheet Deleted | Restore the form and try again

# Update filter conditions
For filter condition parameters, see [User guide for using filter conditions in the filter view](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet-filter_view-condition/filter-view-condition-user-guide)
This API is used to update filter conditions for a column in the range of a filter view. The condition ID is the letter designation of the column.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/filter_views/:filter_view_id/conditions/:condition_id
HTTP Method | PUT
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
spreadsheet_token | string | Spreadsheet token<br>**Example value**: "shtcnmBA*****yGehy8"
sheet_id | string | Sheet ID<br>**Example value**: "0b**12"
filter_view_id | string | Filter view ID<br>**Example value**: "pH9hbVcCXA"
condition_id | string | Column letter designation<br>**Example value**: "E"

### Request body

Parameter | Type | Required | Description
---|---|---|---
filter_type | string | No | Filter type<br>**Example value**: "number"
compare_type | string | No | Comparison type<br>**Example value**: "less"
expected | string\[\] | No | Filter parameter<br>**Example value**: ["6"]

### Request body example
```json
{
    "filter_type": "number",
    "compare_type": "less",
    "expected": [
        "6"
    ]
}
```

```
curl --location --request PUT 'https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/shtcnspY6YDVPxWjhG09Qxxxxxx/sheets/phwh0X/filter_views/1234567890/conditions/E' \
--header 'Authorization: Bearer t-40cdeb051222f889f4229de856517992260aa850' \
--header 'Content-Type: application/json' \
--data-raw '{
    "condition_id": "E",
    "filter_type": "number",
    "compare_type": "between",
    "expected": [
        "2",
        "10"
    ]
}'
```

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
condition | filter_view_condition | Updated filter conditions
condition_id | string | Set filter condition column, using a letter designation
filter_type | string | Filter type
compare_type | string | Comparison type
expected | string\[\] | Filter parameter

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "condition": {
            "condition_id": "E",
            "filter_type": "number",
            "compare_type": "less",
            "expected": [
                "6"
            ]
        }
    }
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
400 | 1310211 | Wrong Sheet Id | Check the sheet_id.
400 | 1310232 | Wrong Style | Invalid style, such as color or font
400 | 1310236 | Wrong Filter Value | Check the filter conditions.
400 | 1310237 | Wrong Filter View Id | Invalid filter view ID
400 | 1310202 | Wrong Range | Invalid range
400 | 1310229 | Wrong URL Param | Check the url parameter.
400 | 1310204 | Wrong Request Body | Check the request body parameter.
400 | 1310213 | Permission Fail | No permission
400 | 1310218 | Locked Cell | Check if the action targets a protected range.
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.
400 | 1310215 | Sheet Id Not Found | Check the sheet_id.
400 | 1310223 | Col Id Not Found | Column ID not found. It may have been entered incorrectly or exceed the spreadsheet's column range.
400 | 1310217 | Too Many Request | Check if requests have been sent too frequently.
400 | 1310235 | Retry Later | Please try again later.
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
400 | 1310242 | In Mix state | Retey Later
400 | 1310249 | Spreadsheet Deleted | Restore the form and try again

# Query filter conditions
For filter condition explanations, see [User guide for using filter conditions in the filter view](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet-filter_view-condition/filter-view-condition-user-guide)
This API is used to query all filter conditions of a filter view. All filter conditions in the range of the filter view are returned.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/filter_views/:filter_view_id/conditions/query
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
spreadsheet_token | string | Spreadsheet token<br>**Example value**: "shtcnmBA*****yGehy8"
sheet_id | string | Sheet ID<br>**Example value**: "0b**12"
filter_view_id | string | Filter view ID<br>**Example value**: "pH9hbVcCXA"

```
curl --location --request GET 'https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/shtcnspY6YDVPxWjhG09Qxxxxxx/sheets/phwh0X/filter_views/1234567890/conditions/query' \
--header 'Authorization: Bearer t-40cdeb051222f889f4229de856517992260aa850' \
--header 'Content-Type: application/json'
```

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
items | filter_view_condition\[\] | All filter conditions set for the filter view
condition_id | string | Set filter condition column, using a letter designation
filter_type | string | Filter type
compare_type | string | Comparison type
expected | string\[\] | Filter parameter

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "items": [
            {
                "condition_id": "E",
                "filter_type": "number",
                "compare_type": "less",
                "expected": [
                    "6"
                ]
            }
        ]
    }
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
400 | 1310211 | Wrong Sheet Id | Check the sheet_id.
400 | 1310237 | Wrong Filter View Id | Invalid filter view ID
400 | 1310229 | Wrong URL Param | Check the url parameter.
400 | 1310213 | Permission Fail | No permission
400 | 1310218 | Locked Cell | Check if the action targets a protected range.
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.
400 | 1310215 | Sheet Id Not Found | Check the sheet_id.
400 | 1310217 | Too Many Request | Check if requests have been sent too frequently.
400 | 1310235 | Retry Later | Please try again later.
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
400 | 1310242 | In Mix state | Retey Later
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
400 | 1310249 | Spreadsheet Deleted | Restore the form and try again

# Obtain filter conditions
For filter condition explanations, see [User guide for using filter conditions in the filter view](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet-filter_view-condition/filter-view-condition-user-guide)
This API is used to obtain the filter conditions of a specified column in the filter view.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/filter_views/:filter_view_id/conditions/:condition_id
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
spreadsheet_token | string | Spreadsheet token<br>**Example value**: "shtcnmBA*****yGehy8"
sheet_id | string | Sheet ID<br>**Example value**: "0b**12"
filter_view_id | string | Filter view ID<br>**Example value**: "pH9hbVcCXA"
condition_id | string | Letter designation of column for which to query filter conditions<br>**Example value**: "E"

```
curl --location --request GET 'https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/shtcnspY6YDVPxWjhG09Qxxxxxx/sheets/phwh0X/filter_views/1234567890/conditions/E' \
--header 'Authorization: Bearer t-40cdeb051222f889f4229de856517992260aa850' \
--header 'Content-Type: application/json'
```

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
condition | filter_view_condition | Filter conditions
condition_id | string | Set filter condition column, using a letter designation
filter_type | string | Filter type
compare_type | string | Comparison type
expected | string\[\] | Filter parameter

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "condition": {
            "condition_id": "E",
            "filter_type": "number",
            "compare_type": "less",
            "expected": [
                "6"
            ]
        }
    }
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
400 | 1310211 | Wrong Sheet Id | Check the sheet_id.
400 | 1310237 | Wrong Filter View Id | Invalid filter view ID
400 | 1310229 | Wrong URL Param | Check the url parameter.
400 | 1310213 | Permission Fail | No permission
400 | 1310218 | Locked Cell | Check if the action targets a protected range.
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.
400 | 1310215 | Sheet Id Not Found | Check the sheet_id.
400 | 1310223 | Col Id Not Found | Column ID not found. It may have been entered incorrectly or exceed the spreadsheet's column range.
400 | 1310217 | Too Many Request | Check if requests have been sent too frequently.
400 | 1310235 | Retry Later | Please try again later.
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
400 | 1310242 | In Mix state | Retey Later
400 | 1310249 | Spreadsheet Deleted | Restore the form and try again

# Delete filter conditions

This API is used to delete filter conditions for a specified column in the range of a filter view.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/filter_views/:filter_view_id/conditions/:condition_id
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
spreadsheet_token | string | Spreadsheet token<br>**Example value**: "shtcnmBA*****yGehy8"
sheet_id | string | Sheet ID<br>**Example value**: "0b**12"
filter_view_id | string | Filter view ID<br>**Example value**: "pH9hbVcCXA"
condition_id | string | Letter designation of a column in the range<br>**Example value**: "E"

```
curl --location --request DELETE 'https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/shtcnspY6YDVPxWjhG09Qxxxxxx/sheets/phwh0X/filter_views/1234567890/conditions/E' \
--header 'Authorization: Bearer t-40cdeb051222f889f4229de856517992260aa850' \
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
400 | 1310211 | Wrong Sheet Id | Check the sheet_id.
400 | 1310237 | Wrong Filter View Id | Invalid filter view ID
400 | 1310229 | Wrong URL Param | Check the url parameter.
400 | 1310213 | Permission Fail | No permission
400 | 1310218 | Locked Cell | Check if the action targets a protected range.
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.
400 | 1310215 | Sheet Id Not Found | Check the sheet_id.
400 | 1310223 | Col Id Not Found | Column ID not found. It may have been entered incorrectly or exceed the spreadsheet's column range.
400 | 1310217 | Too Many Request | Check if requests have been sent too frequently.
400 | 1310235 | Retry Later | Please try again later.
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
400 | 1310242 | In Mix state | Retey Later
400 | 1310249 | Spreadsheet Deleted | Restore the form and try again
