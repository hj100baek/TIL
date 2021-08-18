```sql

-- MYSQL에서 ROWNUM 생성하기 

select @rownum:=@rownum+1 rowNums
  from table,
       (select @rownum:=0) tmp
  

```
