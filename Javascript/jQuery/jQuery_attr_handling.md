## 속성다루기

```html
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html charset="UTF-8">
  		<title>jQuery 속성 다루기</title>
  		<style type="text/css">
     </style>
  		<script type="text/javascript" src="./libs/jquery-3.3.1.js"></script>
  		<script>

  		  $(document).ready(function(){
            //속성값 출력 
            console.log("src="+ $(".header img").attr("src"));
            console.log("href="+ $(".header a").attr("href"));

            //사용자 속성 출력 
            var $panel = $("div.panel");

            console.log("1. data() =" + $panel.data());
            console.log("2. data(name) =" + $panel.data("name"));
            console.log("2. data(name) =" + $panel.data("tel"));
            console.log("3. attr(data-name) =" + $panel.attr("data-name"));
            console.log("4. attr(temp-data) =" + $panel.attr("temp-data"));

      
            //클릭할때 마다 이미지 변경
            var $fish = $("#fish");
            var sw=false;
            $fish.click(function(){
              sw=!sw;
              if(sw == true) {
                  $fish.attr("src","https://kr.seaicons.com/wp-content/uploads/2015/10/Pisces-2-icon.png");
              } else {
                  $fish.attr("src","https://kr.seaicons.com/wp-content/uploads/2015/06/Animals-Fish-icon.png");
              }
            })

            //panel1~3 각 이미지를 클릭할때 마다 이미지 변경 
            var $targetList = $(".target");
            var swInfo=[false,false,false];

            $targetList.click(function(){
                var $target = $(this);
              
              //인덱스 이용시   
              // var index = $targetList.index($(this));  
              // swInfo[index] =!swInfo[index];
              // if(swInfo[index] == true) {
              //     $target.attr("src","./imgs/fish-icon2.jpg");
              // } else {
              //     $target.attr("src","./imgs/fish-icon1.jpg");
              // }

              //data속성 이용시 
               var sw = !$target.data("sw");
               $target.data("sw",sw);

               if(sw == true) {
                  $target.attr("src","./imgs/fish-icon2.jpg");
               }else{
                  $target.attr("src","./imgs/fish-icon1.jpg");
               }
                
            })
        })
  			
  		</script>
 	</head>
 	<body>
      <div class="header">
        <img src="https://kr.seaicons.com/wp-content/uploads/2015/06/Animals-Fish-icon.png" width="256" height="256"  id="fish">
         <img src="https://kr.seaicons.com/wp-content/uploads/2015/10/Pisces-2-icon.png" width="256" height="256" id="fish2">
        <a href="http://www.naver.com">네이버</a>
      </div>   

      <div class="panel" data-name="딴동네" data-tel="010-1234-5678" temp-data="test1">
          <p class="name"> 딴동네</p>
          <p class="tel">010-1234-5678</p>
      </div>


      <div class="panel1">
        <p>테스트1</p>
         <img src="./imgs/fish-icon1.jpg" width="256" height="256"  class="target" data-sw="false">
      </div>

       <div class="panel2">
        <p>테스트2</p>
          <img src="./imgs/fish-icon1.jpg" width="256" height="256"  class="target" data-sw="false">
      </div>

      <div class="panel3">
        <p>테스트3</p>
         <img src="./imgs/fish-icon1.jpg" width="256" height="256"  class="target" data-sw="false">
      </div>

 	</body>
</html>
```
