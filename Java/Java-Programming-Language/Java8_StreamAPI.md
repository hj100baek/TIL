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

- Intermediate Operation method
 + ex) filter , map
- Terminal Operation method
 + ex) findFirst

```java
class Person
{
    private String name;
    private String birthDate;
    public String getName() {
        return name;
    }
     public vodi setName(name) {
        this.name = name;
    }
    public String getBirthDate() {
        return birthDate; 
    }
    Person(String name) {
        this.name = name;
    }
}

// name 으로만 list 만들고 싶을경우 
List<String> names = 
    personList.stream()
              .map(Person::getName)
              .collect(Collectors.toList());

```

```java
// map에서 fucntion 이용 
Function<Person, Person> fp = x -> {
  x.setName("change");
  return x;
};

List<String> names = 
    personList.stream()
              .map(Person::getName)
              .collect(Collectors.toList());

List<String> names_change = names.stream()
                                 .map(fp)
                                 .collect(Collectors.toList());

