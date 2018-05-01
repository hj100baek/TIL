## 노드 삭제

```html
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html charset="UTF-8">
  		<title>jQuery node삭제</title>
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
            //클릭한 특정 노드 삭제
             // var $menu = $("ul.menu");
             // $("ul.menu li").click(function(){
             //     $(this).remove();
             // })

             //인덱스 값이 짝수인 노드 삭제
              // var $menu = $("ul.menu");
              //  $("ul.menu li:even").click(function(){
              //     $(this).remove();
              // })  

             //모든 자식 노드 삭제
            $("#btnRemove").click(function(){
                $("ul.menu").children().remove();
            })

        });

  		</script>
 	</head>
 	<body>
        <button id="btnAdd">메뉴추가</button>
        <button id="btnRemove">메뉴전체삭제</button>
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
