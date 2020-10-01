```python
'''
1차 풀이 : 실패, 정확도는 100%, 효율성 0%
배열에 모든 값을 추가하니 단순하지만 너무 느리다........
'''
def solution(n):
    answer = ''

    source = ['1', '2', '4']
    result = []
    totcnt = 0

    for idx in range(n):
        if idx < 3 :
            totcnt = totcnt + 1
            result.append(source[idx])            
        else:
            for in_idx in range(3):
                if totcnt < n :
                    result.append(result[idx-3] + source[in_idx])
                else:
                    break
                totcnt = totcnt + 1
        
    answer = result[n-1] 

    return answer


'''
2차 풀이 : 성공, 타 풀이 참조
재귀함수 이용, 문자열에도 재귀함수를 쓸수 있다는 생각을 좀 하자..
'''
def solution2(n):

    source = ['1', '2', '4']

    if n <= 3 :
        return source[n-1] 
    else:
        mm = (n-1) // 3
        print("n:"+ str(n) + " mm:"+ str(mm))
        return solution2(mm) + source[(n-1) % 3]  

```
