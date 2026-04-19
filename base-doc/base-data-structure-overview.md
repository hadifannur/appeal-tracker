# Data structure overview

This document introduces the data structure of records, fields, and views in Base tables. The data tables in Base consist of records and fields, and can have multiple views.

## Records
Records consist of two structures: record and fields.

### Record structure

A record is an object structure type.
| Parameter     | Data type         | Description        |
| --------- | -------   | --------- |
|`record_id`| string |  Record ID |
|`fields`| map |  Record fields |

### Fields structure

The fields attribute is of map type, consisting of key-value pairs of field names and their specific contents. For detailed structure and parameter descriptions of fields, refer to [Base record data structure](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/bitable-record-data-structure-overview).
```json
{
  "Task summary": [
    {
      "text": "The website update task is being handled by Huang Paopao and is in progress",
      "type": "text"
    }
  ]
}
```

Parameter | Data type | Description | Example value
---|---|---|---
key | string | Field name in the Base table. | "Task summary"
value | union | The specific content of a field, which can be a number, string, boolean, list of strings, or list of objects. For more details, refer to the following section. | This example value is a list of objects. For more examples, refer to [Base record data structure](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/bitable-record-data-structure-overview).<br>```json<br>[<br>{<br>"text": "The website update task is in progress",<br>"type": "text"<br>}<br>]<br>```

## Fields

Fields are the "columns" in the Base table and are of object structure type. The basic structure of a field is shown below. For detailed structure and parameter descriptions of fields, refer to the [Field editing guide](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-field/guide).

```json
{
    "field_id": "fldYWaldeW", // Field ID
    "field_name": "Text",   // Field name
    "type": 1,  // Field type, see below for details
    "description": "Field description", // More information about the field
    "is_primary": true,   // Whether this field is the primary index field
    "property": null,   // Field property, see below for details
    "ui_type": "Text",  // The display type of the field in the interface, such as progress field being a display form of a number
    "is_hidden": false  // Whether the field is hidden
}
```
Parameter descriptions are as follows:

Name | Type | Description
---|---|---
field_id | string | Field ID
field_name | string | Field name
type | int | Field type: differentiated by ui_type for the same type:<br>- 1: Text (default), Barcode (declare <code>"ui_type": "Barcode"</code>), Email (declare <code>"ui_type": "Email"</code>)<br>- 2: Number (default), Progress (declare <code>"ui_type": "Progress"</code>), Currency (declare <code>"ui_type": "Currency"</code>), Rating (declare <code>"ui_type": "Rating"</code>)<br>- 3: Single select<br>- 4: Multi select<br>- 5: Date<br>- 7: Checkbox<br>- 11: User<br>- 13: Phone number<br>- 15: URL<br>- 17: Attachment<br>- 18: Single link<br>- 19: Lookup<br>- 20: Formula<br>- 21: Duplex link<br>- 22: Location<br>- 23: Group<br>- 1001: Created time<br>- 1002: Last modified time<br>- 1003: Created by<br>- 1004: Modified by<br>- 1005: Auto number
description | Field description | More information about the field.
is_primary | true/false | Whether this field is the primary index field.
property | object | Field property, varies by field type. For details, refer to the [Field editing guide](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-field/guide).
ui_type | string | Field UI type:<br>- "Text": Text<br>- "Email": Email<br>- "Barcode": Barcode<br>- "Number": Number<br>- "Progress": Progress<br>- "Currency": Currency<br>- "Rating": Rating<br>- "SingleSelect": Single select<br>- "MultiSelect": Multi select<br>- "DateTime": Date<br>- "Checkbox": Checkbox<br>- "User": User<br>- "GroupChat": Group<br>- "Phone": Phone number<br>- "Url": URL<br>- "Attachment": Attachment<br>- "SingleLink": Single link<br>- "Formula": Formula<br>- "Lookup": Lookup<br>- "DuplexLink": Duplex link<br>- "Location": Location<br>- "CreatedTime": Created time<br>- "ModifiedTime": Last modified time<br>- "CreatedUser": Created by<br>- "ModifiedUser": Modified by<br>- "AutoNumber": Auto number
is_hidden | true/false | Whether the field is hidden.

## Views

A view is an object structure type.

Parameter | Type | Description
---|---|---
view_id | string | View ID. `view_id` is unique within a Base table but not necessarily globally unique. Retrieval methods:<br>- You can obtain the `view_id` through the Base table URL. The highlighted part in the image below is the unique identifier of the current view.<br>![](//sf3-cn.feishucdn.com/obj/open-platform-opendoc/140668632c97e0095832219001d17c54_c76RMwZAgW.png?height=748&lazyload=true&maxWidth=700&width=2998)<br>- You can also obtain the `view_id` through the [list views](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-view/list) API. Currently, it is not possible to obtain the `view_id` of a Base table embedded in a document.
view_name | string | View name
view_type | string | View type, supporting the following types, with grid as the default type.<br>- grid: Grid view<br>- kanban: Kanban view<br>- gallery: Gallery view<br>- gantt: Gantt view<br>- form: Form view

## Custom data structure

### delete_record
| Parameter         | Data type           |  Description         | 
| --------- | --------------- | ----------- | 
|`deleted` | `boolean` | Whether the deletion was successful |
|`record_id` | `string` | ID of a single record |
