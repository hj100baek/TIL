
###### 참고
https://asktom.oracle.com/pls/apex/f?p=100:11:0::::P11_QUESTION_ID:9532128000346585769

```sql

select distinct referenced_name 
from   user_dependencies
where  referenced_type = 'TABLE'
and    type like 'PACKAGE%'

```
