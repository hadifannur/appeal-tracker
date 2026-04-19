# Cell data structure

## Data Example

The following structure indicates that the cell content in the first row and first column cell is the number 123; there are two elements in the second row and first column cell, the first element is the text "abc", and the second element is mention user. The content in the third row and first column is an image.

```json
[
    [ // The first row
        [  // The first column
            {
                "type": "value",
                "value": {
                    "value": "123"
                }
            }
        ]
    ],
    [ // The second row
        [ // The first column
            {
                "text": {
                    "text": "abc "
                },
                "type": "text"
            },
            {
                "mention_user": {
                    "name": "your name",
                    "user_id": "ou_024be0cf5488c88d5c6e012bb"
                },
                "type": "mention_user"
            }
        ]
    ],
    [ // The third row
        [   // The first column
            {
                "image": {
                    "image_token": "OnwtbeibtoasKFxXZDhcYYabcef"
                },
                "type": "image"
            }
        ]
    ]
]
```

## Cell

When using get rich text content, the obtained values field is a three-dimensional array, the first dimension is a row, and the second dimension is a column. For example, values [1] [2] represents the cell of the third column of the second row in the range. Use the following structure to represent a cell:
```
[
  Object(Element)
]
```

### Element

There are several types of data in a cell, each of which is typed by the "type" field. For unsupported types, "type" = "#UNSUPPORTED_TYPE".The optional values of the type field are "text", "mention_user", "mention_document", "value", "date_time", "checkbox", "file", "image", "link", "reminder", "formula" , "single_option", "multiple_option", "date_validation", "datetime_option".
```
{
    "type": "string",
    // union field, only one of the following field will appear
    "text":object(Text),
    "mention_user":object(MentionUser),
    "mention_document":object(MentionDocument),
    "value":object(Value),
    "date_time":object(DateTime),
    "checkbox":object(Checkbox),
    "file":object(File),
    "image":object(Image),
    "link":object(Link),
    "reminder":object(Reminder),
    "formula":object(Formula),
    "single_option":object(SingleOption),
    "multiple_option":object(MultipleOption),
    "date_validation":object(DateValidation),
    "datetime_option":object(DateTimeOption),
}
```

#### Text

Text type.
```
{
    "text": "string",
    "segment_style": {
        "style": {
            "bold": true,
            "italic": true,
            "strike_through": true,
            "underline": true,
            "fore_color": "#ff00ff",
            "font_size": 30
        },
        "affected_text": "string"
    }
}
```
| Fields           | Is it necessary | Type    | Description                    |
| ---------------- | --------------- | ------- | ------------------------------ |
| text             | Yes             | string  | Text content                   |
| segment_style    | No              |         | Local style                    |
| ∟style           | Yes             |         | Style                          |
|  ∟bold           | No              | boolean | Is it bold?                    |
|  ∟italic         | No              | boolean | Whether italic                 |
|  ∟strike_through | No              | boolean | Is there a strikethrough?      |
|  ∟underline      | No              | boolean | Is there an underscore?        |
|  ∟fore_color     | No              | string  | Font color                     |
|  ∟font_size      | No              | int     | Font size                      |
| ∟affected_text   | No              | string  | String affected by local style |

#### Value

Numerical type
```
{
    "value": "123.3"
}
```
| Fields | Is it necessary | Type   | Description |
| ------ | --------------- | ------ | ----------- |
| value  | Yes             | string | Value       |

#### DateTime

```
{
    "date_time": "2022/2/2 18:11"
}
```
| Fields    | Is it necessary | Type   | Description |
| --------- | --------------- | ------ | ----------- |
| date_time | Yes             | string | Date Time   |

#### Image

```
{
    "image_token": "xxxx"
}
```
| Fields      | Is it necessary | Type   | Description                                                                                                            |
| ----------- | --------------- | ------ | ---------------------------------------------------------------------------------------------------------------------- |
| image_token | Yes             | string | Image token; can be obtained through the[Upload material](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/media/upload_all) interface when writing to a cell; can be downloaded through the [Download a material](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/media/download) interface |

#### File

```
{
    "file_token": "xxxx",
    "name": "xxx",
    "segment_style": {
        "style": {
            "bold": true,
            "italic": true,
            "strike_through": true,
            "underline": true,
            "fore_color": "#ff00ff",
            "font_size": 30
        },
        "affected_text": "xxx"
    }
}
```
| Fields           | Is it necessary                   | Type    | Description                    |
| ---------------- | --------------------------------- | ------- | ------------------------------ |
| file_token       | Yes                               | string  | Attachment token               |
| name             | No (valid only when reading data) | string  | Attachment name                |
| segment_style    | No                                |         | Local style                    |
| ∟style           | Yes                               |         | Style                          |
|  ∟bold           | No                                | boolean | Is it bold?                    |
|  ∟italic         | No                                | boolean | Whether italic                 |
|  ∟strike_through | No                                | boolean | Is there a strikethrough?      |
|  ∟underline      | No                                | boolean | Is there an underscore?        |
|  ∟fore_color     | No                                | string  | Font color                     |
|  ∟font_size      | No                                | int     | Font size                      |
| ∟affected_text   | No                                | string  | String affected by local style. Only supports writing when the cell data is of the link type. Other types are not supported as input parameters. |

#### Reminder

```
{
    "notify_date_time": "2022/2/2 18:00",
    "notify_user_id": [
        "ou_xxx"
    ],
    "notify_text": "xxxx",
    "notify_strategy": 0,
}
```

| Fields           | Is it necessary | Type          | Description    |
| ---------------- | --------------- | ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| notify_date_time | Yes             | string        | Date Reminder Time                                                                                                                                                                                                              |
| notify_user_id   | No              | list<string> | Alerted users, the id type depends on the query parameter user_id_type                                                                                                                                                                                                                    |
| notify_text      | No              | string        | The content of the reminder                                                                                                                                                                                                     |
| notify_strategy  | Yes             | enum          | Reminder strategy, 0: when the event occurs; 1:5 minutes in advance; 2:15 minutes in advance; 3:30 minutes in advance; 4:1 hour in advance; 5:2 hours in advance; 6:1 day in advance; 7:2 days in advance: 8:1 week in advance; |

