#### Pytube를 이용한 mp3다운로드


```
PyCharm, Anaconda 환경에서 실행시 

Error 발생
urllib.error.URLError: <urlopen error unknown url type: https>


Solution
From anaconda3\Library\bin copy below files and paste them in anaconda3/DLLs
-   libcrypto-1_1-x64.dll
-   libssl-1_1-x64.dll 

```
