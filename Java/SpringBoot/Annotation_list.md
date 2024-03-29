### @RestController
클래스 수준 애너테이션

스프링 컨테이너에 이 자바 클래스가 REST기반 서비스에 사용된다고 알리는 역할

반환할 데이터를 JSON으로 직렬화

@ResponseBody를 포함하고 있음

### @RequestMapping
클래스 또는 메서드 수준 애너테이션

스프링 컨테이너에 해당 서비스가 HTTP 앤드포인트를 외부에 공개한다고 알리는데 사용

클래스에서 사용하면 그 컨트롤러가 노출하는 모든 엔드포인트의 최상위(root) URL을 설정할 수 있음


### @Component
클래스 수준 애너테이션

스프링 프레임워크에서 자동 스캔되는 대상. 스프링에 의해 관리된다는 표시

@Controller, @Repository, @Service 도 사용목적이 구체화된 컴포넌트 

```java
@Component
public @interface Service {
    ….
}

@Component
public @interface Repository {
    ….
}

@Component
public @interface Controller {
    …
}
```


### @RestControllerAdvice
ExceptionHandler가  global하게 적용되게 할 수 있다.

```java
@RestControllerAdvice
public class CustExceptionHandler {
  
  @ExceptionHandler(value = RuntimeException.class)
	  public ResponseEntity<?> runtimeExceptionHandler(RuntimeException ex) {
		 return ResponseEntity.status(HttpStatus.CONFLICT)
				 .body(ex.getMessage());
	 }
}
```


