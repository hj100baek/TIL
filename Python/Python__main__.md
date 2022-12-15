### __main__ — Top-level code environment
##### 2가지로 사용된다.
##### 1. __name__ == "\_\_main\_\_"  으로 running을 시작하는 첫 사용자 지정 Python module을 체크한다.
##### 2. Python module or package 이 import됬을때 .py확장자를 제외한 파일명

```python
# 파일명 : importtest.py
import configparser

print(configparser.__name__)
print(__name__)

#### 실행결과 ####
configparser
__main__
```
