## 속성다루기 - 이미지 애니메이션 

```html
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html charset="UTF-8">
  		<title>jQuery 속성 다루기-애니메이션</title>
  		<style type="text/css">
        body {
          font-size: 9pt;
        }

        .panel {
          width: 840px;
          height: 415px;
          border: 1px solid #ccc;
        }

        .nav {
          width: 840px;
          text-align:center;
        }
     </style>
  		<script type="text/javascript" src="./libs/jquery-3.3.1.js"></script>
  		<script>

        var index = 1; 
        var timerID = 0;
        var $view = null;
  		  $(document).ready(function(){
            $view = $("#view");

            $("#play").click(function(){
                console.log("========= play =============");
                startAutoPlay();
            })

            $("#stop").click(function(){
                console.log("========= stop =============");
                stopAutoPlay();
            })


            $("#prev").click(function(){
                console.log("========= prev =============");
                prevImage();
            })

             $("#next").click(function(){
                console.log("========= next =============");
                nextImage();
            })
          
        })

        

        function  startAutoPlay(){
          if( timerID == 0 ){
            timerID = setInterval(function(){nextImage()},100); //interval 0.1sec
          }
        }

        function stopAutoPlay(){
          if( timerID !=0 ){
            clearInterval(timerID);
            timerID = 0;
          }
        }

        function prevImage(){
            index = index - 1;
            if(index < 1) {
               index = 9;
            }
             showImage(index);
        }

         function nextImage(){
            if(index < 9){
              index = index + 1;
            }else{
              index = 1;  
            }
            showImage(index);
        }
        
        function showImage(index){
            $view.attr("src","./imgs/car_"+ index +".jpg");
        }
  			
  		</script>
 	</head>
 	<body>
      <div class="panel">
         <img src="./imgs/car_1.jpg" width="300" height="300"  id="view">
      </div>
      <div>
          <button id="play">play</button>
          <button id="stop">stop</button>
          <button id="prev">prev</button>
          <button id="next">next</button>
      </div>
 	</body>
</html>
```
