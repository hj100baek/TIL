### oracle

컬럼 값 붙이기 함수 
wm_concat()는 oracle12c에서 ora-00904 error를 발생시킨다.
listagg()는 oracle12c에서 작동함

The following group-set aggregate example lists, for each department ID in the hr.employees table, the employees in that department in order of their hire date:

```sql
SELECT department_id "Dept.",
       LISTAGG(last_name, '; ') WITHIN GROUP (ORDER BY hire_date) "Employees"
  FROM employees
  GROUP BY department_id
  ORDER BY department_id;


Dept. Employees
------ ------------------------------------------------------------
    10 Whalen
    20 Hartstein; Fay
    30 Raphaely; Khoo; Tobias; Baida; Himuro; Colmenares
```    
    
    
참조URL : [https://docs.oracle.com/database/121/SQLRF/functions101.htm#SQLRF30030]
