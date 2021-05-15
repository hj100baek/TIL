```
######################
# 1차 풀이
# 실패 : 33.3 / 100.0
# 실패 원인: 모든 숫자를 조합할때 맞지도 않지만 너무 오래 걸림.
######################
```
```python
rcnt = 1
def solution(numbers):
    answer = findPrime(toComb(toArray(numbers),0,rcnt,len(numbers))) 
    return answer


def toArray(numbers):
    arr =[]
    for number in numbers:
        arr.append(number)
    return arr

def toComb(arrs,prelen,rcnt,firstlen):
    arr = arrs[:]
    arrlen = len(arrs)
    startidx = prelen
    
    startidxsub = prelen if prelen > 0 else arrlen

    if rcnt == firstlen  :
        return list(set(arr)) 
    for idx in range(startidx, arrlen):
        for idx2 in range(startidxsub):
            if idx == idx2 : continue                  
            tmp = arrs[idx] + arrs[idx2]
            if not tmp.lstrip("0") in arr:
                arr.append(tmp.lstrip("0"))

    return toComb(arr, len(arrs), rcnt+1,firstlen)
        
def  findPrime(arrs):
    arrPrime = []
    isPrime = True
    for idx in range(len(arrs)):
        isPrime = True
        if int(arrs[idx]) < 2 : 
            continue 
  
        for i in range(2,int(arrs[idx])):
            if int(arrs[idx]) % i == 0:
                isPrime = False
                break


        if isPrime :
            arrPrime.append(arrs[idx])
    return len(arrPrime)
```

```
######################
# 2차 풀이
# 성공 : 100.0/ 100.0
# 원인: 단순 for문은 안됨. 순열. 재귀함수등을 참고 . api는 import하지 않고 시도
######################

def generate(chosen, used, arr, r, rsltstr):
        

        if len(chosen) == r:
           # print(chosen)   
            return rsltstr
	

        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
               # print(f' i = {i} ,  chosen be= {chosen}, used ={used}')
                generate(chosen, used, arr, r, rsltstr)
                #print(f'chosen af= {chosen}')
                #print(f'rsltstr af= {rsltstr}')
                #print(f'arr i= {i}')
                tmp = "".join(chosen[:]) 
                if not tmp.lstrip("0") in rsltstr and isPrime(tmp) :
                    rsltstr.append(tmp.lstrip("0")) 
                

                #print(f'rsltstr af2= {rsltstr}')
                used[i] = 0
                chosen.pop()
                
        return rsltstr

def isPrime(number):
    number = int(number)
    if number <= 1 : return False
    if number == 2 : return True

    for i in range(2,number):
        if number % i == 0:
            return False

    return True

def solution(numbers):
    used = [0 for _ in range(len(numbers))]
    chosen = []
    rslt = generate(chosen, used, numbers, len(numbers),[])
    return len(rslt)

solution("011")


```
