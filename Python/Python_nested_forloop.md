#### Single Line nested for loop

```python
def multiplicationTable(n):
    return [[x*y for y in range(1,n+1)]for x in range(1,n+1)]
    
 # Input : 2   
 # Output
   [[1,2], 
   [2,4]]
```
