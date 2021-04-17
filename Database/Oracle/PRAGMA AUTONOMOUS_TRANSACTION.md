## PRAGMA AUTONOMOUS_TRANSACTION

PRAGMA란 다른 프로그래밍 언어에서도 사용되는데,
컴파일러가 실행되기 전에 처리하는 전처리기 역할을 한다. 
PRAGMA를 사용하면 컴파일러는 런타임 때와는 다른 결과를 내도록 동작한다. 
즉 컴파일할 때 뭔가를 처리하라고 컴파일러에게 지시하는 역할을 하는데, PL/SQL 블록의 선언부에 명시하며 사용법은 다음과 같다.

① PRAGMA AUTONOMOUS_TRANSACTION
트랜잭션 처리를 담당하는데, 
주 트랜잭션이나 다른 트랜잭션에 영향을 받지 않고 
독립적으로 현재 블록 내부에서 데이터베이스에 가해진 변경사항을 COMMIT이나 ROLLBACK 하라는 지시를 하는 역할을 한다.


```sql
 -- Batch Log 
  PROCEDURE PROC_WRITE_BATCH_LOG(P_LOG_SEQ  IN OUT NUMBER 
                                ,P_LOG_TIME IN DATE DEFAULT SYSDATE 
                                 ) IS
    PRAGMA AUTONOMOUS_TRANSACTION;
    V_LOG_SEQ NUMBER := NULL;
  BEGIN
  
    -------------------------------------------------
    -- Batch Start Log
    -------------------------------------------------
    IF P_LOG_SEQ IS NULL THEN
    
      xxxxxxxxxxxxxxx
    
      -------------------------------------------------
      -- Batch End Log
      -------------------------------------------------
    ELSE
       xxxxxxxxxxxxxxx
    END IF;
  
    COMMIT;
  
  EXCEPTION
    WHEN OTHERS THEN
      DBMS_OUTPUT.PUT_LINE('SQLCODE = [' || SQLCODE || ']');
      ROLLBACK;
    
  END PROC_WRITE_BATCH_LOG;
  
  
  
  PROCEDURE PROC_CALLER(P_RETURN_CODE OUT VARCHAR2
                              ,P_RETURN_MSG  OUT VARCHAR2) IS
  

    V_TCNT NUMBER := 0;
  
  BEGIN
  
    -- BATCH LOG 시작
   PROC_WRITE_BATCH_LOG(V_LOG_SEQ, V_JOB_STEP);
  
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
  
    IF V_TCNT != 3 THEN
      P_RETURN_CODE := 'F';
      XXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    END IF;
  
  
  
    IF V_STATUS_CODE = 'F' THEN
    
      P_RETURN_CODE := 'F';
      P_RETURN_MSG  := 'ERROR - [' || V_JOB_STEP || '] ' || V_STATUS_MSG;
    
      PROC_WRITE_BATCH_LOG(V_LOG_SEQ, P_RETURN_MSG, -1);
    
      RETURN;
    
    END IF;
  
   END PROC_CALLER;
  
```
