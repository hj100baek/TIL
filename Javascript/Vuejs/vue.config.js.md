### * vue.config.js is an optional config file that will be automatically loaded by @vue/cli-service

```
module.exports = {
  devServer: {
	  port: 8082,   //vue service port
	  proxy: {
		  '/api': {
			  target: 'http://localhost:8081',   //rest-api service port
			  ws: true,
			  changeOrigin: true
		  }
	  }
  }
}
```

##### - devServer
#####   Some values like host, port and https may be overwritten by command line flag
