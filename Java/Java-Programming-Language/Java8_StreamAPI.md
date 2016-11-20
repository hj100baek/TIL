## Java8 StreamAPI
- Collection Builder

```java
Stream.of(1, 2, 3, 4, 5)
      .forEach(i -> System.out.print(i + " "));

//output
// 1 2 3 4 5
```

```java
 final List<Integer> numbers = Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
 System.out.println("Functional Result: " +
 		    numbers.stream()
 		           .filter(number -> number > 3)
 		           .filter(number -> number < 9)
 		           .map(number -> number * 2)
 		           .filter(number -> number > 10 )
 		           .findFirst()
 		  );   
 //output
 //Functional Result: Optional[12]
 ```
