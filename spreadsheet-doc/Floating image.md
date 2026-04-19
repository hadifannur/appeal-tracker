# Floating image user guide

## Scenarios

These APIs are used to operate on floating images in sheets.

## Image description

Spreadsheets only store image tokens. Before creating a floating image, you must upload the image to the spreadsheet (see [Upload a material](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/media/upload_all) and [Upload media in blocks-Pre­uploading](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/media/upload_prepare)). When you query or obtain images, only the token is returned. To download images, see [Download a material](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/media/download) and [Obtain a temporary material download URL](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/media/batch_get_tmp_download_url).

## Supported APIs

The token of a single image can be placed in different locations in a spreadsheet. The number of floating images with different tokens cannot exceed 4,000 in a spreadsheet. You can use the following APIs to manage floating images:

1. [Obtain a floating image](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet-float_image/get): Obtains floating image information of the specified ID.
2. [Create a floating image](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet-float_image/create): Creates a floating image based on the parameters passed in.
3. [Update a floating image](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet-float_image/patch): Updates the position and size of a floating image.
4. [Delete a floating image](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet-float_image/delete): Deletes a floating image.
5. [Query floating images](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet-float_image/query): Queries the information on all floating images in a sheet.

## Floating image parameters
### Example
![image.png](//sf3-cn.feishucdn.com/obj/open-platform-opendoc/5ba581c9134323943e6d5de6f45bc58e_tdh4ZQGMsG.png?height=438&lazyload=true&width=634)

### **float_image_id**

The unique ID of a floating image in a sub-sheet. You can specify a custom ID when creating an image, which will be verified for validity. Otherwise, a default ID is automatically generated. Valid IDs must be 10 characters long and composed of numbers (0-9) and upper and lowercase English letters.

### **float_image_token**

The token of a floating image, which is obtained through the [Upload images](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/media/upload_all)API. This field is required for creating a floating image.

### **range**

The position of the cell where the top-left corner of a floating image is located. You can only specify a single cell, such as "ahgsch!A1:A1". This field is required for creating a floating image.

### **width**

The display width of a floating image, which must be greater than or equal to 20 pixels. If this field is not specified when an image is created, the actual width of the image is used.

### **height**

The display height of a floating image, which must be greater than or equal to 20 pixels. If this field is not specified when an image is created, the actual height of the image is used.

### **offset_x**

The horizontal offset of the top-left corner of a floating image from the top-left corner of the cell where it is located, which must be greater than or equal to 0 and less than the width of the cell where the top-left corner of the floating image is located. It defaults to 0.

### **offset_y**

The vertical offset of the top-left corner of a floating image from the top-left corner of the cell where it is located, which must be greater than or equal to 0 and less than the height of the cell in the top-left corner of the floating image. It defaults to 0.

# Create a floating image
For information about the settings of a floating image, see [Floating image guide](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet-float_image/float-image-user-guide).
This API is used to create a floating image based on the parameters passed in. Float_image_token ([obtained after uploading an image to a spreadsheet](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/media/upload_all)) and range (only one cell) are required parameters. Float_image_id is optional, and a default ID is generated if this field is not specified. IDs are 10 characters long and composed of numbers (0-9) and upper and lowercase English letters. A spreadsheet cannot have duplicate images, and the total of floating images and cell images cannot exceed 4,000. The width and height specify the display width and height of an image, which are optional. If not specified, the image is displayed according to its actual width and height. offset_x and offset_y specify the offset of the image from the top-left corner of the cell where it is located. These two parameters are optional and default to 0.

## Limitation

The image size must not exceed 20 MB.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/float_images
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
float_image_id | string | No | Floating image ID<br>**Example value**: "ye06SS14ph"
float_image_token | string | No | Floating image token. This field is required for image creation, but not for updates. The token is obtained when you upload an image to a spreadsheet.<br>**Example value**: "boxbcbQsaSqIXsxxxxx1HCPJFbh"
range | string | No | The position of the cell where the top-left corner of the floating image is located. You can only specify a single cell.<br>**Example value**: "0b**12!A1:A1"
width | number(float) | No | Floating image width, which is greater than or equal to 20 px<br>**Example value**: 100
height | number(float) | No | Floating image height, which is greater than or equal to 20 px<br>**Example value**: 100
offset_x | number(float) | No | The horizontal offset of the top-left corner of a floating image from the top-left corner of the cell where it is located, which must be greater than or equal to 0 and less than the height of the cell.<br>**Example value**: 0
offset_y | number(float) | No | The vertical offset of the top-left corner of a floating image from the top-left corner of the cell where it is located, which must be greater than or equal to 0 and less than the height of the cell.<br>**Example value**: 0

### Request body example
```json
{
    "float_image_id": "ye06SS14ph",
    "float_image_token": "boxbcbQsaSqIXsxxxxx1HCPJFbh",
    "range": "0b**12!A1:A1",
    "width": 100,
    "height": 100,
    "offset_x": 0,
    "offset_y": 0
}
```

```
curl --location --request POST 'https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/shtbchuIXPxjaYxsZzQxBqxxxxx/sheets/ea131a/float_images' \
--header 'Authorization: Bearer t-f148d9ee6b5c07373a2671e795e9e855a6f171f6' \
--header 'Content-Type: application/json' \
--data-raw '{
    "float_image_id": "ye06SS14p9",
   "float_image_token": "boxbcbQEhbFAe0XJvGzkD165FGb",
    "offset_x": 0,
    "offset_y": 0,
    "range": "ea131a!C3:C3"
}'
```

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
float_image | float_image | Return value of a floating image
float_image_id | string | Floating image ID
float_image_token | string | Floating image token. This field is required for image creation, but not for updates. The token is obtained when you upload an image to a spreadsheet.
range | string | The position of the cell where the top-left corner of the floating image is located. You can only specify a single cell.
width | number(float) | Floating image width, which is greater than or equal to 20 px
height | number(float) | Floating image height, which is greater than or equal to 20 px
offset_x | number(float) | The horizontal offset of the top-left corner of a floating image from the top-left corner of the cell where it is located, which must be greater than or equal to 0 and less than the height of the cell.
offset_y | number(float) | The vertical offset of the top-left corner of a floating image from the top-left corner of the cell where it is located, which must be greater than or equal to 0 and less than the height of the cell.

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "float_image": {
            "float_image_id": "ye06SS14ph",
            "float_image_token": "boxbcbQsaSqIXsxxxxx1HCPJFbh",
            "range": "0b**12!A1:A1",
            "width": 100,
            "height": 100,
            "offset_x": 0,
            "offset_y": 0
        }
    }
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
400 | 1310229 | Wrong URL Param | Check the url parameter.
400 | 1310217 | Too Many Request | Check if requests have been sent too frequently.
400 | 1310235 | Retry Later | Please try again later.
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.
400 | 1310213 | Permission Fail | No permission
400 | 1310215 | Sheet Id Not Found | Check the sheet_id.
400 | 1310202 | Wrong Range | Invalid range
400 | 1310245 | Wrong Float Image Token | Check the floating image token.
400 | 1310244 | Exist Float Image Id | Check the floating image ID.
400 | 1310243 | Wrong Float Image Id | Check the floating image ID.
400 | 1310211 | Wrong Sheet Id | Check the sheet_id.
400 | 1310247 | Image Excess | The number of images exceeds the limit.
400 | 1310246 | Wrong Float Image Value | Incorrect image width/height or offset.
400 | 1310218 | Locked Cell | Check if the action targets a protected range.
400 | 1310226 | Excess Limit | Exceeds the limit
400 | 1310242 | In Mix state | Retey Later
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
400 | 1310249 | Spreadsheet Deleted | Restore the form and try again

