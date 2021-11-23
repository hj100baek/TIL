##### Error 1093 : You can't specify target table 'xxx' for update in FROM clause 
###### Mysql은 자신의 테이블을 바로 update 할 수 없다
```sql
-- 에러 발생하는 경우
update user
set email = 'aaa'
   ,phone = 'bbbb'
where id = (select max(id) from user)     

-- 수정 : 임시테이블로 한번더 감싸준다.
update user
set email = 'aaa'
   ,phone = 'bbbb'
where id = (select id from 
                  (select max(id) id from user) tmp)     

```
