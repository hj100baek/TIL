### 찾은 노드 다루기 예제

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
          //div 태그 갯수
          //alert("length="+ $("div").length );

          //ul.menu 중 2번째 메뉴 css 속성 변경 
          // var $liList =  $("ul.menu li");
          // var $li_1 = $liList.eq(1);
          // $li_1.css("border", "4px solid #ff0");

          //ul.menu 중 2번째 메뉴 css 속성 변경 DOM객체이용
          // var $liList = $("ul.menu li");
          // var li_1 = $liList.get(1);
          // li_1.style.border = "4px solid #ff0";

          //each()메서드 값 확인 
           // var $liList = $("ul.menu li");
           // $liList.each(function(index){
           //    console.log("index = "+ index);
           // })

          //each()메서드 this 확인 
           // $("ul.menu li").each(function(index){
           //   console.log(this);
           // })

           //select클래스가 적용된 노드를 찾아 css변경 filter-현재노드를 포함하고 자손노드제외하고 검색  
           // var $liList = $("ul.menu li");
           // $liList.filter(".select").css("border", "4px solid #ff0");

           //찾은 노드의 자손노드 중 특정 노드 찾기 find- 현재노드 제외하고 자손노드 중 검색
           // var $content = $("#content");
           // $content.find(".test1").css("border", "4px solid #ff0"); 

           //클릭한 노드의 index
            $("ul.menu li").click(function(){
               console.log($(this).index()); 
            })

  			});
	
  		</script>
 	</head>
 	<body>
    <div id="samplePage" class="page">
      샘플 페이지(div, id=samplePage, class=page)
      <div id="header">
          헤더 영역(div, id=header)
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
        <div id="footer">
            푸터 영역(div, id=footer)
        </div>
      </div> 
 	</body>
</html>
```
