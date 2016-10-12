loop문이 1단계가 아닐때는 반목문에 label을 붙이면 원하는 반복문으로 갈수있다.
 
 ```java
 search:
        for (i = 0; i < arrayOfInts.length; i++) {
            for (j = 0; j < arrayOfInts[i].length;
                 j++) {
                if (arrayOfInts[i][j] == searchfor) {
                    foundIt = true;
                    break search;
                }
            }
        }
```
(http://docs.oracle.com/javase/tutorial/java/nutsandbolts/branch.html)
