
```javascript
 //route_loader.js  --- do it 책에는 소스가 없으니 참고

var config = require('../config');

var route_loader = {};



route_loader.init = function(app, router){
    console.log('route_loader init() 호출됨.');
    return initRoutes(app, router);    
}

function initRoutes(app, router) {

	var infoLen = config.route_info.length;
	console.log('설정에 정의된 route_info의 수 : %d' , infoLen);
 
	for (var i = 0; i < infoLen; i++) {
		var curItem = config.route_info[i];
			

		var curModule = require(curItem.file);
		console.log('%s 설정에 정의된 file.', curItem.file);
		
	
		if (curItem.type == 'get') {
            router.route(curItem.path).get(curModule[curItem.method]);
		} else if (curItem.type == 'post') {
            router.route(curItem.path).post(curModule[curItem.method]);
		} else {
			router.route(curItem.path).post(curModule[curItem.method]);
		}
		
		
		console.log('설정에 정의된 method.', curItem.method);
	}

    
    app.use('/', router);
}

module.exports = route_loader;
```
