```sql

/*  문자열 자르기 */

-- oracle
REGEXP_SUBSTR( string, pattern [, start_position [, nth_appearance [, match_parameter [, sub_expression ] ] ] ] )

select REGEXP_SUBSTR('127.0.0.1', '[^.]+', 1, 1) from dual;  -- 127
select REGEXP_SUBSTR('127.0.0.1', '[^.]+', 1, 4) from dual;  -- 1

-- mysql

SUBSTRING_INDEX(str,delim,count)

select SUBSTRING_INDEX('127.0.0.1', '.', 1);  -- 127
select SUBSTRING_INDEX('127.0.0.1', '.', 4);  -- 127.0.0.1
select SUBSTRING_INDEX('127.0.0.1', '.', -1); -- 1
```