# Update a floating image
For information about how to update a floating image, see [Floating image guide](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet-float_image/float-image-user-guide).
This API is used to update the position and size parameters of an existing floating image, including range, width, height, offset_x, and offset_y. This operation cannot update float_image_id or float_image_token.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/float_images/:float_image_id
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
float_image_id | string | Floating image ID<br>**Example value**: "ye06SS14ph"

### Request body

Parameter | Type | Required | Description
---|---|---|---
float_image_token | string | No | Floating image token. This field is required for image creation, but not for updates. The token is obtained when you upload an image to a spreadsheet.<br>**Example value**: "boxbcbQsaSqIXsxxxxx1HCPJFbh"
range | string | No | The position of the cell where the top-left corner of the floating image is located. You can only specify a single cell.<br>**Example value**: "0b**12!A1:A1"
width | number(float) | No | Floating image width, which is greater than or equal to 20 px<br>**Example value**: 100
height | number(float) | No | Floating image height, which is greater than or equal to 20 px<br>**Example value**: 100
offset_x | number(float) | No | The horizontal offset of the top-left corner of a floating image from the top-left corner of the cell where it is located, which must be greater than or equal to 0 and less than the height of the cell.<br>**Example value**: 0
offset_y | number(float) | No | The vertical offset of the top-left corner of a floating image from the top-left corner of the cell where it is located, which must be greater than or equal to 0 and less than the height of the cell.<br>**Example value**: 0

