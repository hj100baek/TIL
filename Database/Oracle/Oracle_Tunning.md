##### tunning 참고

```sql
 -- 필수조건을 case문으로 쓸경우 리딩테이블이 풀테이블 스캔될수 있음
 WHERE 1=1       ------------>> (잘못된 예)
   AND 1 = CASE WHEN @TMP_VAL='Y' AND A.month = @YYYYMM THEN 1
                WHEN @TMP_VAL='N' AND A.month = @YYYYMM THEN 1
    ELSE 0 END

 -- 필수조건의  case문을 union all로 분리함(개선)
         from  (   select /*+ index(A1) */ * 					
                  from DEPT A1					
                  where :TMP_VAL='Y' 					
                  AND  month = :YYYYMM 					
                  union all					
                  select /*+ index(A2) */ * 					
                  from DEPT A2					
                  where  :TMP_VAL='N' 					
                  AND  month = :YYYYMM  					
              ) X   					





-- max(seq)를  index min/max scan을 위한  힌트적용 
 where x.seq = (select /*+ no_unnest */ max(SEQ)

```
