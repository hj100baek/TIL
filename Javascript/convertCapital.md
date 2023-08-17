```javascript
// AAA_BBB_CCC  =>  aaaBbbCcc
function convertCapital() {
   var textVal = document.getElementById('myTextArea');
   var lines = textVal.value.split('\n');

   var textVal2 = document.getElementById('myTextArea2');
    textVal2.value = '';


   for (var i =0; i < lines.length; i++) {
       lines[i] = lines[i].toLowerCase();
       var lineValArr = lines[i].split("_");
        for (var j=1; j < lineValArr.length; j++) {
             lineValArr[j] = lineValArr[j].charAt(0).toUpperCase +  lineValArr[j].slice(1);  
        }
        var lineValConvert = lineValArr.join("");
        console.log(`line ${i}: ${lineValCOnvert}`);

        textVal2.value += lineValConvert + '\n';
   }

}
```
