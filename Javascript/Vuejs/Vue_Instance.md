#### Vue_Instance

```js
--index.html
<!DOCTYPE html>
<html>
    <head>
        <body>
            <div id="app">
                <h1>{{ product }}</h1>
            </div>

            
<script src="https://cdn.jsdelivr.net/npm/vue/dist/vue.js"></script>
<script src="main.js"></script>
        </body>
    </head>
</html>

--main.js
var app = new Vue({
    el: '#app',
    data: {
        product : 'Stocks'
    }
})
```

```js
var vm = new Vue({
  // 옵션
})
```
