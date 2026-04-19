# Overview of advanced permissions

**Owners** or collaborators with **management permissions** of a Base can set advanced permissions through the open platform interface, including setting custom roles and managing collaborators. This allows for specifying read or edit permissions for designated rows and columns for specific personnel in each Base. For more information on using advanced permissions, please refer to the Feishu Help Center document [Using advanced permissions in Base](https://www.feishu.cn/hc/zh-CN/articles/588604550568).

## Precautions

- Before calling the custom roles and collaborator-related interfaces of advanced permissions, ensure that advanced permissions have been enabled for the Base. You can enable advanced permissions through the [Update Base metadata](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app/update) interface.
- There is a delay in enabling advanced permissions. If you encounter an `OperationTypeError` error when calling the advanced permissions interface immediately after enabling advanced permissions, please try again later.
- The collaborators of advanced permissions are different from the collaborators of cloud document permissions. After adding advanced permissions collaborators, to ensure the normal setting of cloud document permissions, it is recommended to add cloud document permissions through the [Add collaborator permissions](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/permission-member/create) interface.
- After enabling advanced permissions, you need to set custom roles first before adding collaborators.

## Usage restrictions

- Bases embedded in online documents and spreadsheets, and Bases in knowledge bases do not support enabling advanced permissions.
- The advanced permissions interface for Base does not currently support setting dashboard permissions.
## Resource description
The description of custom roles and collaborator resources in advanced permissions is as follows.
### Custom role

Add roles and set permissions in advanced permissions, and the role becomes a custom role. Each custom role has a unique identifier `role_id`. `role_id` needs to be obtained through the [List custom roles](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-role/list) interface.

### Collaborator

In advanced permission settings, a member in a custom role (role) is a collaborator (member). Each collaborator has a unique identifier `member_id`. `member_id` needs to be obtained through the [List collaborators](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-role-member/list) interface.
## Method list

The following is a list of methods for advanced permissions. "Store" represents store applications; "Self-built" represents enterprise self-built applications. For more information about applications, refer to [Application types introduction](https://open.larkoffice.com/document/home/app-types-introduction/overview). For the process of calling server-side APIs, refer to [Process overview](https://open.larkoffice.com/document/ukTMukTMukTM/uITNz4iM1MjLyUzM).

### Role

**[Method (API)](https://open.larkoffice.com/document/ukTMukTMukTM/uITNz4iM1MjLyUzM)** | Permission requirements (meet either) | **[Access Credentials](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM) (choose one)** | Store | Custom
---|---|---|---|---
[List roles](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-role/list)<br>`GET` /open-apis/bitable/v1/apps/:app_token/roles | View, comment, edit and manage Base(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**
[Create role](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-role/create)<br>`POST` /open-apis/bitable/v1/apps/:app_token/roles/:role_id | View, comment, edit and manage Base(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**
[Update role](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-role/update)<br>`PUT` /open-apis/bitable/v1/apps/:app_token/roles/:role_id | View, comment, edit and manage Base(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**
[Delete role](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-role/delete)<br>`DELETE` /open-apis/bitable/v1/apps/:app_token/roles/:role_id | View, comment, edit and manage Base(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**

### Member

**[Method (API)](https://open.larkoffice.com/document/ukTMukTMukTM/uITNz4iM1MjLyUzM)** | Permission requirements (meet either) | **[Access Credentials](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM) (choose one)** | Store | Custom
---|---|---|---|---
[List members](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-role-member/list)<br>`GET` /open-apis/bitable/v1/apps/:app_token/roles/:role_id/members | View, comment, edit and manage Base(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**
[Create member](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-role-member/create)<br>`POST` /open-apis/bitable/v1/apps/:app_token/roles/:role_id/members | View, comment, edit and manage Base(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**
[Delete member](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-role-member/delete)<br>`DELETE` /open-apis/bitable/v1/apps/:app_token/roles/:role_id/members/:member_id | View, comment, edit and manage Base(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**
[Batch add collaborators](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-role-member/batch_create)<br>`POST` /open-apis/bitable/v1/apps/:app_token/roles/:role_id/members/batch_create | View, comment, edit, and manage Base(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**
[Batch delete collaborators](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-role-member/batch_delete)<br>`DELETE` /open-apis/bitable/v1/apps/:app_token/roles/:role_id/members/batch_delete | View, comment, edit, and manage Base(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**

https://open.larkoffice.com/document/docs/bitable-v1/advanced-permission/app-role/create-2

# Update role

Update a role

**Notice**：The update of the role is an incremental update,  where only the passed fields are updated, and the fields that are not passed are not updated

## Prerequisite

To call the custom role-related APIs, you need to ensure that Base has enabled advanced permissions. You can enable advanced permissions through the [Update Base Metadata](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app/update) API.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/base/v2/apps/:app_token/roles/:role_id
HTTP Method | PUT
Rate Limit | [10 per second](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.** | 更新自定义角色(base:role:update)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Path parameters

Parameter | Type | Description
---|---|---
app_token | string | Base unique device identifier [app_token description](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification#8121eebe)<br>**Example value**: "appbcbWCzen6D8dezhoCH2RpMAh"<br>**Data validation rules**:<br>- Length range: `0` ～ `100` characters
role_id | string | Role id<br>**Example value**: "roljRpwIUt"<br>**Data validation rules**:<br>- Length range: `0` ～ `100` characters

### Request body

Parameter | Type | Required | Description
---|---|---|---
role_name | string | Yes | Role name<br>**Example value**: "role1"<br>**Data validation rules**:<br>- Length range: `0` ～ `100` characters
table_roles | table_role\[\] | Yes | Table role<br>**Data validation rules**:<br>- Length range: `0` ～ `100`
table_perm | int | Yes | Table perm<br>**Example value**: 0<br>**Optional values are**:<br>- 0：No access<br>- 1：View only<br>- 2：Can edit<br>- 4：Can manage<br>**Data validation rules**:<br>- Value range: `0` ～ `4`
table_name | string | No | Table name<br>**Example value**: "table1"<br>**Data validation rules**:<br>- Length range: `0` ～ `50` characters
table_id | string | No | Table id<br>**Example value**: "tblKz5D60T4JlfcT"<br>**Data validation rules**:<br>- Length range: `0` ～ `50` characters
rec_rule | rec_rule | No | Record filter rule
conditions | rec_rule_condition\[\] | No | Coditions<br>**Data validation rules**:<br>- Length range: `0` ～ `10`
field_name | string | Yes | Field name<br>**Example value**: "Single option"
operator | string | No | Operator<br>**Example value**: "is"<br>**Optional values are**:<br>- is：Is<br>- isNot：Is not<br>- contains：Contains<br>- doesNotContain：Does not contain<br>- isEmpty：Is empty<br>- isNotEmpty：Is not empty<br>**Default value**: `is`
value | string\[\] | No | conditions value<br>**Example value**: ["optbdVHf4q"]<br>**Data validation rules**:<br>- Length range: `0` ～ `50`
conjunction | string | No | Conjunction<br>**Example value**: "and"<br>**Optional values are**:<br>- and：And<br>- or：Or<br>**Default value**: `and`
other_perm | int | No | other_perm<br>Other record permissions are only valid when table_perm is 2. When other_perm is equal to 1, all records that do not match rec_rule can be read. When other_perm is equal to 0, the range of records that can be read is specified by other_rec_rule. At this time, even if rec_rule and other_rec_rule are not matched, the records will be read statically.<br>**Example value**: 1<br>**Optional values are**:<br>- 0：no access<br>- 1：read<br>**Default value**: `0`
other_rec_rule | other_rec_rule | No | other_rec_rule<br>Record filtering condition, which is meaningful when table_perm is 2 and rec_rule.other_perm is 0. For records that do not hit rec_rule, other_rec_rule is used to filter out the range of readable records.<br>**Note**: At this time, records that do not hit either rec_rule or other_rec_rule are unreadable.
conditions | rec_rule_condition\[\] | No | conditions<br>**Data validation rules**:<br>- Length range: `0` ～ `10`
field_name | string | Yes | Field name<br>**Example value**: "Single option"
operator | string | No | Operator<br>**Example value**: "is"<br>**Optional values are**:<br>- is：Is<br>- isNot：Is not<br>- contains：Contains<br>- doesNotContain：Does not contain<br>- isEmpty：Is empty<br>- isNotEmpty：Is not empty<br>**Default value**: `is`
value | string\[\] | No | conditions value<br>**Example value**: ["optbdVHf4q"]<br>**Data validation rules**:<br>- Length range: `0` ～ `50`
conjunction | string | No | Conjunction<br>**Example value**: "and"<br>**Optional values are**:<br>- and：And<br>- or：Or<br>**Default value**: `and`
field_perm | map&lt;string, int&gt; | No | Permission of fields, only valid when `table_perm` is 2.  The type is map, key is field name, value is permission of field.<br>**Optional values are**:<br>- `1`: View only<br>- `2`: Can add records<br>- `3`: Can edit records<br>**Example value**: {"name": 1, "age": 2}
allow_add_record | boolean | No | Added record permission, only meaningful when the table_perm is 2, used to set whether the record can be added<br>**Example value**: true<br>**Default value**: `true`
allow_delete_record | boolean | No | Delete record permission, meaningful only when the table_perm is 2, used to set whether the record can be deleted<br>**Example value**: true<br>**Default value**: `true`
view_perm | int | No | View permission<br>**Example value**: 2<br>**Optional values are**:<br>- 1：Can read<br>- 2：Can edit<br>**Default value**: `2`<br>**Data validation rules**:<br>- Value range: `0` ～ `2`
view_rules | map&lt;string, int&gt; | No | A readable view collection. This is only meaningful when view_perm is 1. If it is not set, all views are readable. If it is set, it means that only views in the collection are readable, and views outside the collection have no permission.<br>The parameter type is a map, where the key is the view id and the value is the permission corresponding to the view. The value enumeration values ​​are:<br>- `0`: No access<br>- `1`:  Read only<br>**Example value**: {"vewEYknYcC": 0}
field_action_rules | map&lt;string, map&lt;string, int&gt;&gt; | No | Field point permission configuration, optional points are:<br>`select_option_edit`: Option configuration point, configure whether to add, delete, or modify single-select and multiple-select option values<br>`attachment_export`: Attachment operation permission point, configure whether to export attachments<br>This parameter type is a two-layer map structure, where the key is the field point permission and the value is the field permission set. The field permission set is also a map structure, where the key is the field name and the value is the field point permission:<br>- `0`: No access<br>- `1`: Can access<br>**Example value**: {"select_option_edit": {"name":0}}
block_roles | block_role\[\] | No | Block role<br>**Data validation rules**:<br>- Length range: `0` ～ `100`
block_id | string | Yes | Block id, Such as dashboard block id in list dashboards method<br>**Example value**: "blknkqrP3RqUkcAW"<br>**Data validation rules**:<br>- Length range: `0` ～ `100` characters
block_perm | int | Yes | Block perm<br>**Example value**: 0<br>**Optional values are**:<br>- 0：No permissions<br>- 1：View only
base_rule | map&lt;string, int&gt; | No | base role<br>`base_complex_edit`: Set whether you can create copies, download, and print multidimensional tables<br>`copy`: Set whether you can copy the contents of multidimensional tables<br>The parameter type is map, where key is the permission point name and value is the permission switch. The value enumeration values ​​are:<br>- `0`: No access<br>- `1`: Can access<br>**Example value**: {"base_complex_edit": 1, "copy": 0}

### Request body example
```json
{
    "role_name": "role1",
    "table_roles": [
        {
            "table_perm": 0,
            "table_name": "table1",
            "table_id": "tblKz5D60T4JlfcT",
            "rec_rule": {
                "conditions": [
                    {
                        "field_name": "Single option",
                        "operator": "is",
                        "value": [
                            "optbdVHf4q"
                        ]
                    }
                ],
                "conjunction": "and",
                "other_perm": 1
            },
            "other_rec_rule": {
                "conditions": [
                    {
                        "field_name": "Single option",
                        "operator": "is",
                        "value": [
                            "optbdVHf4q"
                        ]
                    }
                ],
                "conjunction": "and"
            },
            "field_perm": {
                "name": 1,
                "age": 2
            },
            "allow_add_record": true,
            "allow_delete_record": true,
            "view_perm": 2,
            "view_rules": {
                "vewEYknYcC": 0
            },
            "field_action_rules": {
                "select_option_edit": {
                    "name": 0
                }
            }
        }
    ],
    "block_roles": [
        {
            "block_id": "blknkqrP3RqUkcAW",
            "block_perm": 0
        }
    ],
    "base_rule": {
        "base_complex_edit": 1,
        "copy": 0
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
role | role | Role information
role_name | string | Role name
table_roles | table_role\[\] | Table role
table_perm | int | Table perm<br>**Optional values are**:<br>- 0：No access<br>- 1：View only<br>- 2：Can edit<br>- 4：Can manage
table_name | string | Table name
table_id | string | Table id
rec_rule | rec_rule | Record filter rule
conditions | rec_rule_condition\[\] | Coditions
field_name | string | Field name
operator | string | Operator<br>**Optional values are**:<br>- is：Is<br>- isNot：Is not<br>- contains：Contains<br>- doesNotContain：Does not contain<br>- isEmpty：Is empty<br>- isNotEmpty：Is not empty
value | string\[\] | conditions value
field_type | int | field_type
conjunction | string | Conjunction<br>**Optional values are**:<br>- and：And<br>- or：Or
perm | int | /<br>**Optional values are**:<br>- 1：read<br>- 2：edit
other_perm | int | other_perm<br>Other record permissions are only valid when table_perm is 2. When other_perm is equal to 1, all records that do not match rec_rule can be read. When other_perm is equal to 0, the range of records that can be read is specified by other_rec_rule. At this time, even if rec_rule and other_rec_rule are not matched, the records will be read statically.<br>**Optional values are**:<br>- 0：no access<br>- 1：read
other_rec_rule | other_rec_rule | other_rec_rule<br>Record filtering condition, which is meaningful when table_perm is 2 and rec_rule.other_perm is 0. For records that do not hit rec_rule, other_rec_rule is used to filter out the range of readable records.<br>**Note**: At this time, records that do not hit either rec_rule or other_rec_rule are unreadable.
conditions | rec_rule_condition\[\] | conditions
field_name | string | Field name
operator | string | Operator<br>**Optional values are**:<br>- is：Is<br>- isNot：Is not<br>- contains：Contains<br>- doesNotContain：Does not contain<br>- isEmpty：Is empty<br>- isNotEmpty：Is not empty
value | string\[\] | conditions value
field_type | int | field_type
conjunction | string | Conjunction<br>**Optional values are**:<br>- and：And<br>- or：Or
perm | int | perm<br>**Optional values are**:<br>- 1：/<br>- 2：/
field_perm | map&lt;string, int&gt; | Permission of fields, only valid when `table_perm` is 2.  The type is map, key is field name, value is permission of field.<br>**Optional values are**:<br>- `1`: View only<br>- `2`: Can add records<br>- `3`: Can edit records
allow_add_record | boolean | Added record permission, only meaningful when the table_perm is 2, used to set whether the record can be added
allow_delete_record | boolean | Delete record permission, meaningful only when the table_perm is 2, used to set whether the record can be deleted
view_perm | int | View permission<br>**Optional values are**:<br>- 1：Can read<br>- 2：Can edit
view_rules | map&lt;string, int&gt; | A readable view collection. This is only meaningful when view_perm is 1. If it is not set, all views are readable. If it is set, it means that only views in the collection are readable, and views outside the collection have no permission.<br>The parameter type is a map, where the key is the view id and the value is the permission corresponding to the view. The value enumeration values ​​are:<br>- `0`: No access<br>- `1`:  Read only
field_action_rules | map&lt;string, map&lt;string, int&gt;&gt; | Field point permission configuration, optional points are:<br>`select_option_edit`: Option configuration point, configure whether to add, delete, or modify single-select and multiple-select option values<br>`attachment_export`: Attachment operation permission point, configure whether to export attachments<br>This parameter type is a two-layer map structure, where the key is the field point permission and the value is the field permission set. The field permission set is also a map structure, where the key is the field name and the value is the field point permission:<br>- `0`: No access<br>- `1`: Can access
role_id | string | role_id
block_roles | block_role\[\] | Block role
block_id | string | Block id, Such as dashboard block id in list dashboards method
block_perm | int | Block perm<br>**Optional values are**:<br>- 0：No permissions<br>- 1：View only
block_type | string | block_type<br>**Optional values are**:<br>- dashboard：dashboard
base_rule | map&lt;string, int&gt; | base role<br>`base_complex_edit`: Set whether you can create copies, download, and print multidimensional tables<br>`copy`: Set whether you can copy the contents of multidimensional tables<br>The parameter type is map, where key is the permission point name and value is the permission switch. The value enumeration values ​​are:<br>- `0`: No access<br>- `1`: Can access

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "role": {
            "role_name": "role1",
            "table_roles": [
                {
                    "table_perm": 0,
                    "table_name": "table1",
                    "table_id": "tblKz5D60T4JlfcT",
                    "rec_rule": {
                        "conditions": [
                            {
                                "field_name": "Single option",
                                "operator": "is",
                                "value": [
                                    "optbdVHf4q"
                                ],
                                "field_type": 3
                            }
                        ],
                        "conjunction": "and",
                        "perm": 1,
                        "other_perm": 1
                    },
                    "other_rec_rule": {
                        "conditions": [
                            {
                                "field_name": "Single option",
                                "operator": "is",
                                "value": [
                                    "optbdVHf4q"
                                ],
                                "field_type": 3
                            }
                        ],
                        "conjunction": "and",
                        "perm": 1
                    },
                    "field_perm": {
                        "name": 1,
                        "age": 2
                    },
                    "allow_add_record": true,
                    "allow_delete_record": true,
                    "view_perm": 2,
                    "view_rules": {
                        "vewEYknYcC": 0
                    },
                    "field_action_rules": {
                        "select_option_edit": {
                            "name": 0
                        }
                    }
                }
            ],
            "role_id": "roljRpwIUt",
            "block_roles": [
                {
                    "block_id": "blknkqrP3RqUkcAW",
                    "block_perm": 0,
                    "block_type": "dashboard"
                }
            ],
            "base_rule": {
                "base_complex_edit": 1,
                "copy": 0
            }
        }
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
200 | 1254010 | ReqConvError | Request error
400 | 1254032 | InvalidRoleName | Invalid role name
400 | 1254033 | RoleNameDuplicated | Role name duplicated
400 | 1254036 | Bitable is copying, please try again later. | Base copy replicating, try again later
200 | 1254040 | BaseTokenNotFound | AppToken not found
404 | 1254047 | RoleIdNotFound | RoleIdNotFound
400 | 1254110 | RoleExceedLimit | Role exceed limit, limited to 30
200 | 1254290 | TooManyRequest | TooManyRequest
400 | 1254301 | OperationTypeError | Base does not have advanced permissions enabled or does not support enabling advanced permissions
403 | 1254304 | Only Available For Business and Enterprise Editions | Advanced permissions for specific rows or columns are only available for Business and Enterprise editions
200 | 1255001 | InternalError | Internal error, have any questions can be consulting service
200 | 1255002 | Something went wrong. Please contact technical support at https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952 | Something went wrong. Please contact technical support at https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952
200 | 1255003 | MarshalError | Serialization failed, have any questions can be consulting service
200 | 1255004 | UmMarshalError | Deserialization failed, have any questions can be consulting service
504 | 1255040 | Request timed out, please try again later | Try again

# List roles

Get all roles according to app_token

## Prerequisite

To call the custom role-related APIs, you need to ensure that Base has enabled advanced permissions. You can enable advanced permissions through the [Update Base Metadata](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app/update) API.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/base/v2/apps/:app_token/roles
HTTP Method | GET
Rate Limit | [20 per second](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.** | Read custom role(base:role:read)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)

### Path parameters

Parameter | Type | Description
---|---|---
app_token | string | Base unique device identifier [app_token description](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification#8121eebe)<br>**Example value**: "appbcbWCzen6D8dezhoCH2RpMAh"<br>**Data validation rules**:<br>- Length range: `0` ～ `100` characters

### Query parameters

Parameter | Type | Required | Description
---|---|---|---
page_size | int | No | page_size<br>**Example value**: 10
page_token | string | No | Page identifier. It is not filled in the first request, indicating traversal from the beginning; when there will be more groups, the new page_token will be returned at the same time, and the next traversal can use the page_token to get more groups<br>**Example value**: roljRpwIUt

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
items | role\[\] | Role information
role_name | string | Role name
table_roles | table_role\[\] | Table role
table_perm | int | Table perm<br>**Optional values are**:<br>- 0：No access<br>- 1：View only<br>- 2：Can edit<br>- 4：Can manage
table_name | string | Table name
table_id | string | Table id
rec_rule | rec_rule | Record filter rule
conditions | rec_rule_condition\[\] | Coditions
field_name | string | Field name
operator | string | Operator<br>**Optional values are**:<br>- is：Is<br>- isNot：Is not<br>- contains：Contains<br>- doesNotContain：Does not contain<br>- isEmpty：Is empty<br>- isNotEmpty：Is not empty
value | string\[\] | conditions value
field_type | int | field_type
conjunction | string | Conjunction<br>**Optional values are**:<br>- and：And<br>- or：Or
perm | int | /<br>**Optional values are**:<br>- 1：read<br>- 2：edit
other_perm | int | other_perm<br>Other record permissions are only valid when table_perm is 2. When other_perm is equal to 1, all records that do not match rec_rule can be read. When other_perm is equal to 0, the range of records that can be read is specified by other_rec_rule. At this time, even if rec_rule and other_rec_rule are not matched, the records will be read statically.<br>**Optional values are**:<br>- 0：no access<br>- 1：read
other_rec_rule | other_rec_rule | other_rec_rule<br>Record filtering condition, which is meaningful when table_perm is 2 and rec_rule.other_perm is 0. For records that do not hit rec_rule, other_rec_rule is used to filter out the range of readable records.<br>**Note**: At this time, records that do not hit either rec_rule or other_rec_rule are unreadable.
conditions | rec_rule_condition\[\] | conditions
field_name | string | Field name
operator | string | Operator<br>**Optional values are**:<br>- is：Is<br>- isNot：Is not<br>- contains：Contains<br>- doesNotContain：Does not contain<br>- isEmpty：Is empty<br>- isNotEmpty：Is not empty
value | string\[\] | conditions value
field_type | int | field_type
conjunction | string | Conjunction<br>**Optional values are**:<br>- and：And<br>- or：Or
perm | int | perm<br>**Optional values are**:<br>- 1：/<br>- 2：/
field_perm | map&lt;string, int&gt; | Permission of fields, only valid when `table_perm` is 2.  The type is map, key is field name, value is permission of field.<br>**Optional values are**:<br>- `1`: View only<br>- `2`: Can add records<br>- `3`: Can edit records
allow_add_record | boolean | Added record permission, only meaningful when the table_perm is 2, used to set whether the record can be added
allow_delete_record | boolean | Delete record permission, meaningful only when the table_perm is 2, used to set whether the record can be deleted
view_perm | int | View permission<br>**Optional values are**:<br>- 1：Can read<br>- 2：Can edit
view_rules | map&lt;string, int&gt; | A readable view collection. This is only meaningful when view_perm is 1. If it is not set, all views are readable. If it is set, it means that only views in the collection are readable, and views outside the collection have no permission.<br>The parameter type is a map, where the key is the view id and the value is the permission corresponding to the view. The value enumeration values ​​are:<br>- `0`: No access<br>- `1`:  Read only
field_action_rules | map&lt;string, map&lt;string, int&gt;&gt; | Field point permission configuration, optional points are:<br>`select_option_edit`: Option configuration point, configure whether to add, delete, or modify single-select and multiple-select option values<br>`attachment_export`: Attachment operation permission point, configure whether to export attachments<br>This parameter type is a two-layer map structure, where the key is the field point permission and the value is the field permission set. The field permission set is also a map structure, where the key is the field name and the value is the field point permission:<br>- `0`: No access<br>- `1`: Can access
role_id | string | role_id
block_roles | block_role\[\] | Block role
block_id | string | Block id, Such as dashboard block id in list dashboards method
block_perm | int | Block perm<br>**Optional values are**:<br>- 0：No permissions<br>- 1：View only
block_type | string | block_type<br>**Optional values are**:<br>- dashboard：dashboard
base_rule | map&lt;string, int&gt; | base role<br>`base_complex_edit`: Set whether you can create copies, download, and print multidimensional tables<br>`copy`: Set whether you can copy the contents of multidimensional tables<br>The parameter type is map, where key is the permission point name and value is the permission switch. The value enumeration values ​​are:<br>- `0`: No access<br>- `1`: Can access
page_token | string | Page identifier, when has_more is true, a new page_token will also be returned. Otherwise, page_token will not be returned
has_more | boolean | Whether the response body has more parameters
total | int | 自定义角色总数

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "items": [
            {
                "role_name": "role1",
                "table_roles": [
                    {
                        "table_perm": 0,
                        "table_name": "table1",
                        "table_id": "tblKz5D60T4JlfcT",
                        "rec_rule": {
                            "conditions": [
                                {
                                    "field_name": "Single option",
                                    "operator": "is",
                                    "value": [
                                        "optbdVHf4q"
                                    ],
                                    "field_type": 3
                                }
                            ],
                            "conjunction": "and",
                            "perm": 1,
                            "other_perm": 1
                        },
                        "other_rec_rule": {
                            "conditions": [
                                {
                                    "field_name": "Single option",
                                    "operator": "is",
                                    "value": [
                                        "optbdVHf4q"
                                    ],
                                    "field_type": 3
                                }
                            ],
                            "conjunction": "and",
                            "perm": 1
                        },
                        "field_perm": {
                            "name": 1,
                            "age": 2
                        },
                        "allow_add_record": true,
                        "allow_delete_record": true,
                        "view_perm": 2,
                        "view_rules": {
                            "vewEYknYcC": 0
                        },
                        "field_action_rules": {
                            "select_option_edit": {
                                "name": 0
                            }
                        }
                    }
                ],
                "role_id": "roljRpwIUt",
                "block_roles": [
                    {
                        "block_id": "blknkqrP3RqUkcAW",
                        "block_perm": 0,
                        "block_type": "dashboard"
                    }
                ],
                "base_rule": {
                    "base_complex_edit": 1,
                    "copy": 0
                }
            }
        ],
        "page_token": "eVQrYzJBNDNONlk4VFZBZVlSdzlKdFJ4bVVHVExENDNKVHoxaVdiVnViQT0=",
        "has_more": true,
        "total": 1
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
200 | 1254010 | ReqConvError | Request error
400 | 1254032 | InvalidRoleName | Invalid role name
400 | 1254033 | RoleNameDuplicated | Role name duplicated
400 | 1254036 | Bitable is copying, please try again later. | Base copy replicating, try again later
200 | 1254040 | BaseTokenNotFound | AppToken not found
404 | 1254047 | RoleIdNotFound | RoleIdNotFound
400 | 1254110 | RoleExceedLimit | Role exceed limit, limited to 30
200 | 1254290 | TooManyRequest | TooManyRequest
400 | 1254301 | OperationTypeError | Base does not have advanced permissions enabled or does not support enabling advanced permissions
200 | 1255001 | InternalError | Internal error, have any questions can be consulting service
200 | 1255002 | Something went wrong. Please contact technical support at https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952 | Something went wrong. Please contact technical support at https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952
200 | 1255003 | MarshalError | Serialization failed, have any questions can be consulting service
200 | 1255004 | UmMarshalError | Deserialization failed, have any questions can be consulting service
504 | 1255040 | Request timed out, please try again later | Try again

# Delete role

Delete a role

## Prerequisite

To call the custom role-related APIs, you need to ensure that Base has enabled advanced permissions. You can enable advanced permissions through the [Update Base Metadata](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app/update) API.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/roles/:role_id
HTTP Method | DELETE
Rate Limit | [10 per second](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.** | View, comment, edit and manage Base(bitable:app)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)

### Path parameters

Parameter | Type | Description
---|---|---
app_token | string | Base unique device identifier [app_token description](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification#8121eebe)<br>**Example value**: "appbcbWCzen6D8dezhoCH2RpMAh"
role_id | string | Role id<br>**Example value**: "roljRpwIUt"

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
200 | 1254000 | WrongRequestJson | Request error
200 | 1254001 | WrongRequestBody | Request body error
200 | 1254002 | Fail | Internal error, have any questions can be consulting service
200 | 1254003 | WrongBaseToken | AppToken error
200 | 1254010 | ReqConvError | Request error
400 | 1254032 | InvalidRoleName | Invalid role name
400 | 1254033 | RoleNameDuplicated | Role name duplicated
400 | 1254036 | Base is copying, please try again later. | Base copy replicating, try again later
200 | 1254040 | BaseTokenNotFound | AppToken not found
404 | 1254047 | RoleIdNotFound | Role not found
400 | 1254110 | RoleExceedLimit | Role exceed limit, limited to 30
200 | 1254290 | TooManyRequest | Request too fast, try again later
200 | 1254291 | Write conflict | The same data table does not support concurrent calls to the write interface, please check whether there is a concurrent call to the write interface. The writing interface includes: adding, modifying, and deleting records; adding, modifying, and deleting fields; modifying forms; modifying views, etc.
400 | 1254301 | OperationTypeError | Base does not have advanced permissions enabled or does not support enabling advanced permissions
403 | 1254302 | Permission denied. | No access rights, usually caused by the table opening of advanced permissions, please add a group containing applications in the advanced permissions settings and give this group read and write permissions
200 | 1255001 | InternalError | Internal error, have any questions can be consulting service
200 | 1255002 | RpcError | Internal error, have any questions can be consulting service
200 | 1255003 | MarshalError | Serialization failed, have any questions can be consulting service
200 | 1255004 | UmMarshalError | Deserialization failed, have any questions can be consulting service
504 | 1255040 | Request timed out, please try again later | Try again

# Create member

Create a member

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/roles/:role_id/members
HTTP Method | POST
Rate Limit | [10 per second](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.** | View, comment, edit and manage Base(bitable:app)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Path parameters

Parameter | Type | Description
---|---|---
app_token | string | Base unique device identifier [app_token description](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification#8121eebe)<br>**Example value**: "appbcbWCzen6D8dezhoCH2RpMAh"
role_id | string | Role id<br>**Example value**: "roljRpwIUt"

### Query parameters

Parameter | Type | Required | Description
---|---|---|---
member_id_type | string | No | Member id type<br>**Example value**: open_id<br>**Optional values are**:<br>- open_id：open_id<br>- union_id：union_id<br>- user_id：user_id<br>- chat_id：chat_id<br>- department_id：department_id. Before using this parameter, make sure the application has departmental visibility, refer to [configure application availability scope](https://open.larkoffice.com/document/home/introduction-to-scope-and-authorization/availability)<br>- open_department_id：open_department_id. Before using this parameter, make sure the application has departmental visibility, refer to [configure application availability scope](https://open.larkoffice.com/document/home/introduction-to-scope-and-authorization/availability)<br>**Default value**: `open_id`

### Request body

Parameter | Type | Required | Description
---|---|---|---
member_id | string | Yes | Member id<br>**Example value**: "ou_7dab8a3d3cdcc9da365777c7ad535d62"

### Request body example
```json
{
    "member_id": "ou_7dab8a3d3cdcc9da365777c7ad535d62"
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
200 | 1254000 | WrongRequestJson | Request error
200 | 1254001 | WrongRequestBody | Request body error
200 | 1254002 | Fail | Internal error, have any questions can be consulting service
200 | 1254003 | WrongBaseToken | AppToken error
200 | 1254010 | ReqConvError | Request error
400 | 1254032 | InvalidRoleName | Invalid role name
400 | 1254033 | RoleNameDuplicated | Role name duplicated
400 | 1254036 | Base is copying, please try again later. | Base copy replicating, try again later
200 | 1254040 | BaseTokenNotFound | AppToken not found
404 | 1254047 | RoleIdNotFound | Role not found
404 | 1254048 | MemberNotFound | Member not found
400 | 1254110 | RoleExceedLimit | Role exceed limit, limited to 30
400 | 1254111 | MemberExceedLimit | Member exceed limit, limited to 200
200 | 1254290 | TooManyRequest | Request too fast, try again later
200 | 1254291 | Write conflict | The same data table does not support concurrent calls to the write interface, please check whether there is a concurrent call to the write interface. The writing interface includes: adding, modifying, and deleting records; adding, modifying, and deleting fields; modifying forms; modifying views, etc.
400 | 1254301 | OperationTypeError | Base does not have advanced permissions enabled or does not support enabling advanced permissions
403 | 1254302 | Permission denied. | No access rights, usually caused by the table opening of advanced permissions, please add a group containing applications in the advanced permissions settings and give this group read and write permissions
200 | 1255001 | InternalError | Internal error, have any questions can be consulting service
200 | 1255002 | RpcError | Internal error, have any questions can be consulting service
200 | 1255003 | MarshalError | Serialization failed, have any questions can be consulting service
200 | 1255004 | UmMarshalError | Deserialization failed, have any questions can be consulting service
504 | 1255040 | Request timed out, please try again later | Try again

# Batch create members

Add role members with custom permissions in bulk

## Prerequisites

To call the collaborator-related APIs, you need to ensure that Base has enabled advanced permissions and set custom roles. You can enable advanced permissions through the [Update Base Metadata](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app/update) API and set custom roles through the [Create Custom Role](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-role/create) API.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/roles/:role_id/members/batch_create
HTTP Method | POST
Rate Limit | [10 per second](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.** | View, comment, edit and manage Base(bitable:app)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Path parameters

Parameter | Type | Description
---|---|---
app_token | string | Base unique device identifier [app_token description](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification#8121eebe)<br>**Example value**: "bascnnKKvcoUblgmmhZkYqabcef"
role_id | string | Custom role ID<br>**Example value**: "rolNGhPqks"

### Request body

Parameter | Type | Required | Description
---|---|---|---
member_list | app.role.member_id\[\] | Yes | List of member<br>**Data validation rules**:<br>- Maximum length: `100`
type | string | No | member id type<br>**Example value**: "open_id"<br>**Optional values are**:<br>- open_id：member ID type is open_id<br>- union_id：member ID type is union_id<br>- user_id：member ID type is user_id<br>- chat_id：member ID type is chat_id<br>- department_id：member ID type is department_id<br>- open_department_id：member ID type is open_department_id<br>**Default value**: `open_id`
id | string | Yes | member ID<br>**Example value**: "ou_35990a9d9052051a2fae9b2f1afabcef"

### Request body example
```json
{
    "member_list": [
        {
            "type": "open_id",
            "id": "ou_35990a9d9052051a2fae9b2f1afabcef"
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
400 | 1254000 | WrongRequestJson | Request error
400 | 1254001 | WrongRequestBody | Request body error
400 | 1254002 | Fail | Internal error, have any questions can be consulting service
400 | 1254003 | WrongBaseToken | AppToken error
400 | 1254032 | InvalidRoleName | Invalid role name
400 | 1254033 | RoleNameDuplicated | Role name duplicated
404 | 1254040 | BaseTokenNotFound | AppToken not found
404 | 1254047 | RoleIdNotFound | Role not found
400 | 1254048 | MemberNotFound | Member not found
400 | 1254110 | RoleExceedLimit | Role exceed limit, limited to 30
429 | 1254290 | TooManyRequest | Request too fast, try again later
400 | 1254291 | Write conflict | The same data table does not support concurrent calls to the write interface, please check whether there is a concurrent call to the write interface. The writing interface includes: adding, modifying, and deleting records; adding, modifying, and deleting fields; modifying forms; modifying views, etc.
400 | 1254301 | OperationTypeError | Base does not have advanced permissions enabled or does not support enabling advanced permissions
403 | 1254302 | Permission denied. | No access rights, usually caused by the table opening of advanced permissions, please add a group containing applications in the advanced permissions settings and give this group read and write permissions
400 | 1255001 | InternalError | Internal error, have any questions can be consulting service
504 | 1255040 | Request timed out, please try again later | Try again
400 | 1254036 | Base is copying, please try again later. | Base copy replicating, try again later

# List members

Get all members according to app_token and role_id

## Prerequisites

To call the collaborator-related APIs, you need to ensure that Base has enabled advanced permissions and set custom roles. You can enable advanced permissions through the [Update Base Metadata](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app/update) API and set custom roles through the [Create Custom Role](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-role/create) API.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/roles/:role_id/members
HTTP Method | GET
Rate Limit | [20 per second](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.**<br>Enable any scope from the list | View, comment, edit and manage Base(bitable:app)<br>View, comment, and export Base(bitable:app:readonly)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)

### Path parameters

Parameter | Type | Description
---|---|---
app_token | string | Base unique device identifier [app_token description](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification#8121eebe)<br>**Example value**: "appbcbWCzen6D8dezhoCH2RpMAh"
role_id | string | Role id<br>**Example value**: "roljRpwIUt"

### Query parameters

Parameter | Type | Required | Description
---|---|---|---
page_size | int | No | Page size<br>**Example value**: 100<br>**Data validation rules**:<br>- Maximum value: `100`
page_token | string | No | Page identifier. It is not filled in the first request, indicating traversal from the beginning; when there will be more groups, the new page_token will be returned at the same time, and the next traversal can use the page_token to get more groups<br>**Example value**: xxxxx

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
items | app.role.member\[\] | Member information
open_id | string | User's open_id
union_id | string | User's union_id
user_id | string | User's user_id
chat_id | string | Chat's chat_id
department_id | string | Department's department_id
open_department_id | string | Department's open_department_id
member_name | string | Member name
member_en_name | string | Member English name
member_type | string | Member type<br>**Optional values are**:<br>- user：User<br>- chat：Chat<br>- department：Department
has_more | boolean | Whether the response body has more parameters
page_token | string | Page identifier, when has_more is true, a new page_token will also be returned. Otherwise, page_token will not be returned
total | int | Total

### Response body example
```json
{
    "msg": "success",
    "data": {
        "items": [
            {
                "member_type": "user",
                "member_name": "Tom",
                "member_en_name": "Tom",
                "open_id": "ou_xxxxxxxxxxxxxxxx",
                "union_id": "on_xxxxxxxxxxxxxxxx",
                "user_id": "xxxxxx"
            },
            {
                "member_type": "chat",
                "member_name": "design-chat",
                "member_en_name": "design-chat",
                "chat_id": "oc_xxxxxxxxxxxxxxxx"
            },
            {
                "member_type": "department",
                "member_name": "design-center",
                "member_en_name": "design-center",
                "department_id": "xxxxxxxxx",
                "open_department_id": "od-xxxxxxxxxxxxxxxx"
            }
        ],
        "page_token": "xxxxxxxxx",
        "total": 3,
        "has_more": false
    },
    "code": 0
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
200 | 1254000 | WrongRequestJson | Request error
200 | 1254001 | WrongRequestBody | Request body error
200 | 1254002 | Fail | Internal error, have any questions can be consulting service
200 | 1254003 | WrongBaseToken | AppToken error
200 | 1254010 | ReqConvError | Request error
400 | 1254032 | InvalidRoleName | Invalid role name
400 | 1254033 | RoleNameDuplicated | Role name duplicated
400 | 1254036 | Base is copying, please try again later. | Base copy replicating, try again later
200 | 1254040 | BaseTokenNotFound | AppToken not found
404 | 1254047 | RoleIdNotFound | Role not found
404 | 1254048 | MemberNotFound | Member not found
400 | 1254110 | RoleExceedLimit | Role exceed limit, limited to 30
400 | 1254111 | MemberExceedLimit | Member exceed limit, limited to 200
400 | 1254200 | Something went wrong. Please contact technical support at https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952 | Internal error, have any questions can be consulting service
200 | 1254290 | TooManyRequest | Request too fast, try again later
200 | 1254291 | Write conflict | The same data table does not support concurrent calls to the write interface, please check whether there is a concurrent call to the write interface. The writing interface includes: adding, modifying, and deleting records; adding, modifying, and deleting fields; modifying forms; modifying views, etc.
400 | 1254301 | OperationTypeError | Base does not have advanced permissions enabled or does not support enabling advanced permissions
403 | 1254302 | Permission denied. | No access rights, usually caused by the table opening of advanced permissions, please add a group containing applications in the advanced permissions settings and give this group read and write permissions
200 | 1255001 | InternalError | Internal error, have any questions can be consulting service
200 | 1255002 | RpcError | Internal error, have any questions can be consulting service
200 | 1255003 | MarshalError | Serialization failed, have any questions can be consulting service
200 | 1255004 | UmMarshalError | Deserialization failed, have any questions can be consulting service
504 | 1255040 | Request timed out, please try again later | Try again

# Delete member

Delete a member

## Prerequisites

To call the collaborator-related APIs, you need to ensure that Base has enabled advanced permissions and set custom roles. You can enable advanced permissions through the [Update Base Metadata](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app/update) API and set custom roles through the [Create Custom Role](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-role/create) API.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/roles/:role_id/members/:member_id
HTTP Method | DELETE
Rate Limit | [10 per second](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.** | View, comment, edit and manage Base(bitable:app)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)

### Path parameters

Parameter | Type | Description
---|---|---
app_token | string | Base unique device identifier [app_token description](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification#8121eebe)<br>**Example value**: "appbcbWCzen6D8dezhoCH2RpMAh"
role_id | string | Role id<br>**Example value**: "roljRpwIUt"
member_id | string | Member id<br>**Example value**: "ou_7dab8a3d3cdcc9da365777c7ad53uew2"

### Query parameters

Parameter | Type | Required | Description
---|---|---|---
member_id_type | string | No | Member id type<br>**Example value**: open_id<br>**Optional values are**:<br>- open_id：open_id<br>- union_id：union_id<br>- user_id：user_id<br>- chat_id：chat_id<br>- department_id：department_id<br>- open_department_id：open_department_id<br>**Default value**: `open_id`

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
200 | 1254000 | WrongRequestJson | Request error
200 | 1254001 | WrongRequestBody | Request body error
200 | 1254002 | Fail | Internal error, have any questions can be consulting service
200 | 1254003 | WrongBaseToken | AppToken error
200 | 1254010 | ReqConvError | Request error
400 | 1254032 | InvalidRoleName | Invalid role name
400 | 1254033 | RoleNameDuplicated | Role name duplicated
400 | 1254036 | Base is copying, please try again later. | Base copy replicating, try again later
200 | 1254040 | BaseTokenNotFound | AppToken not found
404 | 1254047 | RoleIdNotFound | Role not found
404 | 1254048 | MemberNotFound | Member not found
400 | 1254110 | RoleExceedLimit | Role exceed limit, limited to 30
400 | 1254111 | MemberExceedLimit | Member exceed limit, limited to 200
200 | 1254290 | TooManyRequest | Request too fast, try again later
200 | 1254291 | Write conflict | The same data table does not support concurrent calls to the write interface, please check whether there is a concurrent call to the write interface. The writing interface includes: adding, modifying, and deleting records; adding, modifying, and deleting fields; modifying forms; modifying views, etc.
400 | 1254301 | OperationTypeError | Base does not have advanced permissions enabled or does not support enabling advanced permissions
403 | 1254302 | Permission denied. | No access rights, usually caused by the table opening of advanced permissions, please add a group containing applications in the advanced permissions settings and give this group read and write permissions
200 | 1255001 | InternalError | Internal error, have any questions can be consulting service
200 | 1255002 | RpcError | Internal error, have any questions can be consulting service
200 | 1255003 | MarshalError | Serialization failed, have any questions can be consulting service
200 | 1255004 | UmMarshalError | Deserialization failed, have any questions can be consulting service
504 | 1255040 | Request timed out, please try again later | Try again

# Batch delete members

Batch delete role members

## Prerequisites

To call the collaborator-related APIs, you need to ensure that Base has enabled advanced permissions and set custom roles. You can enable advanced permissions through the [Update Base Metadata](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app/update) API and set custom roles through the [Create Custom Role](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-role/create) API.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/bitable/v1/apps/:app_token/roles/:role_id/members/batch_delete
HTTP Method | POST
Rate Limit | [10 per second](https://open.larkoffice.com/document/ukTMukTMukTM/uUzN04SN3QjL1cDN)
Supported app types | Custom App、Store App
Required scopes<br>**To use this API, you must have at least 1 of the listed scopes.** | View, comment, edit and manage Base(bitable:app)

### Request header

Parameter | Type | Required | Description
---|---|---|---
Authorization | string | Yes | `tenant_access_token`<br>or<br>`user_access_token`<br>**Value format**: "Bearer `access_token`"<br>**Example value**: "Bearer u-7f1bcd13fc57d46bac21793a18e560"<br>[How to choose and get access token](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-choose-which-type-of-token-to-use)
Content-Type | string | Yes | **Fixed value**: "application/json; charset=utf-8"

### Path parameters

Parameter | Type | Description
---|---|---
app_token | string | Base unique device identifier [app_token description](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/bitable/notification#8121eebe)<br>**Example value**: "bascnnKKvcoUblgmmhZkYqabcef"
role_id | string | Custom role ID<br>**Example value**: "rolNGhPqks"

### Request body

Parameter | Type | Required | Description
---|---|---|---
member_list | app.role.member_id\[\] | Yes | List of members<br>**Data validation rules**:<br>- Maximum length: `100`
type | string | No | member id type<br>**Example value**: "open_id"<br>**Optional values are**:<br>- open_id：member ID type is open_id<br>- union_id：member ID type is union_id<br>- user_id：member ID type is user_id<br>- chat_id：member ID type is chat_id<br>- department_id：member ID type is department_id<br>- open_department_id：member ID type is open_department_id<br>**Default value**: `open_id`
id | string | Yes | member ID<br>**Example value**: "ou_35990a9d9052051a2fae9b2f1afabcef"

### Request body example
```json
{
    "member_list": [
        {
            "type": "open_id",
            "id": "ou_35990a9d9052051a2fae9b2f1afabcef"
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
400 | 1254000 | WrongRequestJson | Request error
400 | 1254001 | WrongRequestBody | Request body error
400 | 1254002 | Fail | Internal error, have any questions can be consulting service
400 | 1254003 | WrongBaseToken | AppToken error
400 | 1254032 | InvalidRoleName | Invalid role name
400 | 1254033 | RoleNameDuplicated | Role name duplicated
404 | 1254040 | BaseTokenNotFound | AppToken not found
404 | 1254047 | RoleIdNotFound | Role not found
400 | 1254048 | MemberNotFound | Member not found
400 | 1254110 | RoleExceedLimit | Role exceed limit, limited to 30
429 | 1254290 | TooManyRequest | Request too fast, try again later
400 | 1254291 | Write conflict | The same data table does not support concurrent calls to the write interface, please check whether there is a concurrent call to the write interface. The writing interface includes: adding, modifying, and deleting records; adding, modifying, and deleting fields; modifying forms; modifying views, etc.
400 | 1254301 | OperationTypeError | Base does not have advanced permissions enabled or does not support enabling advanced permissions
403 | 1254302 | Permission denied. | No access rights, usually caused by the table opening of advanced permissions, please add a group containing applications in the advanced permissions settings and give this group read and write permissions
400 | 1255001 | InternalError | Internal error, have any questions can be consulting service
504 | 1255040 | Request timed out, please try again later | Try again
400 | 1254036 | Base is copying, please try again later. | Base copy replicating, try again later
