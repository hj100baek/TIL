## Java8 Functional Interface
- 자신만의 Functional Interface 생성 가능
- @FunctionalInterface annotation을 써준다.
- 1개의 abstract method만 있어야 한다.
 + 이유: Functional Interface 도 결국 오브젝트가 생성되어야 하는데</br>           메소드 바디가 없는 메소드를 남겨놓고는 오브젝트 생성이 안됨

```java
@FunctionalInterface
interface FunctionTest<T1, T2, T3, R> {
  R apply(T1 t1, T2 t2, T3 t3);
}
```

- 일반 type이 정해진 method 예제

```java
@FunctionalInterface
interface BigDecimalToCurrency {
 String toCurrency(BigDecimal value);
}

//사용 시
BigDecimalToCurrency bigDecimalToCurrency = bd -> "$" + bd.toString();
System.out.println(bigDecimalToCurrency.toCurrency(new BigDecimal("100.00")));
```

- Generic method는 abstract method로 사용하지 못한다.

```java
@FunctionalInterface
interface InvalidFunction {
  <T>String makeString(T value);
}
.
.
//사용 시 람다식에서 에러 발생
InvalidFunction invalidFunction = value -> value.toString();

System.out.println(invalidFunction.makeString());

```

- Functional interface 활용예제

```java
private static <T> BigDecimal total(List<T> list, Function<T, BigDecimal> mapper) {
 BigDecimal total = BigDecimal.ZERO;
 for (final T t : list) {
   total = total.add(mapper.apply(t)) ;
 }
 return total;
}
```
