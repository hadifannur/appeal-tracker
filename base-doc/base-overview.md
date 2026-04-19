# Base overview

Feishu Base is a powerful data management platform, which can help you build applications and re-organize the online data collaboration. With Feishu Base, you can transform complex data into actionable insights, build up customized applications and keep everything on tracked. Feishu Base APIs enable you to easily integrate Feishu Base with other systems and platforms, ensuring real-time updates for all your data.
## Typical cases

The open platform provides customer practice cases that integrate Base capabilities:

- [Sesame Open, building an access control management system in Feishu in five days](https://open.feishu.cn/solutions/detail/wiseasy)
- [Feishu Integration Platform, upgrading project management and sales experience in the enterprise service industry](https://open.feishu.cn/solutions/detail/cloudwise)
## Development tutorials

Explore the following Base-related tutorials to learn how to use the Base API to facilitate efficient enterprise collaboration.

- [Quickly call a server-side API (using the create Base API as an example)](https://open.larkoffice.com/document/uAjLw4CM/uMzNwEjLzcDMx4yM3ATM/call-a-server-api-base-example/introduction)
- [Quick access to Base](https://open.larkoffice.com/document/home/quick-access-to-base/preparation)
- [Agile project management with Base](https://open.larkoffice.com/document/home/agile-project-cycle-management-based-on-bitable/introduction)
## Authentication instructions
Before using the `tenant_access_token` to access Base resources, ensure your application is either an owner or collaborator of the Base; otherwise, the call will fail. You can add the app as a collaborator by adding it to the document application, as detailed in [Granting Access to Cloud Document Resources](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-add-permissions-to-app#223459af), or create a Base with the app's identity and use the `tenant_access_token` to call the API.

## Usage limitations

The Base API has the following restrictions:
- For batch operations, a maximum of 1,000 records can be processed at a time, with the response status being entirely successful or failed.
- To ensure stability, it is recommended to perform only **one** API write operation at a time on a single Base.
Resource quantity limits within a single Base are listed below:

| **Resource**             | **Maximum Limit**             |
|--------------------------|-------------------------------|
| Records                  | Varies by tenant; no extra restrictions from the platform. Refer to the Base UI for details. ![image.png](//sf3-cn.feishucdn.com/obj/open-platform-opendoc/c05d45fab4f5c8862624821d9370d2dc_1iQ0TinUhV.png?height=582&lazyload=true&width=1128) |
| Fields                   | 300, with up to 100 formula fields |
| Views                    | 200                           |
| Tables                   | 100                           |
| Custom Roles             | 30                            |
| Advanced Permission Collaborators | 200                   |

## Resource introduction

Currently, Base provides interfaces for eight resource types: Base App, Tables, Views, Records, Fields, Dashboards, Custom Roles, and Advanced Permission Collaborators. This section introduces the meaning of these resources. For more details, refer to the [Getting Started with Base](https://www.feishu.cn/hc/zh-CN/articles/697278684206-%E5%BF%AB%E9%80%9F%E4%B8%8A%E6%89%8B%E5%A4%9A%E7%BB%B4%E8%A1%A8%E6%A0%BC) guide in the Feishu Help Center.

![image.png](//sf3-cn.feishucdn.com/obj/open-platform-opendoc/80c83de730f0d48a6e2347009c6b2633_N8DO0TPC1z.png?height=719&lazyload=true&maxWidth=700&width=1280)

### Base App

A Base can be considered an application (not to be confused with developer-created apps), identified by a unique `app_token`. A Base can exist as a standalone app or be integrated as a block within documents and spreadsheets.

#### Forms of Base

| **Form**         | **Resource Definition**     | **Description**                                                                                       |
|------------------|-----------------------------|------------------------------------------------------------------------------------------------------|
| Base in a Folder | Base app                    | Stored in Feishu Cloud (cloud disk), with URL starting with **feishu.cn/base** ![Base URL](//sf3-cn.feishucdn.com/obj/open-platform-opendoc/6916f8cfac4045ba6585b90e3afdfb0a_Xc87lb1mIE.png?height=766&lazyload=true&width=3004) |
| Base in Knowledge Base | Base app and wiki node       | Located in a knowledge base, with URL starting with **feishu.cn/wiki** ![Wiki Base](//sf3-cn.feishucdn.com/obj/open-platform-opendoc/bb2e4afcd9a67d6fac88dd959efbf8f5_W8ma47dqcz.png?height=408&lazyload=true&width=1410) |
| Base Embedded in Document | Base docx block             | Inserted in a document, with URL starting with **feishu.cn/docx** ![Docx Base](//sf3-cn.feishucdn.com/obj/open-platform-opendoc/d6a6091dbd3db056d1e4126651116f00_rLR5ryVX5P.png?height=808&lazyload=true&width=1620) |
| Base Embedded in Spreadsheet | Base sheet block           | Embedded in a spreadsheet, with URL starting with **feishu.cn/sheets** ![Sheet Base](//sf3-cn.feishucdn.com/obj/open-platform-opendoc/3859f7bdf1f00878d2077175e34a09c1_O5wDuyRIFB.png?height=496&lazyload=true&width=1689) |

#### Obtaining Base `app_token`

The method for obtaining the `app_token` varies depending on the form of the Base.

##### **Base in a Folder**

The `app_token` for this form of Base is highlighted in the URL.

![Base Folder URL](//sf3-cn.feishucdn.com/obj/open-platform-opendoc/6916f8cfac4045ba6585b90e3afdfb0a_sTn7sVvhOB.png?height=766&lazyload=true&maxWidth=700&width=3004)

##### **Base in Knowledge Base**

Call the [Get Node Information](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/wiki-v2/space/get_node) API to obtain the `app_token`. For example, when the `obj_type` is `bitable`, the `obj_token` value is the `app_token`.
```json
{
    "node":{
        "space_id":"6946843325487912356",
        "node_token":"wikcnKQ1k3p******8Vabcef",
        "obj_token":"AW3Qbtr2cakCnesXzXVbbsrIcVT",
        "obj_type":"bitable"
    }
}
```

##### **Base Embedded in Document**
To obtain the app_token for a Base embedded in a document, call the Get Document Blocks API.

```json
{
  "bitable": {
    "token": "AW3Qbtr2cakCnesXzXVbbsrIcVT_tblkIYhz52o6G5nx"
  }
}
```
##### **Base Embedded in Spreadsheet**
For Bases embedded in spreadsheets, call the Get Spreadsheet Metadata API.

```json
{
  "blockInfo": {
    "blockToken": "AW3Qbtr2cakCnesXzXVbbsrIcVT_tblkIYhz52o6G5nx",
    "blockType": "BITABLE_BLOCK"
  }
}
```

### Table

The data container in a Base. Each Base has at least one data table, but it can have multiple data tables. Each data table has a unique identifier called `table_id`. The `table_id` is unique within a single Base app but not necessarily unique globally.
You can obtain the `table_id` from the Base URL; the highlighted part in the image below shows the unique identifier for the current data table. You can also use the [List Tables](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table/list) API to get the `table_id`.

![](//sf3-cn.feishucdn.com/obj/open-platform-opendoc/18741fe2a0d3cafafaf9949b263bb57d_yD1wkOrSju.png?height=746&lazyload=true&maxWidth=700&width=2976)

### View

Refers to the summary and presentation format of the data. There are various types of views, including Table View, Kanban View, Gallery View, Gantt View, and Form View. For more details, refer to the [View Types](https://www.feishu.cn/hc/zh-CN/articles/360049067931-%E4%BD%BF%E7%94%A8%E5%A4%9A%E7%BB%B4%E8%A1%A8%E6%A0%BC%E8%A7%86%E5%9B%BE#tabs0|lineguid-6kjqG) documentation in the Feishu Help Center. Each data table has at least one view and may have multiple views. Each view has a unique identifier called `view_id`, which is unique within a single Base but not necessarily unique globally.
You can obtain the `view_id` from the Base URL; the highlighted part in the image below shows the unique identifier for the current view. You can also use the [List Views](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-view/list) API to get the `view_id`. It is currently not possible to retrieve the `view_id` for embedded Bases.

![](//sf3-cn.feishucdn.com/obj/open-platform-opendoc/140668632c97e0095832219001d17c54_c76RMwZAgW.png?height=748&lazyload=true&maxWidth=700&width=2998)

#### **Form View**

Form View is a type of view in a Base, similar to a questionnaire, which can be used to collect information and data. Each form has a unique identifier called `form_id`, which corresponds to the current view's `view_id`. The method for obtaining `form_id` is the same as for `view_id`.

![](//sf3-cn.feishucdn.com/obj/open-platform-opendoc/b8d9bd2d7e1ca7d0cc955ef7f1f4fe16_zDd5TqOh3Q.png?height=942&lazyload=true&maxWidth=600&width=1327)

### Record

Each row of data in a data table is a record. Every record has a unique identifier called `record_id`, which is unique within a single Base but not necessarily unique globally. The `record_id` can be obtained using the [Search Records](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/search) API.

![](//sf3-cn.feishucdn.com/obj/open-platform-opendoc/abc84b39be159ccdcafa707ee141144d_3fcTz7mMP5.png?height=503&lazyload=true&maxWidth=700&width=1536)

### Field

Fields in a Base are equivalent to columns. Bases offer a variety of field types. Each field has a unique identifier called `field_id`, which is unique within a single Base but not necessarily unique globally. The `field_id` can be obtained using the [List Fields](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-field/list) API. For more details on fields, refer to the [Field Editing Guide](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-field/guide).

![](//sf3-cn.feishucdn.com/obj/open-platform-opendoc/6fb2359552ed15433289fbd0d9fc53c1_mGnTo91OJa.png?height=656&lazyload=true&maxWidth=700&width=1170)

### Dashboard

Dashboards are similar to data boards and can be used to analyze data in a Base from different dimensions. For more information, refer to the [Using Base Dashboards](https://www.feishu.cn/hc/zh-CN/articles/161059314076-%E4%BD%BF%E7%94%A8%E5%A4%9A%E7%BB%B4%E8%A1%A8%E6%A0%BC%E4%BB%AA%E8%A1%A8%E7%9B%98) documentation in the Feishu Help Center.

![](//sf3-cn.feishucdn.com/obj/open-platform-opendoc/fae3c8a886a0075fdeeefe5b74f274e5_WepjCfS7Hx.png?height=1490&lazyload=true&maxWidth=600&width=2794)

The unique identifier for a dashboard is called `block_id`, which starts with `blk`. You can get the `block_id` from the Base URL; the highlighted part in the image below shows the unique identifier for the current dashboard. You can also use the [List Dashboards](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-dashboard/list) API to get it.

![image.png](//sf3-cn.feishucdn.com/obj/open-platform-opendoc/a966d15323ee73c66b1e9a31d34ae6c7_x3ctncH2nO.png?height=575&lazyload=true&maxWidth=600&width=1397)

### Advanced Permissions

Advanced permissions allow users to set which users can view or edit specific rows in a data table or to specify which columns can be edited by a user. The advanced permission interfaces are divided into **Custom Roles** and **Collaborators**. The **owner** of the Base or users with **management permissions** can set advanced permissions and manage collaborators via the interface. For more details, see the [Advanced Permission Overview](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-role/advanced-permission-guide).

#### **Custom Role**

A role added in advanced permissions with set permissions is a custom role. Each custom role has a unique identifier called `role_id`. The `role_id` can be obtained using the [List Custom Roles](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-role/list) API.

#### **member**

A member of a custom role in the advanced permissions settings is a collaborator. Each collaborator has a unique identifier called `member_id`, which can be obtained using the [List Collaborators](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-role-member/list) API.
### Workflows

Automated workflows are rules set by the user for automatic operation in the Base. After setting "trigger conditions" and "execute actions," the Base will automatically execute the next step based on data changes. You can obtain the ID of automated workflows, i.e., `workflow_id`, through the [List automated workflows](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-workflow/list) interface.

### Method list

#### Base
> "Store" represents [Store apps](https://open.larkoffice.com/document/home/app-types-introduction/overview); "Custom" represents [Custom apps](https://open.larkoffice.com/document/home/app-types-introduction/overview)

**[Method (API)](https://open.larkoffice.com/document/ukTMukTMukTM/uITNz4iM1MjLyUzM)** | </md-th ><br>Permission requirements (satisfy any one) | **[Access Credentials](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)** **(choose one)** | </ md-th><br>Store | Custom
---|---|---|---|---
[Get App Info](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app/get)<br>`GET` /open-apis/bitable/v1/apps/:app_token | View, comment, and export Bitable(bitable:app:readonly)<br>View, comment, edit and manage Bitable(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**
[Update App Info](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app/update)<br>`GET` /open-apis/bitable/v1/apps/:app_token | View, comment, edit and manage Bitable(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**

#### Table

**[Method (API)](https://open.larkoffice.com/document/ukTMukTMukTM/uITNz4iM1MjLyUzM)** | </md-th ><br>Permission requirements (satisfy any one) | **[Access Credentials](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)** **(choose one)** | </ md-th><br>Store | Custom
---|---|---|---|---
[List Tables](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table/list)<br>`GET` /open-apis/bitable/v1/apps/:app_token/tables | View, comment, and export Bitable(bitable:app:readonly)<br>View, comment, edit and manage Bitable(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**
[Create Table](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table/create)<br>`POST` /open-apis/bitable/v1/apps/:app_token/tables | View, comment, edit and manage Bitable(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**
[Create Tables](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table/batch_create)<br>`POST` /open-apis/bitable/v1/apps/:app_token/tables/batch_create | View, comment, edit and manage Bitable(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**
[Delete Table](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table/delete)<br>`DELETE` /open-apis/bitable/v1/apps/:app_token/tables/:table_id | View, comment, edit and manage Bitable(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**
[Delete Tables](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table/batch_delete)<br>`POST` /open-apis/bitable/v1/apps/:app_token/tables/batch_delete | View, comment, edit and manage Bitable(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**

#### View

**[Method (API)](https://open.larkoffice.com/document/ukTMukTMukTM/uITNz4iM1MjLyUzM)** | </md-th ><br>Permission requirements (satisfy any one) | **[Access Credentials](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)** **(choose one)** | </ md-th><br>Store | Custom
---|---|---|---|---
[List Views](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-view/list)<br>`GET` /open-apis/bitable/v1/apps/:app_token/tables/:table_id/views | View, comment, and export Bitable(bitable:app:readonly)<br>View, comment, edit and manage Bitable(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**
[Create View](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-view/create)<br>`POST` /open-apis/bitable/v1/apps/:app_token/tables/:table_id/views | View, comment, edit and manage Bitable(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**
[Delete View](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-view/delete)<br>`DELETE` /open-apis/bitable/v1/apps/:app_token/tables/:table_id/views/:view_id | View, comment, edit and manage Bitable(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**

#### Record

**[Method (API)](https://open.larkoffice.com/document/ukTMukTMukTM/uITNz4iM1MjLyUzM)** | </md-th ><br>Permission requirements (satisfy any one) | **[Access Credentials](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)** **(choose one)** | </ md-th><br>Store | Custom
---|---|---|---|---
[List records](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/list)<br>`GET` /open-apis/bitable/v1/apps/:app_token/tables/:table_id/records | View, comment, and export Bitable(bitable:app:readonly)<br>View, comment, edit and manage Bitable(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**
[Get Record](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/get)<br>`GET` /open-apis/bitable/v1/apps/:app_token/tables/:table_id/records/:record_id | View, comment, and export Bitable(bitable:app:readonly)<br>View, comment, edit and manage Bitable(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**
[Create record](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/create)<br>`POST` /open-apis/bitable/v1/apps/:app_token/tables/:table_id/records | View, comment, edit and manage Bitable(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**
[Create Records](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/batch_create)<br>`POST` /open-apis/bitable/v1/apps/:app_token/tables/:table_id/records/batch_create | View, comment, edit and manage Bitable(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**
[Update Record](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/update)<br>`PUT` /open-apis/bitable/v1/apps/:app_token/tables/:table_id/records/:record_id | View, comment, edit and manage Bitable(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**
[Update Records](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/batch_update)<br>`POST` /open-apis/bitable/v1/apps/:app_token/tables/:table_id/records/batch_update | View, comment, edit and manage Bitable(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**
[Delete Record](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/delete)<br>`DELETE` /open-apis/bitable/v1/apps/:app_token/tables/:table_id/records/:record_id | View, comment, edit and manage Bitable(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**
[Delete Records](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-record/batch_delete)<br>`POST` /open-apis/bitable/v1/apps/:app_token/tables/:table_id/records/batch_delete | View, comment, edit and manage Bitable(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**

#### Field

**[Method (API)](https://open.larkoffice.com/document/ukTMukTMukTM/uITNz4iM1MjLyUzM)** | </md-th ><br>Permission requirements (satisfy any one) | **[Access Credentials](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM)** **(choose one)** | </ md-th><br>Store | Custom
---|---|---|---|---
[List Fields](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-field/list)<br>`GET` /open-apis/bitable/v1/apps/:app_token/tables/:table_id/fields | View, comment, and export Bitable(bitable:app:readonly)<br>View, comment, edit and manage Bitable(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**
[Create Field](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-field/create)<br>`POST` /open-apis/bitable/v1/apps/:app_token/tables/:table_id/fields | View, comment, edit and manage Bitable(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**
[Update Field](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-field/update)<br>`PUT` /open-apis/bitable/v1/apps/:app_token/tables/:table_id/fields/:field_id | View, comment, edit and manage Bitable(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**
[Delete Field](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-table-field/delete)<br>`DELETE` /open-apis/bitable/v1/apps/:app_token/tables/:table_id/fields/:field_id | View, comment, edit and manage Bitable(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**

#### Role

**[Method (API)](https://open.larkoffice.com/document/ukTMukTMukTM/uITNz4iM1MjLyUzM)** | Permission requirements (meet either) | **[Access Credentials](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM) (choose one)** | Store | Custom
---|---|---|---|---
[List Roles](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-role/list)<br>`GET` /open-apis/bitable/v1/apps/:app_token/roles | View, comment, edit and manage Bitable(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**
[Add Role](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-role/create)<br>`POST` /open-apis/bitable/v1/apps/:app_token/roles/:role_id | View, comment, edit and manage Bitable(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**
[Update Role](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-role/update)<br>`PUT` /open-apis/bitable/v1/apps/:app_token/roles/:role_id | View, comment, edit and manage Bitable(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**
[Delete Role](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-role/delete)<br>`DELETE` /open-apis/bitable/v1/apps/:app_token/roles/:role_id | View, comment, edit and manage Bitable(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**

#### Member

**[Method (API)](https://open.larkoffice.com/document/ukTMukTMukTM/uITNz4iM1MjLyUzM)** | Permission requirements (meet either) | **[Access Credentials](https://open.larkoffice.com/document/ukTMukTMukTM/uMTNz4yM1MjLzUzM) (choose one)** | Store | Custom
---|---|---|---|---
[List Members](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-role-member/list)<br>`GET` /open-apis/bitable/v1/apps/:app_token/roles/:role_id/members | View, comment, edit and manage Bitable(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**
[Add Member](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-role-member/create)<br>`POST` /open-apis/bitable/v1/apps/:app_token/roles/:role_id/members | View, comment, edit and manage Bitable(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**
[Delete Member](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/bitable-v1/app-role-member/delete)<br>`DELETE` /open-apis/bitable/v1/apps/:app_token/roles/:role_id/members/:member_id | View, comment, edit and manage Bitable(bitable:app) | `tenant_access_token`<br>`user_access_token` | **✓** | **✓**
