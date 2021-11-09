```javascript
<div class="black-bg" v-if="modalOpenFlag == true">
```
```javascript
 <p v-if="inStock">In Stock</p>
 <p v-else>Out of Stock</p>
 
 const app = Vue.createApp({
    data () {
        return {
            
            inStock: false
        }
    }

})
```
