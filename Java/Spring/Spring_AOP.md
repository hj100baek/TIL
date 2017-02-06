## Spring AOP
- Advice(어드바이스): 부가기능을 제공하는 오브젝트
- Pointcut(포인컷): 메소드 선정 알고리즘을 담은 오브젝트
- Advisor(어드바이저): Pointcut(포인컷) + Advice(어드바이스)

- 예제: 소문자 -> 대문자로 변환하는 부가기능 제공, sayH로 시작되는 함수만

```java
@Test
	public void pointcutAdvisor() {
		ProxyFactoryBean pfBean = new ProxyFactoryBean();
		pfBean.setTarget(new HelloTarget());

		NameMatchMethodPointcut pointcut = new NameMatchMethodPointcut();
		pointcut.setMappedName("sayH*");

		pfBean.addAdvisor(new DefaultPointcutAdvisor(pointcut, new UppercaseAdvice()));

		Hello proxiedHello = (Hello)pfBean.getObject();

		assertThat(proxiedHello.sayHello("Toby"), is("HELLO TOBY"));
		assertThat(proxiedHello.sayHi("Toby"), is("HI TOBY"));
		assertThat(proxiedHello.sayThankYou("Toby"), is("THANK YOU TOBY"));

	}

	static class UppercaseAdvice implements MethodInterceptor {

		@Override
		public Object invoke(MethodInvocation invocation) throws Throwable {
			String ret = (String)invocation.proceed();
			return ret.toUpperCase();
		}
	}

```

```java
public class HelloTarget implements Hello {

	@Override
	public String sayHello(String name) {
		// TODO Auto-generated method stub
		return "Hello " + name;
	}

	@Override
	public String sayHi(String name) {
		// TODO Auto-generated method stub
		return "Hi " + name;
	}

	@Override
	public String sayThankYou(String name) {
		// TODO Auto-generated method stub
		return "Thank You " + name;
	}

}
```
