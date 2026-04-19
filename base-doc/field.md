# Field editing guide

Fields are the "columns" in a Base data table and are of the `object` structure type. When adding or updating fields in a Base data table, you can refer to this document to learn how to select field types and set field properties.

The basic structure of a field is as follows:

```json
{
    "field_id": "fldYWaldeW", // Field ID
    "field_name": "test",   // Field name
    "type": 1,  // Field type, see below for details
    "description": "description", // More description of the field
    "is_primary": true,   // Whether the field is the primary index field
    "property": null,   // Field properties, see below for details
    "ui_type": "Text",  // Field display type on the interface, e.g., progress field is a type of number display
    "is_hidden": false  // Whether the field is hidden
}
```
Parameter descriptions are as follows:

Name | Type | Description
---|---|---
field_id | string | Field ID
field_name | string | Field name
type | int | Field type: different types are distinguished by ui_type:<br>- 1: Text (default), Barcode (requires <code>"ui_type": "Barcode"</code>), Email (requires <code>"ui_type": "Email"</code>)<br>- 2: Number (default), Progress (requires <code>"ui_type": "Progress"</code>), Currency (requires <code>"ui_type": "Currency"</code>), Rating (requires <code>"ui_type": "Rating"</code>)<br>- 3: Single select<br>- 4: Multi select<br>- 5: Date<br>- 7: Checkbox<br>- 11: User<br>- 13: Phone number<br>- 15: URL<br>- 17: Attachment<br>- 18: Single link<br>- 19: Lookup<br>- 20: Formula<br>- 21: Duplex link<br>- 22: Location<br>- 23: Group<br>- 24: Stage<br>- 1001: Created time<br>- 1002: Modified time<br>- 1003: Created user<br>- 1004: Modified user<br>- 1005: Auto number<br>- 3001: Button
description | string | More description of the field.
is_primary | true/false | Whether the field is the primary index field.
property | object | Field properties, vary by field type. See [Field editing guide](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-field/guide) for details.
ui_type | string | Field UI type:<br>- "Text": Text<br>- "Email": Email<br>- "Barcode": Barcode<br>- "Number": Number<br>- "Progress": Progress<br>- "Currency": Currency<br>- "Rating": Rating<br>- "SingleSelect": Single select<br>- "MultiSelect": Multi select<br>- "DateTime": Date<br>- "Checkbox": Checkbox<br>- "User": User<br>- "GroupChat": Group chat<br>- "Stage": Stage<br>- "Phone": Phone number<br>- "Url": URL<br>- "Attachment": Attachment<br>- "SingleLink": Single link<br>- "Formula": Formula<br>- "Lookup": Lookup<br>- "DuplexLink": Duplex link<br>- "Location": Location<br>- "CreatedTime": Created time<br>- "ModifiedTime": Modified time<br>- "CreatedUser": Created user<br>- "ModifiedUser": Modified user<br>- "AutoNumber": Auto number<br>- "Button": Button
is_hidden | true/false | Whether the field is hidden.

## Index field description

In a data table, the first column is the index column, i.e., the index field. `"is_primary": true` indicates that the field is an index field. Indexes cannot be deleted, moved, or hidden, and only support the following field types (type):
- 1: Multiline text
- 2: Number
- 5: Date
- 13: Phone number
- 15: URL
- 20: Formula
- 22: Location

## Field type `type`

Base provides a variety of field types, corresponding to the parameter `type`. A field type may have multiple display types on the interface, corresponding to the parameter `ui_type`. For example, when the field type `type` is enumerated as 1, it indicates a text type, and the corresponding UI display type `ui_type` can be:
- `Text`: Text display type
- `Barcode`: Barcode display type
- `Email`: Email display type

The following are the enumeration values for field types and field UI display types:
Different interfaces support different field types. Please refer to the corresponding interface documentation for the optional values of field types.

Enumeration values of field type `type` | Enumeration values of field UI display type <code>ui_type</code>
---|---
- 1: Text (default), Barcode (requires <code>"ui_type": "Barcode"</code>), Email (requires <code>"ui_type": "Email"</code>)<br>- 2: Number (default), Progress (requires <code>"ui_type": "Progress"</code>), Currency (requires <code>"ui_type": "Currency"</code>), Rating (requires <code>"ui_type": "Rating"</code>)<br>- 3: Single select<br>- 4: Multi select<br>- 5: Date<br>- 7: Checkbox<br>- 11: User<br>- 13: Phone number<br>- 15: URL<br>- 17: Attachment<br>- 18: Single link<br>- 19: Lookup<br>- 20: Formula<br>- 21: Duplex link<br>- 22: Location<br>- 23: Group<br>- 24: Stage (not supported through write interface for adding or editing, only supported through read interface)<br>- 1001: Created time<br>- 1002: Modified time<br>- 1003: Created user<br>- 1004: Modified user<br>- 1005: Auto number<br>- 3001: Button (not supported through write interface for adding or editing, only supported through read interface) | - "Text": Text<br>- "Email": Email<br>- "Barcode": Barcode<br>- "Number": Number<br>- "Progress": Progress<br>- "Currency": Currency<br>- "Rating": Rating<br>- "SingleSelect": Single select<br>- "MultiSelect": Multi select<br>- "DateTime": Date<br>- "Checkbox": Checkbox<br>- "User": User<br>- "GroupChat": Group chat<br>- "Stage": Stage<br>- "Phone": Phone number<br>- "Url": URL<br>- "Attachment": Attachment<br>- "SingleLink": Single link<br>- "Formula": Formula<br>- "Lookup": Lookup<br>- "DuplexLink": Duplex link<br>- "Location": Location<br>- "CreatedTime": Created time<br>- "ModifiedTime": Modified time<br>- "CreatedUser": Created user<br>- "ModifiedUser": Modified user<br>- "AutoNumber": Auto number<br>- "Button": Button

# Field properties

Field properties refer to additional functional attributes specified for a field type. For example, for a user type field, whether to enable the feature to add multiple members. The `property` structure corresponding to different types of fields is different. The following types of fields have no additional functional attributes, and their `property` is `null`:
- 1: Text (default), Email (requires `"ui_type": "Email"`)
- 7: Checkbox
- 13: Phone number
- 15: URL
- 17: Attachment
- 19: Lookup
- 1003: Created user
- 1004: Modified user

For example, when the field type is text and the field UI display type is email, its `property` should be set to `null`:

```json
{
    "field_name": "Email",
    "type": 1,
    "ui_type": "Email",
    "property": null
}
```

Other types of fields have additional functional attributes. You can refer to the following to understand and use the `property` structure of different types of fields.

### Barcode field

The field type of the barcode field is `1`, and the UI display type `ui_type` is `"Barcode"`. Its functional attributes are as follows:

Name | Type | Required | Description
---|---|---|---
allowed_edit_modes | allowed_edit_modes | No | Configuration of the barcode field
manual | <md-text type="field-type">bool | No | Whether manual input is allowed. Default is true.
<md-text type="field-name">scan | <md-text type="field-type">bool | No | Whether mobile input is allowed. Default is true.

#### Request body example

The request body example for adding or updating a field is as follows:
```json
{
    "field_name": "Barcode",
    "type": 1,
    "ui_type": "Barcode",
    "property": {
        "allowed_edit_modes": {
            "scan": true,
            "manual": true
        }
    }
}
```

#### Response body example

```json
{
  "code": 0,
  "data": {
    "field": {
      "field_id": "fldQoEj2p3",
      "field_name": "Barcode",
      "is_primary": false,
      "property": {
        "allowed_edit_modes": {
          "manual": true,
          "scan": true
        }
      },
      "type": 1,
      "ui_type": "Barcode"
    }
  },
  "msg": "success"
}
```
### Number field

The field type of the number field is `2`, and there is no need to declare the UI display type `ui_type`. Its functional attributes are as follows:

Name | Type | Required | Description
---|---|---|---
formatter | string | No | Number format, default is "0.0", enumeration values are as follows:<br>- "0": Integer<br>- "0.0": 1 decimal place<br>- "0.00": 2 decimal places<br>- "0.000": 3 decimal places<br>- "0.0000": 4 decimal places<br>- "1,000": Thousands separator<br>- "1,000.00": Thousands separator (decimal point)<br>- "%": Percentage<br>- "0.00%": Percentage (decimal point)<br>- "¥": RMB<br>- "¥0.00": RMB (decimal point)<br>- "$": USD<br>- "$0.00": USD (decimal point)

#### Request body example

The request body example for adding or updating a field is as follows:
```json
{
    "field_name": "Number",
    "type": 2,
    "property": {
        "formatter": "0.00"
    }
}
```

#### Response body example

```json
{
  "code": 0,
  "data": {
    "field": {
      "field_id": "fldP9gzwe7",
      "field_name": "Number",
      "is_primary": false,
      "property": {
        "formatter": "0.00"
      },
      "type": 2,
      "ui_type": "Number"
    }
  },
  "msg": "success"
}
```

### Currency field

The field type of the currency field is `2`, and the UI display type `ui_type` is `"Currency"`. Its functional attributes are as follows:

Name | Type | Required | Description
---|---|---|---
formatter | <md-text type="field-type">string | Yes | Number of decimal places for the currency, enumeration values are as follows:<br>- "0": Integer<br>- "0.0": 1 decimal place<br>- "0.00": 2 decimal places<br>- "0.000": 3 decimal places<br>- "0.0000": 4 decimal places
<md-text type="field-name">currency_code | <md-text type="field-type">string | Yes | Specific type of currency, enumeration values are as follows:<br>- "CNY": RMB, currency symbol is ¥<br>- "USD": USD, currency symbol is $<br>- "EUR": Euro, currency symbol is €<br>- "GBP": GBP, currency symbol is £<br>- "AED": AED, currency symbol is dh<br>- "AUD": AUD, currency symbol is $<br>- "BRL": BRL, currency symbol is R$<br>- "CAD": CAD, currency symbol is $<br>- "CHF": CHF, currency symbol is CHF<br>- "HKD": Hong Kong Dollar, currency symbol is $<br>- "INR": Indian Rupee, currency symbol is ₹ <br>- "IDR": Indonesian Rupiah, currency symbol is Rp <br>- "JPY": Japanese Yen, currency symbol is ¥ <br>- "KRW": Korean Won, currency symbol is ₩ <br>- "MOP": Macanese Pataca, currency symbol is MOP$ <br>- "MXN": Mexican Peso, currency symbol is $ <br>- "MYR": Malaysian Ringgit, currency symbol is RM <br>- "PHP": Philippine Peso, currency symbol is ₱ <br>- "PLN": Polish Zloty, currency symbol is zł <br>- "RUB": Russian Ruble, currency symbol is ₽ <br>- "SGD": Singapore Dollar, currency symbol is $ <br>- "THB": Thai Baht, currency symbol is ฿ <br>- "TRY": Turkish Lira, currency symbol is ₺ <br>- "TWD": New Taiwan Dollar, currency symbol is NT$ <br>- "VND": Vietnamese Dong, currency symbol is ₫

#### Request body example

The request body example for adding or updating a field is as follows:
```json
{
    "field_name": "Currency",
    "type": 2,
    "ui_type": "Currency",
    "property": {
        "formatter": "0", 
        "currency_code": "MOP"
    }
}
```

