```sql

-- MYSQL에서 ROWNUM 생성하기 

select @rownum:=@rownum+1 rowNums
  from table,
       (select @rownum:=0) tmp
  


-- MYSQL에서 ROWNUM 생성하기  Partiton By col1컬럼

select @rownum:=if(@prev_val = T.col1, @rownum+1, 1) group_rowNumbs
  from table T,
       (select @rownum:=0) tmp,
       (select @prev_val:='') tmp2
  order by col2    
       

```
