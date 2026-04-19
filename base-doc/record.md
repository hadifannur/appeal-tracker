# Base record data structure
Each row of data in a multi-dimensional table is a record. The data in a record is represented by the `fields` parameter. This document describes the data structure of the multi-dimensional table record data `fields`.

![](//sf3-cn.feishucdn.com/obj/open-platform-opendoc/abc84b39be159ccdcafa707ee141144d_hLPkqUf5x5.png?height=503&lazyload=true&maxWidth=750&width=1536)

## Example of fields

In the above image, the highlighted data structure of the record is shown below:

```json
{
  "fields": {
    "Task Summary": [
      {
        "text": "The website update task is handled by Huang Paopao and is in progress.",
        "type": "text"
      }
    ],
    "Task Executor": [
      {
        "avatar_url": "https://s1-imfile.feishucdn.com/static-resource/v1/v3_00g2_058610dc-f65c-40c5-afac-46e83919630g~?image_size=72x72&cut_type=default-face&quality=&format=jpeg&sticker_format=.webp",
        "email": "amandahuang@bytedance.com",
        "en_name": "Amanda Huang",
        "id": "ou_8240099442cf5da49f04f4bf8f8abcef",
        "name": "Huang Paopao"
      }
    ],
    "Task Description": [
      {
        "text": "Update the company website",
        "type": "text"
      }
    ],
    "Start Date": 1675440000000,
    "Is Delayed": {
      "type": 1,
      "value": [
        {
          "text": "✅ Normal",
          "type": "text"
        }
      ]
    }
  }
}
```

## Structure of fields

The `fields` field is a map consisting of key-value pairs formed by the field names of the table and their specific content.
```json
{
  "Task Summary": [
    {
      "text": "The website update task is handled by Huang Paopao and is in progress.",
      "type": "text"
    }
  ]
}
```

Parameter | Data Type | Description | Example Value
---|---|---|---
key | string | The field name in the multi-dimensional table. | "Task Summary"
value | union | The specific content of a field, which can be a number, string, boolean, list of strings, or list of objects. For more details, refer to the sections below. | This example value is a list of objects; for more examples, see below.<br>```json<br>[<br>{<br>"text": "The website update task is in progress.",<br>"type": "text"<br>}<br>]<br>```

### Structure of key

The key in the `fields` field is always of string type, corresponding to the title of each column in the multi-dimensional table, such as "Task Summary".

### Structure of value

This section introduces the data types and examples of the value structure corresponding to different field types in `fields`.

Field Type type Enumeration | Field Type | value Data Type | value Description | value Example Value | Limitations
---|---|---|---|---|---
1 | Text, Email, or Barcode. Use <code>ui_type</code> to distinguish; for details, refer to the description in the **Text, Email, or Barcode** section below. | When writing, it is a string; when returning, it is a list of objects. | Please refer to the description in the **Text, Email, or Barcode** section below. | Please refer to the examples in the **Text, Email, or Barcode** section below. | None
2 | Number, Progress, Currency, or Rating. Use <code>ui_type</code> to distinguish:<br>- When <code>ui_type</code> is "Number", the field type is a number<br>- When <code>ui_type</code> is "Progress", the field type is progress<br>- When <code>ui_type</code> is "Currency", the field type is currency<br>- When <code>ui_type</code> is "Rating", the field type is rating | number | Numeric type | <code>0.5</code> | None
3 | Single Choice | string | Text of the option name | <code>"In Progress"</code> | The total number of options in a single-choice field cannot exceed 5,000
4 | Multiple Choice | array&lt;string&gt; | An array containing multiple option name strings | ```json<br>[<br>"Approval Integration",<br>"Office Management",<br>"Identity Management"<br>]<br>``` | - The total number of options in a multiple-choice field cannot exceed 5,000<br>- The number of options in a single cell cannot exceed 1,000
5 | Date | number | Unix timestamp, in milliseconds | <code>1675526400000</code> | None
7 | Checkbox | boolean | Optional values:<br>- true: Checked style<br>- false: Unchecked style | <code>true</code> | None
11 | Person | list of object | For fields of type person, the elements in the value are defined as follows:<br>- id: User ID of the person, supports open_id, union_id, and user_id<br>- name: Person's name (Not supported to pass in through the writing interface)<br>- avatar_url: Link to the person's avatar (Not supported to pass in through the writing interface)<br>- en_name: Person's English name (Not supported to pass in through the writing interface)<br>- email: Person's email (Not supported to pass in through the writing interface) | ```json<br>[<br>{<br>"avatar_url": "https://s1-imfile.feishucdn.com/static-resource/v1/v3_00g2_058610dc-f65c-40c5-afac-46e83919630g~?image_size=72x72&cut_type=default-face&quality=&format=jpeg&sticker_format=.webp",<br>"email": "amandahuang@bytedance.com",<br>"en_name": "Amanda Huang",<br>"id": "ou_8240099442cf5da49f04f4bf8f8abcef",<br>"name": "Huang Paopao"<br>}<br>]<br>``` | The number of people in a single cell cannot exceed 1,000
13 | Phone Number | string | Phone number, string matching the regular expression (\+)?\d* | <code>"17899870000"</code> | The length of the phone number cannot exceed 64
15 | Hyperlink | object | For fields of type hyperlink, the elements in the value are defined as follows:<br>- text: Text displayed in the hyperlink<br>- link: URL | ```json<br>{<br>"link": "https://open.feishu.cn/document/home/index",<br>"text": "Feishu Open Platform"<br>}<br>``` | None
17 | Attachment | list of object | Please refer to the description in the **Attachment** section below. | Please refer to the examples in the **Attachment** section below. | The number of attachments in a single cell cannot exceed 100
18 | One-way Association | object | For fields of type one-way association, the elements in the value are defined as follows:<br>- link_record_ids: Associated record IDs, of array type, can contain multiple record ID strings. | ```json<br>{<br>"link_record_ids": [<br>"reclzUoBLn",<br>"rec7bYQoX1",<br>"recFIE3n52"<br>]<br>}<br>``` | The number of One-way associations in a single cell cannot exceed 500
19 | Lookup Reference | object | Lookup references are essentially formulas. Its value definition is the same as that of a formula. Please refer to the description in the **Formula or Lookup Reference** section below. | Please refer to the description in the **Formula or Lookup Reference** section below. | None
20 | Formula | object | Please refer to the description in the **Formula or Lookup Reference** section below. | Please refer to the examples in the **Formula or Lookup Reference** section below. | None
21 | Bidirectional Association | object | For fields of type bidirectional association, the elements in the value are defined as follows:<br>- link_record_ids: Associated record IDs, of array type, can contain multiple record ID strings. | ```json<br>{<br>"link_record_ids": [<br>"reclzUoBLn",<br>"rec7bYQoX1",<br>"recFIE3n52"<br>]<br>}<br>``` | The number of bidirectional associations in a single cell cannot exceed 500
22 | Geolocation | object | For fields of type geolocation, the elements in the value are defined as follows:<br>- location: Latitude and longitude<br>- pname: Province<br>- cityname: City<br>- adname: District<br>- address: Detailed address<br>- name: Place name<br>- full_address: Complete address | ```json<br>{<br>"address": "10 Xueqing Road, Xueqing Jiachang Building",<br>"adname": "Haidian District",<br>"cityname": "Beijing",<br>"full_address": "ByteDance, Beijing, Haidian District, 10 Xueqing Road, Xueqing Jiachang Building",<br>"location": "116.352681,40.01437",<br>"name": "ByteDance",<br>"pname": "Beijing"<br>}<br>``` | None
23 | Group | list of object | For fields of type group, the elements in the value are defined as follows:<br>- name: Group name<br>- avatar_url: Link to the group avatar<br>- id: Group ID | ```json<br>[<br>{<br>"avatar_url": "https://s1-imfile.feishucdn.com/static-resource/avatar/default-avatar_9fb72564-d52a-49b0-9de8-f79071a02286_96.webp",<br>"id": "oc_d2a947abb78bbbbb12d4cad55fbabcef",<br>"name": "Test Department"<br>}<br>]<br>``` | The number of groups in a single cell cannot exceed 10
1001 | Creation Time | number | Unix timestamp, in milliseconds. | <code>1675526400000</code> | -
1002 | Last Update Time | number | Unix timestamp, in milliseconds. | <code>1675526400000</code> | -
1003 | Creator | object | For fields of type person, the elements in the value are defined as follows:<br>- id: User ID of the person, supports open_id, union_id, and user_id<br>- name: Person's name (Not supported to pass in through the writing interface)<br>- avatar_url: Link to the person's avatar (Not supported to pass in through the writing interface)<br>- en_name: Person's English name (Not supported to pass in through the writing interface)<br>- email: Person's email (Not supported to pass in through the writing interface) | ```json<br>[<br>{<br>"avatar_url": "https://s1-imfile.feishucdn.com/static-resource/v1/v3_00g2_058610dc-f65c-40c5-afac-46e83919630g~?image_size=72x72&cut_type=default-face&quality=&format=jpeg&sticker_format=.webp",<br>"email": "amandahuang@bytedance.com",<br>"en_name": "Amanda Huang",<br>"id": "ou_8240099442cf5da49f04f4bf8f8abcef",<br>"name": "Huang Paopao"<br>}<br>]<br>``` | None
1004 | Modifier | object | For fields of type person, the elements in the value are defined as follows:<br>- id: User ID of the person, supports open_id, union_id, and user_id<br>- name: Person's name (Not supported to pass in through the writing interface)<br>- avatar_url: Link to the person's avatar (Not supported to pass in through the writing interface)<br>- en_name: Person's English name (Not supported to pass in through the writing interface)<br>- email: Person's email (Not supported to pass in through the writing interface) | ```json<br>[<br>{<br>"avatar_url": "https://s1-imfile.feishucdn.com/static-resource/v1/v3_00g2_058610dc-f65c-40c5-afac-46e83919630g~?image_size=72x72&cut_type=default-face&quality=&format=jpeg&sticker_format=.webp",<br>"email": "amandahuang@bytedance.com",<br>"en_name": "Amanda Huang",<br>"id": "ou_8240099442cf5da49f04f4bf8f8abcef",<br>"name": "Huang Paopao"<br>}<br>]<br>``` | None
1005 | Auto Number | string | A string composed of automatic numbering rules. | `"1"` | None

#### Text, Email, or Barcode

When the field type `type` enumerates to 1, the field type is distinguished based on `ui_type`, which can be text, email, or barcode. For details, refer to the following sections.

- When `ui_type` is "Text", the field is of text type, and the elements in its `value` are defined as follows:

Parameter | Data Type | Description
---|---|---
type | string | The text display type, optional values are:<br>- text: plain text type<br>- mention: mention user or cloud document type<br>- url: hyperlink type
text | string | The text content
token | string | This field is valid when the type field is mention.<br>- When mentionType is User, token is the user ID<br>- When mentionType is Docx, token is the document's document_id<br>- When mentionType is Sheet, token is the spreadsheet's spreadsheet_token<br>- When mentionType is Bitable, token is the multidimensional table's app_token
link | string | The link. This field is valid when the type field is url
mentionType | string | This field is valid when the type field is mention. The optional values are:<br>- User: mention user<br>- Docx: mention document<br>- Sheet: mention spreadsheet<br>- Bitable: mention multidimensional table
mentionNotify | boolean | This field is valid when the type field is mention and the mentionType field is User. The optional values are:<br>- false: do not mention this user<br>- true: mention this user
name | string | The name of the mentioned user. This field is valid when the type field is mention and the mentionType field is User

<br>
- When `ui_type` is "Barcode", the field type is barcode type, and an example of its value is as follows:
    - type: fixed value "text"
    - text: barcode number
      ```json
      [
        {
          "text": "FS0001",
          "type": "text"
        }
      ]
      ```
- When `ui_type` is "Email", the field type is email type, and an example of its value is as follows:
    - link: the URL link to the email
    - type: fixed value "url"
    - text: user email
      ```json
      {
        "link": "mailto:zhangmin@bytedance.com",
        "text": "zhangmin@bytedance.com",
        "type": "url"
      }
      ```

#### Attachments

For fields of attachment type, the elements in the value are defined as follows:

Parameter | Data Type | Description
---|---|---
file_token | string | The token of the attachment. You can use the download material interface to download this attachment
name | string | The name of the attachment
type | string | The mime type of the attachment, e.g., image/png
size | int | The size of the attachment. Unit: bytes
url | string | The attachment URL link, requires access token authentication. You can use the download material interface to download this attachment
tmp_url | string | The URL link for generating a temporary download link for the attachment, requires access token authentication. You can use the interface to obtain the temporary download link for materials

An example of the value for attachment type is as follows:
```json
[
  {
    "file_token": "J7GdbgNWWoD1fwx7oWccxdgknIe",
    "name": "58cc930b89.png",
    "size": 108867,
    "tmp_url": "https://open.feishu.cn/open-apis/drive/v1/medias/batch_get_tmp_download_url?file_tokens=J7GdbgNWWoD1fwx7oWccxdgknIe&extra=%7B%22bitablePerm%22%3A%7B%22tableId%22%3A%22tblx0Ed2NnBULN6a%22%2C%22rev%22%3A5%7D%7D",
    "type": "image/png",
    "url": "https://open.feishu.cn/open-apis/drive/v1/medias/J7GdbgNWWoD1fwx7oWccxdgknIe/download?extra=%7B%22bitablePerm%22%3A%7B%22tableId%22%3A%22tblx0Ed2NnBULN6a%22%2C%22rev%22%3A5%7D%7D"
  }
]
```

#### Formula or Lookup Reference

For fields of formula or lookup reference type, the elements in the value are defined as follows:

Parameter | Data Structure | Description
---|---|---
type | number | Used to specify the data type of the value, optional values are as follows (the same field type is distinguished by ui_type):<br>- 1: Text, Barcode<br>- 2: Number, Progress, Currency, Rating<br>- 3: Single Select<br>- 4: Multi Select<br>- 5: Date<br>- 7: Checkbox<br>- 11: User<br>- 13: Phone Number<br>- 15: Hyperlink<br>- 17: Attachment<br>- 18: Single Link<br>- 19: Lookup Reference<br>- 20: Formula<br>- 21: Duplex Link<br>- 22: Geographic Location<br>- 23: Group<br>- 1001: Creation Time<br>- 1002: Last Modified Time<br>- 1003: Creator<br>- 1004: Modifier<br>- 1005: Auto Number
ui_type | string | The UI type of the field, optional values are as follows:<br>- Text: Text<br>- Barcode: Barcode<br>- Number: Number<br>- Progress: Progress<br>- Currency: Currency<br>- Rating: Rating<br>- SingleSelect: Single Select<br>- MultiSelect: Multi Select<br>- DateTime: Date<br>- Checkbox: Checkbox<br>- User: User<br>- GroupChat: Group<br>- Phone: Phone Number<br>- Url: Hyperlink<br>- Attachment: Attachment<br>- SingleLink: Single Link<br>- Formula: Formula<br>- DuplexLink: Duplex Link<br>- Location: Geographic Location<br>- CreatedTime: Creation Time<br>- ModifiedTime: Last Modified Time<br>- CreatedUser: Creator<br>- ModifiedUser: Modifier<br>- AutoNumber: Auto Number
value | list | The type field determines the data structure of the value; refer to the value structure in this document. **Note**: When the corresponding base type data structure is not in list format, this field will be in the corresponding data's list format.

An example of the value for formula or lookup reference type is as follows:
```json
{
  "type": 1,
  "value": [
    {
      "text": "✅ Normal",
      "type": "text"
    }
  ]
}
```

# Record filter development guide

In some Base APIs, you can set filtering conditions using request parameters such as `filter` to retrieve the records you need. This document explains how to fill in the filtering parameters.
## Filter description

The description and structure of the `filter` parameter are as follows. For more information, refer to [search records](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/search).

Parameter Name | Data Type | Description
---|---|---
filter | filter_info | An object containing filter information.
└ conjunction | string | Represents the logical conjunction between conditions, which can be "and" or "or".
└ conditions | condition[] | A collection of filtering conditions.
└ └ field_name | string | The name of the condition field.
└ └ operator | string | The condition operator. Its optional values are:<br>- `is`: is<br>- `isNot`: is not<br>- `contains`: contains<br>- `doesNotContain`: does not contain<br>- `isEmpty`: is empty<br>- `isNotEmpty`: is not empty<br>- `isGreater`: greater than<br>- `isGreaterEqual`: greater than or equal to<br>- `isLess`: less than<br>- `isLessEqual`: less than or equal to<br>- `like`: LIKE operator. Not supported yet<br>- `in`: IN operator. Not supported yet
└ └ value | string[] | The value of the condition, which can be a single value or an array of multiple values. Different field types and different operators can have different fillable values. For details, refer to the instructions below.

The structure of filter is as follows:

```json
{
  "filter": {
    "conjunction": "and",
    "conditions": [
      {
        "field_name": "字段1",
        "operator": "is",
        "value": [
          "文本内容"
        ]
      }
    ]
  }
}
```

## filter usage example

Below is a table of employee sales figures. This section provides examples of using the `filter` parameter based on this table.
| Employee Name   | Position           | Sales        |
|-----------------|--------------------|--------------|
| John Smith      | Junior Salesperson | 10,000.0    |
| Emily Johnson   | Junior Salesperson | 15,000.0    |
| Michael Brown   | Junior Salesperson | 20,000.0    |
| Linda Davis     | Senior Salesperson | 30,000.0    |
| James Wilson    | Senior Salesperson | 50,000.0    |
| Jennifer Miller | Sales Manager      | 100,000.0   |

- To filter records where the position is "Junior Salesperson" **and** sales are greater than 10000, the example of the filter parameter is shown below:

```JSON
  {
    "filter": {
      "conjunction": "and",
      "conditions": [
        {
          "field_name": "Position",
          "operator": "is",
          "value": [
            "Junior Salesperson"
          ]
        },
        {
          "field_name": "Sales",
          "operator": "isGreater",
          "value": [
            "10000.0"
          ]
        }
      ]
    }
  }

- To filter records where the position is "Senior Salesperson" or sales are greater than 20000, the example of the filter parameter is shown below:
  ```json
  {
    "filter": {
      "conjunction": "or",
      "conditions": [
        {
          "field_name": "Position",
          "operator": "is",
          "value": [
            "Senior Salesperson"
          ]
        },
        {
          "field_name": "Sales",
          "operator": "isGreater",
          "value": [
            "20000.0"
          ]
        }
      ]
    }
  }
  ```
- To filter records where the position is "Junior Salesperson" **or** "Senior Salesperson" **and** the sales amount is 10000 **or** 20000, the filter parameter example is as follows:
As shown in the example, currently only one layer of children parameters is supported, and nested use is not supported.
  ```json
  {
    "filter": {
      "conjunction": "and",
      "children": [
        {
          "conjunction": "or",
          "conditions": [
            {
              "field_name": "职位",
              "operator": "is",
              "value": [
                "Senior Salesperson"
              ]
            },
            {
              "field_name": "职位",
              "operator": "is",
              "value": [
                "Junior Salesperson"
              ]
            }
          ]
        },
        {
          "conjunction": "or",
          "conditions": [
            {
              "field_name": "销售额",
              "operator": "is",
              "value": [
                "10000.0"
              ]
            },
            {
              "field_name": "销售额",
              "operator": "is",
              "value": [
                "20000.0"
              ]
            }
          ]
        }
      ]
    }
  }
  ```
## Field value filling instructions
Base supports the following types of fields as filter conditions. Currently, formula or lookup reference field types are not supported as filter conditions.
**Notice**：When the value is empty [], please ensure to pass the value in the format `"value":[]`, otherwise a missing value error will be reported.

Field type | Value example | Description | Restrictions
---|---|---|---
Multi-line text | <code>["text content"]</code> | Fill in the corresponding text content | - The list can only have one element or no elements<br>- When the operator is `isEmpty` or `isNotEmpty`, fill in the empty value `[]`
Barcode | <code>["barcode content"]</code> | Fill in the corresponding barcode content | - The list can only have one element or no elements<br>- When the operator is `isEmpty` or `isNotEmpty`, fill in the empty value `[]`
Number | <code>["23.4"]</code> | Fill in the corresponding number in string form | - The list can only have one element or no elements<br>- When the operator is `isEmpty` or `isNotEmpty`, fill in the empty value `[]`
Currency | <code>["23.4"]</code> | Fill in the corresponding number in string form | - The list can only have one element or no elements<br>- When the operator is `isEmpty` or `isNotEmpty`, fill in the empty value `[]`
Progress | <code>["0.34"]</code> | Fill in the corresponding number in string form | - The list can only have one element or no elements<br>- When the operator is `isEmpty` or `isNotEmpty`, fill in the empty value `[]`
Rating | <code>["1"]</code> | Fill in the corresponding number in string form | - The list can only have one element or no elements<br>- When the operator is `isEmpty` or `isNotEmpty`, fill in the empty value `[]`
Single choice | <code>["a","b"]</code> | Fill in the options in the list | The list may contain multiple elements:<br>- When the operator is `is` or `isNot`, fill in one element<br>- When the operator is `isEmpty` or `isNotEmpty`, fill in the empty value `[]`<br>- Other operators can fill in multiple elements
Multiple choice | <code>["a","b"]</code> | An array containing multiple option name strings | The list may contain multiple elements:<br>- When the operator is `is` or `isNot`, fill in one element<br>- When the operator is `isEmpty` or `isNotEmpty`, fill in the empty value `[]`<br>- Other operators can fill in multiple elements
Date | <code>["ExactDate","1702449755000"]</code> | Unix timestamp in milliseconds | The list may contain multiple elements, refer to the detailed instructions below for filling in date fields
Checkbox | <code>["true"]</code> or <code>["false"]</code> | Fill in the corresponding boolean content | The list can only have one element, the operator only supports `is`
Person | <code>["ou_9a971ded01b4ca66f4798549878abcef"]</code> | Fill in the corresponding user ID. The user ID type must match the type specified by the `user_id_type` parameter in the [query records](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/search), the default type is open_id | The list may contain multiple elements:<br>- When the operator is `is` or `isNot`, fill in one element<br>- When the operator is `isEmpty` or `isNotEmpty`, fill in the empty value `[]`<br>- Other operators can fill in multiple elements
Phone number | <code>["131xxxx6666"]</code> | Fill in the corresponding phone number | - The list can only have one element or no elements<br>- When the operator is `isEmpty` or `isNotEmpty`, fill in the empty value `[]`
Hyperlink | <code>["link display name"]</code> | Fill in the corresponding hyperlink name | - The list can only have one element or no elements<br>- When the operator is `isEmpty` or `isNotEmpty`, fill in the empty value `[]`
Attachment | <code>[]</code> | Only supports `isEmpty` or `isNotEmpty` | Fill in the empty value `[]`
Single-link relation | <code>["recnVYsuqV"]</code> | Fill in the corresponding record ID | The list may contain multiple elements:<br>- When the operator is `is` or `isNot`, fill in one element<br>- When the operator is `isEmpty` or `isNotEmpty`, fill in the empty value `[]`<br>- Other operators can fill in multiple elements
Double-link relation | <code>["recnVYsuqV"]</code> | Fill in the corresponding record ID | The list may contain multiple elements:<br>- When the operator is `is` or `isNot`, fill in one element<br>- When the operator is `isEmpty` or `isNotEmpty`, fill in the empty value `[]`<br>- Other operators can fill in multiple elements
Location | <code>["Tiananmen Square, Dongcheng District, Beijing"]</code> | Fill in the corresponding address | The list can only have one element or no elements, fill in the empty value `[]` when the operator is `isEmpty`or `isNotEmpty`
Group | <code>["oc_cd07f55f14d6f4a4f1b51504e7e97f48"]</code> | Fill in the corresponding group ID | The list may contain multiple elements:<br>- When the operator is `is` or `isNot`, fill in one element<br>- When the operator is `isEmpty` or `isNotEmpty`, fill in the empty value `[]`<br>- Other operators can fill in multiple elements
Creation time | <code>["ExactDate","1702449755000"]</code> | Unix timestamp in milliseconds | The list may contain multiple elements, refer to the detailed instructions below for filling in date fields
Last update time | <code>["ExactDate","1702449755000"]</code> | Unix timestamp in milliseconds | The list may contain multiple elements, refer to the detailed instructions below for filling in date fields
Creator | <code>["ou_9a971ded01b4ca66f4798549878abcef"]</code> | Fill in the corresponding user ID. The user ID type must match the type specified by the `user_id_type` parameter in the [query records](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/search), the default type is open_id | The list may contain multiple elements:<br>- When the operator is `is` or `isNot`, fill in one element<br>- When the operator is `isEmpty` or `isNotEmpty`, fill in the empty value `[]`<br>- Other operators can fill in multiple elements
Modifier | <code>["ou_9a971ded01b4ca66f4798549878abcef"]</code> | Fill in the corresponding user ID. The user ID type must match the type specified by the `user_id_type` parameter in the [query records](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/search), the default type is open_id | The list may contain multiple elements:<br>- When the operator is `is` or `isNot`, fill in one element<br>- When the operator is `isEmpty` or `isNotEmpty`, fill in the empty value `[]`<br>- Other operators can fill in multiple elements
Auto number | <code>["1"]</code> | Fill in the corresponding auto number value | - The list can only have one element or no elements<br>- When the operator is `isEmpty` or `isNotEmpty`, fill in the empty value `[]`

## Date field filling instructions
When filtering dates, the operator only supports five values: `is`, `isEmpty`, `isNotEmpty`, `isGreater`, and `isLess`.

When the operator is `isEmpty` or `isNotEmpty`, the value should be empty: `"value":[]`.

When the operator is `is`, `isGreater`, or `isLess`, refer to the table below to fill in the date field.

Optional value elements | Description | Example target value | Notes
---|---|---|---
<code>ExactDate</code> | Specific date | <code>["ExactDate","1702449755000"]</code> | - Requires 2 elements. The second element needs to be the timestamp of the specific date.<br>- Although the second element is a timestamp, it will be converted to the zero point of the day in the document time zone during actual filtering.<br>- For formula date fields, the second element needs to be filled with the date text in yyyy/MM/dd format, such as 2025/01/07.
<code>Today</code> | Today | <code>["Today"]</code> | Requires 1 element
<code>Tomorrow</code> | Tomorrow | <code>["Tomorrow"]</code> | Requires 1 element
<code>Yesterday</code> | Yesterday | <code>["Yesterday"]</code> | Requires 1 element
<code>CurrentWeek</code> | This week | <code>["CurrentWeek"]</code> | - Requires 1 element<br>- The operator only supports `is`
<code>LastWeek</code> | Last week | <code>["LastWeek"]</code> | - Requires 1 element<br>- The operator only supports `is`
<code>CurrentMonth</code> | This month | <code>["CurrentMonth"]</code> | - Requires 1 element<br>- The operator only supports `is`
<code>LastMonth</code> | Last month | <code>["LastMonth"]</code> | - Requires 1 element<br>- The operator only supports `is`
<code>TheLastWeek</code> | In the last seven days | <code>["TheLastWeek"]</code> | - Requires 1 element<br>- The operator only supports <code>is</code>
<code>TheNextWeek</code> | In the next seven days | <code>["TheNextWeek"]</code> | - Requires 1 element<br>- The operator only supports <code>is</code>
<code>TheLastMonth</code> | In the last thirty days | <code>["TheLastMonth"]</code> | - Requires 1 element<br>- The operator only supports <code>is</code>
<code>TheNextMonth</code> | In the next thirty days | <code>["TheNextMonth"]</code> | - Requires 1 element<br>- The operator only supports <code>is</code>

# Add a sub-record in a Base table

Adding sub-records in Base tables essentially involves setting up one-way or two-way link fields between sub-records and parent records. The sub-records are mapped to the parent records through association fields, thereby establishing a connection. This document explains how to add a sub-record to a record in a Base table using OpenAPI.

## Prerequisite

You have already created a Base table, and there is an existing record in the table serving as the parent record.

## Process overview

The overall process of adding sub-records is as follows:
1. Call the [Create Field](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-field/create) API to create a one-way or two-way link field in the Base table to establish the relationship between records. To understand what one-way or two-way link fields are, refer to the Feishu Help Center documents: [Use one-way link fields in Base](https://www.feishu.cn/hc/en-US/articles/361914682520-use-one-way-link-fields-in-base), [Use two-way link fields in Base](https://www.feishu.cn/hc/en-US/articles/653027931590-use-two-way-link-fields-in-base).
1. Call the [Search Records](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/search) API to get the ID of the existing parent record.
1. Call the [Create Record](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/create) API to add a new record as a sub-record and ensure that the record is associated with the existing parent record.
1. Call the [List Fields](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-field/list) API to get the field ID of the "one-way link field."
1. Call the [Update View](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-view/patch) API and set the `field_id` parameter in the `hierarchy_config` to the field ID of the "one-way link field" to update the hierarchical structure style of the table view.

## Steps

This section takes an existing record as an example to illustrate how to add a sub-record to it.

1. Call the [Create Field](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-field/create) API to create a one-way link field in the Base table to establish the relationship between records. The request body is as follows:

```json
    {
      "field_name": "one-way link Field",
      "property": {
        "multiple": true,
        "table_id": "tblY2ha8xGSabcef"
      },
      "type": 18
    }
    ```

2. Call the [Search Records](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/search) API to get the ID of the existing parent record. The request body can be empty:

```json
    {}
    ```

If the call is successful, the API will return data in the following structure, where `rec9k8PAbR` is the ID of the parent record.

```json
    {
      "code": 0,
      "data": {
        "has_more": false,
        "items": [
          {
            "fields": {
              "one-way link Field": {},
              "Text": [
                {
                  "text": "Parent Record",
                  "type": "text"
                }
              ]
            },
            "record_id": "rec9k8PAbR"   // Parent record ID
          },
          {
            "fields": {
              "one-way link Field": {}
            },
            "record_id": "recb9nHBYR"
          },
          {
            "fields": {
              "one-way link Field": {}
            },
            "record_id": "recwG1hh0g"
          },
          {
            "fields": {
              "one-way link Field": {}
            },
            "record_id": "recBlfgGRO"
          },
          {
            "fields": {
              "one-way link Field": {}
            },
            "record_id": "recKZHTepH"
          },
          {
            "fields": {
              "one-way link Field": {}
            },
            "record_id": "recDZXc9fs"
          },
          {
            "fields": {
              "one-way link Field": {}
            },
            "record_id": "recX9dPV90"
          },
          {
            "fields": {
              "one-way link Field": {}
            },
            "record_id": "rec6cq2RIk"
          },
          {
            "fields": {
              "one-way link Field": {}
            },
            "record_id": "recuK6kUA1"
          },
          {
            "fields": {
              "one-way link Field": {}
            },
            "record_id": "recLjQD5Eo"
          }
        ],
        "total": 10
      },
      "msg": "success"
    }
    ```

1. Call the [Create Record](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/create) API to add a new record as a sub-record and ensure that the record is associated with the existing parent record. The request body is as follows:

```json
    {
      "fields": {
        "one-way link Field": [
          "rec9k8PAbR"
        ],
        "Text": "Sub-record"
      }
    }
    ```

2. Call the [List Fields](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-field/list) API to get the field ID of the "one-way link field." If the call is successful, the API will return data in the following structure, where `fldfASqam8` is the field ID of the "one-way link field."

```json
    {
      "code": 0,
      "data": {
        "has_more": false,
        "items": [
          {
            "field_id": "fldplsqa97",
            "field_name": "Text",
            "is_hidden": false,
            "is_primary": true,
            "property": null,
            "type": 1,
            "ui_type": "Text"
          },
          {
            "field_id": "fldfASqam8",   // Field ID of the one-way link field
            "field_name": "one-way link Field",
            "is_hidden": false,
            "is_primary": false,
            "property": {
              "multiple": true,
              "table_id": "tblmyHKpQG3k1kSD",
              "table_name": "Data Table"
            },
            "type": 18,
            "ui_type": "SingleLink"
          }
        ],
        "page_token": "fldfASqam
        "total": 2
      },
      "msg": "success"
    }
    ```

1. Call the [Update View](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-view/patch) API, and refer to the following request example. Set the `field_id` parameter in the `hierarchy_config` to the field ID of the "one-way link field" to update the hierarchical structure style of the table view.

```json
    {
      "property": {
        "hierarchy_config": {
          "field_id": "fldfASqam8"
        }
      },
      "view_name": "table"
    }
    ```

    # Create a record

Create a record

For the first access, please refer to [Cloud Document Interface QuickStart](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN) & [Base OpenAPI Access Guide](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification) 

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/tables/:table_id/records
HTTP Method | POST
Rate Limit | [50 per second](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.**<br>Enable any scope from the list | 新增记录(base:record:create)<br>View, comment, edit and manage Base(bitable:app)
Required field scopes | **Notice**：The response body of the API contains the following sensitive fields, and they will be returned only after corresponding scopes are added. If you do not need the fields, it is not recommended that you request the scopes.<br>Obtain user's basic information(contact:user.base:readonly)<br>Obtain user ID(contact:user.employee_id:readonly)<br>Access Contacts as an app(contact:contact:access_as_app)<br>Read contacts(contact:contact:readonly)<br>Read Contacts as an app(contact:contact:readonly_as_app)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Path parameters

Parameter | Type | Description
---|---|---
app_token | string | Base unique device identifier [app_token description](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification#8121eebe)<br>**Example value**: "appbcbWCzen6D8dezhoCH2RpMAh"
table_id | string | Base data table unique device identifier [table_id description](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification#735fe883)<br>**Example value**: "tblsRc9GRRXKqhvW"

### Query parameters

Parameter | Type | Required | Description
---|---|---|---
user_id_type | string | No | User ID categories<br>**Example value**: open_id<br>**Optional values are**:<br>- open_id：Identifies a user to an app. The same user has different Open IDs in different apps. [How to get Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid)<br>- union_id：Identifies a user to a tenant that acts as a developer. A user has the same Union ID in apps developed by the same developer, and has different Union IDs in apps developed by different developers. A developer can use Union ID to link the same user's identities in multiple apps.[How to get Union ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id)<br>- user_id：Identifies a user to a tenant. The same user has different User IDs in different tenants. In one single tenant, a user has the same User ID in all apps （including store apps）. User ID is usually used to communicate user data between different apps. [How to get User ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**Default value**: `open_id`<br>**When the value is `user_id`, the following field scopes are required**:<br>Obtain user ID(contact:user.employee_id:readonly)
client_token | string | No | The format is a standard uuidv4, the unique identifier of the operation, used for idempotent update operations. This value is null to indicate that a new request will be initiated, and this value is non-null to indicate idempotent update operations.<br>**Example value**: fe599b60-450f-46ff-b2ef-9f6675625b97
ignore_consistency_check | boolean | No | Whether to ignore consistency checks for read and write operations. The default value is `false`, meaning the system will ensure that the data read and written is consistent. Optional values:<br>- **true**: Ignore read/write consistency checks to improve performance, but this may cause data on some nodes to be out of sync, resulting in temporary inconsistency.<br>- **false**: Enable read/write consistency checks to ensure data consistency during read and write operations.<br>**Example value**: true

### Request body

Parameter | Type | Required | Description
---|---|---|---
fields | map&lt;string, union&gt; | Yes | To add new records to the data table, you need to first specify the fields in the table (i.e., specify the columns) and then pass the correctly formatted data as a record.<br>**Note**:<br>The supported field types and their descriptions are as follows:<br>- Text: Enter a value in string format<br>- Number: Enter a value in number format<br>- Single choice: Enter an option value; for new option values, a new option will be created<br>- Multiple choices: Enter multiple option values; for new option values, multiple new options will be created if multiple identical new option values are entered<br>- Date: Enter a timestamp in milliseconds<br>- Checkbox: Enter true or false<br>- Barcode<br>- Person: Enter the user's [open_id](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid), [union_id](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id) or [user_id](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id); the type must match the type specified by user_id_type<br>- Phone number: Enter text content<br>- Hyperlink: Refer to the following example, text is the text value, link is the URL link<br>- Attachment: Enter the attachment token; you need to first call the [upload material](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/media/upload_all) or [fragmented upload material](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/media/upload_prepare) interface to upload the attachment to this Base<br>- One-way association: Enter the record ID of the associated table<br>- Two-way association: Enter the record ID of the associated table<br>- Location: Enter the latitude and longitude coordinates<br>For the data structure of different types of fields, please refer to the [Base record data structure overview](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/bitable-record-data-structure-overview).<br>**Example value**: {"multiline":"HelloWorld"}

### Request body example
```json
{
  "fields": {
    "text": "text",
    "barcode": "+$$3170930509104X512356",
    "number": 100,
    "currency": 3,
    "rating": 3,
    "progress": 0.25,
    "single_select": "option_1",
    "multi_select": [
      "option_1",
      "option_2"
    ],
    "date": 1674206443000,
    "checkbox": true,
    "user": [
      {
        "id": "ou_2910013f1e6456f16a0ce75ede950a0a"
      },
      {
        "id": "ou_e04138c9633dd0d2ea166d79f548ab5d"
      }
    ],
    "GroupChat": [
      {
        "id": "oc_cd07f55f14d6f4a4f1b51504e7e97f48"
      }
    ],
    "phone": "13026162666",
    "url": {
      "text": "Base",
      "link": "https://www.feishu.cn/product/base"
    },
    "attachment": [
      {
        "file_token": "DRiFbwaKsoZaLax4WKZbEGCccoe"
      },
      {
        "file_token": "BZk3bL1Enoy4pzxaPL9bNeKqcLe"
      },
      {
        "file_token": "EmL4bhjFFovrt9xZgaSbjJk9c1b"
      },
      {
        "file_token": "Vl3FbVkvnowlgpxpqsAbBrtFcrd"
      }
    ],
    "single_link": [
      "recHTLvO7x",
      "recbS8zb2m"
    ],
    "duplex_link": [
      "recHTLvO7x",
      "recbS8zb2m"
    ],
    "location": "116.397755,39.903179"
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
record | app.table.record | records
fields | map&lt;string, union&gt; | fields
record_id | string | record id，Update records are required
created_by | person | record creator
id | string | user id
name | string | user name
en_name | string | user english name
email | string | user email
avatar_url | string | user avatar url<br>**Required field scopes (Satisfy any)**:<br>Obtain user's basic information(contact:user.base:readonly)<br>Access Contacts as an app(contact:contact:access_as_app)<br>Read contacts(contact:contact:readonly)<br>Read Contacts as an app(contact:contact:readonly_as_app)
created_time | int | record create timestamp
last_modified_by | person | the person who last modified the record
id | string | user id
name | string | user name
en_name | string | user english name
email | string | user email
avatar_url | string | user avatar url<br>**Required field scopes (Satisfy any)**:<br>Obtain user's basic information(contact:user.base:readonly)<br>Access Contacts as an app(contact:contact:access_as_app)<br>Read contacts(contact:contact:readonly)<br>Read Contacts as an app(contact:contact:readonly_as_app)
last_modified_time | int | record last modified timestamp
shared_url | string | Record sharing link (the batch fetch records interface will return this field)
record_url | string | Record link (the retrieve record interface will return this field)

### Response body example
```json
{
	"code": 0,
	"data": {
		"record": {
			"fields": {
				"text": "text",
                "barcode": "+$$3170930509104X512356",
				"number": 100,
                "currency":3,
                "rating":3,
                "progress":0.25,
				"single_select": "option_1",
				"multi_select": ["option_1", "option_2"],
				"date": 1674206443000,
				"checkbox": true,
				"user": [{
					"id": "ou_2910013f1e6456f16a0ce75ede950a0a"
				}, {
					"id": "ou_e04138c9633dd0d2ea166d79f548ab5d"
				}],
                "GroupChat": [
                    {
                        "id": "oc_cd07f55f14d6f4a4f1b51504e7e97f48"
                    }
                ],
				"phone": "13026162666",
				"url": {
					"text": "Base",
					"link": "https://www.feishu.cn/product/base"
				},
				"attachment": [{
					"file_token": "DRiFbwaKsoZaLax4WKZbEGCccoe"
				}, {
					"file_token": "BZk3bL1Enoy4pzxaPL9bNeKqcLe"
				}, {
					"file_token": "EmL4bhjFFovrt9xZgaSbjJk9c1b"
				}, {
					"file_token": "Vl3FbVkvnowlgpxpqsAbBrtFcrd"
				}],
				"single_link": ["recHTLvO7x", "recbS8zb2m"],
				"duplex_link": ["recHTLvO7x", "recbS8zb2m"],
				"location": "116.397755,39.903179"
			},
			"id": "reclAqylTN",
			"record_id": "reclAqylTN"
		}
	},
	"msg": "success"
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
200 | 1254000 | WrongRequestJson | Request error
200 | 1254001 | WrongRequestBody | Request body error
200 | 1254002 | Fail | Internal error, have any questions can be consulting service
200 | 1254003 | WrongBaseToken | AppToken error
200 | 1254004 | WrongTableId | Table id wrong
200 | 1254005 | WrongViewId | View id wrong
200 | 1254006 | WrongRecordId | Record id wrong
200 | 1254007 | EmptyValue | Empty value
200 | 1254008 | EmptyView | Empty view
200 | 1254009 | WrongFieldId | Wrong fieldId
200 | 1254010 | ReqConvError | Request error
400 | 1254015 | Field types do not match. | FieldTypeValueNotMatch
403 | 1254027 | UploadAttachNotAllowed | Attachments don't belong to the app, not allowed to upload
200 | 1254030 | TooLargeResponse | TooLargeResponse
400 | 1254036 | Base is copying, please try again later. | Base copy replicating, try again later
400 | 1254037 | Invalid client token, make sure that it complies with the specification. | Idempotent key format is wrong, you need to pass in uuidv4 format
200 | 1254040 | BaseTokenNotFound | AppToken not found
200 | 1254041 | TableIdNotFound | Table not found
200 | 1254042 | ViewIdNotFound | View not found
200 | 1254043 | RecordIdNotFound | RecordIdNotFound
200 | 1254044 | FieldIdNotFound | FieldIdNotFound
200 | 1254045 | FieldNameNotFound | Field name does not exist
200 | 1254060 | TextFieldConvFail | TextFieldConvFail
200 | 1254061 | NumberFieldConvFail | NumberFieldConvFail
200 | 1254062 | SingleSelectFieldConvFail | SingleSelectFieldConvFail
200 | 1254063 | MultiSelectFieldConvFail | MultiSelectFieldConvFail
200 | 1254064 | DatetimeFieldConvFail | DatetimeFieldConvFail
200 | 1254065 | CheckboxFieldConvFail | CheckboxFieldConvFail
200 | 1254066 | UserFieldConvFail | The value corresponding to the personnel field type is incorrect. The possible reasons are:<br>- The ID type specified by the user_id_type parameter does not match the type of the provided ID.<br>- An unrecognized type or structure was provided. Currently, only `id` is supported, and it must be passed as an array.<br>- An `open_id` was passed across applications. If you are passing an ID across applications, it is recommended to use `user_id`. The `open_id` obtained from different applications cannot be used interchangeably.
200 | 1254067 | LinkFieldConvFail | LinkFieldConvFail
200 | 1254068 | URLFieldConvFail | URLFieldConvFail
200 | 1254069 | AttachFieldConvFail | AttachFieldConvFail
200 | 1254072 | Failed to convert phone field, please make sure it is correct. | Phone field error
400 | 1254074 | The parameters of Duplex Link field are invalid and need to be filled with an array of string. | DuplexLinkFieldConvFail
200 | 1254100 | TableExceedLimit | TableExceedLimit, limited to 300
200 | 1254101 | ViewExceedLimit | ViewExceedLimit, limited to 200
200 | 1254102 | FileExceedLimit | FileExceedLimit
200 | 1254103 | RecordExceedLimit | RecordExceedLimit, limited to 20,000
200 | 1254104 | RecordAddOnceExceedLimit | RecordAddOnceExceedLimit, limited to 500
200 | 1254105 | ColumnExceedLimit | ColumnExceedLimit
200 | 1254106 | AttachExceedLimit | AttachExceedLimit
200 | 1254130 | TooLargeCell | TooLargeCell
200 | 1254290 | TooManyRequest | Request too fast, try again later
200 | 1254291 | Write conflict | The same data table does not support concurrent calls to the write interface, please check whether there is a concurrent call to the write interface. The writing interface includes: adding, modifying, and deleting records; adding, modifying, and deleting fields; modifying forms; modifying views, etc.
200 | 1254301 | OperationTypeError | Base does not have advanced permissions enabled or does not support enabling advanced permissions
200 | 1254303 | The attachment does not belong to this base. | No attach permission
200 | 1255001 | InternalError | Internal error, have any questions can be consulting service
200 | 1255002 | RpcError | Internal error, have any questions can be consulting service
200 | 1255003 | MarshalError | Serialization failed, have any questions can be consulting service
200 | 1255004 | UmMarshalError | Deserialization failed, have any questions can be consulting service
200 | 1255005 | ConvError | Internal error, have any questions can be consulting service
400 | 1255006 | Client token conflict, please generate a new client token and try again. | Idempotent key conflict, you need to randomly generate an idempotent key
504 | 1255040 | Request timed out, please try again later | Try again
400 | 1254607 | Data not ready, please try again later | There are usually two situations when this error occurs: 1. The last submitted modification has not been processed; 2. The data is too large and the server calculation times out; <br>This error code can be appropriately retried.
403 | 1254302 | Permission denied. | No access rights, usually caused by the table opening of advanced permissions, please add a group containing applications in the advanced permissions settings and give this group read and write permissions
403 | 1254304 | Permission denied. | Advanced permissions for specific rows or columns are only available for Business and Enterprise editions
403 | 1254306 | The tenant or base owner is subject to base plan limits. | The tenant or base owner is subject to base plan limits.
403 | 1254608 | Same API requests are submitted repeatedly. | Same API requests are submitted repeatedly.

# Update a record

Update a record

For the first access, please refer to [Cloud Document Interface QuickStart](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN) & [Base OpenAPI Access Guide](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification) 

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/tables/:table_id/records/:record_id
HTTP Method | PUT
Rate Limit | [50 per second](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.**<br>Enable any scope from the list | 更新记录(base:record:update)<br>View, comment, edit and manage Base(bitable:app)
Required field scopes | **Notice**：The response body of the API contains the following sensitive fields, and they will be returned only after corresponding scopes are added. If you do not need the fields, it is not recommended that you request the scopes.<br>Obtain user's basic information(contact:user.base:readonly)<br>Obtain user ID(contact:user.employee_id:readonly)<br>Access Contacts as an app(contact:contact:access_as_app)<br>Read contacts(contact:contact:readonly)<br>Read Contacts as an app(contact:contact:readonly_as_app)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Path parameters

Parameter | Type | Description
---|---|---
app_token | string | Base unique device identifier [app_token description](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification#8121eebe)<br>**Example value**: "appbcbWCzen6D8dezhoCH2RpMAh"
table_id | string | Base data table unique device identifier [table_id description](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification#735fe883)<br>**Example value**: "tblsRc9GRRXKqhvW"
record_id | string | record_id<br>**Example value**: "recPGfZZ13"

### Query parameters

Parameter | Type | Required | Description
---|---|---|---
user_id_type | string | No | User ID categories<br>**Example value**: open_id<br>**Optional values are**:<br>- open_id：Identifies a user to an app. The same user has different Open IDs in different apps. [How to get Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid)<br>- union_id：Identifies a user to a tenant that acts as a developer. A user has the same Union ID in apps developed by the same developer, and has different Union IDs in apps developed by different developers. A developer can use Union ID to link the same user's identities in multiple apps.[How to get Union ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id)<br>- user_id：Identifies a user to a tenant. The same user has different User IDs in different tenants. In one single tenant, a user has the same User ID in all apps （including store apps）. User ID is usually used to communicate user data between different apps. [How to get User ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**Default value**: `open_id`<br>**When the value is `user_id`, the following field scopes are required**:<br>Obtain user ID(contact:user.employee_id:readonly)
ignore_consistency_check | boolean | No | Whether to ignore consistency checks for read and write operations. The default value is `false`, meaning the system will ensure that the data read and written is consistent. Optional values:<br>- **true**: Ignore read/write consistency checks to improve performance, but this may cause data on some nodes to be out of sync, resulting in temporary inconsistency.<br>- **false**: Enable read/write consistency checks to ensure data consistency during read and write operations.<br>**Example value**: true

### Request body

Parameter | Type | Required | Description
---|---|---|---
fields | map&lt;string, union&gt; | Yes | fields<br>**Example value**: {"multiline":"HelloWorld"}

### Request body example
```json
{
	"fields": {
		"text": "text",
        "barcode":"qawqe",
		"number": 100,
        "currency":3,
        "rating":3,
        "progress":0.25,
		"single_select": "option_1",
		"multi_select": ["option_1", "option_2"],
		"date": 1674206443000,
		"checkbox": true,
		"user": [{
			"id": "ou_2910013f1e6456f16a0ce75ede950a0a"
		}, {
			"id": "ou_e04138c9633dd0d2ea166d79f548ab5d"
		}],
        "groupChat":[
            {
                "id": "oc_cd07f55f14d6f4a4f1b51504e7e97f48"
            }
        ],
		"phone": "130xxxx2666",
		"url": {
			"text": "Base",
			"link": "https://www.feishu.cn/product/base"
		},
		"attachment": [{
			"file_token": "DRiFbwaKsoZaLax4WKZbEGCccoe"
		}, {
			"file_token": "BZk3bL1Enoy4pzxaPL9bNeKqcLe"
		}, {
			"file_token": "EmL4bhjFFovrt9xZgaSbjJk9c1b"
		}, {
			"file_token": "Vl3FbVkvnowlgpxpqsAbBrtFcrd"
		}],
		"single_link": ["recHTLvO7x", "recbS8zb2m"],
		"duplex_link": ["recHTLvO7x", "recbS8zb2m"],
		"location": "116.397755,39.903179"
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
record | app.table.record | record
fields | map&lt;string, union&gt; | fields
record_id | string | record id，Update records are required
created_by | person | record creator
id | string | user id
name | string | user name
en_name | string | user english name
email | string | user email
avatar_url | string | user avatar url<br>**Required field scopes (Satisfy any)**:<br>Obtain user's basic information(contact:user.base:readonly)<br>Access Contacts as an app(contact:contact:access_as_app)<br>Read contacts(contact:contact:readonly)<br>Read Contacts as an app(contact:contact:readonly_as_app)
created_time | int | record create timestamp
last_modified_by | person | the person who last modified the record
id | string | user id
name | string | user name
en_name | string | user english name
email | string | user email
avatar_url | string | user avatar url<br>**Required field scopes (Satisfy any)**:<br>Obtain user's basic information(contact:user.base:readonly)<br>Access Contacts as an app(contact:contact:access_as_app)<br>Read contacts(contact:contact:readonly)<br>Read Contacts as an app(contact:contact:readonly_as_app)
last_modified_time | int | record last modified timestamp
shared_url | string | shared link
record_url | string | record link

### Response body example
```json
{
	"code": 0,
	"data": {
		"record": {
			"fields": {
				"text": "text",
                "barcode": "qawqe",
				"number": 100,
                "currency":3,
                "rating":3,
                "progress":0.25,
				"single_select": "option_1",
				"multi_select": ["option_1", "option_2"],
				"date": 1674206443000,
				"checkbox": true,
				"user": [{
					"id": "ou_2910013f1e6456f16a0ce75ede950a0a"
				}, {
					"id": "ou_e04138c9633dd0d2ea166d79f548ab5d"
				}],
                "groupChat": [
                    {
                        "id": "oc_cd07f55f14d6f4a4f1b51504e7e97f48"
                    }
                ],
				"phone": "13026162666",
				"url": {
					"text": "Base",
					"link": "https://www.feishu.cn/product/base"
				},
				"attachment": [{
					"file_token": "DRiFbwaKsoZaLax4WKZbEGCccoe"
				}, {
					"file_token": "BZk3bL1Enoy4pzxaPL9bNeKqcLe"
				}, {
					"file_token": "EmL4bhjFFovrt9xZgaSbjJk9c1b"
				}, {
					"file_token": "Vl3FbVkvnowlgpxpqsAbBrtFcrd"
				}],
				"single_link": ["recHTLvO7x", "recbS8zb2m"],
				"duplex_link": ["recHTLvO7x", "recbS8zb2m"],
				"location": "116.397755,39.903179"
			},
			"id": "reclAqylTN",
			"record_id": "reclAqylTN"
		}
	},
	"msg": "success"
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
200 | 1254000 | WrongRequestJson | Request error
200 | 1254001 | WrongRequestBody | Request body error
200 | 1254002 | Fail | Internal error, have any questions can be consulting service
200 | 1254003 | WrongBaseToken | AppToken error
200 | 1254004 | WrongTableId | Table id wrong
200 | 1254005 | WrongViewId | View id wrong
200 | 1254006 | WrongRecordId | Record id wrong
200 | 1254007 | EmptyValue | Empty value
200 | 1254008 | EmptyView | Empty view
200 | 1254009 | WrongFieldId | Wrong fieldId
200 | 1254010 | ReqConvError | Request error
400 | 1254015 | Field types do not match. | Field types do not match.
403 | 1254027 | UploadAttachNotAllowed | Attachments don't belong to the app, not allowed to upload
200 | 1254030 | TooLargeResponse | TooLargeResponse
400 | 1254036 | Base is copying, please try again later. | Base copy replicating, try again later
200 | 1254040 | BaseTokenNotFound | AppToken not found
200 | 1254041 | TableIdNotFound | Table not found
200 | 1254042 | ViewIdNotFound | View not found
200 | 1254043 | RecordIdNotFound | RecordIdNotFound
200 | 1254044 | FieldIdNotFound | FieldIdNotFound
200 | 1254045 | FieldNameNotFound | Field name does not exist
200 | 1254060 | TextFieldConvFail | TextFieldConvFail
200 | 1254061 | NumberFieldConvFail | NumberFieldConvFail
200 | 1254062 | SingleSelectFieldConvFail | SingleSelectFieldConvFail
200 | 1254063 | MultiSelectFieldConvFail | MultiSelectFieldConvFail
200 | 1254064 | DatetimeFieldConvFail | DatetimeFieldConvFail
200 | 1254065 | CheckboxFieldConvFail | CheckboxFieldConvFail
200 | 1254066 | UserFieldConvFail | The value corresponding to the personnel field type is incorrect. The possible reasons are:<br>- The ID type specified by the user_id_type parameter does not match the type of the provided ID.<br>- An unrecognized type or structure was provided. Currently, only `id` is supported, and it must be passed as an array.<br>- An `open_id` was passed across applications. If you are passing an ID across applications, it is recommended to use `user_id`. The `open_id` obtained from different applications cannot be used interchangeably.
200 | 1254067 | LinkFieldConvFail | LinkFieldConvFail
200 | 1254068 | URLFieldConvFail | URLFieldConvFail
200 | 1254069 | AttachFieldConvFail | AttachFieldConvFail
200 | 1254072 | InvalidPhoneNumber | Failed to convert phone field, please make sure it is correct.
400 | 1254074 | InvalidDuplexLinkField | The parameters of Duplex Link field are invalid and need to be filled with an array of string.
200 | 1254100 | TableExceedLimit | TableExceedLimit, limited to 300
200 | 1254101 | ViewExceedLimit | ViewExceedLimit, limited to 200
200 | 1254102 | FileExceedLimit | FileExceedLimit
200 | 1254103 | RecordExceedLimit | RecordExceedLimit, limited to 20,000
200 | 1254104 | RecordAddOnceExceedLimit | RecordAddOnceExceedLimit, limited to 500
200 | 1254105 | ColumnExceedLimit | ColumnExceedLimit
200 | 1254106 | AttachExceedLimit | AttachExceedLimit
200 | 1254112 | TooManyRequestInSingleBase | /
200 | 1254130 | TooLargeCell | TooLargeCell
200 | 1254290 | TooManyRequest | Request too fast, try again later
200 | 1254291 | Write conflict | The same data table does not support concurrent calls to the write interface, please check whether there is a concurrent call to the write interface. The writing interface includes: adding, modifying, and deleting records; adding, modifying, and deleting fields; modifying forms; modifying views, etc.
200 | 1254301 | OperationTypeError | Base does not have advanced permissions enabled or does not support enabling advanced permissions
200 | 1254303 | AttachmentNoPermission | The attachment does not belong to this base.
200 | 1255001 | InternalError | Internal error, have any questions can be consulting service
200 | 1255002 | RpcError | Internal error, have any questions can be consulting service
200 | 1255003 | MarshalError | Serialization failed, have any questions can be consulting service
200 | 1255004 | UmMarshalError | Deserialization failed, have any questions can be consulting service
200 | 1255005 | ConvError | Internal error, have any questions can be consulting service
504 | 1255040 | Request timed out, please try again later | Try again
400 | 1254607 | Data not ready, please try again later | There are usually two situations when this error occurs: 1. The last submitted modification has not been processed; 2. The data is too large and the server calculation times out; <br>This error code can be appropriately retried.
403 | 1254302 | Permission denied. | No access rights, usually caused by the table opening of advanced permissions, please add a group containing applications in the advanced permissions settings and give this group read and write permissions
403 | 1254304 | Permission denied. | Advanced permissions for specific rows or columns are only available for Business and Enterprise editions
403 | 1254608 | ReqRecommited | Same API requests are submitted repeatedly.

# Search records

This api is used to query existing records in the  table. A maximum of 500 rows of records can be queried at a time, and paging is supported.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/tables/:table_id/records/search
HTTP Method | POST
Rate Limit | [20 per second](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.**<br>Enable any scope from the list | 根据条件搜索记录(base:record:retrieve)<br>View, comment, edit and manage Base(bitable:app)<br>View, comment, and export Base(bitable:app:readonly)
Required field scopes | **Notice**：The response body of the API contains the following sensitive fields, and they will be returned only after corresponding scopes are added. If you do not need the fields, it is not recommended that you request the scopes.<br>Obtain user's basic information(contact:user.base:readonly)<br>Obtain user ID(contact:user.employee_id:readonly)<br>Access Contacts as an app(contact:contact:access_as_app)<br>Read contacts(contact:contact:readonly)<br>Read Contacts as an app(contact:contact:readonly_as_app)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Path parameters

Parameter | Type | Description
---|---|---
app_token | string | The unique identifier of the Bitable App. Different forms of Bitable have different ways of obtaining app_token:<br>- If a Bitable URL begins with ==** feishu.cn/base **==, the Bitable app_token is highlighted in the image below:<br>![app_token.png](//sf3-cn.feishucdn.com/obj/open-platform-opendoc/6916f8cfac4045ba6585b90e3afdfb0a_GxbfkJHZBa.png?height=766&lazyload=true&width=3004)<br>- If Bitable's URL starts with ==** feishu.cn/wiki **==, you need to call the Knowledge Base related [Get Wiki Workspace Node Information](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/wiki-v2/space/get_node) interface to get Bitable's app_token. When the value of obj_type is bitable, the value of the obj_token field is the app_token of Bitable.<br>For more information, see [How to get app_token](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/bitable-overview#-752212c).<br>**Example value**: "NQRxbRkBMa6OnZsjtERcxhNWnNh"<br>**Data validation rules**:<br>- Length range: `0` ～ `100` characters
table_id | string | Bitable data table unique identifier. How to get:<br>- You can get the table_id through the Bitable URL. The highlighted part of the image below is the table_id of the current data table.<br>- table_id can also be obtained through the [list data table](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table/list) interface<br>![](//sf3-cn.feishucdn.com/obj/open-platform-opendoc/18741fe2a0d3cafafaf9949b263bb57d_yD1wkOrSju.png?height=746&lazyload=true&maxWidth=700&width=2976)<br>**Example value**: "tbl0xe5g8PP3U3cS"<br>**Data validation rules**:<br>- Length range: `0` ～ `50` characters

### Query parameters

Parameter | Type | Required | Description
---|---|---|---
user_id_type | string | No | User ID categories<br>**Example value**: open_id<br>**Optional values are**:<br>- open_id：Identifies a user to an app. The same user has different Open IDs in different apps. [How to get Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid)<br>- union_id：Identifies a user to a tenant that acts as a developer. A user has the same Union ID in apps developed by the same developer, and has different Union IDs in apps developed by different developers. A developer can use Union ID to link the same user's identities in multiple apps.[How to get Union ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id)<br>- user_id：Identifies a user to a tenant. The same user has different User IDs in different tenants. In one single tenant, a user has the same User ID in all apps （including store apps）. User ID is usually used to communicate user data between different apps. [How to get User ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**Default value**: `open_id`<br>**When the value is `user_id`, the following field scopes are required**:<br>Obtain user ID(contact:user.employee_id:readonly)
page_token | string | No | Page identifier. It is not filled in the first request, indicating traversal from the beginning; when there will be more groups, the new page_token will be returned at the same time, and the next traversal can use the page_token to get more groups<br>**Example value**: eVQrYzJBNDNONlk4VFZBZVlSdzlKdFJ4bVVHVExENDNKVHoxaVdiVnViQT0=
page_size | int | No | Page size. The maximum value is 500<br>**Example value**: 10<br>**Default value**: `20`

### Request body

Parameter | Type | Required | Description
---|---|---|---
view_id | string | No | Base view unique device identifier [view_id description](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification#8121eebe)<br>**Example value**: "vewp7nmiS4"<br>**Data validation rules**:<br>- Length range: `0` ～ `50` characters
field_names | string\[\] | No | field_names<br>**Example value**: ["fieldName1"]<br>**Data validation rules**:<br>- Length range: `0` ～ `200`
sort | sort\[\] | No | Data validation rules<br>**Data validation rules**:<br>- Length range: `0` ～ `100`
field_name | string | No | field_name<br>**Example value**: "fieldName1"<br>**Data validation rules**:<br>- Length range: `0` ～ `1000` characters
desc | boolean | No | desc<br>**Example value**: true<br>**Default value**: `false`
filter | filter_info | No | Refer to the [Record Filter Parameter Filling Guide](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/record-filter-guide) to learn how to fill in the filter.
conjunction | string | No | Conjunction. This parameter is required and please ignore the "No" in the Required <br>column<br>**Example value**: "and"<br>**Optional values are**:<br>- and：meeting all of the conditions<br>- or：meeting any of the conditions<br>**Data validation rules**:<br>- Length range: `0` ～ `10` characters
conditions | condition\[\] | No | conditions<br>**Data validation rules**:<br>- Length range: `0` ～ `50`
field_name | string | Yes | field_name<br>**Example value**: "fieldName1"<br>**Data validation rules**:<br>- Length range: `0` ～ `1000` characters
operator | string | Yes | operator<br>**Example value**: "is"<br>**Optional values are**:<br>- is：is<br>- isNot：is not. This value does not support date fields. To learn how to query date fields, refer to [Date Field Entry Guide](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/record-filter-guide#29d9dc89).<br>- contains：contains. This value does not support date fields.<br>- doesNotContain：does not contain. This value does not support date fields.<br>- isEmpty：is empty<br>- isNotEmpty：is not empty<br>- isGreater：greater than.<br>- isGreaterEqual：greater than or equal to. This value does not support date fields.<br>- isLess：less than<br>- isLessEqual：less than or equal to. This value does not support date fields.<br>- like：LIKE operator. Not supported yet<br>- in：IN operator. Not supported yet
value | string\[\] | No | value<br>[Record filter development guide](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/record-filter-guide)<br>**Example value**: ["text content"]<br>**Data validation rules**:<br>- Length range: `0` ～ `10`
automatic_fields | boolean | No | Whether to automatically calculate and return the four types of fields: creation time (`created_time`), modification time (`last_modified_time`), creator (`created_by`), and modifier (`last_modified_by`). The default is false, indicating they will not be returned.<br>**Example value**: false

### Request body example
```json
{
  "view_id": "vewqhz51lk",
  "field_names": [
    "字段1",
    "字段2"
  ],
  "sort": [
    {
      "field_name": "多行文本",
      "desc": true
    }
  ],
  "filter": {
    "conjunction": "and",
    "children": [
      {
        "conjunction": "or",
        "conditions": [
          {
            "field_name": "职位",
            "operator": "is",
            "value": [
              "高级销售员"
            ]
          },
          {
            "field_name": "职位",
            "operator": "is",
            "value": [
              "初级销售员"
            ]
          }
        ]
      },
      {
        "conjunction": "or",
        "conditions": [
          {
            "field_name": "销售额",
            "operator": "is",
            "value": [
              "10000.0"
            ]
          },
          {
            "field_name": "销售额",
            "operator": "is",
            "value": [
              "20000.0"
            ]
          }
        ]
      }
    ]
  },
  "automatic_fields": false
}
```

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
items | app.table.record\[\] | The list of records. The data type is array. For details, see [Data structure](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/development-guide/bitable-structure).
fields | map&lt;string, union&gt; | The record field
record_id | string | record ID
created_by | person | founder
id | string | Person ID. Consistent with the type specified user_id_type query parameter.
name | string | Chinese name
en_name | string | English name
email | string | email
avatar_url | string | avatar link<br>**Required field scopes (Satisfy any)**:<br>Obtain user's basic information(contact:user.base:readonly)<br>Access Contacts as an app(contact:contact:access_as_app)<br>Read contacts(contact:contact:readonly)<br>Read Contacts as an app(contact:contact:readonly_as_app)
created_time | int | creation time
last_modified_by | person | Modifier
id | string | Person ID. Consistent with the type specified user_id_type query parameter.
name | string | Chinese name
en_name | string | English name
email | string | email
avatar_url | string | avatar link<br>**Required field scopes (Satisfy any)**:<br>Obtain user's basic information(contact:user.base:readonly)<br>Access Contacts as an app(contact:contact:access_as_app)<br>Read contacts(contact:contact:readonly)<br>Read Contacts as an app(contact:contact:readonly_as_app)
last_modified_time | int | Last update time
shared_url | string | Record sharing link (the bulk fetch records interface will return this field)
record_url | string | Record link (the retrieve record interface will return this field)
has_more | boolean | Whether the response body has more parameters
page_token | string | Page identifier, when has_more is true, a new page_token will also be returned. Otherwise, page_token will not be returned
total | int | total

### Response body example
```json
{
    "code":0,
    "data":{
        "has_more":false,
        "items":[
            {
                "created_by":{
                    "avatar_url":"https://internal-api-lark-file.feishu.cn/static-resource/v1/06d568cb-f464-4c2e-bd03-76512c545c5j~?image_size=72x72&amp;cut_type=default-face&amp;quality=&amp;format=jpeg&amp;sticker_format=.webp",
                    "email":"",
                    "en_name":"测试1",
                    "id":"ou_92945f86a98bba075174776959c90eda",
                    "name":"测试1"
                },
                "created_time":1691049973000,
                "fields":{
                    "人员":[
                        {
                            "avatar_url":"https://internal-api-lark-file.feishu.cn/static-resource/v1/b2-7619-4b8a-b27b-c72d90b06a2j~?image_size=72x72&amp;cut_type=default-face&amp;quality=&amp;format=jpeg&amp;sticker_format=.webp",
                            "email":"zhangsan.leben@bytedance.com",
                            "en_name":"ZhangSan",
                            "id":"ou_2910013f1e6456f16a0ce75ede950a0a",
                            "name":"张三"
                        },
                        {
                            "avatar_url":"https://internal-api-lark-file.feishu.cn/static-resource/v1/v2_q86-fcb6-4f18-85c7-87ca8881e50j~?image_size=72x72&amp;cut_type=default-face&amp;quality=&amp;format=jpeg&amp;sticker_format=.webp",
                            "email":"lisi.00@bytedance.com",
                            "en_name":"LiSi",
                            "id":"ou_e04138c9633dd0d2ea166d79f548ab5d",
                            "name":"李四"
                        }
                    ],
                    "修改人":[
                        {
                            "avatar_url":"https://internal-api-lark-file.feishu.cn/static-resource/v1/06d568cb-f464-4c2e-bd03-76512c545c5j~?image_size=72x72&amp;cut_type=default-face&amp;quality=&amp;format=jpeg&amp;sticker_format=.webp",
                            "email":"",
                            "en_name":"测试1",
                            "id":"ou_92945f86a98bba075174776959c90eda",
                            "name":"测试1"
                        }
                    ],
                    "创建人":[
                        {
                            "avatar_url":"https://internal-api-lark-file.feishu.cn/static-resource/v1/06d568cb-f464-4c2e-bd03-76512c545c5j~?image_size=72x72&amp;cut_type=default-face&amp;quality=&amp;format=jpeg&amp;sticker_format=.webp",
                            "email":"",
                            "en_name":"测试1",
                            "id":"ou_92945f86a98bba075174776959c90eda",
                            "name":"测试1"
                        }
                    ],
                    "创建时间":1691049973000,
                    "单向关联":{
                        "link_record_ids":[
                            "recnVYsuqV"
                        ]
                    },
                    "单选":"选项1",
                    "双向关联":{
                        "link_record_ids":[
                            "recqLvMaXT",
                            "recrdld32q"
                        ]
                    },
                    "地理位置":{
                        "address":"东长安街",
                        "adname":"东城区",
                        "cityname":"北京市",
                        "full_address":"天安门广场，北京市东城区东长安街",
                        "location":"116.397755,39.903179",
                        "name":"天安门广场",
                        "pname":"北京市"
                    },
                    "复选框":true,
                    "多行文本":[
                        {
                            "text":"多行文本内容1",
                            "type":"text"
                        },
                        {
                            "mentionNotify":false,
                            "mentionType":"User",
                            "name":"张三",
                            "text":"@张三",
                            "token":"ou_2910013f1e6456f16a0ce75ede950a0a",
                            "type":"mention"
                        }
                    ],
                    "多选":[
                        "选项1",
                        "选项2"
                    ],
                    "数字":2323.2323,
                    "日期":1690992000000,
                    "最后更新时间":1702455191000,
                    "条码":[
                        {
                            "text":"123",
                            "type":"text"
                        }
                    ],
                    "电话号码":"131xxxx6666",
                    "自动编号":"17",
                    "群组":[
                        {
                            "avatar_url":"https://internal-api-lark-file.feishu-boe.cn/static-resource/v1/v2_c8d2cd50-ba29-476f-b7f1-5b5917cb18ej~?image_size=72x72&amp;cut_type=&amp;quality=&amp;format=jpeg&amp;sticker_format=.webp",
                            "id":"oc_cd07f55f14d6f4a4f1b51504e7e97f48",
                            "name":"武侠聊天组"
                        }
                    ],
                    "评分":3,
                    "货币":1,
                    "超链接":{
                        "link":"https://bitable.feishu.cn",
                        "text":"飞书多维表格官网"
                    },
                    "进度":0.66,
                    "附件":[
                        {
                            "file_token":"Vl3FbVkvnowlgpxpqsAbBrtFcrd",
                            "name":"飞书.jpeg",
                            "size":32975,
                            "tmp_url":"https://open.feishu.cn/open-apis/drive/v1/medias/batch_get_tmp_download_url?file_tokens=Vl3FbVk11owlgpxpqsAbBrtFcrd&amp;extra=%7B%22bitablePerm%22%3A%7B%22tableId%22%3A%22tblBJyX6jZteblYv%22%2C%22rev%22%3A90%7D%7D",
                            "type":"image/jpeg",
                            "url":"https://open.feishu.cn/open-apis/drive/v1/medias/Vl3FbVk11owlgpxpqsAbBrtFcrd/download?extra=%7B%22bitablePerm%22%3A%7B%22tableId%22%3A%22tblBJyX6jZteblYv%22%2C%22rev%22%3A90%7D%7D"
                        }
                    ]
                },
                "last_modified_by":{
                    "avatar_url":"https://internal-api-lark-file.feishu.cn/static-resource/v1/06d568cb-f464-4c2e-bd03-76512c545c5j~?image_size=72x72&amp;cut_type=default-face&amp;quality=&amp;format=jpeg&amp;sticker_format=.webp",
                    "email":"",
                    "en_name":"测试1",
                    "id":"ou_92945f86a98bba075174776959c90eda",
                    "name":"测试1"
                },
                "last_modified_time":1702455191000,
                "record_id":"recyOaMB2F"
            }
        ],
        "total":1
    },
    "msg":"success"
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
200 | 1254000 | WrongRequestJson | Request error
200 | 1254001 | WrongRequestBody | Request body error
200 | 1254002 | Fail | Internal error, have any questions can be consulting service
200 | 1254003 | WrongBaseToken | AppToken error
200 | 1254004 | WrongTableId | Table id wrong
200 | 1254005 | WrongViewId | View id wrong
200 | 1254006 | WrongRecordId | Record id wrong
200 | 1254007 | EmptyValue | Empty value
200 | 1254008 | EmptyView | Empty view
200 | 1254009 | WrongFieldId | Wrong fieldId
200 | 1254010 | ReqConvError | Request error
400 | 1254011 | Page size must greater than 0. | invalid page_size
200 | 1254016 | InvalidSort | invalid sort
200 | 1254018 | InvalidFilter | The filter parameter is incorrect. Please refer to [Record filter development guide](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/record-filter-guide) for information on how to fill in the filter parameter.
200 | 1254024 | InvalidFieldNames | InvalidFieldNames
200 | 1254030 | TooLargeResponse | TooLargeResponse
400 | 1254036 | Base is copying, please try again later. | Base copy replicating, try again later
200 | 1254040 | BaseTokenNotFound | AppToken not found
200 | 1254041 | TableIdNotFound | Table not found
200 | 1254042 | ViewIdNotFound | View not found
200 | 1254043 | RecordIdNotFound | RecordIdNotFound
200 | 1254044 | FieldIdNotFound | FieldIdNotFound
200 | 1254045 | FieldNameNotFound | Field name does not exist
200 | 1254060 | TextFieldConvFail | TextFieldConvFail
200 | 1254061 | NumberFieldConvFail | NumberFieldConvFail
200 | 1254062 | SingleSelectFieldConvFail | SingleSelectFieldConvFail
200 | 1254063 | MultiSelectFieldConvFail | MultiSelectFieldConvFail
200 | 1254064 | DatetimeFieldConvFail | DatetimeFieldConvFail
200 | 1254065 | CheckboxFieldConvFail | CheckboxFieldConvFail
200 | 1254066 | UserFieldConvFail | The value corresponding to the personnel field type is incorrect. The possible reasons are:<br>- The ID type specified by the user_id_type parameter does not match the type of the provided ID.<br>- An unrecognized type or structure was provided. Currently, only `id` is supported, and it must be passed as an array.<br>- An `open_id` was passed across applications. If you are passing an ID across applications, it is recommended to use `user_id`. The `open_id` obtained from different applications cannot be used interchangeably.
200 | 1254067 | LinkFieldConvFail | LinkFieldConvFail
200 | 1254068 | URLFieldConvFail | URLFieldConvFail
200 | 1254069 | AttachFieldConvFail | AttachFieldConvFail
200 | 1254072 | Failed to convert phone field, please make sure it is correct. | invalid phone format
200 | 1254100 | TableExceedLimit | TableExceedLimit, limited to 300
200 | 1254101 | ViewExceedLimit | ViewExceedLimit, limited to 200
200 | 1254102 | FileExceedLimit | FileExceedLimit
200 | 1254103 | RecordExceedLimit | RecordExceedLimit, limited to 20,000
200 | 1254104 | RecordAddOnceExceedLimit | RecordAddOnceExceedLimit, limited to 500
200 | 1254107 | FilterLengthExceedLimit | FilterLengthExceedLimit, limited to 2,000 characters
200 | 1254108 | SortLengthExceedLimit | SortLengthExceedLimit, limited to 1,000 characters
200 | 1254109 | FormulaTableSizeExceedLimit | FormulaTableSizeExceedLimit
200 | 1254130 | TooLargeCell | TooLargeCell
200 | 1254290 | TooManyRequest | Request too fast, try again later
200 | 1254291 | Write conflict | The same data table does not support concurrent calls to the write interface, please check whether there is a concurrent call to the write interface. The writing interface includes: adding, modifying, and deleting records; adding, modifying, and deleting fields; modifying forms; modifying views, etc.
200 | 1254301 | OperationTypeError | Base does not have advanced permissions enabled or does not support enabling advanced permissions
200 | 1254302 | Permission denied. | No access rights, usually caused by the table opening of advanced permissions, please add a group containing applications in the advanced permissions settings and give this group read and write permissions
200 | 1254303 | AttachPermNotAllow | No attach permission
200 | 1255001 | InternalError | Internal error, have any questions can be consulting service
200 | 1255002 | RpcError | Internal error, have any questions can be consulting service
200 | 1255003 | MarshalError | Serialization failed, have any questions can be consulting service
200 | 1255004 | UmMarshalError | Deserialization failed, have any questions can be consulting service
200 | 1255005 | ConvError | Internal error, have any questions can be consulting service
504 | 1255040 | Request timed out, please try again later | Try again
400 | 1254607 | Data not ready, please try again later | There are usually two situations when this error occurs: 1. The last submitted modification has not been processed; 2. The data is too large and the server calculation times out; <br>This error code can be appropriately retried.

# Delete a record

Delete a record

## Prerequisites

Before calling this interface, make sure that the current calling identity (tenant_access_token or user_access_token) has document permissions such as Bitable's edit, otherwise the interface will return an HTTP 403 or 400 status code. For more information, refer to [How to enable document permissions for an application or user] (/ssl: ttdoc/ukTMukTMukTM/uczNzUjL3czM14yN3MTN #16c6475a).

## Precautions

Data tables synchronized from other data sources do not support adding, deleting, or modifying records.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/tables/:table_id/records/:record_id
HTTP Method | DELETE
Rate Limit | [50 per second](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.**<br>Enable any scope from the list | 删除记录(base:record:delete)<br>View, comment, edit and manage Base(bitable:app)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

The instructions for AccessToken calling Docs API are detailed here [Docs API Overview](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN)

### Path parameters

Parameter | Type | Description
---|---|---
app_token | string | base app_token<br>**Example value**: "appbcbWCzen6D8dezhoCH2RpMAh"
table_id | string | table_id<br>**Example value**: "tblsRc9GRRXKqhvW"
record_id | string | record_id<br>**Example value**: "recpCsf4ME"

### Query parameters

Parameter | Type | Required | Description
---|---|---|---
ignore_consistency_check | boolean | No | Whether to ignore the consistency read and write check, the default is false, that is, when performing read and write operations, the system will ensure that the data read and written are the same. Optional value:<br>- true: Ignore read and write consistency checks to improve performance, but may cause data on some nodes to be out of sync and temporarily inconsistent<br>- false: Enable read and write consistency check to ensure that the data is consistent during read and write<br>**Example value**: false

### Request body example
```json
Curl -i -X DELETE https://fsopen.bytedance.net/open-apis/bitable/v1/apps/appbcbWCzen6D8dezhoCH2RpMAh/tables/tblsRc9GRRXKqhvW/records/recpCsf4ME '\
-H 'Authorization: Bearer t-7f1B ***** 8e560'
```

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | delete_record | \-
deleted | boolean | deleted
record_id | string | record id

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "deleted": true,
        "record_id": "recWqFb7xo"
    }
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
200 | 1254000 | WrongRequestJson | Request error
200 | 1254001 | WrongRequestBody | Request body error
200 | 1254002 | Fail | Internal error, have any questions can be consulting service
200 | 1254003 | WrongBaseToken | AppToken error
200 | 1254004 | WrongTableId | Table id wrong
200 | 1254005 | WrongViewId | View id wrong
200 | 1254006 | WrongRecordId | Record id wrong
200 | 1254007 | EmptyValue | Empty value
200 | 1254008 | EmptyView | Empty view
200 | 1254009 | WrongFieldId | Wrong fieldId
200 | 1254010 | ReqConvError | Request error
200 | 1254030 | TooLargeResponse | TooLargeResponse
400 | 1254036 | Base is copying, please try again later. | Base copy replicating, try again later
200 | 1254040 | BaseTokenNotFound | AppToken not found
200 | 1254041 | TableIdNotFound | Table not found
200 | 1254042 | ViewIdNotFound | View not found
200 | 1254043 | RecordIdNotFound | RecordIdNotFound
200 | 1254044 | FieldIdNotFound | FieldIdNotFound
200 | 1254060 | TextFieldConvFail | TextFieldConvFail
200 | 1254061 | NumberFieldConvFail | NumberFieldConvFail
200 | 1254062 | SingleSelectFieldConvFail | SingleSelectFieldConvFail
200 | 1254063 | MultiSelectFieldConvFail | MultiSelectFieldConvFail
200 | 1254064 | DatetimeFieldConvFail | DatetimeFieldConvFail
200 | 1254065 | CheckboxFieldConvFail | CheckboxFieldConvFail
200 | 1254066 | UserFieldConvFail | The value corresponding to the personnel field type is incorrect. The possible reasons are:<br>- The ID type specified by the user_id_type parameter does not match the type of the provided ID.<br>- An unrecognized type or structure was provided. Currently, only `id` is supported, and it must be passed as an array.<br>- An `open_id` was passed across applications. If you are passing an ID across applications, it is recommended to use `user_id`. The `open_id` obtained from different applications cannot be used interchangeably.
200 | 1254067 | LinkFieldConvFail | LinkFieldConvFail
200 | 1254072 | InvalidPhoneNumber | Failed to convert phone field, please make sure it is correct.
200 | 1254100 | TableExceedLimit | TableExceedLimit, limited to 300
200 | 1254101 | ViewExceedLimit | ViewExceedLimit, limited to 200
200 | 1254102 | FileExceedLimit | FileExceedLimit
200 | 1254103 | RecordExceedLimit | RecordExceedLimit, limited to 20,000
200 | 1254104 | RecordAddOnceExceedLimit | RecordAddOnceExceedLimit, limited to 500
200 | 1254130 | TooLargeCell | TooLargeCell
200 | 1254290 | TooManyRequest | Request too fast, try again later
200 | 1254291 | Write conflict | The same data table does not support concurrent calls to the write interface, please check whether there is a concurrent call to the write interface. The writing interface includes: adding, modifying, and deleting records; adding, modifying, and deleting fields; modifying forms; modifying views, etc.
200 | 1254301 | OperationTypeError | Base does not have advanced permissions enabled or does not support enabling advanced permissions
200 | 1255001 | InternalError | Internal error, have any questions can be consulting service
200 | 1255002 | RpcError | Internal error, have any questions can be consulting service
200 | 1255003 | MarshalError | Serialization failed, have any questions can be consulting service
200 | 1255004 | UmMarshalError | Deserialization failed, have any questions can be consulting service
200 | 1255005 | ConvError | Internal error, have any questions can be consulting service
504 | 1255040 | Request timed out, please try again later | Try again
400 | 1254607 | Data not ready, please try again later | There are usually two situations when this error occurs: 1. The last submitted modification has not been processed; 2. The data is too large and the server calculation times out; <br>This error code can be appropriately retried.
403 | 1254302 | Permission denied. | No access rights, usually caused by the table opening of advanced permissions, please add a group containing applications in the advanced permissions settings and give this group read and write permissions
403 | 1254304 | Permission denied. | Advanced permissions for specific rows or columns are only available for Business and Enterprise editions
403 | 1254608 | ReqRecommited | Same API requests are submitted repeatedly.

# Create records

Create records,up to 500 lines at a time.

For the first access, please refer to [Cloud Document Interface QuickStart](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN) & [Base OpenAPI Access Guide](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification) 

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/tables/:table_id/records/batch_create
HTTP Method | POST
Rate Limit | [50 per second](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.**<br>Enable any scope from the list | 新增记录(base:record:create)<br>View, comment, edit and manage Base(bitable:app)
Required field scopes | **Notice**：The response body of the API contains the following sensitive fields, and they will be returned only after corresponding scopes are added. If you do not need the fields, it is not recommended that you request the scopes.<br>Obtain user's basic information(contact:user.base:readonly)<br>Obtain user ID(contact:user.employee_id:readonly)<br>Access Contacts as an app(contact:contact:access_as_app)<br>Read contacts(contact:contact:readonly)<br>Read Contacts as an app(contact:contact:readonly_as_app)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Path parameters

Parameter | Type | Description
---|---|---
app_token | string | Base unique device identifier [app_token description](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification#8121eebe)<br>**Example value**: "appbcbWCzen6D8dezhoCH2RpMAh"
table_id | string | Base data table unique device identifier [table_id description](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification#735fe883)<br>**Example value**: "tblsRc9GRRXKqhvW"

### Query parameters

Parameter | Type | Required | Description
---|---|---|---
user_id_type | string | No | User ID categories<br>**Example value**: open_id<br>**Optional values are**:<br>- open_id：Identifies a user to an app. The same user has different Open IDs in different apps. [How to get Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid)<br>- union_id：Identifies a user to a tenant that acts as a developer. A user has the same Union ID in apps developed by the same developer, and has different Union IDs in apps developed by different developers. A developer can use Union ID to link the same user's identities in multiple apps.[How to get Union ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id)<br>- user_id：Identifies a user to a tenant. The same user has different User IDs in different tenants. In one single tenant, a user has the same User ID in all apps （including store apps）. User ID is usually used to communicate user data between different apps. [How to get User ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**Default value**: `open_id`<br>**When the value is `user_id`, the following field scopes are required**:<br>Obtain user ID(contact:user.employee_id:readonly)
client_token | string | No | The format is a standard uuidv4, the unique identifier of the operation, used for idempotent update operations. This value is null to indicate that a new request will be initiated, and this value is non-null to indicate idempotent update operations.<br>**Example value**: fe599b60-450f-46ff-b2ef-9f6675625b97
ignore_consistency_check | boolean | No | Whether to ignore consistency checks for read and write operations. The default value is `false`, meaning the system will ensure that the data read and written is consistent. Optional values:<br>- **true**: Ignore read/write consistency checks to improve performance, but this may cause data on some nodes to be out of sync, resulting in temporary inconsistency.<br>- **false**: Enable read/write consistency checks to ensure data consistency during read and write operations.<br>**Example value**: true

### Request body

Parameter | Type | Required | Description
---|---|---|---
records | app.table.record\[\] | Yes | records
fields | map&lt;string, union&gt; | Yes | fields<br>**Example value**: {"multiline":"HelloWorld"}
shared_url | string | No | shared link<br>**Example value**: "https://www.example.com/record/WVoXrzIaqeorcJcHgzAcg8AQnNd"
record_url | string | No | record link<br>**Example value**: "https://www.example.com/record/WVoXrzIaqeorcJcHgzAcg8AQnNd"

### Request body example
```json
{
    "records": [
        {
            "fields": {
                "text": "text",
                "barcode": "qawqe",
                "number": 100,
                "currency": 3,
                "rating": 3,
                "progress": 0.25,
                "single_select": "option_1",
                "multi_select": [
                    "option_1",
                    "option_2"
                ],
                "date": 1674206443000,
                "checkbox": true,
                "user": [
                    {
                        "id": "ou_2910013f1e6456f16a0ce75ede950a0a"
                    },
                    {
                        "id": "ou_e04138c9633dd0d2ea166d79f548ab5d"
                    }
                ],
                "groupChat": [
                    {
                        "id": "oc_cd07f55f14d6f4a4f1b51504e7e97f48"
                    }
                ],
                "phone": "130xxxx2666",
                "url": {
                    "text": "Base",
                    "link": "https://www.feishu.cn/product/base"
                },
                "attachment": [
                    {
                        "file_token": "DRiFbwaKsoZaLax4WKZbEGCccoe"
                    },
                    {
                        "file_token": "BZk3bL1Enoy4pzxaPL9bNeKqcLe"
                    },
                    {
                        "file_token": "EmL4bhjFFovrt9xZgaSbjJk9c1b"
                    },
                    {
                        "file_token": "Vl3FbVkvnowlgpxpqsAbBrtFcrd"
                    }
                ],
                "single_link": [
                    "recHTLvO7x",
                    "recbS8zb2m"
                ],
                "duplex_link": [
                    "recHTLvO7x",
                    "recbS8zb2m"
                ],
                "location": "116.397755,39.903179"
            }
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
records | app.table.record\[\] | records
fields | map&lt;string, union&gt; | fields
record_id | string | record id，Update records are required
created_by | person | record creator
id | string | user id
name | string | user name
en_name | string | user english name
email | string | user email
avatar_url | string | user avatar url<br>**Required field scopes (Satisfy any)**:<br>Obtain user's basic information(contact:user.base:readonly)<br>Access Contacts as an app(contact:contact:access_as_app)<br>Read contacts(contact:contact:readonly)<br>Read Contacts as an app(contact:contact:readonly_as_app)
created_time | int | record create timestamp
last_modified_by | person | the person who last modified the record
id | string | user id
name | string | user name
en_name | string | user english name
email | string | user email
avatar_url | string | user avatar url<br>**Required field scopes (Satisfy any)**:<br>Obtain user's basic information(contact:user.base:readonly)<br>Access Contacts as an app(contact:contact:access_as_app)<br>Read contacts(contact:contact:readonly)<br>Read Contacts as an app(contact:contact:readonly_as_app)
last_modified_time | int | record last modified timestamp
shared_url | string | shared link
record_url | string | record link

### Response body example
```json
{
    "code": 0,
    "data": {
        "records": [
            {
                "fields": {
                    "text": "text",
                    "barcode": "qawqe",
                    "number": 100,
                    "currency": 3,
                    "rating": 3,
                    "progress": 0.25,
                    "single_select": "option_1",
                    "multi_select": [
                        "option_1",
                        "option_2"
                    ],
                    "date": 1674206443000,
                    "checkbox": true,
                    "user": [
                        {
                            "id": "ou_2910013f1e6456f16a0ce75ede950a0a"
                        },
                        {
                            "id": "ou_e04138c9633dd0d2ea166d79f548ab5d"
                        }
                    ],
                    "groupChat": [
                        {
                            "id": "oc_cd07f55f14d6f4a4f1b51504e7e97f48"
                        }
                    ],
                    "phone": "13026162666",
                    "url": {
                        "text": "Base",
                        "link": "https://www.feishu.cn/product/base"
                    },
                    "attachment": [
                        {
                            "file_token": "DRiFbwaKsoZaLax4WKZbEGCccoe"
                        },
                        {
                            "file_token": "BZk3bL1Enoy4pzxaPL9bNeKqcLe"
                        },
                        {
                            "file_token": "EmL4bhjFFovrt9xZgaSbjJk9c1b"
                        },
                        {
                            "file_token": "Vl3FbVkvnowlgpxpqsAbBrtFcrd"
                        }
                    ],
                    "single_link": [
                        "recHTLvO7x",
                        "recbS8zb2m"
                    ],
                    "duplex_link": [
                        "recHTLvO7x",
                        "recbS8zb2m"
                    ],
                    "location": "116.397755,39.903179"
                },
                "id": "reclAqylTN",
                "record_id": "reclAqylTN"
            }
        ]
    },
    "msg": "success"
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
200 | 1254000 | WrongRequestJson | Request error
200 | 1254001 | WrongRequestBody | Request body error
200 | 1254002 | Fail | There are many scenarios that can lead to error code 1254002. Please refer to the following suggestions for troubleshooting:<br>- If the content changes in a single operation are large, try reducing the data volume in a single operation<br>- If you are making concurrent API calls, try controlling the request interval and retry later.<br>- If you are creating a Base in a knowledge base (wiki), check whether you are using the [Create Knowledge Space Node](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/wiki-v2/space-node/create) API to create the Base. In this scenario, you cannot use the [Create Base](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app/create) API.<br>- Check whether the API parameters are incorrect. For example, when paginating a Base query, an invalid `page_token` is passed, or an incorrect `table_id` of the data table is passed.<br>- If this error occurs occasionally, it may be due to server timeout or instability. Please retry to resolve the issue.
200 | 1254003 | WrongBaseToken | AppToken error
200 | 1254004 | WrongTableId | Table id wrong
200 | 1254005 | WrongViewId | View id wrong
200 | 1254006 | WrongRecordId | Record id wrong
200 | 1254007 | EmptyValue | Empty value
200 | 1254008 | EmptyView | Empty view
200 | 1254009 | WrongFieldId | Wrong fieldId
200 | 1254010 | ReqConvError | Request error
400 | 1254015 | Field types do not match. | Field types do not match.
403 | 1254027 | UploadAttachNotAllowed | Attachments don't belong to the app, not allowed to upload
200 | 1254030 | TooLargeResponse | TooLargeResponse
400 | 1254036 | Base is copying, please try again later. | Base copy replicating, try again later
400 | 1254037 | Invalid client token, make sure that it complies with the specification. | Idempotent key format is wrong, you need to pass in uuidv4 format
200 | 1254040 | BaseTokenNotFound | AppToken not found
200 | 1254041 | TableIdNotFound | Table not found
200 | 1254042 | ViewIdNotFound | View not found
200 | 1254043 | RecordIdNotFound | RecordIdNotFound
200 | 1254044 | FieldIdNotFound | FieldIdNotFound
200 | 1254045 | FieldNameNotFound | Field name does not exist or the you do not have the permission to write the field
200 | 1254060 | TextFieldConvFail | TextFieldConvFail
200 | 1254061 | NumberFieldConvFail | NumberFieldConvFail
200 | 1254062 | SingleSelectFieldConvFail | SingleSelectFieldConvFail
200 | 1254063 | MultiSelectFieldConvFail | MultiSelectFieldConvFail
200 | 1254064 | DatetimeFieldConvFail | DatetimeFieldConvFail
200 | 1254065 | CheckboxFieldConvFail | CheckboxFieldConvFail
200 | 1254066 | UserFieldConvFail | The value corresponding to the personnel field type is incorrect. The possible reasons are:<br>- The ID type specified by the user_id_type parameter does not match the type of the provided ID.<br>- An unrecognized type or structure was provided. Currently, only `id` is supported, and it must be passed as an array.<br>- An `open_id` was passed across applications. If you are passing an ID across applications, it is recommended to use `user_id`. The `open_id` obtained from different applications cannot be used interchangeably.
200 | 1254067 | LinkFieldConvFail | LinkFieldConvFail
200 | 1254068 | URLFieldConvFail | URLFieldConvFail
200 | 1254069 | AttachFieldConvFail | AttachFieldConvFail
200 | 1254072 | Failed to convert phone field, please make sure it is correct. | Phone field error
400 | 1254074 | DuplexLinkFieldConvFail | The parameters of Duplex Link field are invalid and need to be filled with an array of string.
200 | 1254100 | TableExceedLimit | TableExceedLimit, limited to 300
200 | 1254101 | ViewExceedLimit | ViewExceedLimit, limited to 200
200 | 1254102 | FileExceedLimit | FileExceedLimit
200 | 1254103 | RecordExceedLimit | RecordExceedLimit, limited to 20,000
200 | 1254104 | RecordAddOnceExceedLimit | RecordAddOnceExceedLimit, limited to 500
200 | 1254105 | ColumnExceedLimit | ColumnExceedLimit
200 | 1254106 | AttachExceedLimit | AttachExceedLimit
200 | 1254130 | TooLargeCell | TooLargeCell
200 | 1254290 | TooManyRequest | Request too fast, try again later
200 | 1254291 | Write conflict | The same data table does not support concurrent calls to the write interface, please check whether there is a concurrent call to the write interface. The writing interface includes: adding, modifying, and deleting records; adding, modifying, and deleting fields; modifying forms; modifying views, etc.
200 | 1254301 | OperationTypeError | Base does not have advanced permissions enabled or does not support enabling advanced permissions
200 | 1254303 | AttachPermNotAllow | No attach permission
200 | 1255001 | InternalError | Internal error, have any questions can be consulting service
200 | 1255002 | RpcError | Internal error, have any questions can be consulting service
200 | 1255003 | MarshalError | Serialization failed, have any questions can be consulting service
200 | 1255004 | UmMarshalError | Deserialization failed, have any questions can be consulting service
200 | 1255005 | ConvError | Internal error, have any questions can be consulting service
400 | 1255006 | Client token conflict, please generate a new client token and try again. | Idempotent key conflict, you need to randomly generate an idempotent key
504 | 1255040 | Request timed out, please try again later | Try again
400 | 1254607 | Data not ready, please try again later | There are usually two situations when this error occurs: 1. The last submitted modification has not been processed; 2. The data is too large and the server calculation times out; <br>This error code can be appropriately retried.
403 | 1254302 | Permission denied. | No access rights, usually caused by the table opening of advanced permissions, please add a group containing applications in the advanced permissions settings and give this group read and write permissions
403 | 1254304 | Permission denied. | Advanced permissions for specific rows or columns are only available for Business and Enterprise editions
403 | 1254306 | The tenant or base owner is subject to base plan limits. | The tenant or base owner is subject to base plan limits.
403 | 1254608 | Same API requests are submitted repeatedly. | Same API requests are submitted repeatedly.

# Update records

Update records,up to 500 lines at a time.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/tables/:table_id/records/batch_update
HTTP Method | POST
Rate Limit | [50 per second](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.**<br>Enable any scope from the list | 更新记录(base:record:update)<br>View, comment, edit and manage Base(bitable:app)
Required field scopes | **Notice**：The response body of the API contains the following sensitive fields, and they will be returned only after corresponding scopes are added. If you do not need the fields, it is not recommended that you request the scopes.<br>Obtain user's basic information(contact:user.base:readonly)<br>Obtain user ID(contact:user.employee_id:readonly)<br>Access Contacts as an app(contact:contact:access_as_app)<br>Read contacts(contact:contact:readonly)<br>Read Contacts as an app(contact:contact:readonly_as_app)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

The instructions for AccessToken calling Docs API are detailed here [Docs API Overview](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN)

### Path parameters

Parameter | Type | Description
---|---|---
app_token | string | base app_token<br>**Example value**: "appbcbWCzen6D8dezhoCH2RpMAh"
table_id | string | table_id<br>**Example value**: "tblsRc9GRRXKqhvW"

### Query parameters

Parameter | Type | Required | Description
---|---|---|---
user_id_type | string | No | User ID categories<br>**Example value**: open_id<br>**Optional values are**:<br>- open_id：Identifies a user to an app. The same user has different Open IDs in different apps. [How to get Open ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-openid)<br>- union_id：Identifies a user to a tenant that acts as a developer. A user has the same Union ID in apps developed by the same developer, and has different Union IDs in apps developed by different developers. A developer can use Union ID to link the same user's identities in multiple apps.[How to get Union ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-union-id)<br>- user_id：Identifies a user to a tenant. The same user has different User IDs in different tenants. In one single tenant, a user has the same User ID in all apps （including store apps）. User ID is usually used to communicate user data between different apps. [How to get User ID](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-obtain-user-id)<br>**Default value**: `open_id`<br>**When the value is `user_id`, the following field scopes are required**:<br>Obtain user ID(contact:user.employee_id:readonly)
ignore_consistency_check | boolean | No | Whether to ignore consistency checks for read and write operations. The default value is `false`, meaning the system will ensure that the data read and written is consistent. Optional values:<br>- **true**: Ignore read/write consistency checks to improve performance, but this may cause data on some nodes to be out of sync, resulting in temporary inconsistency.<br>- **false**: Enable read/write consistency checks to ensure data consistency during read and write operations.<br>**Example value**: true

### Request body

Parameter | Type | Required | Description
---|---|---|---
records | app.table.record\[\] | Yes | records
fields | map&lt;string, union&gt; | Yes | fields<br>**Example value**: {"Multiline text": "HelloWorld"}
record_id | string | No | record id. This parameter is required. Refer to [record_id description](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification#15d8db94) to get record_id<br>**Example value**: "recqwIwhc6"
shared_url | string | No | shared link<br>**Example value**: "https://www.example.com/record/WVoXrzIaqeorcJcHgzAcg8AQnNd"
record_url | string | No | record link<br>**Example value**: "https://www.example.com/record/WVoXrzIaqeorcJcHgzAcg8AQnNd"

### Request body example
```json
{
    "records": [
        {
            "record_id": "recgVdQ7o7",
            "fields": {
                "manpower": 2,
                "performer": [
                    {
                        "id": "ou_debc524b2d8cb187704df652b43d29de"
                    }
                ],
                "description": "collect user feedbacks",
                "corresponding OKR": [
                    "recqwIwhc6",
                    "recOuEJMvN"
                ],
                "deadline": 1609516800000,
                "completed": true,
                "status": "complete",
                "department": [
                    "Sale",
                    "Customer service"
                ]
            }
        },
        {
            "record_id":"recAu2ReK0",
            "fields": {
                "manpower": 2,
                "performer": [
                    {
                        "id": "ou_debc524b2d8cb187704df652b43d29de"
                    }
                ],
                "description": "collect user feedbacks",
                "corresponding OKR": [
                    "recqwIwhc6",
                    "recOuEJMvN"
                ],
                "deadline": 1609516800000,
                "completed": true,
                "status": "complete",
                "department": [
                    "Sale",
                    "Customer service"
                ]
            }
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
records | app.table.record\[\] | records
fields | map&lt;string, union&gt; | fields
record_id | string | record id，Update records are required
created_by | person | record creator
id | string | user id
name | string | user name
en_name | string | user english name
email | string | user email
avatar_url | string | user avatar url<br>**Required field scopes (Satisfy any)**:<br>Obtain user's basic information(contact:user.base:readonly)<br>Access Contacts as an app(contact:contact:access_as_app)<br>Read contacts(contact:contact:readonly)<br>Read Contacts as an app(contact:contact:readonly_as_app)
created_time | int | record create timestamp
last_modified_by | person | the person who last modified the record
id | string | user id
name | string | user name
en_name | string | user english name
email | string | user email
avatar_url | string | user avatar url<br>**Required field scopes (Satisfy any)**:<br>Obtain user's basic information(contact:user.base:readonly)<br>Access Contacts as an app(contact:contact:access_as_app)<br>Read contacts(contact:contact:readonly)<br>Read Contacts as an app(contact:contact:readonly_as_app)
last_modified_time | int | record last modified timestamp
shared_url | string | shared link
record_url | string | record link

### Response body example
```json
{
  "Code": 0,
  "Data": {
    "Records": [
      {
        "Fields": {
          "Personnel": [
            {
              "Id": "ou_2910013f1e6456f16a0ce75ede950a0a"
            },
            {
              "Id": "ou_e04138c9633dd0d2ea166d79f548ab5d"
            }
          ],
          "Group": [
            {
              "Id": "oc_cd07f55f14d6f4a4f1b51504e7e97f48"
            }
          ],
          "One-way association": [
            "recHTLvO7x",
            "recbS8zb2m"
          ],
          "Radio": "Option 3",
          "Bidirectional association": [
            "recHTLvO7x",
            "recbS8zb2m"
          ],
          "Location": "116.397755, 39.903179",
          "Checkbox": true,
          "Multi-line text": "Multi-line text content",
          "Multiple Choice": [
            "Option 1",
            "Option 2"
          ],
          "Number": 100,
          "Date": 1674206443000,
          "Barcode": "qawqe",
          "Phone number": "13026162666",
          "Index": "Indexed column multi-row text type",
          "Hyperlinke": {
            "Link": "https://www.feishu.cn/product/base",
            "Text": "Bitable official website"
          },
          "Attachment": [
            {
              "file_token": "Vl3FbVkvnowlgpxpqsAbBrtFcrd"
            }
          ],
          "Rating": 3,
          "Currency": 3,
          "Progress": 0.25
        },
        "Id": "reclAqylTN",
        "record_id": "reclAqylTN"
      }
    ]
  },
  "Msg": "success"
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
200 | 1254000 | WrongRequestJson | Request error
200 | 1254001 | WrongRequestBody | Request body error
200 | 1254002 | Fail | Internal error, have any questions can be consulting service
200 | 1254003 | WrongBaseToken | AppToken error
200 | 1254004 | WrongTableId | Table id wrong
200 | 1254005 | WrongViewId | View id wrong
200 | 1254006 | WrongRecordId | Record id wrong
200 | 1254007 | EmptyValue | Empty value
200 | 1254008 | EmptyView | Empty view
200 | 1254009 | WrongFieldId | Wrong fieldId
200 | 1254010 | ReqConvError | Request error
400 | 1254015 | FieldTypeValueNotMatch | Field types do not match.
403 | 1254027 | UploadAttachNotAllowed | Attachments don't belong to the app, not allowed to upload
200 | 1254030 | TooLargeResponse | TooLargeResponse
400 | 1254036 | Base is copying, please try again later. | Base copy replicating, try again later
200 | 1254040 | BaseTokenNotFound | AppToken not found
200 | 1254041 | TableIdNotFound | Table not found
200 | 1254042 | ViewIdNotFound | View not found
200 | 1254043 | RecordIdNotFound | RecordIdNotFound
200 | 1254044 | FieldIdNotFound | FieldIdNotFound
200 | 1254045 | FieldNameNotFound | Field name does not exist
200 | 1254060 | TextFieldConvFail | TextFieldConvFail
200 | 1254061 | NumberFieldConvFail | NumberFieldConvFail
200 | 1254062 | SingleSelectFieldConvFail | SingleSelectFieldConvFail
200 | 1254063 | MultiSelectFieldConvFail | MultiSelectFieldConvFail
200 | 1254064 | DatetimeFieldConvFail | DatetimeFieldConvFail
200 | 1254065 | CheckboxFieldConvFail | CheckboxFieldConvFail
200 | 1254066 | UserFieldConvFail | The value corresponding to the personnel field type is incorrect. The possible reasons are:<br>- The ID type specified by the user_id_type parameter does not match the type of the provided ID.<br>- An unrecognized type or structure was provided. Currently, only `id` is supported, and it must be passed as an array.<br>- An `open_id` was passed across applications. If you are passing an ID across applications, it is recommended to use `user_id`. The `open_id` obtained from different applications cannot be used interchangeably.
200 | 1254067 | LinkFieldConvFail | LinkFieldConvFail
200 | 1254068 | URLFieldConvFail | URLFieldConvFail
200 | 1254069 | AttachFieldConvFail | AttachFieldConvFail
200 | 1254072 | InvalidPhoneNumber | Failed to convert phone field, please make sure it is correct.
400 | 1254074 | DuplexLinkFieldConvFail | The parameters of Duplex Link field are invalid and need to be filled with an array of string.
200 | 1254100 | TableExceedLimit | TableExceedLimit, limited to 300
200 | 1254101 | ViewExceedLimit | ViewExceedLimit, limited to 200
200 | 1254102 | FileExceedLimit | FileExceedLimit
200 | 1254103 | RecordExceedLimit | RecordExceedLimit, limited to 20,000
200 | 1254104 | RecordAddOnceExceedLimit | RecordAddOnceExceedLimit, limited to 500
200 | 1254105 | ColumnExceedLimit | ColumnExceedLimit
200 | 1254106 | AttachExceedLimit | AttachExceedLimit
200 | 1254130 | TooLargeCell | TooLargeCell
200 | 1254290 | TooManyRequest | Request too fast, try again later
200 | 1254291 | Write conflict | The same data table does not support concurrent calls to the write interface, please check whether there is a concurrent call to the write interface. The writing interface includes: adding, modifying, and deleting records; adding, modifying, and deleting fields; modifying forms; modifying views, etc.
200 | 1254301 | OperationTypeError | Base does not have advanced permissions enabled or does not support enabling advanced permissions
403 | 1254303 | AttachPermNotAllow | The attachment does not belong to this base.
200 | 1255001 | InternalError | Internal error, have any questions can be consulting service
200 | 1255002 | RpcError | Internal error, have any questions can be consulting service
200 | 1255003 | MarshalError | Serialization failed, have any questions can be consulting service
200 | 1255004 | UmMarshalError | Deserialization failed, have any questions can be consulting service
200 | 1255005 | ConvError | Internal error, have any questions can be consulting service
504 | 1255040 | Request timed out, please try again later | Try again
400 | 1254607 | Data not ready, please try again later | There are usually two situations when this error occurs: 1. The last submitted modification has not been processed; 2. The data is too large and the server calculation times out; <br>This error code can be appropriately retried.
403 | 1254302 | Permission denied. | No access rights, usually caused by the table opening of advanced permissions, please add a group containing applications in the advanced permissions settings and give this group read and write permissions
403 | 1254304 | Permission denied. | Advanced permissions for specific rows or columns are only available for Business and Enterprise editions
403 | 1254608 | ReqRecommited | Same API requests are submitted repeatedly.

# Batch get records

Batch get records by record ids

**Notice**：Only supports querying up to 100 records

## Precautions

If advanced permissions are enabled for Base, you need to ensure that the calling identity has manage permissions for Base. Otherwise, it may result in a successful call but return empty data. For detailed steps, refer to [How to Grant Document Permissions for Apps or Users](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#16c6475a).

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/tables/:table_id/records/batch_get
HTTP Method | POST
Rate Limit | [20 per second](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.**<br>Enable any scope from the list | 检索特定记录(base:record:read)<br>View, comment, edit and manage Base(bitable:app)<br>View, comment, and export Base(bitable:app:readonly)
Required field scopes | **Notice**：The response body of the API contains the following sensitive fields, and they will be returned only after corresponding scopes are added. If you do not need the fields, it is not recommended that you request the scopes.<br>Obtain user's basic information(contact:user.base:readonly)<br>Access Contacts as an app(contact:contact:access_as_app)<br>Read contacts(contact:contact:readonly)<br>Read Contacts as an app(contact:contact:readonly_as_app)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Path parameters

Parameter | Type | Description
---|---|---
app_token | string | Form token<br>**Example value**: "NQRxbRkBMa6OnZsjtERcxhNWnNh"<br>**Data validation rules**:<br>- Length range: `0` ～ `100` characters
table_id | string | Form ID<br>**Example value**: "tbl0xe5g8PP3U3cS"<br>**Data validation rules**:<br>- Length range: `0` ～ `50` characters

### Request body

Parameter | Type | Required | Description
---|---|---|---
record_ids | string\[\] | Yes | record id list. See [Query records](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/search)<br>**Example value**: ["recxq2GJwE"]<br>**Data validation rules**:<br>- Length range: `1` ～ `100`
user_id_type | string | No | **Example value**: "open_id"<br>**Optional values are**:<br>- user_id：<br><md-enum-item key="union_id" ><br><md-enum-item key="open_id" >
with_shared_url | boolean | No | Controls whether to return the recorded share link, true means return the share link<br>**Example value**: True
automatic_fields | boolean | No | Controls whether to return automatically calculated fields, true means return<br>**Example value**: True

### Request body example
```json
{
  "record_ids": [
    "recyOaMB2F",
    "rec111111",
    "recyOaMB2F"
  ],
  "user_id_type": "open_id",
  "with_shared_url": true,
  "automatic_fields": true
}
```

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
records | app.table.record\[\] | record list
fields | map&lt;string, union&gt; | record field
record_id | string | Record Id
created_by | person | founder
id | string | Personnel IDs
name | string | Chinese name
en_name | string | English name
email | string | email
avatar_url | string | avatar link<br>**Required field scopes (Satisfy any)**:<br>Obtain user's basic information(contact:user.base:readonly)<br>Access Contacts as an app(contact:contact:access_as_app)<br>Read contacts(contact:contact:readonly)<br>Read Contacts as an app(contact:contact:readonly_as_app)
created_time | int | creation time
last_modified_by | person | Modifier
id | string | Personnel IDs
name | string | Chinese name
en_name | string | English name
email | string | email
avatar_url | string | avatar link<br>**Required field scopes (Satisfy any)**:<br>Obtain user's basic information(contact:user.base:readonly)<br>Access Contacts as an app(contact:contact:access_as_app)<br>Read contacts(contact:contact:readonly)<br>Read Contacts as an app(contact:contact:readonly_as_app)
last_modified_time | int | Last update time
shared_url | string | Record share link
record_url | string | Record link (the retrieval record interface will return this field, this interface does not return)
forbidden_record_ids | string\[\] | List of prohibited records (for documents with advanced permissions enabled)
absent_record_ids | string\[\] | List of non-existent records

### Response body example
```json
{
  "code": 0,
  "msg": "success",
  "data": {
    "forbidden_record_ids": [
      "recyOaMB2F"
    ],
    "absent_record_ids": [
      "rec111111"
    ],
    "records": [
      {
        "created_by": {
          "avatar_url": "https://internal-api-lark-file.feishu.cn/static-resource/v1/06d568cb-f464-4c2e-bd03-76512c545c5j~?image_size=72x72&amp;cut_type=default-face&amp;quality=&amp;format=jpeg&amp;sticker_format=.webp",
          "email": "",
          "en_name": "测试1",
          "id": "ou_92945f86a98bba075174776959c90eda",
          "name": "测试1"
        },
        "created_time": 1691049973000,
        "fields": {
          "人员": [
            {
              "avatar_url": "https://internal-api-lark-file.feishu.cn/static-resource/v1/b2-7619-4b8a-b27b-c72d90b06a2j~?image_size=72x72&amp;cut_type=default-face&amp;quality=&amp;format=jpeg&amp;sticker_format=.webp",
              "email": "zhangsan.leben@bytedance.com",
              "en_name": "ZhangSan",
              "id": "ou_2910013f1e6456f16a0ce75ede950a0a",
              "name": "张三"
            },
            {
              "avatar_url": "https://internal-api-lark-file.feishu.cn/static-resource/v1/v2_q86-fcb6-4f18-85c7-87ca8881e50j~?image_size=72x72&amp;cut_type=default-face&amp;quality=&amp;format=jpeg&amp;sticker_format=.webp",
              "email": "lisi.00@bytedance.com",
              "en_name": "LiSi",
              "id": "ou_e04138c9633dd0d2ea166d79f548ab5d",
              "name": "李四"
            }
          ],
          "修改人": [
            {
              "avatar_url": "https://internal-api-lark-file.feishu.cn/static-resource/v1/06d568cb-f464-4c2e-bd03-76512c545c5j~?image_size=72x72&amp;cut_type=default-face&amp;quality=&amp;format=jpeg&amp;sticker_format=.webp",
              "email": "",
              "en_name": "测试1",
              "id": "ou_92945f86a98bba075174776959c90eda",
              "name": "测试1"
            }
          ],
          "创建人": [
            {
              "avatar_url": "https://internal-api-lark-file.feishu.cn/static-resource/v1/06d568cb-f464-4c2e-bd03-76512c545c5j~?image_size=72x72&amp;cut_type=default-face&amp;quality=&amp;format=jpeg&amp;sticker_format=.webp",
              "email": "",
              "en_name": "测试1",
              "id": "ou_92945f86a98bba075174776959c90eda",
              "name": "测试1"
            }
          ],
          "创建时间": 1691049973000,
          "单向关联": {
            "link_record_ids": [
              "recnVYsuqV"
            ]
          },
          "单选": "选项1",
          "双向关联": {
            "link_record_ids": [
              "recqLvMaXT",
              "recrdld32q"
            ]
          },
          "地理位置": {
            "address": "东长安街",
            "adname": "东城区",
            "cityname": "北京市",
            "full_address": "天安门广场，北京市东城区东长安街",
            "location": "116.397755,39.903179",
            "name": "天安门广场",
            "pname": "北京市"
          },
          "复选框": true,
          "多行文本": [
            {
              "text": "多行文本内容1",
              "type": "text"
            },
            {
              "mentionNotify": false,
              "mentionType": "User",
              "name": "张三",
              "text": "@张三",
              "token": "ou_2910013f1e6456f16a0ce75ede950a0a",
              "type": "mention"
            }
          ],
          "多选": [
            "选项1",
            "选项2"
          ],
          "数字": 2323.2323,
          "日期": 1690992000000,
          "最后更新时间": 1702455191000,
          "条码": [
            {
              "text": "123",
              "type": "text"
            }
          ],
          "电话号码": "131xxxx6666",
          "自动编号": "17",
          "群组": [
            {
              "avatar_url": "https://internal-api-lark-file.feishu-boe.cn/static-resource/v1/v2_c8d2cd50-ba29-476f-b7f1-5b5917cb18ej~?image_size=72x72&amp;cut_type=&amp;quality=&amp;format=jpeg&amp;sticker_format=.webp",
              "id": "oc_cd07f55f14d6f4a4f1b51504e7e97f48",
              "name": "武侠聊天组"
            }
          ],
          "评分": 3,
          "货币": 1,
          "超链接": {
            "link": "https://bitable.feishu.cn",
            "text": "飞书多维表格官网"
          },
          "进度": 0.66,
          "附件": [
            {
              "file_token": "Vl3FbVkvnowlgpxpqsAbBrtFcrd",
              "name": "飞书.jpeg",
              "size": 32975,
              "tmp_url": "https://open.feishu.cn/open-apis/drive/v1/medias/batch_get_tmp_download_url?file_tokens=Vl3FbVk11owlgpxpqsAbBrtFcrd&amp;extra=%7B%22bitablePerm%22%3A%7B%22tableId%22%3A%22tblBJyX6jZteblYv%22%2C%22rev%22%3A90%7D%7D",
              "type": "image/jpeg",
              "url": "https://open.feishu.cn/open-apis/drive/v1/medias/Vl3FbVk11owlgpxpqsAbBrtFcrd/download?extra=%7B%22bitablePerm%22%3A%7B%22tableId%22%3A%22tblBJyX6jZteblYv%22%2C%22rev%22%3A90%7D%7D"
            }
          ]
        },
        "last_modified_by": {
          "avatar_url": "https://internal-api-lark-file.feishu.cn/static-resource/v1/06d568cb-f464-4c2e-bd03-76512c545c5j~?image_size=72x72&amp;cut_type=default-face&amp;quality=&amp;format=jpeg&amp;sticker_format=.webp",
          "email": "",
          "en_name": "测试1",
          "id": "ou_92945f86a98bba075174776959c90eda",
          "name": "测试1"
        },
        "last_modified_time": 1702455191000,
        "record_id": "recyOaMB2F",
        "shared_url": "https://example.feishu.cn/record/KBcNrNtpWePAlscCvdmb6ZcSc5b"
      }
    ]
  }
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
400 | 1254000 | WrongRequestJson | Request error
400 | 1254001 | WrongRequestBody | Request body error
500 | 1254002 | Fail | Internal error, have any questions can be consulting service
400 | 1254003 | WrongBaseToken | AppToken error
400 | 1254004 | WrongTableId | Table id wrong
400 | 1254005 | WrongViewId | View id wrong
400 | 1254006 | WrongRecordId | Record id wrong
400 | 1254007 | EmptyValue | Empty value
400 | 1254008 | EmptyView | Empty view
400 | 1254009 | WrongFieldId | Wrong fieldId
400 | 1254010 | ReqConvError | Request error
400 | 1254011 | Page size must greater than 0. | invalid page_size
400 | 1254016 | InvalidSort | invalid sort
400 | 1254018 | InvalidFilter | invalid filter
400 | 1254024 | InvalidFieldNames | InvalidFieldNames
400 | 1254030 | InvalidPageToken | Invalid PageToken
400 | 1254036 | Bitable is copying, please try again later. | Base copy replicating, try again later
404 | 1254040 | BaseTokenNotFound | AppToken not found
404 | 1254041 | TableIdNotFound | Table not found
404 | 1254042 | ViewIdNotFound | View not found
404 | 1254043 | RecordIdNotFound | RecordIdNotFound
404 | 1254044 | FieldIdNotFound | FieldIdNotFound
404 | 1254045 | FieldNameNotFound | Field name does not exist
500 | 1254060 | TextFieldConvFail | TextFieldConvFail
500 | 1254061 | NumberFieldConvFail | NumberFieldConvFail
500 | 1254062 | SingleSelectFieldConvFail | SingleSelectFieldConvFail
500 | 1254063 | MultiSelectFieldConvFail | MultiSelectFieldConvFail
500 | 1254064 | DatetimeFieldConvFail | DatetimeFieldConvFail
500 | 1254065 | CheckboxFieldConvFail | CheckboxFieldConvFail
500 | 1254066 | UserFieldConvFail | The value corresponding to the personnel field type is incorrect. The possible reasons are:<br>- The ID type specified by the user_id_type parameter does not match the type of the provided ID.<br>- An unrecognized type or structure was provided. Currently, only `id` is supported, and it must be passed as an array.<br>- An `open_id` was passed across applications. If you are passing an ID across applications, it is recommended to use `user_id`. The `open_id` obtained from different applications cannot be used interchangeably.
500 | 1254067 | LinkFieldConvFail | LinkFieldConvFail
500 | 1254068 | URLFieldConvFail | URLFieldConvFail
500 | 1254069 | AttachFieldConvFail | AttachFieldConvFail
400 | 1254072 | Failed to convert phone field, please make sure it is correct. | invalid phone format
400 | 1254100 | TableExceedLimit | TableExceedLimit, limited to 300
400 | 1254101 | ViewExceedLimit | ViewExceedLimit, limited to 200
400 | 1254102 | FileExceedLimit | FileExceedLimit
400 | 1254103 | RecordExceedLimit | RecordExceedLimit, limited to 20,000
400 | 1254104 | RecordAddOnceExceedLimit | RecordAddOnceExceedLimit, limited to 500
400 | 1254107 | FilterLengthExceedLimit | FilterLengthExceedLimit, limited to 2,000 characters
400 | 1254108 | SortLengthExceedLimit | SortLengthExceedLimit, limited to 1,000 characters
400 | 1254109 | FormulaTableSizeExceedLimit | FormulaTableSizeExceedLimit
400 | 1254130 | TooLargeCell | TooLargeCell
400 | 1254290 | TooManyRequest | Request too fast, try again later
400 | 1254291 | LockNotObtainedError | The same data table does not support concurrent calls to the write interface, please check whether there is a concurrent call to the write interface. The writing interface includes: adding, modifying, and deleting records; adding, modifying, and deleting fields; modifying forms; modifying views, etc.
400 | 1254301 | OperationTypeError | Base does not have advanced permissions enabled or does not support enabling advanced permissions
400 | 1254302 | RolePermNotAllow | No access rights, usually caused by the table opening of advanced permissions, please add a group containing applications in the advanced permissions settings and give this group read and write permissions
400 | 1254303 | AttachPermNotAllow | No attach permission
500 | 1255001 | InternalError | Internal error, have any questions can be consulting service
500 | 1255002 | Something went wrong. Please contact technical support at https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952 | Internal error, have any questions can be consulting service
500 | 1255003 | MarshalError | Serialization failed, have any questions can be consulting service
500 | 1255004 | UmMarshalError | Deserialization failed, have any questions can be consulting service
500 | 1255005 | ConvError | Internal error, have any questions can be consulting service
504 | 1255040 | Request timed out, please try again later | Try again
500 | 1254607 | Data not ready, please try again later | There are usually two situations when this error occurs: 1. The last submitted modification has not been processed; 2. The data is too large and the server calculation times out;This error code can be appropriately retried.

# Delete records

Delete records,up to 500 lines at a time.

## Prerequisites

Before calling this interface, make sure that the current calling identity (tenant_access_token or user_access_token) has document permissions such as Bitable's edit, otherwise the interface will return an HTTP 403 or 400 status code. For more information, refer to [How to enable document permissions for an application or user] (/ssl: ttdoc/ukTMukTMukTM/uczNzUjL3czM14yN3MTN #16c6475a).
## Precautions

- Data tables synchronized from other data sources do not support developers to add, delete, and modify records.
- Delete up to 500 records in a single call.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/tables/:table_id/records/batch_delete
HTTP Method | POST
Rate Limit | [50 per second](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.**<br>Enable any scope from the list | 删除记录(base:record:delete)<br>View, comment, edit and manage Base(bitable:app)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

The instructions for AccessToken calling Docs API are detailed here [Docs API Overview](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN)

### Path parameters

Parameter | Type | Description
---|---|---
app_token | string | base app_token<br>**Example value**: "appbcbWCzen6D8dezhoCH2RpMAh"
table_id | string | table_id<br>**Example value**: "tblsRc9GRRXKqhvW"

### Query parameters

Parameter | Type | Required | Description
---|---|---|---
ignore_consistency_check | boolean | No | Whether to ignore the consistency read and write check, the default is false, that is, when performing read and write operations, the system will ensure that the data read and written are the same. Optional value:<br>- true: Ignore read and write consistency checks to improve performance, but may cause data on some nodes to be out of sync and temporarily inconsistent<br>- false: Enable read and write consistency check to ensure that the data is consistent during read and write<br>**Example value**: false

### Request body

Parameter | Type | Required | Description
---|---|---|---
records | string\[\] | Yes | records<br>**Example value**: ["recwNXzPQv"]

### Request body example
```json
{
    "records": [
        "recwNXzPQv"
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
records | delete_record\[\] | records
deleted | boolean | deleted
record_id | string | record id

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "records": [
            {
                "deleted": true,
                "record_id": "recWqFb7xo"
            }
        ]
    }
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
200 | 1254000 | WrongRequestJson | Request error
200 | 1254001 | WrongRequestBody | Request body error
200 | 1254002 | Fail | Internal error, have any questions can be consulting service
200 | 1254003 | WrongBaseToken | AppToken error
200 | 1254004 | WrongTableId | Table id wrong
200 | 1254005 | WrongViewId | View id wrong
200 | 1254006 | WrongRecordId | Record id wrong
200 | 1254007 | EmptyValue | Empty value
200 | 1254008 | EmptyView | Empty view
200 | 1254009 | WrongFieldId | Wrong fieldId
200 | 1254010 | ReqConvError | Request error
200 | 1254030 | TooLargeResponse | TooLargeResponse
400 | 1254036 | Base is copying, please try again later. | Base copy replicating, try again later
200 | 1254040 | BaseTokenNotFound | AppToken not found
200 | 1254041 | TableIdNotFound | Table not found
200 | 1254042 | ViewIdNotFound | View not found
200 | 1254043 | RecordIdNotFound | RecordIdNotFound
200 | 1254044 | FieldIdNotFound | FieldIdNotFound
200 | 1254060 | TextFieldConvFail | TextFieldConvFail
200 | 1254061 | NumberFieldConvFail | NumberFieldConvFail
200 | 1254062 | SingleSelectFieldConvFail | SingleSelectFieldConvFail
200 | 1254063 | MultiSelectFieldConvFail | MultiSelectFieldConvFail
200 | 1254064 | DatetimeFieldConvFail | DatetimeFieldConvFail
200 | 1254065 | CheckboxFieldConvFail | CheckboxFieldConvFail
200 | 1254066 | UserFieldConvFail | The value corresponding to the personnel field type is incorrect. The possible reasons are:<br>- The ID type specified by the user_id_type parameter does not match the type of the provided ID.<br>- An unrecognized type or structure was provided. Currently, only `id` is supported, and it must be passed as an array.<br>- An `open_id` was passed across applications. If you are passing an ID across applications, it is recommended to use `user_id`. The `open_id` obtained from different applications cannot be used interchangeably.
200 | 1254067 | LinkFieldConvFail | LinkFieldConvFail
200 | 1254072 | InvalidPhoneNumber | Failed to convert phone field, please make sure it is correct.
200 | 1254100 | TableExceedLimit | TableExceedLimit, limited to 300
200 | 1254101 | ViewExceedLimit | ViewExceedLimit, limited to 200
200 | 1254102 | FileExceedLimit | FileExceedLimit
200 | 1254103 | RecordExceedLimit | RecordExceedLimit, limited to 20,000
200 | 1254104 | RecordAddOnceExceedLimit | RecordAddOnceExceedLimit, limited to 500
200 | 1254130 | TooLargeCell | TooLargeCell
200 | 1254290 | TooManyRequest | Request too fast, try again later
200 | 1254291 | Write conflict | The same data table does not support concurrent calls to the write interface, please check whether there is a concurrent call to the write interface. The writing interface includes: adding, modifying, and deleting records; adding, modifying, and deleting fields; modifying forms; modifying views, etc.
200 | 1254301 | OperationTypeError | Base does not have advanced permissions enabled or does not support enabling advanced permissions
200 | 1255001 | InternalError | Internal error, have any questions can be consulting service
200 | 1255002 | RpcError | Internal error, have any questions can be consulting service
200 | 1255003 | MarshalError | Serialization failed, have any questions can be consulting service
200 | 1255004 | UmMarshalError | Deserialization failed, have any questions can be consulting service
200 | 1255005 | ConvError | Internal error, have any questions can be consulting service
504 | 1255040 | Request timed out, please try again later | Try again
400 | 1254607 | Data not ready, please try again later | There are usually two situations when this error occurs: 1. The last submitted modification has not been processed; 2. The data is too large and the server calculation times out; <br>This error code can be appropriately retried.
403 | 1254302 | Permission denied. | No access rights, usually caused by the table opening of advanced permissions, please add a group containing applications in the advanced permissions settings and give this group read and write permissions
403 | 1254304 | Permission denied. | Advanced permissions for specific rows or columns are only available for Business and Enterprise editions
403 | 1254608 | ReqRecommited | Same API requests are submitted repeatedly.
