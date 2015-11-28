
"""
Spreadsheet with some definitions:
|   |       A        |     B    |  C  |
| 1 | 4/5/2014 13:34 | Apples   |  73 |
| 2 |  4/5/2014 3:41 | Cherries |  85 |
| 3 | 4/6/2014 12:46 | Pears    |  14 |
| 4 |  4/8/2014 2:07 | Apples   | 152 |

"""
# Install openpyxl: pip install openpyxl
# code:
>>> import openpyxl
>>> import os
>>> os.chdir('c:\\users\\all\\documents') # file located in folder "documents"
>>> 
>>> 
>>> workbook = openpyxl.load_workbook('example.xlsx')
>>> type(workbook)
<class 'openpyxl.workbook.workbook.Workbook'>
>>> sheet = workbook.get_sheet_by_name('Sheet1')
>>> type(sheet)
<class 'openpyxl.worksheet.worksheet.Worksheet'>
>>> workbook.get_sheet_names()
['Sheet1', 'Sheet2', 'Sheet3']
>>> sheet['A1']
<Cell Sheet1.A1>
>>> cell = sheet['A1']
>>> cell.value
datetime.datetime(2014, 4, 5, 13, 34, 2)
>>> str(cell.value)
'2014-04-05 13:34:02'
>>> str(sheet['A1'].value)
'2014-04-05 13:34:02'
>>> sheet['B1'].value
'Apples'
>>>  sheet['C1'].value
73
>>> str(sheet['C1'].value)
'73'
>>> sheet.cell(row=1, column=2)
<Cell Sheet1.B1>
>>> for i in range(1, 5):
    print(i, sheet.cell(row=i, column=2).value)
    
1 Apples
2 Cherries
3 Pears
4 Apples



"""
To recap:
- The OpenPyXL third-party module handles  Excel spreadsheets (.xlsx files)
- openpyxl.load_workbook(filename) return a Workbook object
- get_sheet_names() and get_sheet_by_name() help get Worksheet objects
- The square brackets in sheet["A1"] get Cell objects
- Cell objects have a value member variable with the content of that cell
- The cell() method also return a Cell object from a sheet
"""
