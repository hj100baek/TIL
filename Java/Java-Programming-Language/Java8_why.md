## Java8 사용 이유
 - 코드 간결성
 - First Class Function 지원
  + 함수 자체를 파라미터로 넘긴다.
  + lambda expression


 - Functional Interface
  + Function

 ```java
 Function<String, Integer> toInt = (value) -> Integer.parseInt(value);

 final Integer number = toInt.apply("100");
 System.out.println(number);
 ```
  + Consumer

  ```java
  Consumer<String> print = (value) -> System.out.println(value);

  print.accept("Hello");
  ```
  + Predicate

  ```java
  Predicate<Integer> isPositive = (i) -> i > 0;

  System.out.println(isPositive.test(1));
  ```
  + Supplier

  ```java
  Supplier<String> hello = () -> "Hello";

  System.out.println(hello.get()+" world");
  ```
