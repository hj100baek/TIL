```sql
/*테이블의 컬럼정보 조회하기*/
SELECT 
--     A.OWNER
    A.TABLE_NAME
   , A.COLUMN_ID
   , A.COLUMN_NAME
   , B.COMMENTS
   , A.DATA_TYPE
   , A.DATA_LENGTH
--    , A.NULLABLE
    , A.DATA_TYPE || '(' || A.DATA_LENGTH || ')' ||' '
      ||CASE WHEN A.NULLABLE = 'N' THEN 'not null' END  as COL_INFO
        , 'comment on column '|| A.OWNER ||'.'|| A.TABLE_NAME ||'.'|| A.COLUMN_NAME || ' is ' || B.COMMENTS ||' ;'  as COL_comment
FROM   ALL_TAB_COLUMNS A
     , ALL_COL_COMMENTS B
WHERE  A.TABLE_NAME = B.TABLE_NAME
      AND  A.COLUMN_NAME = B.COLUMN_NAME
      AND A.OWNER = 'MY'      /*owner name*/
      AND A.TABLE_NAME like 'TB_%' /*table name*/
      AND ( A.DATA_TYPE = 'DATE' OR A.COLUMN_NAME LIKE '%DATE')
ORDER BY A.TABLE_NAME, A.COLUMN_ID
;

```
