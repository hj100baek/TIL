#### Vuejs3 and tailwind 
* install  
1) nodejs install
2) npm install -g @vue/cli  (https://cli.vuejs.org/)
3) vue create my-project
4) cd my-project
5) npm install -D tailwindcss postcss autoprefixer (https://tailwindcss.com/docs/guides/vite)
6) npx tailwindcss init -p
7) change tailwind.config.js  
 ```
 module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```
8) Create a ./src/index.css file  
```
@tailwind base;
@tailwind components;
@tailwind utilities;
```
9) Import the CSS file  
```
// ./src/main.js
import { createApp } from 'vue'
import App from './App.vue'
import './index.css'

createApp(App).mount('#app')
```
10) npm run serve
