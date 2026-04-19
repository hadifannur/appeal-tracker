# Unmerge cells

This interface is used to split cells, and the range in the request parameter needs to be exactly the same as the merged cell size.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/unmerge_cells
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
spreadsheet_token | string | Spreadsheet token<br>**Example value**: "shtxxxxxxxxx"
sheet_id | string | The id of the worksheet<br>**Example value**: "aKJA1I"

### Request body

Parameter | Type | Required | Description
---|---|---|---
unmerge_cells | merge_range\[\] | No | unmerge cells
start_row_index | int | No | Start line<br>**Example value**: 0
end_row_index | int | No | End line<br>**Example value**: 0
start_column_index | int | No | Start column<br>**Example value**: 0
end_column_index | int | No | End column<br>**Example value**: 0

### Request body example
```json
{
    "unmerge_cells": [
        {
            "start_row_index": 0,
            "end_row_index": 0,
            "start_column_index": 0,
            "end_column_index": 0
        }
    ]
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
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
500 | 1315210 | Server Error | Internal service errors, please consult customer service for details

# Merge cells

This interface is used to merge cells

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/merge_cells
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
spreadsheet_token | string | Spreadsheet token<br>**Example value**: "shtxxxxxxxxxxxx"
sheet_id | string | The id of the worksheet<br>**Example value**: "Xs1f3b"

### Request body

Parameter | Type | Required | Description
---|---|---|---
merge_cells | merge_cell\[\] | No | Merge area
range | merge_range | Yes | Range of merged cells<br>**Example value**: Zj2ts!A1:B2
start_row_index | int | No | Start line<br>**Example value**: 0
end_row_index | int | No | End line<br>**Example value**: 0
start_column_index | int | No | Start column<br>**Example value**: 0
end_column_index | int | No | End column<br>**Example value**: 0
merge_type | string | No | Merge cell types<br>**Example value**: "MergeAll"<br>**Optional values are**:<br>- MergeAll：Merge all<br>- MergeRows：Merge each row<br>- MergeColumns：Merge each column

### Request body example
```json
{
    "merge_cells": [
        {
            "range": {
                "start_row_index": 0,
                "end_row_index": 0,
                "start_column_index": 0,
                "end_column_index": 0
            },
            "merge_type": "MergeAll"
        }
    ]
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
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
500 | 1315210 | Server Error | Internal service errors, please consult customer service for details

# Insert row and column

This interface is used to insert rows and columns

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/insert_dimension
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
spreadsheet_token | string | Spreadsheet token<br>**Example value**: "shtxxxxxxxxxxxxxxxxxx"
sheet_id | string | The id of the worksheet<br>**Example value**: "46cdf7"

### Request body

Parameter | Type | Required | Description
---|---|---|---
dimension_range | dimension | No | Dimensions of row and column operations
major_dimension | string | No | Row or column, values: ROWS or COLUMNS<br>**Example value**: "ROWS"
start_index | int | No | Start row or column number<br>**Example value**: 0
end_index | int | No | End row or column number<br>**Example value**: 1
inherit_from | string | No | Whether to inherit the previous/next row/column style<br>**Example value**: "Before"<br>**Optional values are**:<br>- Before：Inherit the style of the previous row/column<br>- After：Inherit the style of the next row/column

### Request body example
```json
{
    "dimension_range": {
        "major_dimension": "ROWS",
        "start_index": 0,
        "end_index": 1
    },
    "inherit_from": "Before"
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
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
500 | 1315210 | Server Error | Internal service errors, please consult customer service for details

# Add dimension

This interface is used to add rows and columns at the end of the worksheet

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/append_dimension
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
spreadsheet_token | string | Form token<br>**Example value**: "shtxxxxxxxxxxxxxxxxx"
sheet_id | string | Sheet id<br>**Example value**: "46cdf7"

### Request body

Parameter | Type | Required | Description
---|---|---|---
major_dimension | string | Yes | Operate row or column, value: ROWS, COLUMNS<br>**Example value**: "ROWS"<br>**Optional values are**:<br>- ROWS：OK<br>- COLUMNS：Column
length | int | Yes | Quantity<br>**Example value**: 10
inherit_from_before | boolean | No | Whether to inherit the style of the previous row/column<br>**Example value**: false

### Request body example
```json
{
    "major_dimension": "ROWS",
    "length": 10,
    "inherit_from_before": false
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
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
500 | 1315210 | Server Error | Internal service errors, please consult customer service for details

# Update row and column properties

This interface is used to update row and column size and visibility

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/update_dimension
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
spreadsheet_token | string | Spreadsheet token<br>**Example value**: "shtxxxxxxxxxxxxxxx"
sheet_id | string | The id of the worksheet<br>**Example value**: "shtxxxxxxxxxxxxxxxxxx"

### Request body

Parameter | Type | Required | Description
---|---|---|---
dimension_range | dimension | Yes | Row and column information that needs to be updated
major_dimension | string | No | Row or column, values: ROWS or COLUMNS<br>**Example value**: "ROWS"
start_index | int | No | Start row or column number<br>**Example value**: 0
end_index | int | No | End row or column number<br>**Example value**: 1
properties | dimension_properties | Yes | Updated properties
hidden | boolean | No | Whether to hide<br>**Example value**: false
pixel_size | int | No | Row/column pixel size<br>**Example value**: 100

### Request body example
```json
{
    "dimension_range": {
        "major_dimension": "ROWS",
        "start_index": 0,
        "end_index": 1
    },
    "properties": {
        "hidden": false,
        "pixel_size": 100
    }
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
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
500 | 1315210 | Server Error | Internal service errors, please consult customer service for details

# Freeze dimension

This interface is used to update worksheet freeze row and column information

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/update_grid_properties
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
spreadsheet_token | string | Spreadsheet token<br>**Example value**: "shtxxxxxxxxxxxxxx"
sheet_id | string | The id of the worksheet<br>**Example value**: "Uk4nMe"

### Request body

Parameter | Type | Required | Description
---|---|---|---
frozen_row_count | int | No | Freeze rows<br>**Example value**: 1
frozen_column_count | int | No | Freeze columns<br>**Example value**: 1

### Request body example
```json
{
    "frozen_row_count": 1,
    "frozen_column_count": 1
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
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
500 | 1315210 | Server Error | Internal service errors, please consult customer service for details
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.

# Delete row and column

This interface is used to delete rows and columns

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/delete_dimension
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
spreadsheet_token | string | Spreadsheet token<br>**Example value**: "shtxxxxxxxx"
sheet_id | string | Sheet id<br>**Example value**: "As2ds2"

### Request body

Parameter | Type | Required | Description
---|---|---|---
major_dimension | string | No | Row or column, values: ROWS or COLUMNS<br>**Example value**: "ROWS"
start_index | int | No | Start row or column number<br>**Example value**: 0
end_index | int | No | End row or column number<br>**Example value**: 1

### Request body example
```json
{
    "major_dimension": "ROWS",
    "start_index": 0,
    "end_index": 1
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
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
500 | 1315210 | Server Error | Internal service errors, please consult customer service for details

# Create worksheet

Creates a worksheet for the specified spreadsheet.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets
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
spreadsheet_token | string | Spreadsheet token<br>**Example value**: "XUMasQlMYhOnMbt6htXv96h0aOg"

### Request body

Parameter | Type | Required | Description
---|---|---|---
title | string | No | Sheet title<br>**Example value**: "abc"
index | int | No | Sheet index<br>**Example value**: 0

### Request body example
```json
{
    "title": "abc",
    "index": 0
}
```

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
sheet | sheet | Sheet
sheet_id | string | Worksheet id
title | string | Worksheet title
index | int | Worksheet index position
hidden | boolean | Is the worksheet hidden?
grid_properties | grid_properties | Cell properties
frozen_row_count | int | Number of rows frozen
frozen_column_count | int | Number of columns frozen
row_count | int | Number of rows in the worksheet
column_count | int | Number of columns in the worksheet
resource_type | string | Worksheet type
merges | merge_range\[\] | Merge cells
start_row_index | int | Start line
end_row_index | int | End line
start_column_index | int | Start column
end_column_index | int | End column

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "sheet": {
            "sheet_id": "sxj5ws",
            "title": "title",
            "index": 0,
            "hidden": false,
            "grid_properties": {
                "frozen_row_count": 0,
                "frozen_column_count": 0,
                "row_count": 200,
                "column_count": 20
            },
            "resource_type": "sheet",
            "merges": [
                {
                    "start_row_index": 0,
                    "end_row_index": 0,
                    "start_column_index": 0,
                    "end_column_index": 0
                }
            ]
        }
    }
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
400 | 1310251 | Invalid Parameters | Reference error message in response body
400 | 1310213 | Permission Fail | No permission
400 | 1310249 | Spreadsheet Deleted | Restore the form and try again
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
500 | 1315210 | Server Error | Internal service errors, please consult customer service for details

# Copy sheet

This interface is used to copy sheet in separate spreadsheet

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/copy
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
spreadsheet_token | string | Spreadsheet token<br>**Example value**: "shtxxxxxxxxxxxxxxx"
sheet_id | string | The id of the sheet<br>**Example value**: "46cdf7"

### Request body

Parameter | Type | Required | Description
---|---|---|---
title | string | No | Sheet title<br>**Example value**: "abc"
index | int | No | Sheet index<br>**Example value**: 0

### Request body example
```json
{
    "title": "abc",
    "index": 0
}
```

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
sheet | sheet | Sheet
sheet_id | string | Worksheet id
title | string | Worksheet title
index | int | Worksheet index position
hidden | boolean | Is the worksheet hidden?
grid_properties | grid_properties | Cell properties
frozen_row_count | int | Number of rows frozen
frozen_column_count | int | Number of columns frozen
row_count | int | Number of rows in the worksheet
column_count | int | Number of columns in the worksheet
resource_type | string | Worksheet type
merges | merge_range\[\] | Merge cells
start_row_index | int | Start line
end_row_index | int | End line
start_column_index | int | Start column
end_column_index | int | End column

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "sheet": {
            "sheet_id": "sxj5ws",
            "title": "title",
            "index": 0,
            "hidden": false,
            "grid_properties": {
                "frozen_row_count": 0,
                "frozen_column_count": 0,
                "row_count": 200,
                "column_count": 20
            },
            "resource_type": "sheet",
            "merges": [
                {
                    "start_row_index": 0,
                    "end_row_index": 0,
                    "start_column_index": 0,
                    "end_column_index": 0
                }
            ]
        }
    }
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
400 | 1310251 | Invalid Parameters | Reference error message in response body
400 | 1310213 | Permission Fail | No permission
400 | 1310249 | Spreadsheet Deleted | Restore the form and try again
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
500 | 1315210 | Server Error | Internal service errors, please consult customer service for details

# Delete worksheet

The interface user deletes the worksheet

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id
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
spreadsheet_token | string | Spreadsheet token<br>**Example value**: "shtxxxxxxxxxxxxxxx"
sheet_id | string | The id of the worksheet<br>**Example value**: "46cdf7"

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
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
500 | 1315210 | Server Error | Internal service errors, please consult customer service for details

# Operate sheets

Use this API to add, copy, or delete sheets based on a spreadsheetToken.
This API uses the same request URL as  [Update sheet properties](https://open.larkoffice.com/document/ukTMukTMukTM/ugjMzUjL4IzM14COyMTN), but has different parameters. Read this document carefully before calling.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v2/spreadsheets/:spreadsheet_token/sheets_batch_update
HTTP Method | POST
Supported app types | Custom App、Store App
Required scopes<br>**The scopes required to call this API. You can call the API with any of the scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space(drive:drive)<br>View, comment, edit, and manage Sheets(sheets:spreadsheet)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | When calling an API, the app needs to authenticate its identity through an access token. Refer to [Choose and obtain access tokens](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM#5aa2e490).<br>**Value format**："Bearer `access_token`"<br>Supported options are:<br>- `tenant_access_token`：<br>Call the API on behalf of the app. The range of readable and writable data is determined by the app's own [data permission range](https://open.larkoffice.com/document/home/introduction-to-scope-and-authorization/configure-app-data-permissions). Refer to [Get custom app tenant_access_token](https://open.larkoffice.com/document/ukTMukTMukTM/ukDNz4SO0MjL5QzM/auth-v3/auth/tenant_access_token_internal) or [Get store app tenant_access_token](https://open.larkoffice.com/document/ukTMukTMukTM/ukDNz4SO0MjL5QzM/auth-v3/auth/tenant_access_token). **Example value**："Bearer t-g1044qeGEDXTB6NDJOGV4JQCYDGHRBARFTGT1234"<br>- `user_access_token`：<br>Call the API on behalf of the user. The range of readable and writable data is determined by the user's data permission range. Refer to [Get user_access_token](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/authentication-management/access-token/get-user-access-token). **Example value**："Bearer u-cjz1eKCEx289x1TXEiQJqAh5171B4gDHPq00l0GE1234"
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Path parameters

Parameter | Type | Description
---|---|---
spreadsheet_token | string | Spreadsheet token. Ways to get: <br>- Through the URL of the sheet: https://sample.feishu.cn/sheets/==shtcnmBAyGehy8abcef==<br>- Through the [List items in folder](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file/list) API.

###  Request body   

Name | Type | Required | Description
---|---|---|---
requests | / | Yes | Supports adding, copying, and deleting sheets. Supports multiple requests simultaneously.
addSheet | <md-text type="field-type" >/ | No | Add a sheet
properties | <md-text type="field-type" >/ | Yes | Sheet properties
title | <md-text type="field-type" >string | Yes | Title of the new sheet
index | <md-text type="field-type" >int | No | Position of the new sheet. If not specified, the default position is at index 0.
copySheet | <md-text type="field-type" >/ | No | Copy a sheet. The copied sheet is placed after the source sheet's index.
source | <md-text type="field-type" >/ | Yes | The sheet resource to be copied
sheetId | <md-text type="field-type" >string | Yes | ID of the source sheet. Call [Get Sheet](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet/query) to get the ID
destination | <md-text type="field-type" >/ | Yes | Properties of the new sheet
title | <md-text type="field-type" >string | No | Name of the new sheet. If not specified, the default name is "source sheet name" + "(copy_source sheet's `index` value)", e.g., "Sheet1(copy_0)".
deleteSheet | <md-text type="field-type" >/ | No | Delete a sheet.
sheetId | <md-text type="field-type" >string | Yes | ID of the sheet to be deleted. Call [Get Sheet](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet/query) to get the ID

### Request body example  
```json
{
  "requests": [
    {
      "addSheet": {
        "properties": {
          "title": "new_sheet",
          "index": 1
        }
      }
    },
    {
      "copySheet": {
        "source": {
          "sheetId": "2jm6f7"
        },
        "destination": {
          "title": "sheet_copy"
        }
      }
    },
    {
      "deleteSheet": {
        "sheetId": "l8Gdub"
      }
    }
  ]
}

```
### cURL Request example
```
curl --location --request POST 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/Ios7sNNEphp3WbtnbCscPqabcef/sheets_batch_update' \
--header 'Authorization: Bearer t-e346617a4acfc3a11d4ed24dca0d0c0fc8e0067e' \
--header 'Content-Type: application/json' \
--data-raw '{
  "requests": [
    {
      "addSheet": {
        "properties": {
          "title": "new_sheet",
          "index": 1
        }
      }
    },
    {
      "copySheet": {
        "source": {
          "sheetId": "2jm6f7"
        },
        "destination": {
          "title": "sheet_copy"
        }
      }
    },
    {
      "deleteSheet": {
        "sheetId": "l8Gdub"
      }
    }
  ]
}
'
```
## Response  

### Response body

Name | Type | Description
---|---|---
replies | <md-text type="field-type" >/ | Result of the sheet operation
addSheet | <md-text type="field-type" >/ | Result of adding a sheet
properties | <md-text type="field-type" >/ | Properties of the new sheet
sheetId | <md-text type="field-type" >string | `shetId` of the new sheet
title | <md-text type="field-type" >string | Title of the new sheet
index | <md-text type="field-type" >int | Position of the new sheet
copySheet | <md-text type="field-type" >/ | Result of copying a sheet
properties | <md-text type="field-type" >/ | Properties of the copied sheet
sheetId | <md-text type="field-type" >string | `shetId` of the copied sheet
title | <md-text type="field-type" >string | Title of the copied sheet
index | <md-text type="field-type" >int | Position of the copied sheet
deleteSheet | <md-text type="field-type" >/ | Result of deleting a sheet
result | <md-text type="field-type" >bool | Whether deleting the sheet was successful
sheetId | <md-text type="field-type" >string | ID of the deleted sheet

### Response body example  
```json
{
  "code": 0,
  "msg": "Success",
  "data": {
    "replies": [
      {
        "addSheet": {
          "properties": {
            "sheetId": "l8Gddg",
            "title": "new_sheet",
            "index": 1
          }
        },
        "copySheet": {
          "properties": {
            "sheetId": "dso4jn",
            "title": "sheet_copy",
            "index": 0
          }
        },
        "deleteSheet": {
          "result": true,
          "sheetId": "l8Gdub"
        }
      }
    ]
  }
}
```
### Error code

For details, refer to [Server-side error codes](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN).

#  Update sheet properties

Update worksheets in spreadsheets. Supports updating worksheet titles, positions, and properties such as hidden, frozen, protected, etc.
This API uses the same request URL as [Operate sheets](https://open.larkoffice.com/document/ukTMukTMukTM/uYTMzUjL2EzM14iNxMTN), but has different parameters. Read this document carefully before calling.
## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v2/spreadsheets/:spreadsheet_token/sheets_batch_update
HTTP Method | POST
Supported app types | Custom App、Store App
Required scopes<br>**The scopes required to call this API. You can call the API with any of the scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space(drive:drive)<br>View, comment, edit, and manage Sheets(sheets:spreadsheet)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | Authenticate the caller's identity through the access token. Optional values:<br>- `tenant_access_token`: Tenant authorization credential. The application acts on behalf of the tenant (i.e., a company or team) to perform corresponding operations. Example value: "Bearer t-7f1bcd13fc57d46bac21793aabcef"<br>- `user_access_token`: User authorization credential. The application acts on behalf of the user to perform corresponding operations. Example value: "Bearer u-7f1bcd13fc57d46bac21793aabcef"<br>For more information, refer to [Obtaining Access Tokens](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM).
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Query parameters

Parameter | Type | Required | Description
---|---|---|---
user_id_type | string | No | User ID type. The default is `lark_id`. It is recommended to choose `open_id` or `union_id`. For more information, refer to [User Identity Overview](https://open.larkoffice.com/document/home/user-identity-introduction/introduction). Optional values:<br>- `open_id`: Identifies a user within a specific application. The same user has different Open IDs in different applications. Learn more: [How to Obtain Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid)<br>- `union_id`: Identifies a user under a specific application developer. The same user has the same Union ID in applications under the same developer and different Union IDs in applications under different developers. With Union ID, developers can link the identity of the same user across multiple applications. Learn more: [How to Obtain Union ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id)

### Path parameters

Parameter | Type | Description
---|---|---
spreadsheet_token | string | Spreadsheet token. Ways to get: <br>- Through the URL of the sheet: https://sample.feishu.cn/sheets/==shtcnmBAyGehy8abcef==<br>- Through the [List items in folder](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file/list) API .

### Request body 

Name | Type | Required | Description
---|---|---|---
requests | / | Yes | Request to update spreadsheet properties
updateSheet | / | No | Update spreadsheet
properties | <md-text type="field-type">/</md-dt-text> | Yes | Spreadsheet properties
sheetId | string | Yes | ID of the spreadsheet to be updated. Call [Get Spreadsheet](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet/query) to get the ID
title | string | No | Title of the spreadsheet. The title needs to comply with the following rules:<br>- Not more than 100 characters in length<br>- Do not include these special characters: `/ \ ? * [ ] :`
index | int | No | Index of the spreadsheet. Count from 0.
hidden | <md-text type="field-type">bool | No | Whether to hide the sheet. Default value is false
frozenRowCount | <md-text type="field-type">int | No | Row index to freeze up to. If set to 3, it means freezing from the first row up to the third row. Must be less than or equal to the maximum number of rows in the sheet, 0 means no rows are frozen
frozenColCount | <md-text type="field-type">int | No | Column index to freeze up to. If set to 3, it means freezing from the first column up to the third column. Must be less than or equal to the maximum number of columns in the sheet, 0 means no columns are frozen
protect | <md-text type="field-type">/ | No | Whether to protect the spreadsheet
lock | <md-text type="field-type">string | Yes | Whether to protect the spreadsheet. Optional values:<br>- LOCK: Protect<br>- UNLOCK: Unprotect
<md-text type="field-name">lockInfo | <md-text type="field-type">string | No | Remarks information for protecting the spreadsheet
<md-text type="field-name">userIDs | <md-text type="field-type">array<string> | No | Add other users' IDs to give them edit permissions in the protected range, in addition to the owner and the user themselves. This field takes effect when the `user_id_type` query parameter is not empty.

### Request body example    

```json
{
  "requests": [
    {
      "updateSheet": {
        "properties": {
          "sheetId": "1SW8ik",
          "title": "Sales sheet",
          "index": 3,
          "hidden": true,
          "frozenColCount": 8,
          "frozenRowCount": 2,
          "protect": {
            "lock": "LOCK",
            "lockInfo": "privacy info",
            "userIDs": [
              "ou_48d0958ee4b2ab3eaf0b5f6c968abcef"
            ]
          }
        }
      }
    }
  ]
}
```
### cURL Request example

```bash
curl --location --request POST 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/shtcngNygNfuqhxTBf588jwgWbJ/sheets_batch_update?user_id_type=open_id' \
--header 'Authorization: Bearer t-e346617a4acfc3a11d4ed24dca0d0c0fc8e0067e' \
--header 'Content-Type: application/json' \
--data-raw '{
  "requests": [
    {
      "updateSheet": {
        "properties": {
          "sheetId": "zajIJ",
          "title": "Sales sheet",
          "index": 3,
          "hidden": true,
          "frozenColCount": 8,
          "frozenRowCount": 2,
          "protect": {
            "lock": "LOCK",
            "lockInfo": "privacy info"
            "userIDs": [
               "ou_48d0958ee4b2ab3eaf0b5f6c968abcef"
            ]
          }
        }
      }
    }
  ]
}'
```
## Response

### Response body

Name | Type | Description
---|---|---
replies | / | The result of this operation on the worksheet
updateSheet | <md-text type="field-type" >/ | The result of updating the worksheet
properties | <md-text type="field-type" >/ | Worksheet properties
sheetId | string | The ID of the updated worksheet
title | <md-text type="field-type" >string | The title of the updated worksheet
index | <md-text type="field-type" >int | The position of the moved worksheet
hidden | <md-text type="field-type" >bool | Whether to hide the sheet
frozen RowCount | <md-text type="field-type" >int | Row index to freeze up to
frozen ColCount | <md-text type="field-type" >int | Column index to freeze up to
protect | <md-text type="field-type" >/ | Worksheet protection properties
lock | <md-text type="field-type" >string | Whether to protect the worksheet. Optional values:<br>- LOCK: Protect<br>- UNLOCK: Unprotect
lockInfo | <md-text type="field-type" >string | Remarks on worksheet protection
<md-text type="field-name" >userIDs | <md-text type="field-type" >array<string> | IDs of other users with permission to edit the protected range, except for the owner and the user. The type of ID is determined by the query parameter `user_id_type`.

### Response body example    
```json
 {
  "code": 0,
  "msg": "Success",
  "data": {
    "replies": [
      {
        "updateSheet": {
          "properties": {
            "sheetId": "1SW8ik",
            "title": "Sales sheet",
            "index": 3,
            "hidden": true,
            "frozenColCount": 2,
            "frozenRowCount": 8,
            "protect": {
              "lock": "LOCK",
              "lockInfo": "privacy info",
              "userIDs": [
                "ou_48d0958ee4b2ab3eaf0b5f6c968abcef"
              ]
            }
          }
        }
      }
    ]
  }
}
```
### Error code

For details, refer to [Server-side error codes](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN).

# Get a sheet

This interface is used to get all worksheets and their properties under the spreadsheet, including ID, title, index, and whether the worksheet is hidden.

## Prerequisite

Before calling this API, ensure that the current identity (either `tenant_access_token` or `user_access_token`) has been granted permissions to read or edit spreadsheets. Otherwise, the API will return HTTP 403 or 400 status codes. For more information, refer to [How to enable document permissions for applications or users](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#16c6475a).

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/query
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
spreadsheet_token | string | Spreadsheet token. Ways to get: <br>- Through the URL of the sheet: https://sample.feishu.cn/sheets/==shtcnmBAyGehy8abcef==<br>- Through the [List items in folder](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file/list)<br>**Example value**: "Iow7sNNEphp3WbtnbCscPqabcef"

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
sheets | sheet\[\] | List of worksheets
sheet_id | string | Worksheet ID
title | string | Worksheet title
index | int | Worksheet index
hidden | boolean | whether the worksheet is hidden
grid_properties | grid_properties | Cell properties, returned only when `resource_type=sheet`
frozen_row_count | int | Number of rows frozen
frozen_column_count | int | Number of columns frozen
row_count | int | Number of rows in the worksheet
column_count | int | Number of columns in the worksheet
resource_type | string | Worksheet type
merges | merge_range\[\] | Merge cells
start_row_index | int | Start line. Counts from 0
end_row_index | int | End line. Counts from 0
start_column_index | int | Start column. Counts from 0
end_column_index | int | End column. Counts from 0

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "sheets": [
            {
                "sheet_id": "sxj5ws",
                "title": "sheet1",
                "index": 0,
                "hidden": false,
                "grid_properties": {
                    "frozen_row_count": 0,
                    "frozen_column_count": 0,
                    "row_count": 200,
                    "column_count": 20
                },
                "resource_type": "sheet",
                "merges": [
                    {
                        "start_row_index": 0,
                        "end_row_index": 0,
                        "start_column_index": 0,
                        "end_column_index": 0
                    }
                ]
            }
        ]
    }
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
400 | 1310251 | Invalid Parameters | Reference error message in response body
400 | 1310213 | Permission Fail | Confirm whether the current access identity has permission to read or edit spreadsheets. Please refer to the following methods to resolve this:<br>- If you are using a `tenant_access_token`, it means the current application does not have permission to read or edit spreadsheets. You need to add document permissions for the application through the cloud document webpage by navigating to the top right corner **"..."** -> **"... More"** -> **"Add applications"**.<br>**Note**: Before adding a document application, you need to ensure that the target application has at least one cloud document [API permission](https://open.larkoffice.com/document/ukTMukTMukTM/uYTM5UjL2ETO14iNxkTN/scope-list) enabled. Otherwise, you will not be able to search for the target application in the document application window.<br>![](//sf3-cn.feishucdn.com/obj/open-platform-opendoc/bb60f97ebb402475f2af1d3131d4914f_sLOzoqYRXX.png?height=1992&maxWidth=550&width=3278)<br>- If you are using a `user_access_token`, it means the current user does not have permission to read or edit spreadsheets. You need to add document permissions for the current user through the **Share** entry in the top right corner of the cloud document webpage.<br>![image.png](//sf3-cn.feishucdn.com/obj/open-platform-opendoc/caceea2ac91c170555194d7a8dc2a317_GfTRc9xLAt.png&maxWidth=550)<br>For more details on the specific steps or other methods to add permissions, refer to [Cloud Document FAQ 3](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#16c6475a).
400 | 1310249 | Spreadsheet Deleted | Restore the form and try again
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
500 | 1315210 | Server Error | Internal service errors, please consult customer service for details

# Query a sheet

This interface is used to query worksheet information by worksheet ID, including the title, index, and whether the sheet is hidden.

## Prerequisite

Before calling this API, ensure that the current identity (either `tenant_access_token` or `user_access_token`) has been granted permissions to read or edit spreadsheets. Otherwise, the API will return HTTP 403 or 400 status codes. For more information, refer to [How to enable document permissions for applications or users](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#16c6475a).

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id
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
spreadsheet_token | string | Spreadsheet token. Ways to get: <br>- Through the URL of the sheet: https://sample.feishu.cn/sheets/==shtcnmBAyGehy8abcef==<br>- Through the [List items in folder] API (https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file/list)<br>**Example value**: "Iow7sNNEphp3WbtnbCscPqabcef"
sheet_id | string | The ID of the worksheet<br>**Example value**: "giDk9k"

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
sheet | sheet | sheet
sheet_id | string | Worksheet id
title | string | Worksheet title
index | int | Worksheet index. Counts from 0
hidden | boolean | Is the worksheet hidden
grid_properties | grid_properties | Cell properties, returned only when `resource_type=sheet`
frozen_row_count | int | Number of rows frozen
frozen_column_count | int | Number of columns frozen
row_count | int | Number of rows in the worksheet
column_count | int | Number of columns in the worksheet
resource_type | string | Worksheet type
merges | merge_range\[\] | Merge cells
start_row_index | int | Start line. Counts from 0
end_row_index | int | End line. Counts from 0
start_column_index | int | Start column. Counts from 0
end_column_index | int | End column. Counts from 0

### Response body example
```json
{
    "code": 0,
    "msg": "",
    "data": {
        "sheet": {
            "sheet_id": "sxj5ws",
            "title": "sheet1",
            "index": 0,
            "hidden": false,
            "grid_properties": {
                "frozen_row_count": 0,
                "frozen_column_count": 0,
                "row_count": 200,
                "column_count": 20
            },
            "resource_type": "sheet",
            "merges": [
                {
                    "start_row_index": 0,
                    "end_row_index": 0,
                    "start_column_index": 0,
                    "end_column_index": 0
                }
            ]
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
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
500 | 1315210 | Server Error | Internal service errors, please consult customer service for details
