```
######################
# 1차 풀이
# 실패 : 33.3 / 100.0
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
