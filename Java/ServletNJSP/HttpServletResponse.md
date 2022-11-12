#### HttpServletResponse
##### Defines an object to assist a servlet in sending a response to the client.
##### to provide HTTP-specific functionality in sending a response
```java
protected void service(
			HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException{
  
   //1) 각각 지정하는 방법
    res.setCharacterEncoding("UTF-8"); // Set character encoding of the response
    res.setContentType(""text/html");  // Set content type of the response 
   
   //2) 한번에 지정하는 방법
    res.setContentType(""text/html; charset=UTF-8");  // Set content type of the response 
  }
```
