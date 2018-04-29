## 부모노드 찾기

```html
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html charset="UTF-8">
  		<title>jQuery node찾기</title>
  		<style type="text/css">
        body{
          font-size: 9pt;
          font-family: "굴림";
        }
        div, p, ul, li {
          border: 1px #eeeeee solid;
          margin: 10px;
        }
        ul {
          padding: 10px;
        }
        li.select {
          background-color: #ccc;
        }
 
      </style>
  		<script type="text/javascript" src="./libs/jquery-3.3.1.js"></script>
  		<script>
  		
  			$(document).ready(function(){

            var $menu = $("ul.menu");
            //직계 부모 찾기 
            //$menu.parent().css("border", "4px solid #f00");
            //모든 조상 노드 찾기 
            $menu.parents().css("border", "4px solid #f00");
        });

      
	   
  		</script>
 	</head>
 	<body>
    <div id="samplePage" class="page">
      샘플 페이지(div, id=samplePage, class=page)
      <div id="header" class="test1">
          헤더 영역(div, id=header, class=test1)
      </div>
      <div id="content" class="sample-content">
        노드 찾기(div, id=content, class=sample-content)
        <ul class="menu">
          일반 노드 찾기(ul, class=menu)
          <li>id로 찾기(li)</li>
          <li class="select">tag로 찾기(li, class=select)</li>
          <li>class로 찾기(li)</li>
          <li class="test1">속성으로 찾기(li, class=test1)</li>
        </ul>
        <div class="content-data">
          자식 노드 찾기(div, class=content-data)
          <p class="test1">1. 모든 자식 노트 찾기(p, class=test1)</p>
          <p>2. 특정 자식 노드만 찾기(p)</p>
          <p class="test2">3. 마지막 자식 노드 찾기(p, class=test2)</p>
        </div>
      </div> 
      <div id="footer">
        푸터 영역(div, id=footer)
      </div>
     </div>
 	</body>
</html>
```
