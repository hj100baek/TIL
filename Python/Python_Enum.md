### class enum.Enum
열거형 상수를 만들기 위한 베이스 클래스.

```python
from enum import Enum

class Color(Enum):
...     RED = 1
...     GREEN = 2
...     BLUE = 3

print(Color.RED)
Color.RED

print(repr(Color.RED))
<Color.RED: 1>

# 함수형 API
Animal = Enum('Animal', 'ANT BEE CAT DOG')
Animal.ANT
<Animal.ANT: 1>
```
