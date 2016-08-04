### Branching Statements
 
   Q: 중첩된 for 문인데 첫번째로 for문으로 가고싶다면?
   
   ```java
   firstFor:
   for (int i=0; i < 10; i++) {
       for (int j=1; j <3; j++) {
         if (i % j == 0) { 
           continue firstFor;  
          }
       }
   }
  ```
(http://docs.oracle.com/javase/tutorial/java/nutsandbolts/branch.html)
