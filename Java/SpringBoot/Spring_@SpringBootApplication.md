### @SpringBootApplication

##### @Configuration, @EnableAutoConfiguration, @ComponentScan 를 선언한것과 같은 기능
##### scan package의 기준이된다. 
##### 만약 아래와 같이 com.example.myapplication 패키지에 @SpringBootApplication이 있다면 com.example.others 패키지에 클래스들은 스캔되지 않는다.

```java
package com.example.myapplication;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class Application {

	public static void main(String[] args) {
		SpringApplication.run(Application.class, args);
	}

}
```
