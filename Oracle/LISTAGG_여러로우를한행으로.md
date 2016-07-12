
### LISTAGG

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

@ 행으로 만들 때 중복제거 시
```sql
SELECT t01.department_id
    ,  LISTAGG(job_id, '; ') WITHIN GROUP (ORDER BY job_id) "job_ids"
    ,  LISTAGG(case when t01.rn = 1 then job_id end, '; ') WITHIN GROUP (ORDER BY job_id) "job_ids_distinct"
FROM (
  SELECT department_id
       , job_id
       , row_number() OVER (PARTITION BY department_id,job_id ORDER BY department_id) "RN"
  FROM job_history
) t01  
GROUP BY t01.department_id;

DEPARTMENT_ID	  job_ids	            job_ids_distinct
------ ------------------------------------------------------------
20	            MK_REP                  MK_REP
50	            ST_CLERK; ST_CLERK	  ST_CLERK
60                IT_PROG            	 IT_PROG
80	            SA_MAN; SA_REP	      SA_MAN; SA_REP
```
