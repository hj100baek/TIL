C:\python3>python -m venv myvenv

C:\python3>myvenv\Scripts\activate
(myvenv) C:\python3>pip install --upgrade pip
Could not fetch URL https://pypi.python.org/simple/pip/: There was a problem con
firming the ssl certificate: [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify
 failed (_ssl.c:748) - skipping
Requirement already up-to-date: pip in c:\python3\myvenv\lib\site-packages


(myvenv) C:\python3>pip install --trusted-host pypi.python.org --upgrade pip

(myvenv) C:\python3>pip install --trusted-host pypi.python.org django~=1.11.0

