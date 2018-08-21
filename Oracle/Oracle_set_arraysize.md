### SET ARRAYSIZE 

```
SET ARRAYSIZE 1000;
 
array size를 늘린다.

Sets the number of rows that SQL*Plus will fetch from the database at one time. Valid values are 1 to 5000.

The effectiveness of setting ARRAYSIZE depends on how well Oracle Database fills network packets and your network latency and throughput. In recent versions of SQL*Plus and Oracle Database, ARRAYSIZE may have little effect. Overlarge sizes can easily take more SQL*Plus memory which may decrease overall performance.
