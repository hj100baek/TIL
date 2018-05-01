## 노드 이동

```html
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html charset="UTF-8">
  		<title>jQuery node이동</title>
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
            //클릭한 아이템을 첫 번째 자식 노드로 이동
            // var $menu = $("ul.menu");
            // $("ul.menu li").click(function(){
            //    $menu.prepend(this);
            // })
            
            //클릭한 아이템을 마지막 번째 자식 노드로 이동
            // var $menu = $("ul.menu");
            //  $("ul.menu li").click(function(){
            //     $menu.append(this);
            //  })

            //특정 노드의 이전 노드로 이동
            // var $menu = $("ul.menu");
            // $("ul.menu li").click(function(){
            //     //menu3은 대상에서 제외시키기 위함 
            //     if($(this).hasClass("select") == true)
            //       return;
            //     //menu3 이전으로 이동 
            //     $(this).insertBefore(".select");
            // })

            //특정 노드의 다음 노드로 이동
             var $menu = $("ul.menu");
             $("ul.menu li").click(function(){
                 //menu3은 대상에서 제외시키기 위함 
                 if($(this).hasClass("select") == true)
                   return;
                 //menu3 다음으로 이동 
                 $(this).insertAfter(".select");
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
