#### forfiles
```
/p "경로"
/s 하위폴더를 포함하여 검색
/m 검색할 단어
/d 날짜(-30 은 30일 이전까지)
/c 명령어
```

```vbs
REM------------------------------
REM-- 30일 이상 지난 파일 삭제
REM------------------------------
forfiles /p "c:\workspacd\logs" /s /m *.log /d -30 /c "cmd /c del @path"
```
