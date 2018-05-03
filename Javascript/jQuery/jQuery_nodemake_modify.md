## 노드 변경

```html
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html charset="UTF-8">
  		<title>jQuery node읽기 및 변경</title>
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

            //$("#ok").click(function(){
                //노드 내용을 문자열로 읽기 - 태그 포함
                //console.log($("ul.menu").html());
                //console.log($(".menu").html());

                //노드 내용을 문자열로 읽기 - 텍스트만
                //console.log($(".menu").text());
            //})

            //클릭한 메뉴 아이템의 내용 변경
            // $("ul.menu li").click(function(){
            //    var $item = $(this);
            //    $item.html("<a href='http://google.com'> new menu"+ (1+$item.index()));
            // })

            //노드 내용을 이용해 여러개 자식 노드 추가  
            $("#add").click(function(){
                var data ="";
                for(var i=1;i<=10;i++){
                   data+="<li>menu new ["+ i +"]";
                }

                $("ul.menu2").html(data);
            })

            //노드 내용을 이용해 모든 자식 노드 제거
             $("#del").click(function(){
                $("ul.menu2").html("");
             })
        });

  		</script>
 	</head>
 	<body>
        <button id="ok">확인</button>
        <button id="add">추가</button>
        <button id="del">삭제</button>
        <ul class="menu">
          <li>menu1</li>
          <li>menu2</li>
          <li class="select">menu3</li>
          <li>menu4</li>
          <li>menu5</li>
          <li>menu6</li>
        </ul>

         <ul class="menu2">
         </ul>
      
 	</body>
</html>
```
