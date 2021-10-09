```js
  <div class="menu">
    <a v-for="(menuNm,i) in menus" :key="i">{{ i }} {{ menuNm }}</a> //===>  0 Home 1 Shop 2 Products 3 About
    <a v-for="menuNm in menus" :key="menuNm">{{ menuNm }}</a>        //===>  Home  Shop  Products  About                
  </div>

<script>
export default {
  name: 'App',
  data(){
    return {
      menus : ['Home','Shop', 'Products', 'About']
    }
  },
  components: {
 
  }
}
</script>

<style>
  .menu {
  background: darkslateblue;
  padding: 15px;
  border-radius : 5px;
}

.menu a {
  color: white;
  padding: 10px;
}

</style>
```
