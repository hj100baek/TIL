#### javascript callback

```javascript
// 1) 함수자체를 파라미터로 넘기는경우

function callTestMain() {
     callTest(test1, function(res){
        console.log("=========callTestMain.callTest================");  
        console.log(res);          
     });
}


function callTest (fun1,callbackFunc) {
     callbackFunc(fun1);  //차이점
}

function test1(param) {
   console.log("==============test1================");
   
   return "test1" + param ;
}

//////////////// 결과값////////////////////////
=========callTestMain.callTest================
ƒ test1(param) {
   console.log("==============test1================");
   
   return "test1" + param ;
}


// 2) 함수 결과값을 받는 경우
function callTestMain() {
     callTest(test1, function(res){
        console.log("=========callTestMain.callTest================");  
        console.log(res);          
     });
}


function callTest (fun1,callbackFunc) {
     callbackFunc(fun1('Hello'));   //차이점
}

function test1(param) {
   console.log("==============test1================");
   
   return "test1" + param ;
}

//////////////// 결과값////////////////////////
==============test1================
=========callTestMain.callTest================
test1Hello

```
