
### Python은 한 파일내에 여러 클래스를 정의할 수 있다. multiple classes in a file.

```python
ex) a.py

class Node:
    def __init__(self, key):  #__init__()는 새로 생성된 클래스 인스턴스를 위해 클래스 초기화시 자동 호출됨
      self.key = key
 
 
 
 class ChainedHash:
     def __init(self, capacity):
        self.capacity = capacity
    
```

### Python 상속
```python
class Node:

    class Empty(Exception):   #Exception을 상속
        pass
```
