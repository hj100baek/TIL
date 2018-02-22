### autoex.vbs


```vbs
' IE오브젝트 생성
Set objIE = CreateObject("InternetExplorer.Application")

' 홈페이지 접속
objIE.Navigate "http://aaa.bbb.com/abc.jsp"
objIE.Visible = True                                            '  화면을 표시
waitIE objIE                                                    '  화면 로딩이 끝날때까지 스크립트 정지

With objIE.Document
    .title = "IE Title"
    .all("MID").Value = "mid"                                 
    .all("USER_ID").Value = "myid"                      
End With


Call objIE.Document.parentWindow.execScript("makeid();", "JavaScript") '자바스크립트 호출

WScript.Sleep 1

Call objIE.Document.parentWindow.execScript("getIt();", "JavaScript")

' IE의 화면로딩이 끝날때까지 스크립트 정지
Sub waitIE(objIE)
     Do While objIE.Busy = True Or objIE.ReadyState <> 4
          WScript.Sleep 100
     Loop
End Sub

```

cmd> cscript autoex.vbs
