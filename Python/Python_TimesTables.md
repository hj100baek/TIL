```python
def timesTables_for():
    # 9 * 9
    for i in range(1, 10):
        for j in range(1, 10):
            print(f'{i} * {j} = {i*j}')

def timesTables_recursion(x, y):
    # 9 * 9
    if x == 10:
        return 
    
    for j in range(y, 10):
        print(f'{x} * {j} = {x*j}')
    timesTables_recursion(x+1, y)


# timesTables_for()

timesTables_recursion(1, 1)
```
