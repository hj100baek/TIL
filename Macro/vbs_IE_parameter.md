cscript autoex.vbs "http://123.123.123.123"     'parameter

```
'autoex.vbs

surl = "http://aaa.bbb.com"
Set args = Wscript.Arguments


Set shapp = CreateObject("Shell.Application")

For Each owin In shapp.Windows
  if InStr(owin.LocationURL,surl) > 0 then
         Set objIE = owin
   end if

Next

 objIE.Navigate2 surl
 objIE.Visible = True                                            '  화면을 표시
 waitIE objIE

With objIE.Document.Frames("body").Document
    .all("id").Value = "myid"                                 
    .all("testtype").Value = args.item(0)                              'parameter
    .all("btn").Click                                                  
End With





' IE의 화면로딩이 끝날때까지 스크립트 정지
Sub waitIE(objIE)
     Do While objIE.Busy = True Or objIE.ReadyState <> 4
          WScript.Sleep 100
     Loop
End Sub
```
