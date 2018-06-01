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
