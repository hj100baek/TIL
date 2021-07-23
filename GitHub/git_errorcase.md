### git error case
```
 1) fetch result :  lock fail

   - 해당 에러가 발생하면 pull해도 저 에러가 발생하고 reset해도 저 에러가 발생
   - 해결방법: (STS 기준)
       해당 프로젝트 오른쪽 마우스 클릭> Show in Local Terminal > Terminal
       
       Terminal에서 
       $ rm .git/refs/remotes/origin/develop  (origin 뒤 경로는 환경에 따라 다를 수 있다)
       $ git fetch    (잘하다가 Unlink of file ...ㄴShould I try again? (y/n) 다오면 n으로 무시)
       
       $git pull
        
        
```
