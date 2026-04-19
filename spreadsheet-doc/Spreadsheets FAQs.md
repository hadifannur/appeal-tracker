# Spreadsheets FAQs

## 1. How to obtain the spreadsheet token?

Each spreadsheet has a unique identifier called `spreadsheetToken`. You can obtain the `spreadsheetToken` in one of the following ways:<br>- From the spreadsheet URL: `https://sample.feishu.cn/sheets/==Iow7sNNEphp3WbtnbCscPqabcef==`<br>- By calling the [List Files in a Folder](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/file/list) API.warning<br>For spreadsheets stored in the Knowledge Base, you need to call the [Get Knowledge Space Node Info](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/wiki-v2/space/get_node) API to obtain the spreadsheet's `obj_token`. In this case, the `obj_token` also serves as the spreadsheet's `spreadsheetToken`.
---

## 2. What are the limitations of spreadsheets?

The following limitations apply to spreadsheets:<br>- The number of sheets in a single spreadsheet cannot exceed 300.<br>- The number of columns in a single sheet cannot exceed 13,000 (including empty columns).<br>- The number of cells in a single sheet cannot exceed 2,000,000 (including empty cells).<br>- The number of characters in a single cell cannot exceed 45,000.<br>- The number of spreadsheets in a single document cannot exceed 1,500.
---

## 3. How to grant an app access to a spreadsheet?

To grant access, add the app as a collaborator to the spreadsheet. For details, refer to Question 3 in [Cloud Documents FAQs](https://open.larkoffice.com/document/ukTMukTMukTM/uczNzUjL3czM14yN3MTN#78a03ee2), which explains how to add an app as a collaborator to a spreadsheet and grant it read access.
---

## 4. How to resolve "no folder permission" when creating a spreadsheet?

This error indicates that the calling identity does not have permission to create cloud documents in the specified folder. For details, refer to [How to Add Permissions to an App for Cloud Document Resources](https://open.larkoffice.com/document/uAjLw4CM/ugTN1YjL4UTN24CO1UjN/trouble-shooting/how-to-add-permissions-to-app) to add the user or app as a collaborator to the specified folder and grant it editing permissions.
---

## 5. Why are some spreadsheet APIs unavailable in the API debugging tool?

This occurs because these APIs are version 2 (v2) APIs, and currently, the API debugging tool only supports version 3 (v3) APIs.<br>**Note**: A version 2 API is identified by the `v2` marker in the HTTP URL of the API. For example, the URL for the [Add Rows and Columns](https://open.larkoffice.com/document/ukTMukTMukTM/uUjMzUjL1IzM14SNyMTN) API, `/sheets/v2/spreadsheets/:spreadsheet_token/dimension_range`, contains `v2`, indicating it is a version 2 API.
---

## 6. Why doesn't the worksheet title update after calling [Update Worksheet Properties](https://open.larkoffice.com/document/ukTMukTMukTM/ugjMzUjL4IzM14COyMTN)?

The updated title must meet the following rules:<br>- The length cannot exceed 100 characters.<br>- It must not contain the following special characters: `/ \ ? * [ ] :`
---

## 7. How to insert colored data into a spreadsheet?
Call the [Insert Data](https://open.larkoffice.com/document/ukTMukTMukTM/uIjMzUjLyIzM14iMyMTN) API and refer to the following request body example to set colors and other text styles for partial content in a cell. For more text styling options, see [Partial Styling](https://open.larkoffice.com/document/ukTMukTMukTM/ugjN1UjL4YTN14CO2UTN#e5f8fe55).

## 8. How to retrieve and download images from a spreadsheet?

1. **Determine the Image Type**:  
   Identify whether the image is a cell-embedded image or a floating image:  
   - **Cell-embedded images** are inserted into a specific cell.  
   - **Floating images** hover over the worksheet.

2. **Call APIs to Get the Unique Image Identifier**:  
   - For **floating images**, call the [Get Floating Image](https://open.larkoffice.com/document/ukTMukTMukTM/uUDN04SN0QjL1QDN/sheets-v3/spreadsheet-sheet-float_image/get) API to retrieve the `float_image_token`.  
   - For **cell-embedded images**, call the [Read a Single Range](https://open.larkoffice.com/document/ukTMukTMukTM/ugTMzUjL4EzM14COxMTN) or [Read Multiple Ranges](https://open.larkoffice.com/document/ukTMukTMukTM/ukTMzUjL5EzM14SOxMTN) API to obtain the `fileToken`. Below is an example of the request:  

```bash
   curl --location --request GET 'https://open.feishu.cn/open-apis/sheets/v2/spreadsheets/XUMasQlMYhOnMbt5htXc96abcef/values/2jm6f6!B1:B1' \
   --header 'Authorization: Bearer t-ce3540c5f02ac074535f1f14d64fa90fa49621c0'
   ```

If the request is successful, the response might look like this:  

```json
   {
       "code": 0,
       "data": {
           "revision": 112,
           "spreadsheetToken": "XUMasQlMYhOnMbt5htXc96abcef",
           "valueRange": {
               "majorDimension": "ROWS",
               "range": "2jm6f6!B1:B1",
               "revision": 112,
               "values": [
                   [
                       {
                           "fileToken": "UeZNbAxAIojSuRxarT1ccsabcef",
                           "height": 1994,
                           "link": "https://internal-api-drive-stream.feishu.cn/space/api/box/stream/download/v2/cover/UeZNbAxAIojSuRxarT1ccsabcef/?height=1280&mount_node_token=Iow7sNNEphp3WbtnbCscPqQPnTd&mount_point=sheet_image&policy=equal&width=1280",
                           "text": "",
                           "type": "embed-image",
                           "width": 3278
                       }
                   ]
               ]
           }
       },
       "msg": "success"
   }
   ```

3. **Download the Image**:  
   Based on the `fileToken` (for cell-embedded images) or `float_image_token` (for floating images), call the [Download Media](https://open.larkoffice.com/document/uAjLw4CM/ukTMukTMukTM/reference/drive-v1/media/download) API to download the image.

---

## 9. How to Write Dates into a Spreadsheet?

1. **Set the Cell Format to Date**:  
   Use the [Set Cell Style](https://open.larkoffice.com/document/ukTMukTMukTM/ukjMzUjL5IzM14SOyMTN) API to format the cell as a date. Below is an example of the request body:  

```json
   {
       "appendStyle": {
           "range": "vJFUIq!A1:A10",
           "style": {
               "formatter": "yyyy/MM/dd"
           }
       }
   }
   ```

2. **Write Floating-Point Data to the Cell**:  
   Use the [Write Data to a Single Range](https://open.larkoffice.com/document/ukTMukTMukTM/uAjMzUjLwIzM14CMyMTN) API to input floating-point data. Below is an example of the request body:  

```json
   {
       "valueRanges": [
           {
               "range": "vJFUIq!A1:A10",
               "values": [
                   [
                       0
                   ],
                   [
                       1
                   ],
                   [
                       2
                   ],
                   [
                       42101
                   ]
               ]
           }
       ]
   }
   ```

The integer part represents the number of days since December 30, 1899, and the decimal part represents the fraction of the day (in 24 hours). After writing the data, the dates will appear as shown below:  

![image.png](//sf3-cn.feishucdn.com/obj/open-platform-opendoc/c598f964ca602b69dd3ed11bdfb40885_dZM5cD74rz.png?height=442&lazyload=true&maxWidth=200&width=219)