#### Formula

```
{
    "formula": "xxxxx",
    "formula_value": "xxx", 
    "affected_range": "sheet1!A1:B2"
}
```
| Fields         | Is it necessary                   | Type   | Description                   |
| -------------- | --------------------------------- | ------ | ----------------------------- |
| formula        | Yes                               | string | Formula                       |
| formula_value  | No (valid only when reading data) | string | Formula calculation result    |
| affected_range | No (valid only when reading data) | string | Range of influence of formula |

#### MentionUser

```
{
    "name": "zyb",
    "user_id": "ou_xxxxx",
    "notify": false,
    "segment_styles": {
        "style": {
            "bold": true,
            "italic": true,
            "strike_through": true,
            "underline": true,
            "fore_color": "#ff00ff",
            "font_size": 30
        },
        "affected_text": "zyb"
    }
}
```
| Fields           | Is it necessary                   | Type    | Description                    |
| ---------------- | --------------------------------- | ------- | ------------------------------ |
| name             | No (valid only when reading data) | string  | Username                       |
| user_id          | Yes                               | string  | User ID, the id type depends on the query parameter user_id_type                       |
| notify           | No                                | boolean | Alert the user                 |
| segment_style    | No                                |         | Local style                    |
| ∟style           | Yes                               |         | Style                          |
|  ∟bold           | No                                | boolean | Is it bold?                    |
|  ∟italic         | No                                | boolean | Whether italic                 |
|  ∟strike_through | No                                | boolean | Is there a strikethrough?      |
|  ∟underline      | No                                | boolean | Is there an underscore?        |
|  ∟fore_color     | No                                | string  | Font color                     |
|  ∟font_size      | No                                | int     | Font size                      |
| ∟affected_text   | No                                | string  | String affected by local style |

#### MentionDocument

```
{
    "title": "xxxx",
    "object_type":"sheet",
    "token": "shtxxxxx",
    "segment_styles": {
         "style": {
            "bold": true,
            "italic": true,
            "strike_through": true,
            "underline": true,
            "fore_color": "#ff00ff",
            "font_size": 30
        },
        "affected_text": "xxxx"
    }
}
```
| Fields           | Is it necessary                   | Type    | Description                    |
| ---------------- | --------------------------------- | ------- | ------------------------------ |
| title            | No (valid only when reading data) | string  | Doc title                      |
| object_type      | Yes                               | string  | Type doc                       |
| token            | Yes                               | string  | Doc token                      |
| segment_style    | No                                |         | Local style                    |
| ∟style           | Yes                               |         | Style                          |
|  ∟bold           | No                                | boolean | Is it bold?                    |
|  ∟italic         | No                                | boolean | Whether italic                 |
|  ∟strike_through | No                                | boolean | Is there a strikethrough?      |
|  ∟underline      | No                                | boolean | Is there an underscore?        |
|  ∟fore_color     | No                                | string  | Font color                     |
|  ∟font_size      | No                                | int     | Font size                      |
| ∟affected_text   | No                                | string  | String affected by local style |

#### Link

```
{
    "text": "xxxx",
    "link":"www.baidu.com",
    "segment_styles": [
        {
            "style": {
                "bold": true,
                "italic": true,
                "strike_through": true,
                "underline": true,
                "fore_color": "#ff00ff",
                "font_size": 30
            },
            "affected_text": "xxxx"
        }
    ]
}
```
| Fields           | Is it necessary | Type                 | Description                    |
| ---------------- | --------------- | -------------------- | ------------------------------ |
| text             | No              | string               | Link text                      |
| link             | Yes             | string               | Link                           |
| segment_styles   | No              | list<segment_style> | Local style                    |
| ∟style           | Yes             |                      | Style                          |
|  ∟bold           | No              | boolean              | Is it bold?                    |
|  ∟italic         | No              | boolean              | Whether italic                 |
|  ∟strike_through | No              | boolean              | Is there a strikethrough?      |
|  ∟underline      | No              | boolean              | Is there an underscore?        |
|  ∟fore_color     | No              | string               | Font color                     |
|  ∟font_size      | No              | int                  | Font size                      |
| ∟affected_text   | Yes             | string               | String affected by local style |

#### Checkbox

Not supported yet

#### SingleOption

Not supported yet

#### MultipleOption

Not supported yet

#### DateTimeOption

Not supported yet

### Element exclusivity

It is said that there can only be at most one element in a cell, and the element is exclusive to the cell. Exclusive elements cannot co-exist in a cell with other elements. For example, value cannot be placed in the same cell with other elements such as text and mention_user.

| Element type        | Whether exclusive |
| ---------------- | -------- |
| text             | No       |
| mention_user     | No       |
| mention_document | No       |
| value            | Yes       |
| date_time        | Yes       |
| checkbox         | Yes       |
| file             | No       |
| image            | Yes       |
| link             | No       |
| reminder         | Yes       |
| formula          | Yes       |
| single_option    | Yes       |
| multiple_option  | Yes       |
| date_validation  | Yes       |
| datetime_option  | Yes       |

## Undefined behavior

The behavior that does not write according to the semantics agreed upon by the element is called undefined behavior. Undefined behavior may produce unexpected results, or even cause the results to be inconsistent with previous behavior. Such as writing formulas in text elements.

# Write cell

This interface is used to write data to the specified area, and the number of requested areas does not exceed 10. When the write range exceeds the existing range of the table, the row and column will be automatically expanded, and the expanded row and column will inherit the style of the previous row/column.