#### Response body example

```json
{
  "code": 0,
  "data": {
    "field": {
      "field_id": "fld6vPlPZ1",
      "field_name": "Currency",
      "is_primary": false,
      "property": {
        "currency_code": "MOP",
        "formatter": "0"
      },
      "type": 2,
      "ui_type": "Currency"
    }
  },
  "msg": "success"
}
```

### Progress field

The field type of the progress field is `2`, and the UI display type `ui_type` is `"Progress"`. Its functional attributes are as follows:

Name | Type | Required | Description
---|---|---|---
formatter | string | Yes | Progress format, enumeration values are as follows:<br>- "0": Integer, no decimal places<br>- "0.0": Value, 1 decimal place<br>- "0.00": Value, 2 decimal places<br>- "0%": Percentage, integer<br>- "0.0%": Percentage, 1 decimal place<br>- "0.00%": Percentage, 2 decimal places
<md-text type="field-name">range_customize | <md-text type="field-type">bool | No | Whether to allow custom progress bar values, default is false.
<md-text type="field-name">min | <md-text type="field-type">number | Required when range_customize is true | Minimum value of the progress
<md-text type="field-name">max | <md-text type="field-type">number | Required when range_customize is true | Maximum value of the progress

#### Request body example

The request body example for adding or updating a field is as follows:
```json
{
    "field_name": "Progress",
    "type": 2,
    "ui_type": "Progress",
    "property": {
        "formatter": "0.00%", 
        "min": 0.1,
        "max": 4,
        "range_customize": true  
    }
}
```

#### Response body example

```json
{
  "code": 0,
  "data": {
    "field": {
      "field_id": "fldANhA0do",
      "field_name": "Progress",
      "is_primary": false,
      "property": {
        "formatter": "0.00%",
        "max": 100,
        "min": 0.1,
        "range_customize": true
      },
      "type": 2,
      "ui_type": "Progress"
    }
  },
  "msg": "success"
}
```

### Rating field

The type of the rating field `type` is `2`, and the UI display type `ui_type` is `"Rating"`. Its functional properties are as follows:

Name | Type | Required | Description
---|---|---|---
formatter | string | Yes | The format of the rating, fixed as "0"
rating | rating | No | Rating settings
symbol | string | No | The icon for the rating, default is "star". The enumeration values are as follows: <br>- "star": star<br>- "heart": heart<br>- "thumbsup": thumbs up<br>- "fire": fire<br>- "smile": smiley face<br>- "lightning": lightning<br>- "flower": flower<br>- "number": number
min | number | Yes | The minimum value of the rating, can be 0 or 1.
max | number | Yes | The maximum value of the rating, an integer between 1 and 10 inclusive.

#### Request body example

The request body example for adding or updating a field is as follows:
```json
{
    "field_name": "评分",
    "type": 2,
    "ui_type": "Rating",
    "property": {
        "formatter": "0",
        "min": 0,
        "max": 10,
        "rating": {
            "symbol": "lightning"
        }
    }
}
```

#### Response body example

```json
{
  "code": 0,
  "data": {
    "field": {
      "field_id": "fldTOLqnni",
      "field_name": "评分",
      "is_primary": false,
      "property": {
        "formatter": "0",
        "max": 10,
        "min": 0,
        "rating": {
          "symbol": "lightning"
        }
      },
      "type": 2,
      "ui_type": "Rating"
    }
  },
  "msg": "success"
}
```

### Single select field

The type of the single select field `type` is `3`. Its functional properties are as follows:

Name | Type | Required | Description
---|---|---|---
options | app.table.field.property.option&lt;string&gt;[] | No | Option list
id | string | No | Option ID. For the add field interface, there is no need to specify the option ID
name | string | No | Option name
color | int | No | Option color, default increments from the previous option's color. Range: 0~54

#### Request body example for adding a field

```json
{
    "field_name": "单选",
    "type": 3,
    "property": {
        "options": [
            {
                "name": "选项 A"
            },
            {
                "name": "选项 B"
            },
            {
                "name": "选项 C",
                "color": 5
            },
            {
                "name": "选项 D"
            }
        ]
    }
}
```

#### Response body example for adding a field

```json
{
  "code": 0,
  "data": {
    "field": {
      "field_id": "fldQrcCPFs",
      "field_name": "单选",
      "is_primary": false,
      "property": {
        "options": [
          {
            "color": 0,
            "id": "optQQM0hOZ",
            "name": "选项 A"
          },
          {
            "color": 1,
            "id": "opt6wdUh3n",
            "name": "选项 B"
          },
          {
            "color": 5,
            "id": "optazha8oD",
            "name": "选项 C"
          },
          {
            "color": 6,
            "id": "optLdIy4nl",
            "name": "选项 D"
          }
        ]
      },
      "type": 3,
      "ui_type": "SingleSelect"
    }
  },
  "msg": "success"
}
```

#### Example request body for updating fields

To update the name of option A to `a++`, keep option B unchanged, delete options C and D, and add option Z, the request body is as follows:
```json
{
    "field_name": "single choice",
    "type": 3,
    "property": {
        "options": [
            {
                "color": 0,
                "id": "optQQM0hOZ",
                "name": "a++"
            },
            {
                "color": 1,
                "id": "opt6wdUh3n",
                "name": "option B"
            },
            {
                "color": 6,
                "name": "option Z"
            }
        ]
    }
}
```

#### Example response body for updating fields

Updating fields is a full update, options C and D have been deleted, the response body is as follows:
```json
{
    "code": 0,
    "data": {
        "field": {
            "field_id": "fldQrcCPFs",
            "field_name": "single choice",
            "property": {
                "options": [
                    {
                        "color": 0,
                        "id": "optQQM0hOZ",
                        "name": "a++"
                    },
                    {
                        "color": 1,
                        "id": "opt5g3xLFT",
                        "name": "option B"
                    },
                    {
                        "color": 6,
                        "id": "opt558YmTi",
                        "name": "option Z"
                    }
                ]
            },
            "type": 3
        }
    },
    "msg": "Success"
}
```

### Multi-select field

The type `type` of the multi-select field is `4`. Its functional properties are as follows:

Name | Type | Required | Description
---|---|---|---
options | app.table.field.property.option&lt;string&gt;[] | No | Option list
id | string | No | Option ID. For the add field interface, there is no need to specify the option ID
name | <md-text type="field-type">string | No | Option name
color | <md-text type="field-type">int | No | Option color, default incremented from the previous option's color. Range: 0~54

#### Example request body for adding fields

```json
{
    "field_name": "multi-select",
    "type": 4,
    "property": {
        "options": [
            {
                "name": "a"
            },
            {
                "name": "b"
            },
            {
                "name": "c",
                "color": 5
            },
            {
                "name": "d"
            }
        ]
    }
}
```

#### Example response body for adding fields

```json
{
  "code": 0,
  "data": {
    "field": {
      "field_id": "fldLyDzkdA",
      "field_name": "multi-select",
      "is_primary": false,
      "property": {
        "options": [
          {
            "color": 0,
            "id": "opt2H40Z1F",
            "name": "a"
          },
          {
            "color": 1,
            "id": "optYQrPhiq",
            "name": "b"
          },
          {
            "color": 5,
            "id": "opt0xiSsy9",
            "name": "c"
          },
          {
            "color": 6,
            "id": "optNudypoa",
            "name": "d"
          }
        ]
      },
      "type": 4,
      "ui_type": "MultiSelect"
    }
  },
  "msg": "success"
}
```

#### Example request body for updating fields

To update the option name of `a` to `a++`, keep option `b` unchanged, delete options `c` and `d`, and add option `z`, the request body is as follows:
```json
{
    "field_name": "单选",
    "type": 3,
    "property": {
        "options": [
            {
                "color": 0,
                "id": "optpeuQVqp",
                "name": "a++"
            },
            {
                "color": 1,
                "id": "opt5g3xLFT",
                "name": "b"
            },
            {
                "color": 6,
                "name": "z"
            }
        ]
    }
}
```

#### Example response body for updating fields

Updating fields is a full update, options `c` and `d` have been deleted, the response body is as follows:
```json
{
    "code": 0,
    "data": {
        "field": {
            "field_id": "fld2RxOyB8",
            "field_name": "single choice",
            "property": {
                "options": [
                    {
                        "color": 0,
                        "id": "optpeuQVqp",
                        "name": "a++"
                    },
                    {
                        "color": 1,
                        "id": "opt5g3xLFT",
                        "name": "b"
                    },
                    {
                        "color": 6,
                        "id": "opt558YmTi",
                        "name": "z"
                    }
                ]
            },
            "type": 3
        }
    },
    "msg": "Success"
}
```

### Date field

The type `type` of the date field is `5`. Its functional properties are as follows:

Name | Type | Required | Description
---|---|---|---
date_formatter | string | No | Date format, default is "yyyy/MM/dd", enumeration values are as follows: <br>- "yyyy/MM/dd": format like 2021/01/30<br>- "yyyy-MM-dd HH:mm"：2021-01-30 14:00<br>- "MM-dd"：01-30<br>- "MM/dd/yyyy"：01/30/2021<br>- "dd/MM/yyyy"：30/01/2021
auto_fill | boolean | No | For new records, whether to automatically fill in the creation time. Default is false.

#### Example request body

The example request body for adding and updating fields is as follows:
```json
{
    "field_name": "date",
    "type": 5,
    "property": {
        "date_formatter": "yyyy/MM/dd HH:mm",
        "auto_fill": false
    }
}
```

#### Example response body

```json
{
    "code": 0,
    "data": {
        "field": {
            "field_id": "fldHBDkAfH",
            "field_name": "date",
            "property": {
                "auto_fill": false,
                "date_formatter": "yyyy/MM/dd HH:mm"
            },
            "type": 5
        }
    },
    "msg": "Success"
}
```

### Personnel field

The type `type` of the personnel field is `11`. Its functional properties are as follows:
| Name     | Type    | Required | Description                        |
| -------- | ------- | -------- | ---------------------------------- |
| multiple | boolean | No       | Whether to allow adding multiple members, default is true. |

#### Example request body

The example request body for adding and updating fields is as follows:
```json
{
    "field_name": "personnel",
    "type": 11,
    "property": {
        "multiple": true
    }
}
```

#### Example response body

```json
{
    "code": 0,
    "data": {
        "field": {
            "field_id": "fldlQDzjyK",
            "field_name": "personnel",
            "property": {
                "multiple": true
            },
            "type": 11
        }
    },
    "msg": "Success"
}
```

### Unidirectional association field

The type `type` of the unidirectional association is `18`. Its functional properties are as follows:
| Name     | Type    | Required | Description                        |
| -------- | ------- | -------- | ---------------------------------- |
| multiple | boolean | No       | Whether to allow adding multiple records, default is true. |
| table_id | string  | Yes      | ID of the associated data table    |

#### Example request body

The example request body for adding and updating fields is as follows:
```json
{
    "field_name": "unidirectional association",
    "type": 18,
    "property": {
        "multiple": true,
        "table_id": "tblw92ErelmCmgHc"
    }
}
```

#### Example response body

