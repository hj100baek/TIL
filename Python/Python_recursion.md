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


rec([1,2],3)   

## result

* rcnt:3 item:1
  * rcnt:2 item:1
 * rcnt:1 item:1
 ** rcnt:1 item:2
  ** rcnt:2 item:2
 * rcnt:1 item:1
** rcnt:1 item:2
   ** rcnt:3 item:2
  * rcnt:2 item:1
 * rcnt:1 item:1
 ** rcnt:1 item:2
  ** rcnt:2 item:2
 * rcnt:1 item:1
 ** rcnt:1 item:2

```
![rec2](https://user-images.githubusercontent.com/7253111/161381746-56382d9d-9a7e-436a-a176-83e002d95074.png) 
```

```python
### 각 열에 퀸 1개 배치
pos = ['*'] * 3

def put() -> None:
    for i in range(3):
        print(f'{pos[i]:2}', end='')
    print()

def set(i: int)-> None:
   
    """i열에 퀸 배치"""
    for j in range(3):
        pos[i] = j
       
        if i == 2:
            put()
        else:
            print(f'call set({i}+1)')
            set(i+1)  #다음 열에 퀸을 배치
    
set(0)     


## result
call set(0+1)
call set(1+1)
 0 0 0
 0 0 1
 0 0 2
call set(1+1)
 0 1 0
 0 1 1
 0 1 2
call set(1+1)
 0 2 0
 0 2 1
 0 2 2
call set(0+1)
call set(1+1)
 1 0 0
 1 0 1
 1 0 2
call set(1+1)
 1 1 0
 1 1 1
 1 1 2
call set(1+1)
 1 2 0
 1 2 1
 1 2 2
call set(0+1)
call set(1+1)
 2 0 0
 2 0 1
 2 0 2
call set(1+1)
 2 1 0
 2 1 1
 2 1 2
call set(1+1)
 2 2 0
 2 2 1
 2 2 2
```

![image](https://user-images.githubusercontent.com/7253111/170824335-bfd013a1-d94d-47e7-9305-c17fcb2eaf3b.png)

