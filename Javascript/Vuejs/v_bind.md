#### v-bind

```js
--index.html
<!DOCTYPE html>
<html>
    <head>
        <body>
            <div id="app">
                <h1>{{ product }}</h1>
                <p></p>
                <a v-bind:href="url">{{ url }}</a>
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
        product : 'Stocks',
        url: "http://google.com"
    }
})
```
