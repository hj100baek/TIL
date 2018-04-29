## 노드 추가

```html
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html charset="UTF-8">
  		<title>jQuery node생성</title>
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
          //신규 노드를 첫 번째 자식 노드로 추가 
          var count = 0;
          $("#btnAdd").click(function(){
            count++;
            //신규노드 생성
            var $newItem = $("<li>new menu"+ count + "</li>");
            //첫 번째 자식 노드로 추가 
            //$("ul.menu").prepend($newItem);
            //$newItem.prependTo("ul.menu");

            //마지막 번쩨 자식 노드로 추가 
            //$("ul.menu").append($newItem);
            //$newItem.appendTo("ul.menu");

            //특정 노드 이전에 추가 - 형제 노드 추가 
            //$newItem.insertBefore("ul.menu li.select");
            //$("ul.menu li.select").before($newItem);

            //특정 노드 다음에 추가 - 형제 노드 추가 
            //$newItem.insertAfter("ul.menu li.select");
            $("ul.menu li.select").after($newItem);
          })
        });

  		</script>
 	</head>
 	<body>
        <button id="btnAdd">메뉴추가</button>
        <ul class="menu">
          <li>menu1</li>
          <li>menu2</li>
          <li class="select">menu3</li>
          <li>menu4</li>
          <li>menu5</li>
          <li>menu6</li>
        </ul>
      
 	</body>
</html>
```
