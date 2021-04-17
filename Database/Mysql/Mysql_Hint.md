#### USE INDEX

* The USE INDEX (index_list) hint tells MySQL to use only one of the named indexes to find rows in the table
* 지정된 index를 사용하게 한다. 잘못된 index를 탈 경우 이 힌트를 사용한다.

```mysql
SELECT * FROM table1 USE INDEX (col1_index,col2_index)
  WHERE col1=1 AND col2=2 AND col3=3;

SELECT * FROM table1 IGNORE INDEX (col3_index)
  WHERE col1=1 AND col2=2 AND col3=3;
```

#### STRAIGHT_JOIN

* STRAIGHT_JOIN forces the optimizer to join the tables in the order in which they are listed in the FROM clause
* 옵티마이져가 From절에 순서대로 join하도록 한다. nonoptimal order로 탈 경우 속도 향상을 위해 사용한다.

```mysql
SELECT STRAIGHT_JOIN
       col1,
       col2
FROM table1 t1
inner join table2 t2
    on t1.col3 = t2.col3 
  
 
```
