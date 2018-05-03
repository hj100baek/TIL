## 노드 핸들링 모음

```html
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html charset="UTF-8">
  		<title>jQuery node 전체 </title>
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

        var menuNm ;
  	    var $selectedItem = null;
        var $selectedItemAdd = null;

  			$(document).ready(function(){
        
          //추가
          $("#add").click(function(){
              menuNm = $("#menuName").val() ;             
              console.log(menuNm);
              var $item = $("<li>"+ menuNm +"</li>");
            
            //선택된 아이템이 있을 경우 선택된 아이템 아래 추가 
              if($selectedItem != null){
                  if($selectedItemAdd != null) {
                    $selectedItemAdd.after($item);
                    $selectedItemAdd =  $selectedItemAdd.next();  //순차적으로 추가하고 싶을경우. 이렇게 해야 추가된 객체 선택가능 
                    console.log("AA:" +$selectedItemAdd.html() );
                  }else{
                    $selectedItem.after($item);
                    $selectedItemAdd  = $selectedItem.next();     //순차적으로 추가하고 싶을경우. 이렇게 해야 추가된 객체 선택가능 
                    console.log("BB:" + $selectedItemAdd.html());
                  }  
              }else{
             // 메뉴에 신규 아이템 추가  
                 $("ul.menu").append($item);
              }
          })
        
          //선택
          $("ul.menu").on("click","li",function(){
              if($selectedItem != null) {
                  $selectedItem.removeClass("select");
               }      
              $selectedItem = $(this); 
              $(this).addClass("select");
              $selectedItemAdd = null;
          })

          //수정
          $("#update").click(function(){
            if($selectedItem){
              menuNm = $("#menuName").val() ;  
              $selectedItem.html(menuNm);
            }else{
              alert("선택된 메뉴가 없습니다.");
            }
          })

          //삭제 
          $("#remove").click(function(){
            if($selectedItem){
              $selectedItem.remove();
              $selectedItem = null;
            }else{
              alert("선택된 메뉴가 없습니다.");
            }  
          })

          //선택한 메뉴 아이템 위치를 위로 이동 
           $("#up").click(function(){
              var $prevItem = $selectedItem.prev();
              if($prevItem)
                $selectedItem.insertBefore($prevItem);
           })

           //선택한 메뉴 아이템 위치를 아래로 이동 
            $("#down").click(function(){
              var $nextItem = $selectedItem.next();
              $selectedItem.insertAfter($nextItem); 
            })
        });

  		</script>
 	</head>
 	<body>
      <div>
        <input type="text" id="menuName"/>
        <button id="add">추가</button>
        <button id="update">수정</button>
        <button id="remove">삭제</button>
        <button id="up">UP</button>
        <button id="down">DOWN</button>
      <div>    
      <ul class="menu">
      </ul>    
      

        
      
 	</body>
</html>
```
