
###  row 형식자료를 column 형식자료로 위치 변환

```sql
-- column형식자료를 row형식자료로 위치변환

select 
    decode(cnt,1,c1,2,c2)
from (

  -- row 형식자료를 column 형식자료로 위치 변환
 select 
     rno,
     max(decode(cno,1,country_name)) c1,
     max(decode(cno,2,country_name)) c2
 from (
  select '1' as rno,
      mod(rownum,4) cno,        
      country_name
  from countries
  where country_name like 'A%'
  union
  select '2' as rno, 
      mod(rownum,4) cno,
      country_name
  from countries
  where country_name like 'B%'
  )
 group by rno
) ,
 (
  select rownum cnt
  from user_tables
  where rownum < 3
 )
;
```
