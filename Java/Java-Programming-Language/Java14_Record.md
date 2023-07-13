#### Record Classes
```
간단한 data 이동을 위해 사용되는특별한 종류의 class
record를 사용하기 전에는 데이터가 불변임에도 class를 생성해서 생성자, 필드당 getter, equals, hashCode, toString 작성을
해줘야 했음
record를 사용하면 필드 타입과 필드명만 지정해주면 전에 해야됬던 작업을 자동 생성해줌

1. Constructor
2. Getters
3. equals
4. hashCode
5. toString

```
```java
public record Rectangle(double length, double width) { }
```

참고 https://www.baeldung.com/java-record-keyword
     https://docs.oracle.com/en/java/javase/20/language/records.html#GUID-6699E26F-4A9B-4393-A08B-1E47D4B2D263
