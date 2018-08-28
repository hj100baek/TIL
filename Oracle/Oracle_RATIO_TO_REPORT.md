### RATIO_TO_REPORT
##### RATION_TO_REPORT ( expr ) OVER ( PARTITION BY 절 )
##### 분석함수. 계산 대상 값 전체에 대한 현재 로우의 상대적인 비율 값을 반환


```sql
SELECT T.TNUM
      , ROUND(RATIO_TO_REPORT(TNUM) OVER (),2) * 100 AS ROW_PERCENT
FROM (
  SELECT ROUND(LEVEL*DBMS_RANDOM.VALUE(1,1000),0)  TNUM                    
  FROM   DUAL CONNECT BY LEVEL <= 10
) T
;


/*=================================================================
result
=================================================================*/
   TNUM	ROW_PERCENT
1	 924	4
2	 1971	8
3	 852	4
4	 3082	13
5	 3531	15
6	 5701	24
7	 1512	6
8	 272	1
9	 4003	17
10       2196	9
```

