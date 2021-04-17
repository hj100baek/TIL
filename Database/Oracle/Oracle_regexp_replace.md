### regexp_replace

```
-- 정규표현식을 이용한 replace 가능

SELECT --이름, 첫번째짜리만 보이고 나머지는 마스킹처리 김**  양****
       name, regexp_replace(name, '^(.)(.?+)', '\1')||regexp_replace(regexp_replace(name, '^(.)(.?+)', '\2'),'.','*') name_replace 
       --번호, 마지막4자리만 보이고 나머지는 마스킹처리 *******1234  ***1234
     ,account_num, regexp_replace(substr(account_num,1,length(account_num)-4),'[0-9]' ,'*')||substr(account_num, -4) account_num_replace 
FROM TARGET_TABLE a
WHERE seq=60;


```
