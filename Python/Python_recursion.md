```python
### 탐색 대상은 고정이고 재귀 깊이만 변경될 경우
### 탐색 item별로 재귀깊이만큼 반복

def rec(nums, rcnt):
    if rcnt == 0 : return
    for item in nums:
        print(' ' * rcnt + '*' * item + ' rcnt:'+ str(rcnt) + ' item:'+ str(item) )
        print(nums)
        rec(nums, rcnt-1)




rec([1,2],1)  

#### result
* rcnt:1 item:1
[1, 2]
 ** rcnt:1 item:2
[1, 2]

rec([1,2],2)  

#### result

* rcnt:2 item:1
[1, 2]
 * rcnt:1 item:1
[1, 2]
** rcnt:1 item:2
[1, 2]
  ** rcnt:2 item:2
[1, 2]
 * rcnt:1 item:1
[1, 2]
 ** rcnt:1 item:2
[1, 2]

```
