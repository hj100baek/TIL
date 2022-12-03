### 액션(Action)
##### servlet engine의 행위를 제어하기 위해 사용한다. 

```jsp
<jsp:action_name attribute="value" />
```
```
jsp:include 다른 페이지를 현재 페이지에 포함 시킨다.
jsp:forward 현재 페이지의 제어를 다른 페이지로 전달한다.
jsp:useBean 자바클래스를 사용하기 위해서 useBean을 사용한다.
jsp:setProperty useBean으로 선언된 빈즈 클래스의 setXXX()메서드를 호출
jsp:getProperty	useBean으로 선언된 빈즈 클래스의 getXXX()메서드를 호출
jsp:plugin	applet이나 빈즈 클래스를 플러그인 형태로 로딩
jsp:param	include, forward액션에서 사용할 수 있는 파라미터를 설정
```
