```java
public static String addDays(String sDate, int day, String format) {
 
  SimpleDateFormat formatter = new SimpleDateFormat(format, java.util.Locale.KOREA);    
  Date date = formatter.parse(sDate);    //String -> Date
  
  date.setTime(date.getTime() + ((long) day * 1000 * 60 * 60 * 24));
  return formatter.format(date);        //Date -> String
}
```
