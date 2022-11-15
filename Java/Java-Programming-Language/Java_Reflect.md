```java
@Test
public void testMethod() throws Exception {
    MyObject newobject = new MyObject();
    setVal(newobject);
    
}

//string type set same value
public void setVal(Object object) throws Exception {
    Class<?> cls = object.getClass();
    Field fieldlist[] = cls.getDeclaredFields();
    
    for (int i = 0; i < fieldlist.length; i++) {
       Field fld = fieldlist[i];
       
       if("java.lang.String".equals(fld.getType().getTypeName())){
           System.out.println("name=" + fld.getName());
           fld.setAccessible(true);
           fld.set(object, String.format("%-30s","TEST").replace('','A'));
       }
    }
}

//string type trim
public static <T> void setVoTrim(T object) {
    Class cls = object.getClass();
    Arrays.stream(cls.getDeclaredFields()).forEach(f -> {
      try {
          f.setAccessible(true);
          if (f.get(object).getClass().equals(String.class) && f.get(object) != null) {
              f.set(object, f.get(object).toString().trim());
          }
          f.setAccessible(false);
      } catch (IllegalAccessException e) {
        e.printStackTrace();
      }
    });  
       
}
```
