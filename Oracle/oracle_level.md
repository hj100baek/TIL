```
oracle LEVEL



계층(hierarchical) 레벨을 나타낸다. 
 CONNECT BY 와 함께 사용해야만 한다. 
 LEVEL을 이용해 ROW생성이 가능하다.



 WITH T AS (
   SELECT 'A' FROM DUAL
 )
 SELECT T.*, LEVEL
 FROM T
 CONNECT BY LEVEL <=3
 ;

 [RESULT]
 A 1
 A 2
 A 3

root대상건이 1건일 경우는 3개 ROW를 생성함



WITH T AS (
   SELECT 'A' FROM DUAL
   UNION ALL
   SELECT 'B' FROM DUAL
 )
 SELECT T.*, LEVEL
 FROM T
 CONNECT BY LEVEL <=3
 ;

[RESULT]
A 1
A 2
A 3
B 3
B 2
A 3
B 3
B 1
A 2
A 3
B 3
B 2
A 3
B 3

root대상건이 2건일 경우는 14개 ROW를 생성함 
14 = 2 + (2x2) + (2x2x2)



root대상건이 3건일 경우는 39개 ROW를 생성함 
39 = 3 + (3x3) + (3x3x3)
```
