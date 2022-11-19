### HttpServletRequest

```txt
* getParameter : parameter 값을 String로 리턴
* getParameterNames :  parameter 이름들을 Enumeration<java.lang.String> 으로 리턴
* getParameterValues : parameter명이 같은 값을 String 배열로 리턴, 만약 1개라도 String배열로 받을 수 있다.
* getParameterMap : parameter들을 Map으로 리턴
```

```java
private static Map<String, List<String>> getParams(HttpServletRequest req) {
  final Map<String, List<String>> results = new HashMap<>();
  final Enumeration<String> names = req.getParameterNames();
  while (names.hasMoreElements()) {
    final String name = names.nextElement();
    final List<String> values = Arrays.asList(req.getParameterValues(name));
    results.put(name, values);
  }
  return results;
}
```
