
###### 참고
https://asktom.oracle.com/pls/apex/f?p=100:11:0::::P11_QUESTION_ID:9532128000346585769

https://docs.oracle.com/cd/B28359_01/server.111/b28320/statviews_1066.htm#REFRN20053

```sql

select distinct referenced_name 
from   user_dependencies
where  referenced_type = 'TABLE'
and    type like 'PACKAGE%'

```
