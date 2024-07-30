---
title: vba
order: 8
toc: content
nav:
  title: 项目记录
  order: 7
group: 
  title: 项目记录
  order: 3
---
# 项目路径

D:\w\excel-vba
D:\w\almfirst-lmm-vba
D:\w\almfirst-psa-vba
# 语法

## 忽略logs文件夹下的所有文件
- logs/*
- 除去忽略error.log和debug.log
!logs/error.log
!logs/debug.log
## **多尝试变量类型**
- Collection
- Object
- Worksheet

## **GET,POST,PUT 接口请求的封装**

## **定义数组，数组的动态创建**

``` vb
    Dim myArray() As String
    ReDim myArray(1 To 13)
    
    myArray(1) = ActiveSheet.Range("F" & p)
    myArray(2) = ActiveSheet.Range("G" & p)
    myArray(3) = ActiveSheet.Range("H" & p)
    myArray(4) = ActiveSheet.Range("I" & p)
    myArray(5) = ActiveSheet.Range("J" & p)
    myArray(6) = ActiveSheet.Range("K" & p)
    myArray(7) = ActiveSheet.Range("L" & p)
    myArray(8) = ActiveSheet.Range("M" & p)
    myArray(9) = ActiveSheet.Range("N" & p)
    myArray(10) = ActiveSheet.Range("O" & p)
    myArray(11) = ActiveSheet.Range("P" & p)
    myArray(12) = ActiveSheet.Range("Q" & p)
    myArray(13) = ActiveSheet.Range("R" & p)

```

## 接口数据 String 转json
``` vb
    Dim dictionarysJsonData As Object
    Set dictionarysJsonData = WebHelpers.ParseJson(dictionarysData)

    Debug.Print ("BalanceSheet: " & dictionarysJsonData.Count)
    Debug.Print ("BalanceSheet accounts: " & dictionarysJsonData("accounts").Count)
```

## 循环
``` vb
For i = 1 To children.Count

Next i

```

## If 语句
``` vb
    If hasGrowthActionID Then

    ElseIf hierarchy = "Hierarchy 1" Then   

    ElseIf hierarchy = "Hierarchy 1" Then   

    Else

    End If
```

## 字符串拼接
- 也可以试试 +
- `& institutionsSelected & "/as-of-dates/" & asofdatesValue & "/forecast-scenarios"`

## 全局变量
`Public hasBalanceData As Boolean`

## 字符串转数组
``` vb
        Dim j As Integer
        Dim stringArray() As String
        stringArray = Split("AL_Side,H1,H2,H3,AcctID,", ",")
        For j = LBound(stringArray) To UBound(stringArray)
            If sheetName <> stringArray(j) Then
                Sheets(stringArray(j)).Range(position).value = val
            End If
        Next j

```

## VBA对象转json
`WebHelpers.ConvertToJson(params)`

## 创建对象去接口传参
``` vb
     Dim affectedAccount As Object
     Set affectedAccount = CreateObject("Scripting.Dictionary")
     affectedAccount.add "id", Action_id
     affectedAccount.add "currentBalance", Action_currentBalance
     affectedAccount.add "preForecastMonths", Action_months
     
     
     Dim jsonObject As Object
     Set jsonObject = CreateObject("Scripting.Dictionary")
     jsonObject.add "description", "Growth Description"
     jsonObject.add "affectedAccount", affectedAccount
     jsonObject.add "forecastMonths", myArray
     jsonObject.add "id", Action_id
```

## 判断是不是对象
``` vb
    Dim hasGrowthActionID As Boolean
    hasGrowthActionID = IsObject(children(i)("growthAction"))
```
## sub 参数可选

``` vb
'reload 参数可传可不传
Sub InitScenariosSelectData(Optional ByVal reload As Boolean = True)

end Sub
```

## 错误处理 On Error Resume Next
``` vb
                Dim btn As Button
                On Error Resume Next
                For i = 7 To 100
                    Set btn = Sheeted.Buttons("A" & i)
                    
                    'If Not IsError(btn) Then
                    '    Debug.Print "IsError"
                    '    If Not btn Is Nothing Then
                    '        btn.Delete
                    '    End If
                    'End If
                    
                    If Err.Number <> 0 Then
                        '  Err.Clear
                        Err.Clear
                        '
                    Else
                        '
                        btn.Delete
                    End If
                 Next i
                On Error GoTo 0

```

## 给数组添加字典元素 **Set arr_AL_Side(arr_AL_Side_num) = children(i)**
``` vb
                Public arr_AL_Side() As Dictionary
                ReDim Preserve arr_AL_Side(1 To arr_AL_Side_num)   '设置数组元素个数
                Set arr_AL_Side(arr_AL_Side_num) = children(i)
                arr_AL_Side_num = arr_AL_Side_num + 1

```

``` vb
        Dim arr() As Integer
        ReDim arr(1 To 3) '初始化数组为3个元素
        arr(1) = 1
        arr(2) = 2
        arr(3) = 3
        ReDim Preserve arr(1 To 4) '添加一个新元素
        arr(4) = 4
```

## 定义函数的参数是数组
``` vb
Function SumArray(arr() As Variant) As Double
   
End Function


## 判断字符串是否包含某个指定字符串
``` vb
        Dim position As Integer
        position = InStr("scenarios AL_Side", "scenarios")
        '  "scenarios AL_Side" 字符串包含 "scenarios" 字符串
        If position > 0 Then
            
        End If
```

## 从第3行开始，每隔7行对第3列（C列）的单元格加粗，直到第100行
``` vb
   For j = 3 To 100 Step 7 ' Step 7 确保每隔7行执行一次
        ws.Cells(j, 3).Font.Bold = True ' 对第j行的第三列（C列）加粗
    Next j
```

# Excel操作

## InsertData 一次性插入数据
## GrowthAction.bas 
- **创建按钮并绑定宏 PlaceButtonInA1**
- **删除按钮 DeleteButton**

## **Worksheet_Change 事件**
## 开启自动计算
``` vb
    Sub SetCalculationToAutomatic()
        Application.Calculation = xlCalculationAutomatic
    End Sub
```

## 获取工作表
``` vb
    Dim AL_SideSheet As Worksheet
    Set AL_SideSheet = ThisWorkbook.Sheets("AL_Side")
```

``` vb
    Dim AL_SideSheet As Worksheet
    Set AL_SideSheet = Sheets("AL_Side")
```

## 激活工作表
`'Sheets("API").Activate`

## 设置单元格内容

``` vb
sheet.Range("B10").value = "Login Successfully"
sheet.Cells(rowIndex, 20).value = "Login Successfully"
```
## 清空单元格
- ClearContents只清除值，即单元格中的数字文本或输入单元格中的任何内容，其它的东西都将被保留
`Sheets("API").Range("D2").ClearContents`
`Sheets("API").Range("D2:D100").ClearContents`

## 阻止屏幕刷新
`Application.ScreenUpdating = False`

## 阻止操作
`Application.Interactive = False`

## ActiveSheet 当前活动工作表

## 延迟两秒执行
``` vb
    Application.Wait Now() + CDate("00:00:02")
    TipsForm.Hide
```
## 工作表名称
`Sheets("API").Name`
`ActiveSheet.Name`

## 获取某列最大的行数
``` vb
Dim LastRow As Long
LastRow = Sheets("API").Cells(Sheets("API").Rows.Count, "I").End(xlUp).row
```

## 获取按钮显示的文字
``` vb
    Set btn = ActiveSheet.Buttons("A" & rowNum)
    Debug.Print btn.Caption
```

## 设置按钮文字颜色
``` vb

                    Dim btn As Button
                    On Error Resume Next
                    Set btn = Sheeted.Buttons("A" & i)
                    If Not btn Is Nothing Then
                         With btn.Font
                                .Color = RGB(0, 0, 0)
                                .Bold = False
                         End With
                         
                         If (btn.Caption = Caption) Then
                             With btn.Font
                                .Color = RGB(255, 0, 0)
                                .Bold = True
                             End With
                         End If
                    End If
```

## 激活工作表事件
``` vb
Private Sub Worksheet_Activate()
If hasSummaryData Then
    Debug.Print ("yes hasSummaryData")
Else
    InitSummarySheet
    Debug.Print ("no hasSummaryData")
End If
End Sub
```

## 获取某行的列数
``` vb
    Dim colCount As Long
    ' 第三行的列数
    colCount = objSheet.Cells(3, objSheet.Columns.Count).End(xlToLeft).Column
    Debug.Print colCount
```

## 获取某列的行数
``` vb
    Dim rowCount As Long
     ' 第三列的行数
    rowCount = objSheet.Cells(objSheet.Rows.Count, 3).End(xlUp).row '
    Debug.Print (rowCount & "JJJJJJJJJJJ")
```

## 用excel VBA批量修改工作表保存后弹出“图片太大，超过部分将被截去”怎么办？

``` vb
' Workbook_BeforeSave 保存之前的事件
Private Sub Workbook_BeforeSave(ByVal SaveAsUI As Boolean, Cancel As Boolean)
   Sheets("Login").Cells(1, 1).Copy
End Sub
```

## 新增工作表
``` vb
        Dim AL_Side As Object
        Set AL_Side = ThisWorkbook.Sheets.add
        ' 设置表名
        AL_Side.name = scenariosName & " AL_Side scenarios"
```

## 阻止允许弹窗提示
``` vb
    Application.DisplayAlerts = False
    ''''''
    
    '''''
    Application.DisplayAlerts = True
```
`

## 删除工作表，隐藏的工作表删除前必须显示
``` vb
      Sheets(sheetName).Visible = xlSheetVisible
      Sheets(sheetName).Delete
```

## 隐藏和显示工作表
``` vb
  Sheets(sheetName).Visible = xlSheetVeryHidden
  Sheets(sheetName).Visible = xlSheetVisible
```

## 输出时间到毫秒
``` vb
    Sub PrintTime()
    Debug.Print Application.Text(Now(), "yyyy/mm/dd hh:mm:ss:") & Application.Text((Timer - Int(Timer)) * 1000, "000")
    End Sub
```

## 循环所有的工作表
``` vb
     For Each Sheet In ThisWorkbook.Sheets
               If InStr(Sheet.name, "verify") > 0 Then
                    Sheet.Visible = xlSheetVisible
                    Sheet.Delete
               End If
     Next Sheet
```

## 复制单元区域到到指定区域
``` vb
    Dim rowCount As Long
    Dim sourceRange As Range
    ' 复制 sourceSheet 工作表的b3后面所有的区域到 AL_Side 工作表的B3单元格
    With Sheets("sourceSheet")
        rowCount = .Cells(.Rows.Count, 2).End(xlUp).row
        Set sourceRange = .Range("B3:R" & rowCount)
        
        Set destinationCe = Sheets("AL_Side").Range("B3")
        ' 会复制单元格格式，也会复制按钮
        'sourceRange.Copy Destination:=destinationCe
        ' 只复制值，但不包括按钮
        destinationCe.value = sourceRange.value
        ' 单独复制按钮
        .Range("F3:F" & rowCount).Copy Destination:=Sheets("AL_Side").Range("F3:F" & rowCount)
    End With
```
## 修改单元格背景颜色
``` vb
 Sheets("H1").Range("A1:B3").Interior.Color = RGB(0, 0, 255) 
 Sheets("H1").Range("A1").Interior.Color = RGB(0, 0, 255) 
```
## 动态改变下拉框的数据
``` vb
Sub SetDropdownList(col)
    Dim ws As Worksheet
    Dim dataList As Variant
    
    
    Set ws = Sheets("Login")
    
    Dim oneDimArray() As Variant
    ReDim oneDimArray(1 To 20)
    Dim i As Integer
    For i = 2 To 20
        oneDimArray(i) = Sheets("API").Cells(i, col).Value
    Next i
    
   
    With ws.Range("B5").Validation
        .Delete
        .Add Type:=xlValidateList, AlertStyle:=xlValidAlertStop, Operator:= _
        xlBetween, Formula1:=Join(oneDimArray, ",")
        .IgnoreBlank = True
        .InCellDropdown = True
        .ShowInput = True
        .ShowError = False
    End With
End Sub
```
# 窗体操作

## 窗体控件出现
- vbModeless时，表示启动无模式的用户窗体，窗体启动后还可以操作窗体以外的其它内容。
如果不指定参数或者指定参数为vbModal则表示启动有模式的用户窗体，窗体启动后无法操作窗体以外的所有其它内容。
`UserForm1.Show vbModeless`
## 窗体控件关闭
`UserForm1.Hide`

## 窗体下拉框控件数据清除
`UserForm1.ComboBox1.Clear`

## 窗体下拉框控件数据添加
`UserForm1.ComboBox1.AddItem 123`

## 获取窗体控件下拉框的值
``` vb
    Dim selectedValue As String
    selectedValue = UserForm1.ComboBox1.value
```

## 获取窗体控件输入框的值
``` vb
    Dim TextValue As String
    TextValue = UserForm1.TextBox1.value
```

## 设置某个窗体控件的值
`UserForm1.ComboBox1.value = dictionarysJsonData(1)("name")`

## 窗体控件的字体大小
```vb
    With UserForm1
        .Label1.Font.Size = 14
        .ComboBox1.Font.Size = 14
        
        .Label2.Font.Size = 14
        .TextBox1.Font.Size = 14
        
        .CommandButton1.Font.Size = 14
    
    End With
```




