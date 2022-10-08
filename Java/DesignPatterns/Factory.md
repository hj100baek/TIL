#### [ Factory method pattern ]
##### 객체 생성의 캡슐화 , 관련성 정의 (병렬적인 클래스 계통을 연결하는 역할)

###### Spring에서 Factory method pattern은 어떻게 되는지 의문이 생김
###### Spring은 컨테이너에서 Bean을 관리한다는데 옛날 책들의 예제는 new를 사용함

##### Spring에서 Factory method pattern 사용방법
##### 1) Map을 사용하는 방식
##### 2) ServiceLocatorFactoryBean 을 이용한 방식

```java
// 1) Map을 사용하는 방식 
@Service
public class PizzaFactory {

  private CheesePizza cheesePizza;  //@Component로 Pizza별 class파일 생성, Pizza interface 생성 
  private MeatPizza meatPizza;
  private PepperoniPizza pepproniPizza;
  private VeggiePizza veggiePizza;

  public PizzaFactory(CheesePizza pizza1, MeatPizza pizza2, PepperoniPizza pizza3,
      VeggiePizza pizza4) {
    System.out.println("======== PizzaFactory Constructor =======");
    cheesePizza = pizza1;
    meatPizza = pizza2;
    pepproniPizza = pizza3;
    veggiePizza = pizza4;

    getPizzaInit();
  }

  private static final Map<String, Pizza> handler = new HashMap<String, Pizza>();  

  // @PostConstruct
  private Map<String, Pizza> getPizzaInit() {
    System.out.println("======== getPizzaInit =======");
    handler.put(cheesePizza.getType(), cheesePizza);
    handler.put(meatPizza.getType(), meatPizza);
    handler.put(pepproniPizza.getType(), pepproniPizza);
    handler.put(veggiePizza.getType(), veggiePizza);
    return handler;
  }

  public static Pizza createPizza(String pizza) throws Exception {
    return Optional.ofNullable(handler.get(pizza))
        .orElseThrow(() -> new IllegalArgumentException("Invalid pizza"));
  }

}

/////////////////////////////////////////
@RestController
public class FactoryController {
  @GetMapping("/info/{pizza}")
  public String getPizzaTypeInfo(@PathVariable("pizza") String pizza) throws Exception {

    Pizza pizzaFactory = PizzaFactory.createPizza(pizza);
    return pizzaFactory.getIngredients();
  }

  //////////////////////////////////////
  public interface Pizza {

  public String getType();

  public String getIngredients();
}
//////////////////////////////////////
  @Component
public class CheesePizza implements Pizza {

  @Override
  public String getType() {
    return "CheesePizza";
  }

  @Override
  public String getIngredients() {
    return "grated parmesan cheese";
  }

}

}



```
