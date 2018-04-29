### 자식 노드 찾기 
 ###### 자식과 자손은 찾는 방법 다름 주의

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
        //#samplePage 바로 하위 자식만 css 변경
        //   $("#samplePage").children().css("border", "4px solid #f00");

        //#samplePage의 하위 자식 노드중 test1클래스가 적용된 노드 css 변경-직계 자식만 찾아 변경
        //  $("#samplePage").children(".test1").css("border", "4px solid #f00");

        //#samplePage의 하위 자식 노드중 test1클래스가 적용된 노드 css 변경-전체 자손 찾아 변경  
         // $("#samplePage").find(".test1").css("border", "4px solid #f00");
  			//ul.menu중 첫번째 자식 노드 css변경
           //var $menu = $("ul.menu");
          // $menu.children(":first").css("border", "4px solid #f00"); //아래방법보다는 이거이 더 효율적, 함수 1회 덜 호출
          // $menu.children().first().css("border", "4px solid #f00");
        //전체 div 태그 노드 중 첫 번째 자식 노드 css속성 변경 
         //$("div").find(":first").css("border", "4px solid #f00");  

         //ul.menu중 마지막 번째 자식노드 css 변경 
         var $menu = $("ul.menu");
         // $menu.children(":last").css("border", "4px solid #f00"); 
           //ul.menu중 n번째 자식노드 css 변경 
          $menu.children(":eq(1)").css("border", "4px solid #f00"); //2번째 자식노드 
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