```json
{
    "code": 0,
    "data": {
        "field": {
            "field_id": "fldNdr8VNW",
            "field_name": "unidirectional association",
            "property": {
                "multiple": true,
                "table_id": "tblw92ErelmCmgHc",
                "table_name": "Table 2"
            },
            "type": 18
        }
    },
    "msg": "Success"
}
```

### Bidirectional association field

The type `type` of the bidirectional association is `21`. Its functional properties are as follows:
| Name              | Type      | Required | Description                                 |
| ---------------   | -------   | -------- | ------------------------------------------- |
| back_field_name   | string    | No       | ID of the bidirectional association field in the associated data table, default is "associated table name-field name" |
| multiple          | boolean   | No       | Whether to allow adding multiple records, default is true.               |
| table_id          | string    | Yes      | ID of the associated data table                         |

#### Example request body

The example request body for adding and updating fields is as follows:
```json
{
    "field_name": "bidirectional association",
    "type": 21,
    "property": {
        "multiple": true,
        "table_id": "tblw92ErelmCmgHc",
        "back_field_name": "bidirectional association table-auto generated"
    }
}
```

#### Example response body

```json
{
    "code": 0,
    "data": {
        "field": {
            "field_id": "fldpfIDIi0",
            "field_name": "bidirectional association",
            "property": {
                "back_field_id": "fldmQGUnWh",  // ID of the bidirectional association field in the associated data table
                "back_field_name": "bidirectional association table-auto generated",
                "multiple": true,
                "table_id": "tblw92ErelmCmgHc",
                "table_name": "Table 2"   // Name of the associated data table
            },
            "type": 21
        }
    },
    "msg": "Success"
}
```

### Formula field

The type `type` of the formula field is `20`. Its functional properties are as follows:

Name | Type | Required | Description
---|---|---|---
formatter | <md-text type="field-type">string | No | Formula format, default is empty. It can be a number, currency, or date. Optional values are as follows:<br>- "0": integer <br>- "0.0": one decimal place <br>- "0.00": two decimal places <br>- "1,000": thousand separator <br>- "1,000.00": thousand separator (decimal) <br>- "%": percentage <br>- "0.00%": percentage (decimal) <br>- "¥": RMB <br>- "¥0.00": RMB (decimal) <br>- "$": USD <br>- "$0.00": USD (decimal) <br>- "yyyy/MM/dd HH:mm": 2021/01/30 14:00 <br>- "yyyy/MM/dd": 2021/01/30 <br>- "yyyy-MM-dd": 2021-01-30 <br>- "MM-dd": 01-30
formula_expression | <md-text type="field-type">string | No | Formula expression. Refer to the [Feishu Help Center](https://www.feishu.cn/hc/zh-CN/articles/360049067853-%E5%A4%9A%E7%BB%B4%E8%A1%A8%E6%A0%BC%E5%85%AC%E5%BC%8F%E5%AD%97%E6%AE%B5%E6%A6%82%E8%BF%B0) document to learn how to set formulas.

#### Example request body

The example request body for adding or updating fields is as follows:
```json
{
    "field_name": "formula",
    "type": 20,
    "property": {
        "formatter": "0.00%",
        "formula_expression": "IF(bitable::$table[tblxxxxxxxxxxxxx].$field[fldxxxxxxx].CONTAIN(\"Feishu\"),\"aaa\",\"bbb\")"
    }
}
```

#### Example response body

```json
{
    "code": 0,
    "data": {
        "field": {
            "field_id": "fldFuAdYEI",
            "field_name": "formula",
            "property": {
                "formatter": "0.00%",
                "formula_expression": "IF(bitable::$table[tblxxxxxxxxxxxxx].$field[fldxxxxxxx].CONTAIN(\"Feishu\"),\"aaa\",\"bbb\")"
            },
            "type": 20
        }
    },
    "msg": "Success"
}
```

### Location field

The type `type` of the location field is `22`. Its functional properties are as follows:

Name | Type | Required | Description
---|---|---|---
location | app.field.property.location | No | Geolocation input method
input_type | string | Yes | Geolocation input restriction, optional values are: <br>- only_mobile: only allow real-time location on mobile devices <br>- not_limit: no restriction, can input any geolocation

#### Example request body

The example request body for adding or updating fields is as follows:
```json
{
    "field_name": "location",
    "type": 22,
    "property": {
        "location": {
            "input_type": "not_limit"
        }
    }
}
```

#### Example response body

```json
{
  "code": 0,
  "data": {
    "field": {
      "field_id": "fldc7JNkVa",
      "field_name": "location",
      "is_primary": false,
      "property": {
        "location": {
          "input_type": "not_limit"
        }
      },
      "type": 22,
      "ui_type": "Location"
    }
  },
  "msg": "success"
}
```

### Group field

The type `type` of the group field is `23`. Its functional properties are as follows:
| Name     | Type    | Required | Description                        |
| -------- | ------- | -------- | ---------------------------------- |
| multiple | boolean | No       | Whether to allow adding multiple groups, default is true. |

#### Example request body

The example request body for adding or updating fields is as follows:
```json
{
    "field_name": "group field - allow adding multiple groups",
    "type": 23,
    "property": {
        "multiple": true
    },
    "description": {
        "disable_sync": false,
        "text": "group field - allow adding multiple groups"
    }
}
```

#### Example response body

```json
{
    "code": 0,
    "data": {
        "field": {
            "description": {
                "disable_sync": false,
                "text": "group field - allow adding multiple groups"
            },
            "field_id": "fldw6fSubT",
            "field_name": "group field - allow adding multiple groups",
            "is_primary": false,
            "property": {
                "multiple": true
            },
            "type": 23,
            "ui_type": "GroupChat"
        }
    },
    "msg": "success"
}
```

### Creation time and last update time fields

The type `type` of the creation time field is `1001`. The type `type` of the last update time field is `1002`. Their functional properties are the same, as follows:

Name | Type | Required | Description
---|---|---|---
date_formatter | string | No | Date format, default is "yyyy/MM/dd", enum values are as follows: <br>- "yyyy/MM/dd": format like 2021/1/30<br>- "yyyy-MM-dd HH:mm": 2021/01/30 14:00<br>- "MM-dd": 01-30<br>- "MM/dd/yyyy": 01/30/2021<br>- "dd/MM/yyyy": 30/01/2021

#### Example request body

The example request body for adding or updating the "creation time" field is as follows:
```json
{
    "field_name": "creation time",
    "type": 1001,
    "property": {
        "date_formatter": "yyyy/MM/dd"
    }
}
```

#### Example response body

```json
{
    "code": 0,
    "data": {
        "field": {
            "field_id": "fldoblwmUC",
            "field_name": "creation time",
            "property": {
                "date_formatter": "yyyy/MM/dd"
            },
            "type": 1001
        }
    },
    "msg": "Success"
}
```

### Auto number field

The type `type` of the auto number field is `1005`. Its functional properties are as follows:

Name | Type | Required | Description
---|---|---|---
auto_serial | <md-text type="field-type">app.field.property.auto_serial | No | Auto number
<md-text type="field-name">type | <md-text type="field-type">string | Yes | Auto number type, optional values are as follows: <br>- "custom": custom number <br>- "auto_increment_number": auto-increment number
<md-text type="field-name">reformat_existing_records | <md-text type="field-type">bool | No | Whether to apply changes to existing numbers, default is false.
<md-text type="field-name">options | <md-text type="field-type">app.field.property.auto_serial.options[] | No | Custom number rule list
<md-text type="field-name">type | <md-text type="field-type">string | Yes | Rule type, optional values are as follows: <br>- "system_number": number of digits for auto-increment number, range is 1-9 <br>- "fixed_text": fixed characters, maximum character length is 20 <br>- "created_time": creation date
<md-text type="field-name">value | <md-text type="field-type">string | Yes | Value corresponding to the rule type. <br>- If the rule type is `"type": "system_number"`, value is an integer in the range of 1-9, indicating the number of digits for auto-increment number <br>- If the rule type is `"type": "fixed_text"`, value is fixed characters within 20 characters <br>- If the rule type is "type": "created_time", value is used to specify the date format. Optional values are as follows: - "yyyyMMdd": date format is 20220130 <br>- "yyyyMM": date format is 202201 <br>- "yyyy": date format is 2022 <br>- "MMdd": date format is 130, indicating January 30 <br>- "MM": date format is 1, indicating the month - "dd": date format is 30, indicating the day

#### Example of adding "custom" auto number

To add or update a field with the "custom" type auto number, the example request body is as follows:
```json
{
    "field_name": "custom number",
    "property": {
        "auto_serial": {
            "type": "custom",
            "reformat_existing_records": true, 
            "options": [
                {
                    "type": "system_number",
                    "value": "3" 
                },
                {
                    "type": "fixed_text", 
                    "value": "keyword"
                },
                {
                    "type": "created_time",
                    "value": "yyyyMMdd"
                }
            ]
        }
    },
    "type": 1005
}
```
The corresponding example response body is as follows:
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "field": {
            "property": {
                "auto_serial": {
                    "type": "custom",
                    "options": [
                        {
                            "type": "system_number",
                            "value": "3"
                        },
                        {
                            "value": "keyword",
                            "type": "fixed_text"
                        },
                        {
                            "type": "created_time",
                            "value": "yyyyMMdd"
                        }
                    ]
                }
            },
            "field_id": "fldmVunQuc",
            "field_name": "custom number",
            "type": 1005
        }
    }
}
```

#### Example of adding "auto_increment_number" auto number

To add or update a field with the "auto_increment_number" type auto number, the example request body is as follows:
```json
{
    "field_name": "auto-increment number auto number",
    "property": {
        "auto_serial": {
            "type": "auto_increment_number",
            "reformat_existing_records": true
        }
    },
    "type": 1005
}
```
The corresponding example response body is as follows:
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "field": {
            "field_name": "auto-increment number auto number",
            "type": 1005,
            "property": {
                "auto_serial": {
                    "type": "auto_increment_number"
                }
            },
            "field_id": "fldwq16vz2"
        }
    }
}
```

# Attachment field

**Notice**：Before using this API, carefully read [Materials Overview](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/media/introduction).

## Data structure

| Field name | Field description |
|:---|:---|
 |file_token | file token|
 | name | file name |
 |size | file size |
 |tmp_url|A temporary download link|
 |type|file type|
 |url| URL for download the file|

**Response body**

```json 
{
  "Attachment": [
    {
      "file_token": "boxcnzm3dPEcutYDPplx5iDak4b",
      "name": "Hawaii_1_15Retina_R.jpg",
      "size": 5069121,
      "tmp_url": "https://open.feishu.cn/open-apis/drive/v1/medias/batch_get_tmp_download_url?file_tokens=boxcnzm3dPEcutYDPplx5iDak4b",
      "type": "image/jpeg",
      "url": "https://open.feishu.cn/open-apis/drive/v1/medias/boxcnzm3dPEcutYDPplx5iDak4b/download"
    }
]
}
``` 

## Upload attachments

Upload attachments, upload attachments in a multi-dimensional table in 2 steps

1.Call[Upload media](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/media/upload_all) or [Upload media in blocks](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/media/upload_prepare) interface upload file, upload success after obtaining the file fille_token

