## 형제 노드 찾기

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
          //특정 노드 이전 형제 노드 찾기
          //var $select = $("ul.menu li.select");
          //$select.prev().css("border", "4px solid #f00");

          //마지막 노드의 모든 이전 형제 노드 
          //var $last6 = $("ul.menu").children(":last");
          //var $last6 = $("ul.menu li:last");
          //$last6.prevAll().css("border", "4px solid #f00");

          //특정 노드 다음 형제 노드 찾기
          //var $select = $("ul.menu li.select");
          //$select.next().css("border", "4px solid #f00");

          //첫번째 노드의 모든 다음 형제 노드 
          var $first0 = $("ul.menu li:first");
          $first0.nextAll().css("border", "4px solid #f00");
        });

      
	   
  		</script>
 	</head>
 	<body>
   
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
