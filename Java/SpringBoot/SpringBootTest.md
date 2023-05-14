참고 : SrpingBoot Testing
[https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/#features.testing](https://docs.spring.io/spring-boot/docs/current/reference/htmlsingle/#features.testing)
### @SpringBootTest
##### 테스트에 적합한 ApplicationContext 을 생성한다.
```java
package com.example.testingweb;

import org.junit.jupiter.api.Test;

import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
public class TestingWebApplicationTests {

	@Test
	public void contextLoads() {
	}

}
```

### @WebMvcTest
##### Controller를 테스트하기 위해 사용한다.
```java
@WebMvcTest(GreetingController.class)
public class WebMockTest {

	@Autowired
	private MockMvc mockMvc;

	@MockBean
	private GreetingService service;

	@Test
	public void greetingShouldReturnMessageFromService() throws Exception {
		when(service.greet()).thenReturn("Hello, Mock");
		this.mockMvc.perform(get("/greeting")).andDo(print()).andExpect(status().isOk())
				.andExpect(content().string(containsString("Hello, Mock")));
	}
}
```

### @WebFluxTest
##### Spring WebFlux controller를 테스트하기 위해 사용한다.
```java
@WebFluxTest(HomeController.class)
public class HomeControllerSliceTest {

	@Autowired
	private WebTestClient client;

	@MockBean 
	InventoryService inventoryService;
	

	@Test
	void homePage() {
		when(inventoryService.getInventory()).thenReturn(Flux.just( //
				new Item("id1", "name1",  1.99), //
				new Item("id2", "name2",  9.99) //
		));
		when(inventoryService.getCart("My Cart")) //
				.thenReturn(Mono.just(new Cart("My Cart")));

		client.get().uri("/").exchange() //
				.expectStatus().isOk() //
				.expectBody(String.class) //
				.consumeWith(exchangeResult -> {
					assertThat( //
							exchangeResult.getResponseBody()).contains("action=\"/add/id1\"");
					assertThat( //
							exchangeResult.getResponseBody()).contains("action=\"/add/id2\"");
				});
	}
}
```

### @RunWith(SpringRunner.class)
##### Spring TestContext Framework을 사용한 테스트를 실행한다.
```
@RunWith(SpringRunner.class)
@DataJpaTest
public class MemberServiceTest {
	....
} 
```

### @DataJpaTest
##### JPA applications을 테스트하기 위해 사용한다. 
##### @Component and @ConfigurationProperties  beans는 scan되지 않는다!  그래서 @Service가 scan되지 않으므로 @Service를  테스트하고 싶다면 @SpringBootTest를 사용
##### 테스트가 끝나면 트랜잭션을 자동으로 롤백처리 해준다. (@Transactional을 포함하고 있기 때문)
```
@DataJpaTest
class MyNonTransactionalTests {

    // ...
    @Autowired MemberService memberService;    //@DataJpaTest를 사용하면 test시 org.springframework.beans.factory.unsatisfieddependencyexception .. 에러가 발생한다.
    
}  
```
