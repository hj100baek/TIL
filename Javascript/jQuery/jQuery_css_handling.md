## 스타일 다루기

```html
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html charset="UTF-8">
  		<title>jQuery css처리</title>
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
        .border {
          border: 1px #ff0000 solid;
        }
 
      </style>
  		<script type="text/javascript" src="./libs/jquery-3.3.1.js"></script>
  		<script>
  		
  			$(document).ready(function(){
            //li 글자 크기 출력 
            console.log("font-size="+ $("ul.menu li").css("font-size"))

            //메뉴 너비와 높이 출력
            var info = $("ul.menu").css(["width", "height"]);
            console.log("width="+ info.width +",height="+ info.height );

            //선택 메뉴 아이템 글자크기 1px씩 증가 
            // var $item = $("ul.menu li.select");
            // $("#btnTest").click(function(){
            //     var fontSize = parseInt($item.css("fontSize"));
            //     $item.css("fontSize", fontSize+1);
            // })

            //폰트 크기 11부터 시작해 5씩 증가 
             // $("#btnTest").click(function(){
             //    var size =11;
             //    $("ul.menu li").each(function(index){
             //        $(this).css("fontSize", size);
             //        size+=5;
             //    })
             // })

             //선택메뉴 아이템의 너비와 높이를 100px
            // $("#btnTest").click(function(){
            //         $("ul.menu li.select").css({
            //             width:100,
            //             height:100

            //         })
            //  })

            //클래스 추가 
             // $("ul.menu li").click(function(){
             //    $(this).addClass("select");
             // })

             //클래스 여러개 추가 
             // $("ul.menu li").click(function(){
             //     $(this).addClass("select border");
             //  })

             //클릭한 메뉴 아이템에 클래스 적용되있으면 제거 , 없으면 추가 
             // $("ul.menu li").click(function(){
             //      var $item = $(this)
             //      if($item.hasClass("select") == false)
             //          $item.addClass("select");
             //      else
             //          $item.removeClass("select");

             // })

             //toggleClass() 이용하기 
             // $("ul.menu li").click(function(){
             //    $(this).toggleClass("select");
             // })
                
             //메뉴 항목에 모든 클래스 제거       
             $("#btnRemove").click(function(){
                $("ul.menu li").each(function(){
                    $(this).removeClass();
                })
             })
        });

  		</script>
 	</head>
 	<body>
        <button id="btnTest">실행</button>
        <button id="btnRemove">제거</button>
        <ul class="menu">
          <li>menu1</li>
          <li>menu2</li>
          <li class="select">menu3</li>
          <li>menu4</li>
          <li>menu5</li>
        </ul>
      
 	</body>
</html>
```