**Notice**：- A single write does not exceed 5000 cells
- Each grid does not exceed 50,000 characters; since the server will increase control characters, it is recommended that each grid does not exceed 40,000 characters
- The number of Reminders written at a time does not exceed 100
- The number of Reminders for a single write to Remidner does not exceed 1000
- The number of mentioned documents in a single write does not exceed 10
- The number of pictures written at a time does not exceed 50

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/values/batch_update
HTTP Method | POST
Rate Limit | [100 per minute](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space(drive:drive)<br>View, comment, edit, and manage Sheets(sheets:spreadsheet)
Required field scopes | **Notice**：The response body of the API contains the following sensitive fields, and they will be returned only after corresponding scopes are added. If you do not need the fields, it is not recommended that you request the scopes.<br>Obtain user ID(contact:user.employee_id:readonly)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Path parameters

Parameter | Type | Description
---|---|---
spreadsheet_token | string | Spreadsheet token<br>**Example value**: "shtxxxxxxxxxxxxxxxxx"
sheet_id | string | Sheet id<br>**Example value**: "0354d1"

### Query parameters

Parameter | Type | Required | Description
---|---|---|---
user_id_type | string | No | User ID categories<br>**Example value**: open_id<br>**Optional values are**:<br>- open_id：Identifies a user to an app. The same user has different Open IDs in different apps. [How to get Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid)<br>- union_id：Identifies a user to a tenant that acts as a developer. A user has the same Union ID in apps developed by the same developer, and has different Union IDs in apps developed by different developers. A developer can use Union ID to link the same user's identities in multiple apps.[How to get Union ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id)<br>- user_id：Identifies a user to a tenant. The same user has different User IDs in different tenants. In one single tenant, a user has the same User ID in all apps （including store apps）. User ID is usually used to communicate user data between different apps. [How to get User ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**Default value**: `open_id`<br>**When the value is `user_id`, the following field scopes are required**:<br>Obtain user ID(contact:user.employee_id:readonly)

### Request body

Parameter | Type | Required | Description
---|---|---|---
value_ranges | value\[\] | No | Data and Scope
range | string | No | Range. For details, see [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)<br>**Example value**: "Sheet1!A1:A2"
values | cell_value\[\]\[\]\[\] | No | Data,For data structure, see  [Data Structure](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet-value/cell-data-structure)<br>**Example value**: []

### Request body example
```json
{
    "value_ranges": [
        {
            "range": "d23283!C1:C1",
            "values": [
                [
                    [
                        {
                            "image": {
                                "image_token": "OnwtbeibtoasKFxXZDhcYYabcef"
                            },
                            "type": "image"
                        }
                    ]
                ]
            ]
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
500 | 1315210 | Server Error | Internal service errors, please consult customer service for details
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.

# Insert data

According to the SpreadsheetToken, add several rows above the start of its **specific worksheet specified area** and fill the corresponding data. The area is determined by the `range` attribute of the interface path parameter, for example:<br>
`range=8fe9d6!A2:B2`. `8fe9d6` is the worksheet unique identifier (SheetID), `A2:B2` represents the range from A2 to B2 of the second row of the worksheet, that is, it is expected to add a new row above the second row of the worksheet, and the data will be inserted into the A2 and B2 cells of the new row. <br> 
For a detailed definition of range , see [Overview > Terminology Explanation > Range](https://open.feishu.cn/document/server-docs/docs/sheets-v3/overview#a311e772).

**Notice**：- A single write does not exceed 5,000 cells
- Each grid does not exceed 50,000 characters; since the server will increase control characters, it is recommended that each grid does not exceed 40,000 characters
- The number of Reminders written at a time does not exceed 100
- The number of reminders for a single write to Reminder does not exceed 1,000
- The number of mentioned documents in a single write does not exceed 10
- The number of pictures written at a time does not exceed 50

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/values/:range/insert
HTTP Method | POST
Rate Limit | [100 per minute](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space(drive:drive)<br>View, comment, edit, and manage Sheets(sheets:spreadsheet)
Required field scopes | **Notice**：The response body of the API contains the following sensitive fields, and they will be returned only after corresponding scopes are added. If you do not need the fields, it is not recommended that you request the scopes.<br>Obtain user ID(contact:user.employee_id:readonly)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Path parameters

Parameter | Type | Description
---|---|---
spreadsheet_token | string | Spreadsheet token<br>**Example value**: "XUMasQlMYhOnMbt5htXc96h0nOg"
sheet_id | string | Sheet id<br>**Example value**: "0354d1"
range | string | Data range, including SheetID and Cell Range, currently supports three indexing methods, see [Spreadsheet overview > Glossary > Range](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview#a311e772), the range represented by range needs to be greater than or equal to the range occupied by values.<br>**Example value**: "0354d1!A1:B2"

### Query parameters

Parameter | Type | Required | Description
---|---|---|---
user_id_type | string | No | User ID categories<br>**Example value**: open_id<br>**Optional values are**:<br>- open_id：Identifies a user to an app. The same user has different Open IDs in different apps. [How to get Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid)<br>- union_id：Identifies a user to a tenant that acts as a developer. A user has the same Union ID in apps developed by the same developer, and has different Union IDs in apps developed by different developers. A developer can use Union ID to link the same user's identities in multiple apps.[How to get Union ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id)<br>- user_id：Identifies a user to a tenant. The same user has different User IDs in different tenants. In one single tenant, a user has the same User ID in all apps （including store apps）. User ID is usually used to communicate user data between different apps. [How to get User ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**Default value**: `open_id`<br>**When the value is `user_id`, the following field scopes are required**:<br>Obtain user ID(contact:user.employee_id:readonly)

### Request body

Parameter | Type | Required | Description
---|---|---|---
values | cell_value\[\]\[\]\[\] | No | Data<br>**Example value**: Data

### Request body example
```json
{
    "values": [
        [
            [
                {
                    "type": "value",
                    "value": {
                        "value": "123"
                    }
                }
            ]
        ]
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

# Append data

This interface is used to append data to an empty space. It will start from the starting cell of the given range and look down until a cell with no content is found and the given data is written.

**Notice**：- A single write does not exceed 5000 cells
- Each grid does not exceed 50,000 characters; since the server will increase control characters, it is recommended that each grid does not exceed 40,000 characters
- The number of Reminders written at a time does not exceed 100
- The number of Reminder for a single write to Remidner does not exceed 1000
- The number of mentioned documents in a single write does not exceed 10
- The number of pictures written at a time does not exceed 50

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/values/:range/append
HTTP Method | POST
Rate Limit | [100 per minute](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space(drive:drive)<br>View, comment, edit, and manage Sheets(sheets:spreadsheet)
Required field scopes | **Notice**：The response body of the API contains the following sensitive fields, and they will be returned only after corresponding scopes are added. If you do not need the fields, it is not recommended that you request the scopes.<br>Obtain user ID(contact:user.employee_id:readonly)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Path parameters

Parameter | Type | Description
---|---|---
spreadsheet_token | string | Spreadsheet token<br>**Example value**: "shtxxxxxxxxxxx"
sheet_id | string | Sheet id<br>**Example value**: "0354d1"
range | string | Data range. For details, see [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)<br>**Example value**: "Sheet1!A1:B2"

### Query parameters

Parameter | Type | Required | Description
---|---|---|---
user_id_type | string | No | User ID categories<br>**Example value**: open_id<br>**Optional values are**:<br>- open_id：Identifies a user to an app. The same user has different Open IDs in different apps. [How to get Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid)<br>- union_id：Identifies a user to a tenant that acts as a developer. A user has the same Union ID in apps developed by the same developer, and has different Union IDs in apps developed by different developers. A developer can use Union ID to link the same user's identities in multiple apps.[How to get Union ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id)<br>- user_id：Identifies a user to a tenant. The same user has different User IDs in different tenants. In one single tenant, a user has the same User ID in all apps （including store apps）. User ID is usually used to communicate user data between different apps. [How to get User ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**Default value**: `open_id`<br>**When the value is `user_id`, the following field scopes are required**:<br>Obtain user ID(contact:user.employee_id:readonly)

### Request body

Parameter | Type | Required | Description
---|---|---|---
values | cell_value\[\]\[\]\[\] | No | Data<br>**Example value**: Data

### Request body example
```json
{
    "values": [
        [
            [
                {
                    "type": "value",
                    "value": {
                        "value": "123"
                    }
                }
            ]
        ]
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

# Get spreadsheet plain text content

This interface is used to get the plain text content of the worksheet.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/values/batch_get_plain
HTTP Method | POST
Rate Limit | [1000 per minute & 50 per second](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space(drive:drive)<br>View, comment, and download all files in My Space(drive:drive:readonly)<br>View, comment, edit, and manage Sheets(sheets:spreadsheet)<br>View, comment, and export Sheets(sheets:spreadsheet:readonly)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Path parameters

Parameter | Type | Description
---|---|---
spreadsheet_token | string | Spreadsheet token<br>**Example value**: "shtxxxxxxxxxxxxx"
sheet_id | string | Worksheet id<br>**Example value**: "0354d1"

### Request body

Parameter | Type | Required | Description
---|---|---|---
ranges | string\[\] | No | Multiple ranges of the same worksheet. This parameter is required. For details, see [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)<br>**Example value**: ["Asn1m8! A1: B2"]

### Request body example
```json
{
    "ranges": [
        "0WVC18!A1:A1",
        "0WVC18!G2:G2"
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
value_ranges | plain_text_value_range\[\] | Cell content
range | string | Scope
values | string\[\]\[\] | Data

### Response body example
```json
{
    "code": 0,
    "data": {
        "value_ranges": [
            {
                "range": "0WVC18!A1:A1",
                "values": [
                    [
                        "@Li Hua"
                    ]
                ]
            },
            {
                "range": "0WVC18!G2:G2",
                "values": [
                    [
                        "r"
                    ]
                ]
            }
        ]
    },
    "msg": ""
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
400 | 1310251 | Invalid Parameters | Reference error message in response body
400 | 1310213 | Permission Fail | No permission
400 | 1310249 | Spreadsheet Deleted | Restore the form and try again
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.
400 | 1310226 | Excess Limit | Exceeds the limit
400 | 1310221 | Response Too Large | Reduce the number of requests
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
400 | 1310235 | Retry Later | Please try again later.
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
500 | 1315210 | Server Error | Internal service errors, please consult customer service for details

# Get spreadsheet rich text content

The interface user obtains the rich text content of the spreadsheet/

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/values/batch_get
HTTP Method | POST
Rate Limit | [1000 per minute & 50 per second](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space(drive:drive)<br>View, comment, and download all files in My Space(drive:drive:readonly)<br>View, comment, edit, and manage Sheets(sheets:spreadsheet)<br>View, comment, and export Sheets(sheets:spreadsheet:readonly)
Required field scopes | **Notice**：The response body of the API contains the following sensitive fields, and they will be returned only after corresponding scopes are added. If you do not need the fields, it is not recommended that you request the scopes.<br>Obtain user ID(contact:user.employee_id:readonly)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Path parameters

Parameter | Type | Description
---|---|---
spreadsheet_token | string | Spreadsheet token<br>**Example value**: "shtxxxxxxxxxxxxx"
sheet_id | string | Worksheet id<br>**Example value**: "0354d1"

### Query parameters

Parameter | Type | Required | Description
---|---|---|---
datetime_render_option | string | No | Time Date Rendering Options<br>**Example value**: formatted_string<br>**Optional values are**:<br>- formatted_string：Format date as string<br>- serial_number：Returns the number of days since December 30, 1899
value_render_option | string | No | Numerical rendering options<br>**Example value**: formatted_value<br>**Optional values are**:<br>- formatted_value：Format numeric values in number format<br>- unformatted_value：Original value
user_id_type | string | No | User ID categories<br>**Example value**: open_id<br>**Optional values are**:<br>- open_id：Identifies a user to an app. The same user has different Open IDs in different apps. [How to get Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid)<br>- union_id：Identifies a user to a tenant that acts as a developer. A user has the same Union ID in apps developed by the same developer, and has different Union IDs in apps developed by different developers. A developer can use Union ID to link the same user's identities in multiple apps.[How to get Union ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id)<br>- user_id：Identifies a user to a tenant. The same user has different User IDs in different tenants. In one single tenant, a user has the same User ID in all apps （including store apps）. User ID is usually used to communicate user data between different apps. [How to get User ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**Default value**: `open_id`<br>**When the value is `user_id`, the following field scopes are required**:<br>Obtain user ID(contact:user.employee_id:readonly)

### Request body

Parameter | Type | Required | Description
---|---|---|---
ranges | string\[\] | No | Multiple ranges of the same worksheet. For details, see [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)<br>**Example value**: ["S8MX1N! A1: B2"]

### Request body example
```json
{
    "ranges": [
        "0WVC18!A1:A1",
        "0WVC18!G2:G2"
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
value_ranges | value\[\] | Data list
range | string | Range. For details, see [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)
values | cell_value\[\]\[\]\[\] | Data,For data structure, see  [Data Structure](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet-value/cell-data-structure)

### Response body example
```json
{
    "code": 0,
    "data": {
        "value_ranges": [
            {
                "range": "0WVC18!A1:A1",
                "values": [
                    [
                        [
                            {
                                "mention_user": {
                                    "name": "Li Hua",
                                    "user_id": "ou_74f02700fasxxxxxxxx35"
                                },
                                "type": "mention_user"
                            }
                        ]
                    ]
                ]
            },
            {
                "range": "0WVC18!G2:G2",
                "values": [
                    [
                        [
                            {
                                "text": {
                                    "text": "r"
                                },
                                "type": "text"
                            }
                        ]
                    ]
                ]
            }
        ]
    },
    "msg": ""
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
400 | 1310251 | Invalid Parameters | Reference error message in response body
400 | 1310213 | Permission Fail | No permission
400 | 1310249 | Spreadsheet Deleted | Restore the form and try again
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.
400 | 1310226 | Excess Limit | Exceeds the limit
400 | 1310221 | Response Too Large | Reduce the number of requests
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
400 | 1310235 | Retry Later | Please try again later.
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
500 | 1315210 | Server Error | Internal service errors, please consult customer service for details

# Clear cell contents

This interface is used to clear the cell content while preserving the original style of the cell. The number of range cannot exceed 10.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/values/batch_clear
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
spreadsheet_token | string | Spreadsheet token<br>**Example value**: "shtxxxxxxxxxxxxxxxx"
sheet_id | string | Sheet id<br>**Example value**: "0354d1"

### Request body

Parameter | Type | Required | Description
---|---|---|---
ranges | string\[\] | No | Multiple ranges of the same worksheet. For details, see [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)<br>**Example value**: ["XS1JC3!A1:B3"]

### Request body example
```json
{
    "ranges": [
        "XS1JC3!A1:B3"
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

This API is used to merge cells based on spreadsheetToken and dimension information. You can act on up to 5,000 rows and 100 columns at once.

##  Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/merge_cells
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
|spreadsheetToken|string|Yes|Spreadsheet token. For more information about how to obtain the token, see [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)|
###  Request body
|Parameter|Type|Required|Description|
|--|-----|--|----|
|range|string|Yes|Query range, includes the sheetId range and cell range. Four indexing methods are supported. For details, see  [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview).|
|mergeType|string|Yes|Values: "MERGE_ALL": directly merge the selected area, "MERGE_ROWS": merge the selected area by row, and "MERGE_COLUMNS": merge the selected area by column| 
### Request body example
```json
{
        "range": "string", 
        "mergeType": "string"
}
```
### cURL  Request example
```
curl --location --request POST 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/shtcngNygNfuqhxTBf588jabcef/merge_cells' \
--header 'Authorization: Bearer t-e346617a4acfc3a11d4ed24dca0d0c0fc8e0067e' \
--header 'Content-Type: application/json' \
--data-raw '{
        "range": "Q7PlXT!F11:G12", 
        "mergeType": "MERGE_ROWS"
}'
```
##  Response
### Response body
 |Parameter|Type|Description|
|--|-----|--|
|spreadsheetToken|string |spreadsheet token|
### Response body example
```json
{
    "code": 0,
    "data": {
        "spreadsheetToken": "shtcngNygNfuqhxTBf588jabcef"
    },
    "msg": "success"
}

```
### Error code

For details, refer to [Server-side error codes](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN).

# Split cells

This API is used to split cells based on spreadsheetToken and dimension information. You can act on up to 5,000 rows and 100 columns at once.
##  Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/unmerge_cells
HTTP Method | POST
Supported app types | Custom App、Store App
Required scopes<br>**The scopes required to call this API. You can call the API with any of the scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space(drive:drive)<br>View, comment, edit, and manage Sheets(sheets:spreadsheet)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | When calling an API, the app needs to authenticate its identity through an access token. Refer to [Choose and obtain access tokens](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM#5aa2e490).<br>**Value format**："Bearer `access_token`"<br>Supported options are:<br>- `tenant_access_token`：<br>Call the API on behalf of the app. The range of readable and writable data is determined by the app's own [data permission range](https://open.larkoffice.com/document/home/introduction-to-scope-and-authorization/configure-app-data-permissions). Refer to [Get custom app tenant_access_token](https://open.larkoffice.com/document/ukTMukTMukTM/ukDNz4SO0MjL5QzM/auth-v3/auth/tenant_access_token_internal) or [Get store app tenant_access_token](https://open.larkoffice.com/document/ukTMukTMukTM/ukDNz4SO0MjL5QzM/auth-v3/auth/tenant_access_token). **Example value**："Bearer t-g1044qeGEDXTB6NDJOGV4JQCYDGHRBARFTGT1234"<br>- `user_access_token`：<br>Call the API on behalf of the user. The range of readable and writable data is determined by the user's data permission range. Refer to [Get user_access_token](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/authentication-management/access-token/get-user-access-token). **Example value**："Bearer u-cjz1eKCEx289x1TXEiQJqAh5171B4gDHPq00l0GE1234"
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

###  Path parameters
|Parameter|Type|Required|Description|
|--|-----|--|----|
|spreadsheetToken|string|Yes|Spreadsheet token. For more information about how to obtain the token, see [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview).|
###  Request body
|Parameter|Type|Required|Description|
|--|-----|--|----|
|range|string|Yes|Query range, includes the sheetId range and cell range. Four indexing methods are supported. For details, see [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview).|
### Request body example
```json
  {
     "range": "string"
  }
```
### cURL Request example
```
curl --location --request POST 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/shtcngNygNfuqhxTBf588jwgWbJ/unmerge_cells' \
--header 'Authorization: Bearer t-e346617a4acfc3a11d4ed24dca0d0c0fc8e0067e' \
--header 'Content-Type: application/json' \
--data-raw '  {
     "range": "Q7PlXT!F7:F8"
  }'
```
##  Response
### Response body
  |Parameter|Type|Description|
|--|-----|--|
|spreadsheetToken|string |Spreadsheet token|
### Response body example
```json
{
    "code": 0,
    "data": {
        "spreadsheetToken": "***"
    },
    "msg": "Success"
}

```
### Error code

For details, refer to [Server-side error codes](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN).

# Search

Search cell locations that match specified conditions in a certain range of the sheet. The range and find fields are required in the request body.

**Notice**：Notes:
- When the request range is larger than the actual data area, such as worksheet only 200 rows, but the range filled in is 1 to 201 rows, the API will return error code `1310202`

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/find
HTTP Method | POST
Rate Limit | [100 per minute](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.**<br>Enable any scope from the list | View, comment, edit, and manage all files in My Space(drive:drive)<br>View, comment, and download all files in My Space(drive:drive:readonly)<br>View, comment, edit, and manage Sheets(sheets:spreadsheet)<br>View, comment, and export Sheets(sheets:spreadsheet:readonly)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Path parameters

Parameter | Type | Description
---|---|---
spreadsheet_token | string | Sheet token,[how to get related cloud document resources]((https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN))<br>**Example value**: "shtcnmBA*****yGehy8"
sheet_id | string | Sheet ID, [how to get worksheet id](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet/query)<br>**Example value**: "0b**12"

### Request body

Parameter | Type | Required | Description
---|---|---|---
find_condition | find_condition | Yes | Search conditions
range | string | Yes | Search range, [glossary range](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)<br>**Example value**: "0b**12!A1:H10"
match_case | boolean | No | Whether it is case insensitive<br>- `true`: Ignore differences in case of letters in a string<br>- `false`: case sensitive<br>**Example value**: true
match_entire_cell | boolean | No | Whether to match the entire cell<br>- `true`: exact match<br>- `false`: partial match<br>**Example value**: false
search_by_regex | boolean | No | Whether it is regular expression matching<br>- `true`: regular match<br>- `false`: not regular match<br>**Example value**: false
include_formulas | boolean | No | Whether to search formula content<br>- `true`: search formula only<br>- `false`: Search cell contents only<br>**Example value**: false
find | string | Yes | Found string<br>**Example value**: "如下<br>- Common lookup example: "hello"<br>- Regular lookup example：”[A-Z]\w+“"

### Request body example
```json
{
    "find_condition": {
        "range": "PNIfrm!A1:C5",
        "match_case": true,
        "match_entire_cell": false,
        "search_by_regex": false,
        "include_formulas": false
    },
    "find": "hello"
}
```

### Request example 
```bash 
 Curl --location --request POST 'https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/shtcnmBA ***** yGehy8/sheets/PNIfrm/find'\ 
 --Header 'Authorization: Bearer u-3iqkd6KWzRLzNeXfeuCMEb'\ 
 --Header'Content-Type: application/json '\ 
 --Data-raw '{ 
 "find_condition": { 
 "Range": "PNIfrm! A1: C5", 
 "match_case": true, 
 "match_entire_cell": false, 
 "search_by_regex": false, 
 "include_formulas": false 
 }, 
 "Find": "hello" 
 } ' 
 ```

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
find_result | find_replace_result | Search return information that matches conditions
matched_cells | string\[\] | Array of cells that meet the search conditions, not including formulas, such as: ["A1", "A2"...]
matched_formula_cells | string\[\] | Array of cells that meet the search conditions including formulas, such as: ["B3", "H7"...]
rows_count | int | Total rows that meet search conditions

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "find_result": {
            "matched_cells": [
                "A1"
            ],
            "matched_formula_cells": [
                "B3"
            ],
            "rows_count": 2
        }
    }
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
400 | 1310242 | In Mix state | Retey Later
400 | 1310211 | Wrong Sheet Id | Check the sheet_id.
400 | 1310248 | Wrong Regular Expression | Check Regular Expression
400 | 1310202 | Wrong Range | Invalid range
400 | 1310229 | Wrong URL Param | Check the url parameter.
400 | 1310204 | Wrong Request Body | Check the request body parameter.
400 | 1310213 | Permission Fail | No permission
400 | 1310218 | Locked Cell | Check if the action targets a protected range.
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.
400 | 1310215 | Sheet Id Not Found | Check the sheet_id.
400 | 1310226 | Excess Limit | Exceeds the limit
400 | 1310217 | Too Many Request | Check if requests have been sent too frequently.
400 | 1310235 | Retry Later | Please try again later.
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
400 | 1310249 | Spreadsheet Deleted | Restore the form and try again

# Replace cells

Find data that matches specified conditions in a certain range of the sheet, replace the values, and return the location of the successfully replaced cell. You can replace up to 5,000 cells at a time. If the number of matching cells exceeds the limit, narrow the range before the action. The range, find, and replacement fields are required in the request body.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/replace
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
spreadsheet_token | string | Spreadsheet token<br>**Example value**: "Iow7sNNEphp3WbtnbCscPqabcef"
sheet_id | string | Sheet id<br>**Example value**: "PNIfrm"

### Request body

Parameter | Type | Required | Description
---|---|---|---
find_condition | find_condition | Yes | Search conditions
range | string | Yes | Search range, [glossary range](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)<br>**Example value**: "PNIfrm!A1:H10"
match_case | boolean | No | Whether it is case insensitive<br>- `true`: Ignore differences in case of letters in a string<br>- `false`: case sensitive<br>**Example value**: true
match_entire_cell | boolean | No | Whether to match the entire cell<br>- `true`: exact match<br>- `false`: partial match<br>**Example value**: false
search_by_regex | boolean | No | Whether it is regular expression matching<br>- `true`: regular match<br>- `false`: not regular match<br>**Example value**: false
include_formulas | boolean | No | Whether to search formula content<br>- `true`: search formula only<br>- `false`: Search cell contents only<br>**Example value**: false
find | string | Yes | Found string<br>**Example value**: "hello"
replacement | string | Yes | Replaced string<br>**Example value**: "world"

### Request body example
```json
{
    "find_condition": {
        "range": "PNIfrm!A1:H10",
        "match_case": true,
        "match_entire_cell": false,
        "search_by_regex": false,
        "include_formulas": false
    },
    "find": "hello",
    "replacement": "world"
}
```

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
replace_result | find_replace_result | Find and replace matching cell information
matched_cells | string\[\] | Array of cells that meet the search conditions, not including formulas, such as: ["A1", "A2"...]
matched_formula_cells | string\[\] | Array of cells that meet the search conditions including formulas, such as: ["B3", "H7"...]
rows_count | int | Total rows that meet search conditions

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "replace_result": {
            "matched_cells": [
                "A1"
            ],
            "matched_formula_cells": [
                "B3"
            ],
            "rows_count": 2
        }
    }
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
400 | 1310242 | In Mix state | Retey Later
400 | 1310211 | Wrong Sheet Id | Check the sheet_id.
400 | 1310248 | Wrong Regular Expression | Check Regular Expression
400 | 1310202 | Wrong Range | Invalid range
400 | 1310229 | Wrong URL Param | Check the url parameter.
400 | 1310204 | Wrong Request Body | Check the request body parameter.
400 | 1310213 | Permission Fail | No permission
400 | 1310218 | Locked Cell | Check if the action targets a protected range.
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.
400 | 1310215 | Sheet Id Not Found | Check the sheet_id.
400 | 1310226 | Excess Limit | Exceeds the limit
400 | 1310217 | Too Many Request | Check if requests have been sent too frequently.
400 | 1310235 | Retry Later | Please try again later.
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
500 | 1315210 | Server Error | Internal service errors, please consult customer service for details
400 | 1310249 | Spreadsheet Deleted | Restore the form and try again

# Set cell style

This API is used to set the cell style based on spreadsheetToken, range, and style information. You can act on up to 5,000 rows and 100 columns. It is recommended to limit the number of cells updated at a time to no more than 30,000 when setting border styles. 

##  Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/style
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
|spreadsheetToken|string|Yes| Spreadsheet token. For more information about how to obtain the token, see  [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview).|
###  Request body
**Request parameter description** :  <br>
|Parameter|Type|Required|Description|
|--|-----|--|----|
|appendStyle||Yes|Set cell style
|&emsp;∟range|string|Yes|Query range, includes the sheetId range and cell range. Four indexing methods are supported. For details, see [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview).|
|&emsp;∟style||Yes|The style to update| 
|&emsp;&emsp;∟font| |No|Font style|
|&emsp;&emsp;&emsp;∟bold|bool|No|Bold|
|&emsp;&emsp;&emsp;∟italic|bool|No|Italics| 
|&emsp;&emsp;&emsp;∟fontSize|string|No|Font size: 9 to 36, line spacing fixed at 1.5, for example: 10pt/1.5| 
|&emsp;&emsp;&emsp;∟clean|bool|No|Clear font formatting, default: false| Request body |
|&emsp;&emsp;∟textDecoration|int|No|Text decoration, 0: default, 1: underline, 2: strikethrough, 3: underline and strikethrough|
|&emsp;&emsp;∟formatter|string|No|Number format. For details, see the appendix  [Number formats supported by sheet](https://open.larkoffice.com/document/ukTMukTMukTM/uMjM2UjLzIjN14yMyYTN) .| 
|&emsp;&emsp;∟hAlign|int|No|Horizontal align, 0: Align left, 1: Align center, 2: Align right | 
|&emsp;&emsp;∟vAlign|int|No|Vertical align, 0: Align top, 1: Align center, 2: Align bottom| 
|&emsp;&emsp;∟foreColor|string|No|Text color| 
|&emsp;&emsp;∟backColor|string|No|Background color|
|&emsp;&emsp;∟borderType|string|No|Border type, values: "FULL_BORDER", "OUTER_BORDER", "INNER_BORDER", "NO_BORDER", "LEFT_BORDER", "RIGHT_BORDER", "TOP_BORDER", and "BOTTOM_BORDER"| 
|&emsp;&emsp;∟borderColor|string|No|Border color| 
|&emsp;&emsp;∟clean|bool|No|Whether to clear all formatting, default: false| 
### Request body example

```json
{
	"appendStyle":{
       "range": "string",
       "style":{
            "font":{
                "bold":true,
                "italic":true,
                "fontSize":"10pt/1.5",
                "clean":false  
                },    
            "textDecoration":0,
            "formatter":"",
            "hAlign": 0 , 
            "vAlign":0,   
            "foreColor":"#000000",
            "backColor":"#21d11f",
            "borderType":"FULL_BORDER",
            "borderColor": "#ff0000",
            "clean": false 
            }
        }
}
```
### cURL Request example
```
curl --location --request PUT 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/shtcngNygNfuqhxTBf588jwgWbJ/style' \
--header 'Authorization: Bearer t-e346617a4acfc3a11d4ed24dca0d0c0fc8e0067e' \
--header 'Content-Type: application/json' \
--data-raw '{
  "appendStyle":{
     "range": "BzY8T5!A3:C4",
     "style":{
          "font":{
              "bold":true,
              "italic":true,
              "fontSize":"10pt/1.5",
              "clean":false  
              },    
          "textDecoration":0,
          "formatter":"",
          "hAlign": 0 , 
          "vAlign":0,   
          "foreColor":"#000000",
          "backColor":"#21d11f",
          "borderType":"FULL_BORDER",
          "borderColor": "#ff0000",
          "clean": false 
          }
      }
}'
```
##  Response
### Response body
  |Parameter|Type|Description|
|--|-----|--|
|spreadsheetToken|string |spreadsheet   token|
|updatedRange|string |Range for which to set the style|
|updatedRows|int|Number of rows for which to set the style|
|updatedColumns|int|Number of columns for which to set the style|
|updatedCells|int|Total cells for which to set the style|
|revision|int|Version number of sheet |

###  Response body example 
```json
{
    "code": 0,
    "msg": "Success",
    "data":{
      "spreadsheetToken": "string",
      "updatedRange": "string",
      "updatedRows": 0,
      "updatedColumns": 0,
      "updatedCells": 0,
      "revision": 0
	}
}
```

### Error code

For details, refer to [Server-side error codes](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN).

# Set cell styles in batches

This API is used to set the style of multiple cells based on spreadsheetToken, range, and style information. You can act on up to 5,000 rows and 100 columns. It is recommended to limit the number of cells updated at a time to no more than 30,000 when setting border styles. When an area is covered by multiple ranges, only the last style will be applied. 
##  Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v2/spreadsheets/:spreadsheetToken/styles_batch_update
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
|spreadsheetToken|string|Yes|Spreadsheet token. For more information about how to obtain the token, see [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview)| URL PATH.|
###  Request body
|Parameter|Type|Required|Description|
|--|-----|--|----|
|data||Yes|Request data|
|&emsp;∟ranges|array<string>|Yes|Query range, includes the sheetId range and cell range. Four indexing methods are supported. For details, see  [Sheets Developer's Guide](https://open.larkoffice.com/document/ukTMukTMukTM/uATMzUjLwEzM14CMxMTN/overview).|
|&emsp;∟style||Yes|The style to update|
|&emsp;&emsp;∟font| |No|Font style|
|&emsp;&emsp;&emsp;∟bold|bool|No|Bold|
|&emsp;&emsp;&emsp;∟italic|bool|No|Italics|
|&emsp;&emsp;&emsp;∟fontSize|string|No|Font size: 9 to 36, line spacing fixed at 1.5, for example:10pt/1.5| |&emsp;&emsp;∟clean|bool|No|Clear font style, default value: false|
|&emsp;&emsp;∟textDecoration|int|No|Text decoration, 0: default, 1: underline, 2: strikethrough, 3: underline and strikethrough|  
|&emsp;&emsp;∟formatter|string| No |Number format. For details, see the appendix [Number formats supported by sheets](https://open.larkoffice.com/document/ukTMukTMukTM/uMjM2UjLzIjN14yMyYTN) .|
|&emsp;&emsp;∟hAlign|int|No|Horizontal align, 0: Align left, 1: Align center, 2: Align right |
|&emsp;&emsp;∟vAlign|int|No|Vertical align, 0: Align top, 1: Align center, 2: Align bottom|
|&emsp;&emsp;∟foreColor|string|No|Text color|
|&emsp;&emsp;∟backColor|string|No|Background color|
|&emsp;&emsp;∟borderType|string|No|Border type, values: "FULL_BORDER", "OUTER_BORDER", "INNER_BORDER", "NO_BORDER", "LEFT_BORDER", "RIGHT_BORDER", "TOP_BORDER", and "BOTTOM_BORDER"|
|&emsp;&emsp;∟borderColor|string|No|Border color|
|&emsp;&emsp;∟clean|bool|No|Whether to clear all formatting, default: false| 
### Request body example
```json
{
    "data":[
        {
            "ranges":[
                "string",
                "string"
            ],
            "style":{
                "font":{
                    "bold":true,
                    "italic":true,
                    "fontSize":"10pt/1.5",
                    "clean":false
                },
                "textDecoration":0,
                "formatter":"",
                "hAlign":0,
                "vAlign":0,
                "foreColor":"#000000",
                "backColor":"#21d11f",
                "borderType":"FULL_BORDER",
                "borderColor":"#ff0000",
                "clean":false
            }
        },
        {
            "ranges":[
                "string"
            ],
            "style":{
              ...
            }
        }
    ]
}
```

###  cURL Request example
```
curl --location --request PUT 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/shtcngNygNfuqhxTBf588jwgWbJ/styles_batch_update' \
--header 'Authorization: Bearer t-e346617a4acfc3a11d4ed24dca0d0c0fc8e0067e' \
--header 'Content-Type: application/json' \
--data-raw '{
    "data":[
        {
            "ranges":[
                "Q7PlXT!C7:E12",
                "Q7PlXT!I20:K27"
            ],
            "style":{
                "font":{
                    "bold":true,
                    "italic":true,
                    "fontSize":"10pt/1.5",
                    "clean":false
                },
                "textDecoration":0,
                "formatter":"",
                "hAlign":0,
                "vAlign":0,
                "foreColor":"#000000",
                "backColor":"#21d11f",
                "borderType":"FULL_BORDER",
                "borderColor":"#ff0000",
                "clean":false
            }
        },
        {
            "ranges":[
                "BzY8T5!A1:C2"
            ],
            "style":{
                "font":{
                    "bold":true,
                    "italic":true,
                    "fontSize":"10pt/1.5",
                    "clean":false
                },
                "textDecoration":0,
                "formatter":"",
                "hAlign":0,
                "vAlign":0,
                "foreColor":"#000000",
                "backColor":"#21d11f",
                "borderType":"FULL_BORDER",
                "borderColor":"#ff0000",
                "clean":false
            }
        }
    ]
}
'
```

##  Response
### Response body
  |Parameter|Type|Description|
|--|-----|--|
|spreadsheetToken|string | Spreadsheet token|
|totalUpdatedRows|int|Total rows for which to set the style|
|totalUpdatedColumns|int|Total columns for which to set the style|
|totalUpdatedCells|int|Total cells for which to set the style|
|revision|int|Version number of sheet |
|responses||Range and number of rows and columns for which to set the cell style for each range|
|&emsp;∟spreadsheetToken|string |Spreadsheet token|
|&emsp;∟updatedRange|string |Range for which to set the style|
|&emsp;∟updatedRows|int|Number of rows for which to set the style|
|&emsp;∟updatedColumns|int|Number of columns for which to set the style|
|&emsp;∟updatedCells|int|Number of cells for which to set the style|
### Response body example
```json
{
    "code": 0,
    "msg": "Success",
    "data": {
        "spreadsheetToken": "string",
        "totalUpdatedCells": 0,
        "totalUpdatedColumns": 0,
        "totalUpdatedRows": 0,
        "revision": 0,
        "responses": [
            {
                "spreadsheetToken": "string",
                "updatedRange": "string",
                "updatedRows": 0,
                "updatedColumns": 0,
                "updatedCells": 0
            }
        ]
    }
}
```
### Error code

For details, refer to [Server-side error codes](https://open.larkoffice.com/document/ukTMukTMukTM/ugjM14COyUjL4ITN).
