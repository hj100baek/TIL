### SELECT ... FOR UPDATE 

```sql
  -- 동시성 제어 목적, Row level lock
  -- 1) FOR UPDATE NOWAIT
  --     다른 세션이 row를 잡고있다면 바로 에러 발생 
  --    (ORA-00054: resource busy and acquire with NOWAIT specified or timeout expired)
  
  
  -- session 1
     declare
     var1    varchar2(100);
     var2    varchar2(100);
   
   begin

    select '1' into var1  from dual; 

    dbms_output.put_line(var1);

    SELECT PROCESS_NAME into var2
    FROM TEST_TABLE 
    WHERE PROCESS_ID = '1001'
    FOR UPDATE NOWAIT;


    dbms_lock.sleep(15);    -- 15초 대기 


    dbms_output.put_line(var2);
     
   end;
   
   -- session 1 result
     1
     PROCESS_NAME
  
  -- session 2
  SELECT PROCESS_NAME 
  FROM TEST_TABLE 
  WHERE PROCESS_ID = '1001'
  FOR UPDATE NOWAIT;
  
  -- session 2 result
  ORA-00054: resource busy and acquire with NOWAIT specified or timeout expired
```