### Request body example
```json
{
    "float_image_token": "boxbcbQsaSqIXsxxxxx1HCPJFbh",
    "range": "0b**12!A1:A1",
    "width": 100,
    "height": 100,
    "offset_x": 0,
    "offset_y": 0
}
```

```
curl --location --request PATCH 'https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/shtbchuIXPxjaYxsZzQxBqPxxxxx/sheets/ea131a/float_images/ye06SS14pr' \
--header 'Authorization: Bearer t-384c15ba0644b82caecec91553386563c814c4b9' \
--header 'Content-Type: application/json' \
--data-raw '{
    "offset_y": 20,
    "width": 100
}'
```

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
float_image | float_image | Floating image information
float_image_id | string | Floating image ID
float_image_token | string | Floating image token. This field is required for image creation, but not for updates. The token is obtained when you upload an image to a spreadsheet.
range | string | The position of the cell where the top-left corner of the floating image is located. You can only specify a single cell.
width | number(float) | Floating image width, which is greater than or equal to 20 px
height | number(float) | Floating image height, which is greater than or equal to 20 px
offset_x | number(float) | The horizontal offset of the top-left corner of a floating image from the top-left corner of the cell where it is located, which must be greater than or equal to 0 and less than the height of the cell.
offset_y | number(float) | The vertical offset of the top-left corner of a floating image from the top-left corner of the cell where it is located, which must be greater than or equal to 0 and less than the height of the cell.

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "float_image": {
            "float_image_id": "ye06SS14ph",
            "float_image_token": "boxbcbQsaSqIXsxxxxx1HCPJFbh",
            "range": "0b**12!A1:A1",
            "width": 100,
            "height": 100,
            "offset_x": 0,
            "offset_y": 0
        }
    }
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
400 | 1310235 | Retry Later | Please try again later.
400 | 1310217 | Too Many Request | Check if requests have been sent too frequently.
400 | 1310226 | Excess Limit | Exceeds the limit
400 | 1310215 | Sheet Id Not Found | Check the sheet_id.
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.
400 | 1310218 | Locked Cell | Check if the action targets a protected range.
400 | 1310213 | Permission Fail | No permission
400 | 1310229 | Wrong URL Param | Check the url parameter.
400 | 1310202 | Wrong Range | Invalid range
400 | 1310246 | Wrong Float Image Value | Incorrect image width/height or offset.
400 | 1310243 | Wrong Float Image Id | Check the floating image ID.
400 | 1310211 | Wrong Sheet Id | Check the sheet_id.
400 | 1310242 | In Mix state | Retey Later
400 | 1310249 | Spreadsheet Deleted | Restore the form and try again

# Obtain a floating image
For information about floating images, see [Floating image guide](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet-float_image/float-image-user-guide)
This API is used to obtain floating image information based on a float_image_id.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/float_images/:float_image_id
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
float_image_id | string | Floating image ID<br>**Example value**: "ye06SS14ph"

```
curl --location --request GET 'https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/shtbchuIXPxjaYxsZzQxBqPxxxxx/sheets/ea131a/float_images/ye06SS14p' \
--header 'Authorization: Bearer t-384c15ba0644b82caecec91553386563c814c4b9' \
--header 'Content-Type: application/json'
```

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
float_image | float_image | Floating image information
float_image_id | string | Floating image ID
float_image_token | string | Floating image token. This field is required for image creation, but not for updates. The token is obtained when you upload an image to a spreadsheet.
range | string | The position of the cell where the top-left corner of the floating image is located. You can only specify a single cell.
width | number(float) | Floating image width, which is greater than or equal to 20 px
height | number(float) | Floating image height, which is greater than or equal to 20 px
offset_x | number(float) | The horizontal offset of the top-left corner of a floating image from the top-left corner of the cell where it is located, which must be greater than or equal to 0 and less than the height of the cell.
offset_y | number(float) | The vertical offset of the top-left corner of a floating image from the top-left corner of the cell where it is located, which must be greater than or equal to 0 and less than the height of the cell.

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "float_image": {
            "float_image_id": "ye06SS14ph",
            "float_image_token": "boxbcbQsaSqIXsxxxxx1HCPJFbh",
            "range": "0b**12!A1:A1",
            "width": 100,
            "height": 100,
            "offset_x": 0,
            "offset_y": 0
        }
    }
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
400 | 1310243 | Wrong Float Image Id | Check the floating image ID.
400 | 1310229 | Wrong URL Param | Check the url parameter.
400 | 1310218 | Locked Cell | Check if the action targets a protected range.
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.
400 | 1310215 | Sheet Id Not Found | Check the sheet_id.
400 | 1310217 | Too Many Request | Check if requests have been sent too frequently.
400 | 1310235 | Retry Later | Please try again later.
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
500 | 1315202 | Server Error | Internal service error. For more information, contact support.
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
400 | 1310213 | Permission Fail | No permission
400 | 1310242 | In Mix state | Retey Later
400 | 1310249 | Spreadsheet Deleted | Restore the form and try again

