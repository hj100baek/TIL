## ready()

```
- ready() 메서드는 Document 객체에서 발생하는 DOMContent Loaded이벤트를 포장한 메서드 
DOMContent Loaded이벤트는 웹브라우져가 웹 페이지를 읽은 후 태그와 1:1 매핑되는 DOM객체를 생성한 후 발생
그래서 이미지나 무거운 컨텐츠가 로드되기 전에 실행될 수 있음. 

- window.onload는 컨텐츠가 모두 로드된 후 실행된는 이벤트. 

- Basic syntax is: $(selector).action()
A $ sign to define/access jQuery
A (selector) to "query (or find)" HTML elements
A jQuery action() to be performed on the element(s)

```
```html
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html charset="UTF-8">
  		<title>jQuery 사용준비</title>
  		<style>
  			body {
  				font-size: 9pt;
  				font-family: "굴림";
  			}
  		</style>
  		<script type="text/javascript" src="./libs/jquery-3.3.1.js"></script>
  		<script>
  			jQuery(document).ready(function(){
  				alert("안녕하세요 . JQuery type1");
  			});

  			jQuery(function(){
  				alert("안녕하세요 . JQuery type2");
  			});

  			$(document).ready(function(){
  				alert("안녕하세요 . JQuery type3, Best!");
  			});

  			$(function(){
  				alert("안녕하세요 . JQuery type4");
  			});
  		</script>
 	</head>
 	<body>
    	jQuery를 사용할 준비가 됬나요?
 	</body>
</html>
```
