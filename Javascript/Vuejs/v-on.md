
v-on : 메소드 이벤트 핸들러
```javascript
<div id="example-3">
  <button v-on:click="say('hi')">Say hi</button>    //v-on:click or @click  , click이벤트 외에 다른 이벤트들도 가능 <div @click.ctrl="doSomething">Do something</div>
  <button v-on:click="say('what')">Say what</button>
</div>

new Vue({
  el: '#example-3',
  methods: {                      //methods에 fucttion을 선언한다.
    say: function (message) {
      alert(message)
    }
  }
})

```
