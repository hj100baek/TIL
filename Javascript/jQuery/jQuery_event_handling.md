## 이벤트 핸들링

```html
<html>
	<head>
		<meta http-equiv="Content-Type" content="text/html charset="UTF-8">
  		<title>jQuery 이벤트 다루기</title>
  		<style type="text/css">
       

         div {
           border:1px solid #999;
        }

        #A1 {
           width: 320px;
           height: 320px;
           position:relative;
           float: left;
        }

        #B1,#B2 {
             width: 220px;
             height: 220px;
             position: absolute;
             top: 50%; 
             left: 50%;
             margin-top: -110px; 
             margin-left: -110px; 
        }

        #C1,#C2 {
             width: 120px;
             height: 120px;
             position: absolute;
             top: 50%; 
             left: 50%;
             margin-top: -60px; 
             margin-left: -60px; 
        }

         #A2 {
            width: 320px;
            height: 320px;
            position:relative;
            float: left;
        }

         #A3 {
           width: 320px;
           height: 320px;
           float: left;
        }


     </style>
  		<script type="text/javascript" src="./libs/jquery-3.3.1.js"></script>
  		<script>
        var count = 0;
  		  $(document).ready(function(){ 
           //캡쳐 
            document.addEventListener("click",function(e){
                count++;
                console.log("01. document phase="+ e.eventPhase, "count="+count);

                //e.stopPropagation();
            },true);

            document.body.addEventListener("click",function(e){
                count++;
                console.log("02. body phase="+ e.eventPhase, "count="+count);
            },true);

      
            $("#A1").get(0).addEventListener("click",function(e){
                count++;
                 console.log("03. A1 phase="+ e.eventPhase, "count="+count);
            },true);

             $("#B1").get(0).addEventListener("click",function(e){
                count++;
                 console.log("04. B1 phase="+ e.eventPhase, "count="+count);
            },true);

            $("#A2").get(0).addEventListener("click",function(e){
                count++;
                 console.log("05. A2 phase="+ e.eventPhase, "count="+count);
            },true);

            //타깃/버블링 
            $(document).on("click",function(e){
                count++;
                 console.log("11. document phase="+ e.eventPhase, "count="+count);
            })

           $("body").on("click",function(e){
                count++;
                 console.log("12. body phase="+ e.eventPhase, "count="+count);
            }) 

            $("#A1").on("click",function(e){
                count++;
                console.log("13. A1 phase="+ e.eventPhase, "count="+count);
            }) 

             $("#B1").on("click",function(e){
                count++;
                console.log("14. B1 phase="+ e.eventPhase, "count="+count);
            }) 

            $("#A2").on("click",function(e){
                count++;
                console.log("15. A2 phase="+ e.eventPhase, "count="+count);
            }) 

             $("#B2").on("click",function(e){
                count++;
                console.log("16. B2 phase="+ e.eventPhase, "count="+count);
            }) 

        })

  			
  		</script>
 	</head>
 	<body>
     <div id="A1">
        A1
        <div id="B1">
          B1
            <div id="C1">
              C1
            </div>
        </div>
      </div>
      
      <div id="A2">
        A2
        <div id="B2">
          B2
            <div id="C2">
              C2
            </div>
        </div>
      </div>
      
      <div id="A3">
        A3
      </div>

 	</body>
</html>
```

[이벤트 Bubbling and Capturing 참고] https://javascript.info/bubbling-and-capturing