2.Call [CreateRecord](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/create) or [UpdateRecord](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/update) to update files to records; 

**Request body**

```json 
 {
    "records": [
        {
            "fields": {
            "Attachment": [
                {"file_token": "boxbcCFb2dBwMK9S8kDILk1tayh"},
                {"file_token": "boxbcCFb2dBwMK9S8kDILk1tayh"}
                ]
             }
        },
        {
            "fields": {
            "Attachment": [
                {"file_token": "boxbcCFb2dBwMK9S8kDILk1tayh"},
                {"file_token": "boxbcCFb2dBwMK9S8kDILk1tayh"}
                ]
             }
        }

]

}
``` 
**Response body：**
```json 
{
    "code": 0,
    "data": {
        "records": [
            {
                "fields": {
                    "Attachment": [
                        {
                            "file_token": "boxbcCFb2dBwMK9S8kDILk1tayh"
                        },
                        {
                            "file_token": "boxbcCFb2dBwMK9S8kDILk1tayh"
                        }
                    ]
                },
                "id": "recxgOKlB0"
            },

{
                "fields": {
                    "Attachment": [
                        {
                            "file_token": "boxbcCFb2dBwMK9S8kDILk1tayh"
                        },
                        {
                            "file_token": "boxbcCFb2dBwMK9S8kDILk1tayh"
                        }
                    ]
                },
                "id": "reciGVHpI8"
            }
        ]
    },
    "msg": "Success"
}

``` 

## Download Attachment

1.Call [ListRecord](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/list)  to query the attachments file token

2.Call[Download media](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/media/download) . or [Get temporary download URL of media](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/media/batch_get_tmp_download_url) These interface already supports Base.

# Create field

Create a field

