### exports vs module.exports
##### require 키워드는 object 를 반환합니다. 그리고 module.exports 와 exports 는 call by reference 로 동일한 객체를 바라보고 있고, 리턴되는 값은 항상 module.exports 입니다.

```javascript
//module_test_main.js


var obj = require('./module_test21');
require('./module_test22')();

obj.hello();  

/*
 1) module_test21 case 1 : exports 
exports.hello = () => {
   console.log('Hello exports');
}
 result : Hello exports
 --------------------------------------------------
2) module_test21 case 2 : exports, module.exports

exports.hello = () => {
    console.log('Hello exports');
}

module.exports.hello = () => {
    console.log('Hello module.exports');
}

result : Hello module.exports

 --------------------------------------------------
3) module_test22 case 1 : exports, module.exports
exports = () => {
    console.log('Just exports');
}

module.exports = () => {
    console.log('Just module.exports');
}
result : Just module.exports
*/



```
