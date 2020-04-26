### * pip 
```
error:
Retrying (Retry(total=4, connect=None, read=None, redirect=None, status=None))
after connection broken by 'SSLError(SSLError(1, '[SSL: CERTIFICATE_VERIFY_FAIL
ED] certificate verify failed (_ssl.c:777)'),)': /simple/jupyter/
```
```
solution: 
pip install --trusted-host pypi.python.org jupyter
```

```
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org openpyx
pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org openpyx
```

```
PyCharm, Anaconda 설치 된 상태에서 SSLError 발생한다면
환경변수에 bin경로 추가 후 cmd창 다시 열어 시도

C:\python\anaconda\Library\bin

```
