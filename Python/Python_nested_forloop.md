#### Single Line nested for loop

```python
def multiplicationTable(n):
    return [[x*y for y in range(1,n+1)]for x in range(1,n+1)]
    
 # Input : 2   
 # Output
   [[1,2], 
   [2,4]]
   
 # Input : 3
 # Output:
   [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
   
 # x=1 , y=1 -> 1 
   x=1 , y=2 -> 2
   x=1 , y=3 -> 3
   
   x=2 , y=1 -> 2 
   x=2 , y=2 -> 4
   x=2 , y=3 -> 6
   
   x=3 , y=1 -> 3 
   x=3 , y=2 -> 6
   x=3 , y=3 -> 9
   
```