# Query floating images
For information about floating images, see [Floating image guide](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet-float_image/float-image-user-guide)
This API returns information on all floating images in a sheet.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/float_images/query
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
curl --location --request GET 'https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/shtbchuIXPxjaYxsZzQxBqxxxxx/sheets/ea131a/float_images/query' \
--header 'Authorization: Bearer t-384c15ba0644b82caecec91553386563c814c4b9' \
--header 'Content-Type: application/json'
```

## Response

### Response body

Parameter | Type | Description
---|---|---
code | int | Error codes, fail if not zero
msg | string | Error descriptions
data | \- | \-
items | float_image\[\] | Information on all floating images in the sheet
float_image_id | string | Floating image ID
float_image_token | string | Floating image token. This field is required for image creation, but not for updates. The token is obtained when you upload an image to a spreadsheet.
range | string | The position of the cell where the top-left corner of the floating image is located. You can only specify a single cell.
width | number(float) | Floating image width, which is greater than or equal to 20 px
height | number(float) | Floating image height, which is greater than or equal to 20 px
offset_x | number(float) | The horizontal offset of the top-left corner of a floating image from the top-left corner of the cell where it is located, which must be greater than or equal to 0 and less than the height of the cell.
offset_y | number(float) | The vertical offset of the top-left corner of a floating image from the top-left corner of the cell where it is located, which must be greater than or equal to 0 and less than the height of the cell.

### Response body example
```json
{
    "code": 0,
    "msg": "success",
    "data": {
        "items": [
            {
                "float_image_id": "ye06SS14ph",
                "float_image_token": "boxbcbQsaSqIXsxxxxx1HCPJFbh",
                "range": "0b**12!A1:A1",
                "width": 100,
                "height": 100,
                "offset_x": 0,
                "offset_y": 0
            }
        ]
    }
}
```

### Error code

HTTP status code | Error code | Description | Troubleshooting suggestions
---|---|---|---
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

# Delete a floating image

This API is used to delete the floating image with the specified float_image_id.

## Request

Facts | &nbsp;
---|---
HTTP URL | https://fsopen.bytedance.net/open-apis/sheets/v3/spreadsheets/:spreadsheet_token/sheets/:sheet_id/float_images/:float_image_id
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
float_image_id | string | Floating image ID<br>**Example value**: "ye06SS14ph"

```
curl --location --request DELETE 'https://open.feishu.cn/open-apis/sheets/v3/spreadsheets/shtbchuIXPxjaYxsZzQxBqxxxxx/sheets/ea131a/float_images/ye06SS14pr' \
--header 'Authorization: Bearer t-384c15ba0644b82caecec91553386563c814c4b9' \
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
400 | 1310243 | Wrong Float Image Id | Check the floating image ID.
400 | 1310229 | Wrong URL Param | Check the url parameter.
400 | 1310213 | Permission Fail | No permission
400 | 1310217 | Too Many Request | Check if requests have been sent too frequently.
400 | 1310214 | SpreadSheet Not Found | Check the spreadsheet token.
400 | 1310215 | Sheet Id Not Found | Check the sheet_id.
400 | 1310235 | Retry Later | Please try again later.
500 | 1315201 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952)
500 | 1315203 | Server Error | Internal service error. For more information, [contact support](https://applink.feishu.cn/client/helpdesk/open?id=6626260912531570952).
400 | 1310242 | In Mix state | Retey Later
400 | 1310249 | Spreadsheet Deleted | Restore the form and try again

