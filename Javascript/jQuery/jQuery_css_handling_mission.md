## CSS속성으로 아이콘 랜덤이동

```html
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html charset="UTF-8">
  		<title>jQuery css로 물고기 이동</title>
  		<style type="text/css">
       #panel {
          width:600px;
          height:500px;
          border:1px solid #999;
          position:relative;
       }
       #fish {
          position: absolute;
          left:250px;
          top:150px;
       }
      </style>
  		<script type="text/javascript" src="./libs/jquery-3.3.1.js"></script>
  		<script>
  		  window.onload=function(){
            var $fish = $("#fish");

            //패널 너비, 높이 
            var panelWidth = parseInt($("#panel").css("width"));
            var panelHeight= parseInt($("#panel").css("height"));


            //물고기 최대 움직일 영역 구하기 
            panelWidth = panelWidth - parseInt($("#fish").css("width"));
            panelHeight= panelHeight - parseInt($("#fish").css("height"));

            $("#btnStart").click(function(){
                var left = parseInt(Math.random()*panelWidth);
                var top = parseInt(Math.random()*panelHeight);

                $fish.css({
                   left:left,
                   top:top
                })
            });
        }
  			
  		</script>
 	</head>
 	<body>
      <div>
        <button id="btnStart">클릭하면 물고기가 움직여요.</button>
      </div>
      <div id="panel">
        <img src="https://kr.seaicons.com/wp-content/uploads/2015/06/Animals-Fish-icon.png" width="256" height="256"  id="fish">
      </div>   
 	</body>
</html>
```
