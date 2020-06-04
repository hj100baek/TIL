#### EventEmitter
- 노드는 대부분 이벤트를 기반으로 하는 비동기 방식으로 처리
- 노드는 이벤트를 보내고 받을 수 있도록 EventEmitter 이용
- 노드 객체는 EventEmitter를 상속받을 수 있음

```
const EventEmitter = require('events');
const emitter = new EventEmitter();

//Register a listener
emitter.on('messageLogged', function(){
  console.log('Listner called');
});

//Raise an event
emitter.emit('messageLogged');

================================
[result]
Listner called
```
