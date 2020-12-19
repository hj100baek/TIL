```
' Copy Source 파일이 동일 폴더에 있을 경우 
' ID_LIST.txt : 바꿀 파일명 목록

Set fso = CreateObject("Scripting.FileSystemObject")  'source 파일용
curDir = fso.GetAbsolutePathName(".")

c_source = curDir & "TEST_001.xlsx"
c_target = curDir & "UT_"

CONST ForReading = 1
strTextFile = curDir & "\ID_LIST.txt"     
Set objFSO = CreateObject("Scripting.FileSystemObject") '파일명목록용
strData = objFSO.OpenTextFile(strTextFile,ForReading).ReadAll
arrLines = Split(strData,vbCrLf)

For Each strLine in arrLines
 c_target1 = c_target & strLine & "NAME_v1.0.xlsx"
 
 Call fso.CopyFile(c_source, c_target1)
Next

```
