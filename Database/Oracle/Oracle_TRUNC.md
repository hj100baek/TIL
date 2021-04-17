### TRUNC

```sql

 -- TRUNC (number,n2)
 -- n2 can be negative to truncate (make zero) n2 digits left of the decimal point.
 
 SELECT TRUNC(15.79,1) "Truncate" FROM DUAL;

  Truncate
----------
      15.7

SELECT TRUNC(15.79,-1) "Truncate" FROM DUAL;

  Truncate
----------
        10

```
