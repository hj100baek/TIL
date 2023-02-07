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
