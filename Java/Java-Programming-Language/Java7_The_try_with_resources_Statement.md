### The try-with-resources Statement

   Q: 리소스를 가진 try문?
   
    +  AutoCloseable or Closeable interfaces 를 구현한 경우만 try resource로 사용될 수 있음
    +   try resource를 사용할 경우는 finally없어도 Statement가 끝나면 자동으로 resources를 close해준다.

   ```java
  // java7 이전
  public class TryWithoutResources {

 public static void main(String[] args) throws IOException {
    CharArrayWriter chw = null;

   try {
      System.out.println("TryWithoutResources try");
     String str = "Try without Resources";

     chw = new CharArrayWriter();
     chw.write(str);

     char[] ch = chw.toCharArray();

     for(char c : ch) {
        System.out.println(c);
     }

   } catch(Exception e) {
      System.out.println("TryWithoutResources catch");
     e.printStackTrace();

   } finally{
      System.out.println("TryWithoutResources finally");
      if(chw!=null)
             chw.close();
   }

    System.out.println("TryWithoutResources End");
 }

}

  ```

  ```java
 // java7 이후
 public class TryWithResources {
	public static void main(String[] args) throws IOException {
		try(
				CharArrayWriter chw =  new CharArrayWriter();
		   ) {
			 System.out.println("TryWithResources try");
			String str = "Try with Resources";

			chw.write(str);

			char[] ch = chw.toCharArray();

			for(char c : ch) {
				 System.out.println(c);
			}

		} catch(Exception e) {
			 System.out.println("TryWithResources catch");
			e.printStackTrace();

		}

		 System.out.println("TryWithResources End");
	}
}
 ```