**Notice**：This API supports up to 10 queries per second (QPS).

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/tables/:table_id/fields
HTTP Method | POST
Rate Limit | [10 per second](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.**<br>Enable any scope from the list | 新增字段(base:field:create)<br>View, comment, edit and manage Base(bitable:app)

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
client_token | string | No | The format is a standard uuidv4, the unique identifier of the operation, used for idempotent update operations. This value is null to indicate that a new request will be initiated, and this value is non-null to indicate idempotent update operations.<br>**Example value**: fe599b60-450f-46ff-b2ef-9f6675625b97

### Request body

Parameter | Type | Required | Description
---|---|---|---
field_name | string | Yes | Field Name<br>Please note: <br>1. The first and last spaces in the name will be removed.<br>**Example value**: "Multiline text"
type | int | Yes | Field Type<br>**Example value**: 1<br>**Optional values are**:<br>- 1：Multiline<br>- 2：Number<br>- 3：Single option<br>- 4：Multiple options<br>- 5：Date<br>- 7：Checkbox<br>- 11：Person<br>- 13：PhoneNumber<br>- 15：Link<br>- 17：Attachment<br>- 18：One-way link<br>- 20：Formula<br>- 21：Two-way link<br>- 22：Location<br>- 23：group<br>- 1001：Date created<br>- 1002：Last modified date<br>- 1003：Created by<br>- 1004：Modified by<br>- 1005：AutoSerial
property | app.table.field.property | No | Field Property, ref: [Field edit development guide](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-field/guide)
options | app.table.field.property.option\[\] | No | Option information for radio and multi-select fields
name | string | No | Option name<br>**Example value**: "Red."
id | string | No | Option ID, not allowed to specify ID at creation time<br>**Example value**: "optKl35lnG"
color | int | No | Option color<br>**Example value**: 0.<br>**Data validation rules**:<br>- Value range: `0` ～ `54`
formatter | string | No | Display format of numbers and formula fields<br>**Example value**: "0."
date_formatter | string | No | The display format of the date, creation time, and last updated time fields<br>**Example value**: "Date format"
auto_fill | boolean | No | New records in the date field are automatically filled in Creation time<br>**Example value**: False
multiple | boolean | No | Multiple members are allowed to be added in the personnel field, and multiple records are allowed in one-way association and two-way association<br>**Example value**: False
table_id | string | No | The id of the associated data table in the one-way association, two-way association field<br>**Example value**: "tblsRc9GRRXKqhvW"
back_field_name | string | No | The name of the corresponding bidirectional association field in the associated data table in the bidirectional association field<br>**Example value**: ""Table1 - Bidirectional Association""
auto_serial | app.field.property.auto_serial | No | Automatic numbering type
type | string | Yes | Automatic numbering type<br>**Example value**: "auto_increment_number"<br>**Optional values are**:<br>- custom：Custom number<br>- auto_increment_number：Autoincrement number
options | app.field.property.auto_serial.options\[\] | No | List of auto-numbering rules
type | string | Yes | Optional rule item types for auto-numbering<br>**Example value**: "created_time"<br>**Optional values are**:<br>- system_number：Incremental digits, value range 1-9<br>- fixed_text：Fixed characters, maximum length: 20<br>- created_time：Creation time, supports formats "yyyyMMdd", "yyyyMM", "yyyy", "MMdd", "MM", "dd"
value | string | Yes | Values corresponding to auto-numbered optional rule item types<br>**Example value**: "YyyyMMdd"
location | app.field.property.location | No | Geolocation input method
input_type | string | Yes | Geolocation input restrictions<br>**Example value**: "not_limit"<br>**Optional values are**:<br>- only_mobile：Only allow uploads on mobile ends<br>- not_limit：Unlimited
formula_expression | string | No | Expression of formula field<br>**Example value**: "Bitable:: $table [tblNj92WQBAasdEf]. $field [fldMV60rYs] * 2"
allowed_edit_modes | allowed_edit_modes | No | Editing modes supported by the field
manual | boolean | No | Whether to allow manual entry<br>**Example value**: true
scan | boolean | No | Whether to allow mobile end entry<br>**Example value**: true
min | number(float) | No | Minimum data range for fields such as progress, score, etc<br>**Example value**: 0
max | number(float) | No | Maximum data range for fields such as progress, score, etc<br>**Example value**: 10
range_customize | boolean | No | Whether fields such as progress support custom ranges<br>**Example value**: true
currency_code | string | No | Currency Currency<br>**Example value**: "CNY"
rating | rating | No | Relevant settings for scoring fields
symbol | string | No | Symbol display for rating fields<br>**Example value**: "star"
type | app.table.field.property.type | No | Set the type of the formula field
data_type | int | Yes | Set the data type of the formula field<br>**Example value**: 1<br>**Optional values are**:<br>- 1：Text<br>- 2：Number<br>- 3：SingleSelect<br>- 4：MultiSelect<br>- 5：DateTime<br>- 7：Checkbox<br>- 11：User<br>- 13：PhoneNumber<br>- 15：Url<br>- 17：Attachment<br>- 18：Link<br>- 20：Formula<br>- 21：DuplexLink<br>- 22：Location<br>- 23：GroupChat<br>- 1001：CreatedTime<br>- 1002：ModifiedTime<br>- 1003：CreatedUser<br>- 1004：ModifiedUser<br>- 1005：AutoSerial
ui_property | app.table.field.property.type.ui_property | No | Field Property, ref: [Field edit development guide](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-field/guide)
currency_code | string | No | Currency<br>**Example value**: "CNY"<br>**Data validation rules**:<br>- Length range: `0` ～ `20` characters
formatter | string | No | Display format of numbers and formula fields<br>**Example value**: "0"<br>**Data validation rules**:<br>- Length range: `0` ～ `50` characters
range_customize | boolean | No | Whether fields such as progress support custom ranges<br>**Example value**: true
min | number(float) | No | Minimum data range for fields such as progress, score, etc<br>**Example value**: 1<br>**Data validation rules**:<br>- Value range: `0` ～ `1`
max | number(float) | No | Maximum data range for fields such as progress, score, etc<br>**Example value**: 100<br>**Data validation rules**:<br>- Value range: `1` ～ `100`
date_formatter | string | No | The display format of the date, creation time, and last updated time fields<br>**Example value**: "yyyy/MM/dd"<br>**Data validation rules**:<br>- Length range: `0` ～ `50` characters
rating | rating | No | Relevant settings for scoring fields
symbol | string | No | Symbol display for rating fields<br>**Example value**: "star"
ui_type | string | No | The type of display of the formula field on the interface, such as the progress field, which is a display form of numbers<br>**Example value**: "Progress"<br>**Optional values are**:<br>- Number：Number<br>- Progress：Progress<br>- Currency：Currency<br>- Rating：Rating<br>- DateTime：DateTime
description | app.table.field.description | No | Field description
disable_sync | boolean | No | Whether to disable synchronization, if true, it means that synchronization of the description content to the problem description of the form is prohibited (only valid when fields are added or modified)<br>**Example value**: True<br>**Default value**: `true`
text | string | No | Field description content<br>**Example value**: "This is a field description"
ui_type | string | No | The type of display of the field on the interface, such as the progress field, which is a display form of numbers<br>**Example value**: "Progress"<br>**Optional values are**:<br>- Text：multiline text<br>- Email：Email<br>- Barcode：barcode<br>- Number：number<br>- Progress：progress<br>- Currency：currency<br>- Rating：score<br>- SingleSelect：radio<br>- MultiSelect：multiple choice<br>- DateTime：date<br>- Checkbox：checkbox<br>- User：Personnel<br>- GroupChat：group<br>- Phone：Phone number<br>- Url：Hyperlink<br>- Attachment：Attachment<br>- SingleLink：one-way association<br>- Formula：formula<br>- DuplexLink：bidirectional association<br>- Location：Geographical location<br>- CreatedTime：Creation time<br>- ModifiedTime：Last update time<br>- CreatedUser：founder<br>- ModifiedUser：Modifier<br>- AutoNumber：Automatic numbering

### Request body example
```json
{
    "field_name":"Text",
    "type":1
}
```

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
field | app.table.field | Field
field_name | string | Field Name<br>Please note: <br>1. The first and last spaces in the name will be removed.
type | int | Field Type<br>**Optional values are**:<br>- 1：Multiline<br>- 2：Number<br>- 3：Single option<br>- 4：Multiple options<br>- 5：Date<br>- 7：Checkbox<br>- 11：Person<br>- 13：PhoneNumber<br>- 15：Link<br>- 17：Attachment<br>- 18：One-way link<br>- 20：Formula<br>- 21：Two-way link<br>- 22：Location<br>- 23：group<br>- 1001：Date created<br>- 1002：Last modified date<br>- 1003：Created by<br>- 1004：Modified by<br>- 1005：AutoSerial
property | app.table.field.property | Field Property, ref: [Field edit development guide](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-field/guide)
options | app.table.field.property.option\[\] | Option information for radio and multi-select fields
name | string | Option name
id | string | Option ID, not allowed to specify ID at creation time
color | int | Option color
formatter | string | Display format of numbers and formula fields
date_formatter | string | The display format of the date, creation time, and last updated time fields
auto_fill | boolean | New records in the date field are automatically filled in Creation time
multiple | boolean | Multiple members are allowed to be added in the personnel field, and multiple records are allowed in one-way association and two-way association
table_id | string | The id of the associated data table in the one-way association, two-way association field
table_name | string | The name of the associated data table in the one-way association, two-way association field
back_field_name | string | The name of the corresponding bidirectional association field in the associated data table in the bidirectional association field
auto_serial | app.field.property.auto_serial | Automatic numbering type
type | string | Automatic numbering type<br>**Optional values are**:<br>- custom：Custom number<br>- auto_increment_number：Autoincrement number
options | app.field.property.auto_serial.options\[\] | List of auto-numbering rules
type | string | Optional rule item types for auto-numbering<br>**Optional values are**:<br>- system_number：Incremental digits, value range 1-9<br>- fixed_text：Fixed characters, maximum length: 20<br>- created_time：Creation time, supports formats "yyyyMMdd", "yyyyMM", "yyyy", "MMdd", "MM", "dd"
value | string | Values corresponding to auto-numbered optional rule item types
location | app.field.property.location | Geolocation input method
input_type | string | Geolocation input restrictions<br>**Optional values are**:<br>- only_mobile：Only allow uploads on mobile ends<br>- not_limit：Unlimited
formula_expression | string | Expression of formula field
allowed_edit_modes | allowed_edit_modes | Editing modes supported by the field
manual | boolean | Whether to allow manual entry
scan | boolean | Whether to allow mobile end entry
min | number(float) | Minimum data range for fields such as progress, score, etc
max | number(float) | Maximum data range for fields such as progress, score, etc
range_customize | boolean | Whether fields such as progress support custom ranges
currency_code | string | Currency Currency
rating | rating | Relevant settings for scoring fields
symbol | string | Symbol display for rating fields
type | app.table.field.property.type | Set the type of the formula field
data_type | int | Set the data type of the formula field<br>**Optional values are**:<br>- 1：Text<br>- 2：Number<br>- 3：SingleSelect<br>- 4：MultiSelect<br>- 5：DateTime<br>- 7：Checkbox<br>- 11：User<br>- 13：PhoneNumber<br>- 15：Url<br>- 17：Attachment<br>- 18：Link<br>- 20：Formula<br>- 21：DuplexLink<br>- 22：Location<br>- 23：GroupChat<br>- 1001：CreatedTime<br>- 1002：ModifiedTime<br>- 1003：CreatedUser<br>- 1004：ModifiedUser<br>- 1005：AutoSerial
ui_property | app.table.field.property.type.ui_property | Field Property, ref: [Field edit development guide](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-field/guide)
currency_code | string | Currency
formatter | string | Display format of numbers and formula fields
range_customize | boolean | Whether fields such as progress support custom ranges
min | number(float) | Minimum data range for fields such as progress, score, etc
max | number(float) | Maximum data range for fields such as progress, score, etc
date_formatter | string | The display format of the date, creation time, and last updated time fields
rating | rating | Relevant settings for scoring fields
symbol | string | Symbol display for rating fields
ui_type | string | The type of display of the formula field on the interface, such as the progress field, which is a display form of numbers<br>**Optional values are**:<br>- Number：Number<br>- Progress：Progress<br>- Currency：Currency<br>- Rating：Rating<br>- DateTime：DateTime
description | app.table.field.description | Field description
disable_sync | boolean | Whether to disable synchronization, if true, it means that synchronization of the description content to the problem description of the form is prohibited (only valid when fields are added or modified)
text | string | Field description content
is_primary | boolean | Identifies whether the current field is the primary key
field_id | string | Field Id
ui_type | string | Identifies whether the current field is hidden<br>**Optional values are**:<br>- Text：multiline text<br>- Email：Email<br>- Barcode：barcode<br>- Number：number<br>- Progress：progress<br>- Currency：currency<br>- Rating：score<br>- SingleSelect：radio<br>- MultiSelect：multiple choice<br>- DateTime：date<br>- Checkbox：checkbox<br>- User：Personnel<br>- GroupChat：group<br>- Phone：Phone number<br>- Url：Hyperlinke<br>- Attachment：Annex<br>- SingleLink：one-way association<br>- Formula：formula<br>- DuplexLink：Two-way link<br>- Location：Geographical location<br>- CreatedTime：Creation time<br>- ModifiedTime：Last update time<br>- CreatedUser：creator<br>- ModifiedUser：Modifier<br>- AutoNumber：Automatic numbering
is_hidden | boolean | Is it a hidden field

### Response body example
```json
{
    "code": 0,
    "data": {
        "field": {
            "field_id": "fld4bocNLY",
            "field_name": "Text",
            "type": 1,
            "property": null
        }
    },
    "msg": "Success"
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
200 | 1254012 | NotSupportFieldOrView | Unsupported fields or views
200 | 1254013 | TableNameDuplicated | TableNameDuplicated
200 | 1254014 | FieldNameDuplicated | Field name duplicate
200 | 1254015 | FieldTypeValueNotMatch | FieldTypeValueNotMatch
200 | 1254026 | EmptyOptionName | option name should not be empty
400 | 1254028 | EmptyFieldName | field name should not be empty
400 | 1254029 | InvalidFieldName | Invalid field name
200 | 1254030 | TooLargeResponse | TooLargeResponse
400 | 1254036 | Base is copying, please try again later. | Base copy replicating, try again later
400 | 1254037 | Invalid client token, make sure that it complies with the specification. | Idempotent key format is wrong, you need to pass in uuidv4 format
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
200 | 1254070 | ActionValidateFailed | ActionValidateFailed
400 | 1254080 | TextFieldPropertyError | TextFieldPropertyError
400 | 1254081 | NumberFieldPropertyError | NumberFieldPropertyError
400 | 1254082 | SingleSelectFieldPropertyError | SingleSelectFieldPropertyError
400 | 1254083 | MultiSelectFieldPropertyError | MultiSelectFieldPropertyError
400 | 1254084 | DateFieldPropertyError | DateFieldPropertyError
400 | 1254085 | CheckboxFieldPropertyError | CheckboxFieldPropertyError
400 | 1254086 | UserFieldPropertyError | UserFieldPropertyError
400 | 1254087 | URLFieldPropertyError | URLFieldPropertyError
400 | 1254088 | AttachFieldPropertyError | AttachFieldPropertyError
400 | 1254089 | LinkFieldPropertyError | LinkFieldPropertyError
400 | 1254090 | LookUpFieldPropertyError | LookUpFieldPropertyError
400 | 1254091 | FormulaFieldPropertyError | FormulaFieldPropertyError
400 | 1254092 | DuplexLinkFieldPropertyError | DuplexLinkFieldPropertyError
400 | 1254093 | CreatedTimeFieldPropertyError | CreatedTimeFieldPropertyError
400 | 1254094 | ModifiedTimeFieldPropertyError | ModifiedTimeFieldPropertyError
400 | 1254095 | CreatedUserFieldPropertyError | CreatedUserFieldPropertyError
400 | 1254096 | ModifiedUserFieldPropertyError | ModifiedUserFieldPropertyError
200 | 1254100 | TableExceedLimit | TableExceedLimit, limited to 300
200 | 1254101 | ViewExceedLimit | ViewExceedLimit, limited to 200
200 | 1254102 | FileExceedLimit | FileExceedLimit
200 | 1254103 | RecordExceedLimit | RecordExceedLimit, limited to 20,000
200 | 1254104 | RecordAddOnceExceedLimit | RecordAddOnceExceedLimit, limited to 500
200 | 1254105 | ColumnExceedLimit | ColumnExceedLimit
200 | 1254130 | TooLargeCell | TooLargeCell
200 | 1254290 | TooManyRequest | Request too fast, try again later
200 | 1254291 | Write conflict | The same data table does not support concurrent calls to the write interface, please check whether there is a concurrent call to the write interface. The writing interface includes: adding, modifying, and deleting records; adding, modifying, and deleting fields; modifying forms; modifying views, etc.
200 | 1254301 | OperationTypeError | Base does not have advanced permissions enabled or does not support enabling advanced permissions
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
403 | 1254608 | ReqRecommited | Same API requests are submitted repeatedly.

# Update field

Update a field

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/tables/:table_id/fields/:field_id
HTTP Method | PUT
Rate Limit | [10 per second](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.**<br>Enable any scope from the list | 更新字段(base:field:update)<br>View, comment, edit and manage Base(bitable:app)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

The instructions for AccessToken calling Docs API are detailed here [Docs API Overview](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN)

### Path parameters

Parameter | Type | Description
---|---|---
app_token | string | base app token<br>**Example value**: "appbcbWCzen6D8dezhoCH2RpMAh"
table_id | string | table id<br>**Example value**: "tblsRc9GRRXKqhvW"
field_id | string | field id<br>**Example value**: "fldPTb0U2y"

### Request body

Parameter | Type | Required | Description
---|---|---|---
field_name | string | Yes | Field Name<br>Please note: <br>1. The first and last spaces in the name will be removed.<br>**Example value**: "Multiline text"
type | int | Yes | Field Type<br>**Example value**: 1<br>**Optional values are**:<br>- 1：Multiline<br>- 2：Number<br>- 3：Single option<br>- 4：Multiple options<br>- 5：Date<br>- 7：Checkbox<br>- 11：Person<br>- 13：PhoneNumber<br>- 15：Link<br>- 17：Attachment<br>- 18：One-way link<br>- 20：Formula<br>- 21：Two-way link<br>- 22：Location<br>- 23：group<br>- 1001：Date created<br>- 1002：Last modified date<br>- 1003：Created by<br>- 1004：Modified by<br>- 1005：AutoSerial
property | app.table.field.property | No | Field Property, ref: [Field edit development guide](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-field/guide)
options | app.table.field.property.option\[\] | No | Option information for radio and multi-select fields
name | string | No | Option name<br>**Example value**: "Red."
id | string | No | Option ID, not allowed to specify ID at creation time<br>**Example value**: "optKl35lnG"
color | int | No | Option color<br>**Example value**: 0.<br>**Data validation rules**:<br>- Value range: `0` ～ `54`
formatter | string | No | Display format of numbers and formula fields<br>**Example value**: "0."
date_formatter | string | No | The display format of the date, creation time, and last updated time fields<br>**Example value**: "Date format"
auto_fill | boolean | No | New records in the date field are automatically filled in Creation time<br>**Example value**: False
multiple | boolean | No | Multiple members are allowed to be added in the personnel field, and multiple records are allowed in one-way association and two-way association<br>**Example value**: False
table_id | string | No | The id of the associated data table in the one-way association, two-way association field<br>**Example value**: "tblsRc9GRRXKqhvW"
table_name | string | No | The name of the associated data table in the one-way association, two-way association field<br>**Example value**: ""Table2""
back_field_name | string | No | The name of the corresponding bidirectional association field in the associated data table in the bidirectional association field<br>**Example value**: ""Table1 - Bidirectional Association""
auto_serial | app.field.property.auto_serial | No | Automatic numbering type
type | string | Yes | Automatic numbering type<br>**Example value**: "auto_increment_number"<br>**Optional values are**:<br>- custom：Custom number<br>- auto_increment_number：Autoincrement number
options | app.field.property.auto_serial.options\[\] | No | List of auto-numbering rules
type | string | Yes | Optional rule item types for auto-numbering<br>**Example value**: "created_time"<br>**Optional values are**:<br>- system_number：Incremental digits, value range 1-9<br>- fixed_text：Fixed characters, maximum length: 20<br>- created_time：Creation time, supports formats "yyyyMMdd", "yyyyMM", "yyyy", "MMdd", "MM", "dd"
value | string | Yes | Values corresponding to auto-numbered optional rule item types<br>**Example value**: "YyyyMMdd"
location | app.field.property.location | No | Geolocation input method
input_type | string | Yes | Geolocation input restrictions<br>**Example value**: "not_limit"<br>**Optional values are**:<br>- only_mobile：Only allow uploads on mobile ends<br>- not_limit：Unlimited
formula_expression | string | No | Expression of formula field<br>**Example value**: "Bitable:: $table [tblNj92WQBAasdEf]. $field [fldMV60rYs] * 2"
allowed_edit_modes | allowed_edit_modes | No | Editing modes supported by the field
manual | boolean | No | Whether to allow manual entry<br>**Example value**: true
scan | boolean | No | Whether to allow mobile end entry<br>**Example value**: true
min | number(float) | No | Minimum data range for fields such as progress, score, etc<br>**Example value**: 0
max | number(float) | No | Maximum data range for fields such as progress, score, etc<br>**Example value**: 10
range_customize | boolean | No | Whether fields such as progress support custom ranges<br>**Example value**: true
currency_code | string | No | Currency Currency<br>**Example value**: "CNY"
rating | rating | No | Relevant settings for scoring fields
symbol | string | No | Symbol display for rating fields<br>**Example value**: "star"
type | app.table.field.property.type | No | Set the type of the formula field
data_type | int | Yes | Set the data type of the formula field<br>**Example value**: 1<br>**Optional values are**:<br>- 1：Text<br>- 2：Number<br>- 3：SingleSelect<br>- 4：MultiSelect<br>- 5：DateTime<br>- 7：Checkbox<br>- 11：User<br>- 13：PhoneNumber<br>- 15：Url<br>- 17：Attachment<br>- 18：Link<br>- 20：Formula<br>- 21：DuplexLink<br>- 22：Location<br>- 23：GroupChat<br>- 1001：CreatedTime<br>- 1002：ModifiedTime<br>- 1003：CreatedUser<br>- 1004：ModifiedUser<br>- 1005：AutoSerial
ui_property | app.table.field.property.type.ui_property | No | Field Property, ref: [Field edit development guide](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-field/guide)
currency_code | string | No | Currency<br>**Example value**: "CNY"<br>**Data validation rules**:<br>- Length range: `0` ～ `20` characters
formatter | string | No | Display format of numbers and formula fields<br>**Example value**: "0"<br>**Data validation rules**:<br>- Length range: `0` ～ `50` characters
range_customize | boolean | No | Whether fields such as progress support custom ranges<br>**Example value**: true
min | number(float) | No | Minimum data range for fields such as progress, score, etc<br>**Example value**: 1<br>**Data validation rules**:<br>- Value range: `0` ～ `1`
max | number(float) | No | Maximum data range for fields such as progress, score, etc<br>**Example value**: 100<br>**Data validation rules**:<br>- Value range: `1` ～ `100`
date_formatter | string | No | The display format of the date, creation time, and last updated time fields<br>**Example value**: "yyyy/MM/dd"<br>**Data validation rules**:<br>- Length range: `0` ～ `50` characters
rating | rating | No | Relevant settings for scoring fields
symbol | string | No | Symbol display for rating fields<br>**Example value**: "star"
ui_type | string | No | The type of display of the formula field on the interface, such as the progress field, which is a display form of numbers<br>**Example value**: "Progress"<br>**Optional values are**:<br>- Number：Number<br>- Progress：Progress<br>- Currency：Currency<br>- Rating：Rating<br>- DateTime：DateTime
description | app.table.field.description | No | Field description
disable_sync | boolean | No | Whether to disable synchronization, if true, it means that synchronization of the description content to the problem description of the form is prohibited (only valid when fields are added or modified)<br>**Example value**: True<br>**Default value**: `true`
text | string | No | Field description content<br>**Example value**: "This is a field description"
ui_type | string | No | The type of display of the field on the interface, such as the progress field, which is a display form of numbers<br>**Example value**: "Progress"<br>**Optional values are**:<br>- Text：multiline text<br>- Email：Email<br>- Barcode：barcode<br>- Number：number<br>- Progress：progress<br>- Currency：currency<br>- Rating：score<br>- SingleSelect：radio<br>- MultiSelect：multiple choice<br>- DateTime：date<br>- Checkbox：checkbox<br>- User：Personnel<br>- GroupChat：group<br>- Phone：Phone number<br>- Url：Hyperlinke<br>- Attachment：Annex<br>- SingleLink：one-way association<br>- Formula：formula<br>- DuplexLink：bidirectional association<br>- Location：Geographical location<br>- CreatedTime：Creation time<br>- ModifiedTime：Last update time<br>- CreatedUser：founder<br>- ModifiedUser：Modifier<br>- AutoNumber：Automatic numbering

### Request body example
```json
{
    "field_name": "person",
    "type": 11,
    "property": {
        "multiple": true
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
field | app.table.field | Field
field_name | string | Field Name<br>Please note: <br>1. The first and last spaces in the name will be removed.
type | int | Field Type<br>**Optional values are**:<br>- 1：Multiline<br>- 2：Number<br>- 3：Single option<br>- 4：Multiple options<br>- 5：Date<br>- 7：Checkbox<br>- 11：Person<br>- 13：PhoneNumber<br>- 15：Link<br>- 17：Attachment<br>- 18：One-way link<br>- 20：Formula<br>- 21：Two-way link<br>- 22：Location<br>- 23：group<br>- 1001：Date created<br>- 1002：Last modified date<br>- 1003：Created by<br>- 1004：Modified by<br>- 1005：AutoSerial
property | app.table.field.property | Field Property, ref: [Field edit development guide](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-field/guide)
options | app.table.field.property.option\[\] | Option information for radio and multi-select fields
name | string | Option name
id | string | Option ID, not allowed to specify ID at creation time
color | int | Option color
formatter | string | Display format of numbers and formula fields
date_formatter | string | The display format of the date, creation time, and last updated time fields
auto_fill | boolean | New records in the date field are automatically filled in Creation time
multiple | boolean | Multiple members are allowed to be added in the personnel field, and multiple records are allowed in one-way association and two-way association
table_id | string | The id of the associated data table in the one-way association, two-way association field
table_name | string | The name of the associated data table in the one-way association, two-way association field
back_field_name | string | The name of the corresponding bidirectional association field in the associated data table in the bidirectional association field
auto_serial | app.field.property.auto_serial | Automatic numbering type
type | string | Automatic numbering type<br>**Optional values are**:<br>- custom：Custom number<br>- auto_increment_number：Autoincrement number
options | app.field.property.auto_serial.options\[\] | List of auto-numbering rules
type | string | Optional rule item types for auto-numbering<br>**Optional values are**:<br>- system_number：Incremental digits, value range 1-9<br>- fixed_text：Fixed characters, maximum length: 20<br>- created_time：Creation time, supports formats "yyyyMMdd", "yyyyMM", "yyyy", "MMdd", "MM", "dd"
value | string | Values corresponding to auto-numbered optional rule item types
location | app.field.property.location | Geolocation input method
input_type | string | Geolocation input restrictions<br>**Optional values are**:<br>- only_mobile：Only allow uploads on mobile ends<br>- not_limit：Unlimited
formula_expression | string | Expression of formula field
allowed_edit_modes | allowed_edit_modes | Editing modes supported by the field
manual | boolean | Whether to allow manual entry
scan | boolean | Whether to allow mobile end entry
min | number(float) | Minimum data range for fields such as progress, score, etc
max | number(float) | Maximum data range for fields such as progress, score, etc
range_customize | boolean | Whether fields such as progress support custom ranges
currency_code | string | Currency Currency
rating | rating | Relevant settings for scoring fields
symbol | string | Symbol display for rating fields
type | app.table.field.property.type | Set the type of the formula field
data_type | int | Set the data type of the formula field<br>**Optional values are**:<br>- 1：Text<br>- 2：Number<br>- 3：SingleSelect<br>- 4：MultiSelect<br>- 5：DateTime<br>- 7：Checkbox<br>- 11：User<br>- 13：PhoneNumber<br>- 15：Url<br>- 17：Attachment<br>- 18：Link<br>- 20：Formula<br>- 21：DuplexLink<br>- 22：Location<br>- 23：GroupChat<br>- 1001：CreatedTime<br>- 1002：ModifiedTime<br>- 1003：CreatedUser<br>- 1004：ModifiedUser<br>- 1005：AutoSerial
ui_property | app.table.field.property.type.ui_property | Field Property, ref: [Field edit development guide](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-field/guide)
currency_code | string | Currency
formatter | string | Display format of numbers and formula fields
range_customize | boolean | Whether fields such as progress support custom ranges
min | number(float) | Minimum data range for fields such as progress, score, etc
max | number(float) | Maximum data range for fields such as progress, score, etc
date_formatter | string | The display format of the date, creation time, and last updated time fields
rating | rating | Relevant settings for scoring fields
symbol | string | Symbol display for rating fields
ui_type | string | The type of display of the formula field on the interface, such as the progress field, which is a display form of numbers<br>**Optional values are**:<br>- Number：Number<br>- Progress：Progress<br>- Currency：Currency<br>- Rating：Rating<br>- DateTime：DateTime
description | app.table.field.description | Field description
disable_sync | boolean | Whether to disable synchronization, if true, it means that synchronization of the description content to the problem description of the form is prohibited (only valid when fields are added or modified)
text | string | Field description content
is_primary | boolean | Identifies whether the current column is the primary key
field_id | string | Field Id
ui_type | string | Identifies whether the current column is hidden<br>**Optional values are**:<br>- Text：multiline text<br>- Email：Email<br>- Barcode：barcode<br>- Number：number<br>- Progress：progress<br>- Currency：currency<br>- Rating：score<br>- SingleSelect：radio<br>- MultiSelect：multiple choice<br>- DateTime：date<br>- Checkbox：checkbox<br>- User：Personnel<br>- GroupChat：group<br>- Phone：Phone number<br>- Url：Hyperlinke<br>- Attachment：Annex<br>- SingleLink：one-way association<br>- Formula：formula<br>- DuplexLink：bidirectional association<br>- Location：Geographical location<br>- CreatedTime：Creation time<br>- ModifiedTime：Last update time<br>- CreatedUser：founder<br>- ModifiedUser：Modifier<br>- AutoNumber：Automatic numbering
is_hidden | boolean | Is it a hidden field

### Response body example
```json
{
    "code": 0,
    "data": {
        "field": {
            "field_id": "fldEPIQAXw",
            "field_name": "person",
            "is_primary": false,
            "property": {
                "multiple": true
            },
            "type": 11
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
200 | 1254012 | NotSupportFieldOrView | Unsupported fields or views
200 | 1254013 | TableNameDuplicated | TableNameDuplicated
200 | 1254014 | FieldNameDuplicated | Field name duplicate
200 | 1254015 | FieldTypeValueNotMatch | FieldTypeValueNotMatch
200 | 1254026 | EmptyOptionName | option name should not be empty
400 | 1254028 | EmptyFieldName | field name should not be empty
400 | 1254029 | InvalidFieldName | Invalid field name
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
200 | 1254070 | ActionValidateFailed | ActionValidateFailed
400 | 1254080 | TextFieldPropertyError | TextFieldPropertyError
400 | 1254081 | NumberFieldPropertyError | NumberFieldPropertyError
400 | 1254082 | SingleSelectFieldPropertyError | SingleSelectFieldPropertyError
400 | 1254083 | MultiSelectFieldPropertyError | MultiSelectFieldPropertyError
400 | 1254084 | DateFieldPropertyError | DateFieldPropertyError
400 | 1254085 | CheckboxFieldPropertyError | CheckboxFieldPropertyError
400 | 1254086 | UserFieldPropertyError | UserFieldPropertyError
400 | 1254087 | URLFieldPropertyError | URLFieldPropertyError
400 | 1254088 | AttachFieldPropertyError | AttachFieldPropertyError
400 | 1254089 | LinkFieldPropertyError | LinkFieldPropertyError
400 | 1254090 | LookUpFieldPropertyError | LookUpFieldPropertyError
400 | 1254091 | FormulaFieldPropertyError | FormulaFieldPropertyError
400 | 1254092 | DuplexLinkFieldPropertyError | DuplexLinkFieldPropertyError
400 | 1254093 | CreatedTimeFieldPropertyError | CreatedTimeFieldPropertyError
400 | 1254094 | ModifiedTimeFieldPropertyError | ModifiedTimeFieldPropertyError
400 | 1254095 | CreatedUserFieldPropertyError | CreatedUserFieldPropertyError
400 | 1254096 | ModifiedUserFieldPropertyError | ModifiedUserFieldPropertyError
200 | 1254100 | TableExceedLimit | TableExceedLimit, limited to 300
200 | 1254101 | ViewExceedLimit | ViewExceedLimit, limited to 200
200 | 1254102 | FileExceedLimit | FileExceedLimit
200 | 1254103 | RecordExceedLimit | RecordExceedLimit, limited to 20,000
200 | 1254104 | RecordAddOnceExceedLimit | RecordAddOnceExceedLimit, limited to 500
200 | 1254105 | ColumnExceedLimit | ColumnExceedLimit
200 | 1254130 | TooLargeCell | TooLargeCell
200 | 1254290 | TooManyRequest | Request too fast, try again later
200 | 1254291 | Write conflict | The same data table does not support concurrent calls to the write interface, please check whether there is a concurrent call to the write interface. The writing interface includes: adding, modifying, and deleting records; adding, modifying, and deleting fields; modifying forms; modifying views, etc.
200 | 1254301 | OperationTypeError | Base does not have advanced permissions enabled or does not support enabling advanced permissions
200 | 1254606 | DataNotChange | data not change
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

# List fields

Get all fields according to app_token and table_id

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/tables/:table_id/fields
HTTP Method | GET
Rate Limit | [20 per second](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.**<br>Enable any scope from the list | 获取字段信息(base:field:read)<br>View, comment, edit and manage Base(bitable:app)<br>View, comment, and export Base(bitable:app:readonly)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)

The instructions for AccessToken calling Docs API are detailed here [Docs API Overview](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN)

### Path parameters

Parameter | Type | Description
---|---|---
app_token | string | Base app token<br>**Example value**: "appbcbWCzen6D8dezhoCH2RpMAh"
table_id | string | table id<br>**Example value**: "tblsRc9GRRXKqhvW"

### Query parameters

Parameter | Type | Required | Description
---|---|---|---
view_id | string | No | view id<br>**Example value**: vewOVMEXPF
text_field_as_array | boolean | No | Control the return format of field description (multi-line text format) data, true means return in array rich text form<br>**Example value**: True
page_token | string | No | Page identifier. It is not filled in the first request, indicating traversal from the beginning; when there will be more groups, the new page_token will be returned at the same time, and the next traversal can use the page_token to get more groups<br>**Example value**: fldwJ4YrtB
page_size | int | No | paging size<br>**Example value**: 10<br>**Default value**: `20`<br>**Data validation rules**:<br>- Maximum value: `100`

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
has_more | boolean | Whether the response body has more parameters
page_token | string | Page identifier, when has_more is true, a new page_token will also be returned. Otherwise, page_token will not be returned
total | int | Total
items | app.table.fieldForList\[\] | Field information
field_name | string | Field Name<br>Please note: <br>1. The first and last spaces in the name will be removed.
type | int | Field Type<br>**Optional values are**:<br>- 1：Multiline<br>- 2：Number<br>- 3：Single option<br>- 4：Multiple options<br>- 5：Date<br>- 7：Checkbox<br>- 11：Person<br>- 13：PhoneNumber<br>- 15：Link<br>- 17：Attachment<br>- 18：One-way link<br>- 20：Formula<br>- 21：Two-way link<br>- 22：Location<br>- 23：group<br>- 1001：Date created<br>- 1002：Last modified date<br>- 1003：Created by<br>- 1004：Modified by<br>- 1005：AutoSerial
property | app.table.field.property | Field Property, ref: [Field edit development guide](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-field/guide)
options | app.table.field.property.option\[\] | Option information for radio and multi-select fields
name | string | Option name
id | string | Option ID, not allowed to specify ID at creation time
color | int | Option color
formatter | string | Display format of numbers and formula fields
date_formatter | string | The display format of the date, creation time, and last updated time fields
auto_fill | boolean | New records in the date field are automatically filled in Creation time
multiple | boolean | Multiple members are allowed to be added in the personnel field, and multiple records are allowed in one-way association and two-way association
table_id | string | The id of the associated data table in the one-way association, two-way association field
table_name | string | The name of the associated data table in the one-way association, two-way association field
back_field_name | string | The name of the corresponding bidirectional association field in the associated data table in the bidirectional association field
auto_serial | app.field.property.auto_serial | Automatic numbering type
type | string | Automatic numbering type<br>**Optional values are**:<br>- custom：Custom number<br>- auto_increment_number：Autoincrement number
options | app.field.property.auto_serial.options\[\] | List of auto-numbering rules
type | string | Optional rule item types for auto-numbering<br>**Optional values are**:<br>- system_number：Incremental digits, value range 1-9<br>- fixed_text：Fixed characters, maximum length: 20<br>- created_time：Creation time, supports formats "yyyyMMdd", "yyyyMM", "yyyy", "MMdd", "MM", "dd"
value | string | Values corresponding to auto-numbered optional rule item types
location | app.field.property.location | Geolocation input method
input_type | string | Geolocation input restrictions<br>**Optional values are**:<br>- only_mobile：Only allow uploads on mobile ends<br>- not_limit：Unlimited
formula_expression | string | Expression of formula field
allowed_edit_modes | allowed_edit_modes | Editing modes supported by the field
manual | boolean | Whether to allow manual entry
scan | boolean | Whether to allow mobile end entry
min | number(float) | Minimum data range for fields such as progress, score, etc
max | number(float) | Maximum data range for fields such as progress, score, etc
range_customize | boolean | Whether fields such as progress support custom ranges
currency_code | string | Currency Currency
rating | rating | Relevant settings for scoring fields
symbol | string | Symbol display for rating fields
type | app.table.field.property.type | Set the type of the formula field
data_type | int | Set the data type of the formula field<br>**Optional values are**:<br>- 1：Text<br>- 2：Number<br>- 3：SingleSelect<br>- 4：MultiSelect<br>- 5：DateTime<br>- 7：Checkbox<br>- 11：User<br>- 13：PhoneNumber<br>- 15：Url<br>- 17：Attachment<br>- 18：Link<br>- 20：Formula<br>- 21：DuplexLink<br>- 22：Location<br>- 23：GroupChat<br>- 1001：CreatedTime<br>- 1002：ModifiedTime<br>- 1003：CreatedUser<br>- 1004：ModifiedUser<br>- 1005：AutoSerial
ui_property | app.table.field.property.type.ui_property | Field Property, ref: [Field edit development guide](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-field/guide)
currency_code | string | Currency
formatter | string | Display format of numbers and formula fields
range_customize | boolean | Whether fields such as progress support custom ranges
min | number(float) | Minimum data range for fields such as progress, score, etc
max | number(float) | Maximum data range for fields such as progress, score, etc
date_formatter | string | The display format of the date, creation time, and last updated time fields
rating | rating | Relevant settings for scoring fields
symbol | string | Symbol display for rating fields
ui_type | string | The type of display of the formula field on the interface, such as the progress field, which is a display form of numbers<br>**Optional values are**:<br>- Number：Number<br>- Progress：Progress<br>- Currency：Currency<br>- Rating：Rating<br>- DateTime：DateTime
filter_info | app.table.field.property.lookup_filter | Find reference relationships
target_table | string | citation form
filter_info | app.table.field.property.filter_info | search criteria
conjunction | string | Relationship between multiple filters<br>**Optional values are**:<br>- and：with<br>- or：or
conditions | app.table.field.property.filter_info.condition\[\] | filter criteria
field_id | string | Field unique ID for filtering
operator | string | Types of filtering operations<br>**Optional values are**:<br>- is：equal to<br>- isNot：Not equal to<br>- contains：contain<br>- doesNotContain：Do not include<br>- isEmpty：empty<br>- isNotEmpty：Not empty<br>- isGreater：greater than<br>- isGreaterEqual：greater than or equal to<br>- isLess：less than<br>- isLessEqual：less than or equal to
value | string | filter value
condition_id | string | The unique ID of the filter condition
field_type | int | Type of field used for filtering
description | union | Description of the field. It can be either an array or a string type, determined by the request parameter `text_field_as_array`.
is_primary | boolean | Whether it is an primary field.
field_id | string | Field Id
ui_type | string | The type of presentation of the field.<br>**Optional values are**:<br>- Text：multiline text<br>- Barcode：barcode<br>- Number：number<br>- Progress：progress<br>- Currency：currency<br>- Rating：score<br>- SingleSelect：radio<br>- MultiSelect：multiple choice<br>- DateTime：date<br>- Checkbox：checkbox<br>- User：Personnel<br>- GroupChat：group<br>- Phone：Phone number<br>- Url：Hyperlinke<br>- Attachment：Annex<br>- SingleLink：one-way association<br>- Formula：formula<br>- DuplexLink：bidirectional association<br>- Location：Geographical location<br>- CreatedTime：Creation time<br>- ModifiedTime：Last update time<br>- CreatedUser：founder<br>- ModifiedUser：Modifier<br>- AutoNumber：Automatic numbering
is_hidden | boolean | Whether it is a hidden field.

### Response body example
```json
{
    "code": 0,
    "data": {
        "has_more": false,
        "items": [
            {
                "field_id": "fldob4JqjK",
                "field_name": "primary",
                "is_primary": true,
                "property": null,
                "type": 1,
                "ui_type": "Text"
            },
            {
                "field_id": "fldJlvK2FH",
                "field_name": "text",
                "property": null,
                "type": 1,
                "ui_type": "Text"
            },
            {
                "field_id": "fldzwmS7AJ",
                "field_name": "number",
                "property": {
                    "formatter": "0.00"
                },
                "type": 2,
                "ui_type": "Number"
            },
            {
                "field_id": "fldm4AFURc",
                "field_name": "single_select",
                "property": {
                    "options": [
                        {
                            "color": 0,
                            "id": "optjelQbc7",
                            "name": "option_1"
                        },
                        {
                            "color": 1,
                            "id": "optvln6wtL",
                            "name": "option_2"
                        },
                        {
                            "color": 2,
                            "id": "opt88b49bs",
                            "name": "option_3"
                        }
                    ]
                },
                "type": 3,
                "ui_type": "SingleSelect"
            },
            {
                "field_id": "fldm4AFUpp",
                "field_name": "multi_select",
                "property": {
                    "options": [
                        {
                            "color": 0,
                            "id": "optoZ1U6SY",
                            "name": "选项1"
                        },
                        {
                            "color": 1,
                            "id": "optG9NcxmW",
                            "name": "选项2"
                        }
                    ]
                },
                "type": 4,
                "ui_type": "MultiSelect"
            },
            {
                "field_id": "fldGXNlvnR",
                "field_name": "date",
                "property": {
                    "auto_fill": true,
                    "date_formatter": "yyyy/MM/dd"
                },
                "type": 5,
                "ui_type": "DateTime"
            },
            {
                "field_id": "fldDn51X7W",
                "field_name": "checkbox",
                "property": null,
                "type": 7,
                "ui_type": "Checkbox"
            },
            {
                "field_id": "fldX96f4cH",
                "field_name": "user",
                "property": {
                    "multiple": true
                },
                "type": 11,
                "ui_type": "User"
            },
            {
                "field_id": "fldUgDVrl7",
                "field_name": "phone",
                "property": null,
                "type": 13,
                "ui_type": "Phone"
            },
            {
                "field_id": "fldVw52oFt",
                "field_name": "url",
                "property": null,
                "type": 15,
                "ui_type": "Url"
            },
            {
                "field_id": "fldkd6eX5b",
                "field_name": "attachment",
                "property": null,
                "type": 17,
                "ui_type": "Attachment"
            },
            {
                "field_id": "fld5AzyPGi",
                "field_name": "single_link",
                "property": {
                    "multiple": true,
                    "table_id": "tblBJyX6jZteblYv",
                    "table_name": "your table"
                },
                "type": 18,
                "ui_type": "SingleLink"
            },
            {
                "field_id": "fld1cXEUhn",
                "field_name": "duplex_link",
                "property": {
                    "back_field_id": "fldfjaXrPf",
                    "back_field_name": "duplex_link_add_field",
                    "multiple": true,
                    "table_id": "tblBJyX6jZteblYv",
                    "table_name": "your table"
                },
                "type": 21,
                "ui_type": "DuplexLink"
            },
            {
                "field_id": "fld9wy0PKz",
                "field_name": "location",
                "property": {
                    "location": {
                        "input_type": "not_limit"
                    }
                },
                "type": 22,
                "ui_type": "Location"
            },
            {
                "field_id": "fldWPpN2Wm",
                "field_name": "formula",
                "property": {
                    "formatter": "0.00%",
                    "formula_expression": "CONTAINTEXT(bitable::$table[tblBJyX6jZteblYv].$field[fldJlvK2FH],\"hello world\")"
                },
                "type": 20,
                "ui_type": "Formula"
            },
            {
                "field_id": "fldWqpN1Wm",
                "field_name": "created_time",
                "property": {
                    "date_formatter": "yyyy/MM/dd"
                },
                "type": 1001,
                "ui_type": "CreatedTime"
            },
            {
                "field_id": "fldWzzN1zm",
                "field_name": "modified_time",
                "property": {
                    "date_formatter": "yyyy/MM/dd HH:mm"
                },
                "type": 1002,
                "ui_type": "ModifiedTime"
            },
            {
                "field_id": "fldWzzN1ww",
                "field_name": "created_user",
                "property": null,
                "type": 1003,
                "ui_type": "CreatedUser"
            },
            {
                "field_id": "fldnnoWrgm",
                "field_name": "modified_user",
                "property": null,
                "type": 1004,
                "ui_type": "ModifiedUser"
            },
            {
                "field_id": "fldc4YUB2m",
                "field_name": "custom_auto_number",
                "property": {
                    "auto_serial": {
                        "options": [
                            {
                                "type": "system_number",
                                "value": "3"
                            },
                            {
                                "type": "fixed_text",
                                "value": "no"
                            },
                            {
                                "type": "created_time",
                                "value": "yyyyMMdd"
                            }
                        ],
                        "type": "custom"
                    }
                },
                "type": 1005,
                "ui_type": "AutoNumber"
            },
            {
                "field_id": "fld7sQvLyF",
                "field_name": "auto_number",
                "property": {
                    "auto_serial": {
                        "type": "auto_increment_number"
                    }
                },
                "type": 1005,
                "ui_type": "AutoNumber"
            },
            {
                "field_id": "fldvDB32aX",
                "field_name": "lookup",
                "property": null,
                "type": 19,
                "ui_type": "Lookup"
            },
            {
                "field_id": "fldUHxZlqG",
                "field_name": "barcode",
                "property": null,
                "type": 1,
                "ui_type": "Barcode"
            },
            {
                "field_id": "fldVanes5j",
                "field_name": "progress",
                "property": {
                    "formatter": "%"
                },
                "type": 2,
                "ui_type": "Progress"
            },
            {
                "field_id": "fldlwg2erf",
                "field_name": "currency",
                "property": {
                    "formatter": "0.0"
                },
                "type": 2,
                "ui_type": "Currency"
            }
        ],
        "page_token": "fldlwg2erf",
        "total": 25
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
200 | 1254012 | NotSupportFieldOrView | Unsupported fields or views
200 | 1254013 | TableNameDuplicated | TableNameDuplicated
200 | 1254014 | FieldNameDuplicated | Field name duplicate
200 | 1254015 | FieldTypeValueNotMatch | FieldTypeValueNotMatch
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
200 | 1254070 | ActionValidateFailed | ActionValidateFailed
200 | 1254100 | TableExceedLimit | TableExceedLimit, limited to 300
200 | 1254101 | ViewExceedLimit | ViewExceedLimit, limited to 200
200 | 1254102 | FileExceedLimit | FileExceedLimit
200 | 1254103 | RecordExceedLimit | RecordExceedLimit, limited to 20,000
200 | 1254104 | RecordAddOnceExceedLimit | RecordAddOnceExceedLimit, limited to 500
200 | 1254105 | ColumnExceedLimit | ColumnExceedLimit
200 | 1254130 | TooLargeCell | TooLargeCell
200 | 1254290 | TooManyRequest | Request too fast, try again later
200 | 1254291 | Write conflict | The same data table does not support concurrent calls to the write interface, please check whether there is a concurrent call to the write interface. The writing interface includes: adding, modifying, and deleting records; adding, modifying, and deleting fields; modifying forms; modifying views, etc.
200 | 1254301 | OperationTypeError | Base does not have advanced permissions enabled or does not support enabling advanced permissions
403 | 1254302 | Permission denied. | No access rights, usually caused by the table opening of advanced permissions, please add a group containing applications in the advanced permissions settings and give this group read and write permissions
200 | 1255001 | InternalError | Internal error, have any questions can be consulting service
200 | 1255002 | RpcError | Internal error, have any questions can be consulting service
200 | 1255003 | MarshalError | Serialization failed, have any questions can be consulting service
200 | 1255004 | UmMarshalError | Deserialization failed, have any questions can be consulting service
200 | 1255005 | ConvError | Internal error, have any questions can be consulting service
500 | 1255040 | Request timed out, please try again later | Try again
400 | 1254607 | Data not ready, please try again later | There are usually two situations when this error occurs: 1. The last submitted modification has not been processed; 2. The data is too large and the server calculation times out; <br>This error code can be appropriately retried.

# Delete field

Delete a field

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/tables/:table_id/fields/:field_id
HTTP Method | DELETE
Rate Limit | [10 per second](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.** | View, comment, edit and manage Base(bitable:app)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)

The instructions for AccessToken calling Docs API are detailed here [Docs API Overview](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN)

### Path parameters

Parameter | Type | Description
---|---|---
app_token | string | Base unique device identifier [app_token description](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification#8121eebe)<br>**Example value**: "appbcbWCzen6D8dezhoCH2RpMAh"
table_id | string | table id<br>**Example value**: "tblsRc9GRRXKqhvW"
field_id | string | field id<br>**Example value**: "fldPTb0U2y"

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
field_id | string | field id
deleted | boolean | deleted

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "field_id": "fldPTb0U2y",
        "deleted": true
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
200 | 1254012 | NotSupportFieldOrView | Unsupported fields or views
200 | 1254013 | TableNameDuplicated | TableNameDuplicated
200 | 1254014 | FieldNameDuplicated | Field name duplicate
200 | 1254015 | FieldTypeValueNotMatch | FieldTypeValueNotMatch
200 | 1254030 | TooLargeResponse | TooLargeResponse
400 | 1254036 | Base is copying, please try again later. | Base copy replicating, try again later
200 | 1254040 | BaseTokenNotFound | AppToken not found
200 | 1254041 | TableIdNotFound | Table not found
200 | 1254042 | ViewIdNotFound | View not found
200 | 1254043 | RecordIdNotFound | RecordIdNotFound
200 | 1254044 | FieldIdNotFound | FieldIdNotFound
200 | 1254046 | The Primary Field cannot be deleted. | The Primary Field cannot be deleted.
200 | 1254060 | TextFieldConvFail | TextFieldConvFail
200 | 1254061 | NumberFieldConvFail | NumberFieldConvFail
200 | 1254062 | SingleSelectFieldConvFail | SingleSelectFieldConvFail
200 | 1254063 | MultiSelectFieldConvFail | MultiSelectFieldConvFail
200 | 1254064 | DatetimeFieldConvFail | DatetimeFieldConvFail
200 | 1254065 | CheckboxFieldConvFail | CheckboxFieldConvFail
200 | 1254066 | UserFieldConvFail | The value corresponding to the personnel field type is incorrect. The possible reasons are:<br>- The ID type specified by the user_id_type parameter does not match the type of the provided ID.<br>- An unrecognized type or structure was provided. Currently, only `id` is supported, and it must be passed as an array.<br>- An `open_id` was passed across applications. If you are passing an ID across applications, it is recommended to use `user_id`. The `open_id` obtained from different applications cannot be used interchangeably.
200 | 1254067 | LinkFieldConvFail | LinkFieldConvFail
200 | 1254070 | ActionValidateFailed | ActionValidateFailed
200 | 1254100 | TableExceedLimit | TableExceedLimit, limited to 300
200 | 1254101 | ViewExceedLimit | ViewExceedLimit, limited to 200
200 | 1254102 | FileExceedLimit | FileExceedLimit
200 | 1254103 | RecordExceedLimit | RecordExceedLimit, limited to 20,000
200 | 1254104 | RecordAddOnceExceedLimit | RecordAddOnceExceedLimit, limited to 500
200 | 1254105 | ColumnExceedLimit | ColumnExceedLimit
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
403 | 1254608 | Same API requests are submitted repeatedly. | Repeat the request submission to confirm that the request parameters of this request are exactly the same as the previous one.
