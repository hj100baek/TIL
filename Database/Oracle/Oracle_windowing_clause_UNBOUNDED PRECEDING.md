### windowing_clause
   각 row가 calculating the function을 위해 사용된다.
  
  - ROWS specifies the window in physical units (rows).

  - RANGE specifies the window as a logical offset.
  
BETWEEN ... AND 
Use the BETWEEN ... AND clause to specify a start point and end point for the window. The first expression (before AND) defines the start point and the second expression (after AND) defines the end point.

If you omit BETWEEN and specify only one end point, then Oracle considers it the start point, and the end point defaults to the current row.

UNBOUNDED PRECEDING 
Specify UNBOUNDED PRECEDING to indicate that the window starts at the first row of the partition. This is the start point specification and cannot be used as an end point specification.

UNBOUNDED FOLLOWING 
Specify UNBOUNDED FOLLOWING to indicate that the window ends at the last row of the partition. This is the end point specification and cannot be used as a start point specification.

CURRENT ROW 
As a start point, CURRENT ROW specifies that the window begins at the current row or value (depending on whether you have specified ROW or RANGE, respectively). In this case the end point cannot be value_expr PRECEDING.
  
  
  ```
  윈도우 함수 OVER (
        PARTITION BY 절
            ORDER BY 절 [ASC|DESC]
        ROWS | RANGE
        BETWEEN UNBOUNDED PRECEDING | n PRECEDING | CURRENT ROW
            AND UNBOUNDED FOLLOWING | n FOLLOWING | CURRENT ROW
  ```
  
  
  참고사이트 : http://www.gurubee.net/lecture/2674
