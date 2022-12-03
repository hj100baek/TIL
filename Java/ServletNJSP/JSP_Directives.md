### 지시어(Directives)
##### 해당하는 JSP 파일의 속성을 기술, JSP 컨테이너에게 해당 페이지를 어떻게 처리해야하는지 전달하기 위한 내용을 담고 있다.
##### 유형 : page, include, tablib
```jsp 
 <%@ directive attribute="value" %>
```

### page directive
##### JSP 페이지에 적용하는 속성들을 정의하기 위해 사용된다.
```jsp
<%@ page attribute1="value" attribute2="value" %>
```

### include directive
##### 현재 JSP파일에 다른 HTML이나 JSP문서를 포함하기 위한 기능을 제공
##### 한개의 파일로 실행됨으로 static resource에 유용
```jsp
<%@ include file="filename" %>
```

### taglib directive
##### 커스텀 태그 라이브러리를 JS 파일에서 사용하기 위한 지시어

```jsp
<%@ taglib uri="mytag.tld" preifx="mytag %>

<mytag:GetInfo name="user" />
```
