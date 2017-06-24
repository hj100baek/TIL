#   중첩 try catch문
>   이중으로 중첩되어있을 경우 내부에서 발생한 exception은 내부에서 catch되고
    외부에 있는 다음 문장이 실행된다.

```java
	public static void main(String[] args) {

		int i = 4;
		int j = 0;
		int k = 0;

		try {
			try {

				//try inner
				k = i / j;

			} catch (Exception e) {
				System.out.println ("=======> catch inner exception ") ;
				System.out.println(e.getStackTrace());   
			} finally {
				System.out.println ("=======> try inner finally ") ;	
			}
			
			System.out.println ("=======> Outer Source !!! ") ;	
			System.out.println ("=======> Outer Source !!! ") ;		
			System.out.println ("=======> Outer Source !!! ") ;		
			System.out.println ("=======> Outer Source !!! ") ;		
			
		} catch (Exception e) {
			System.out.println ("=======> catch outer exception ") ;
			System.out.println(e.getStackTrace());   	
		} finally {
			System.out.println ("=======> try outer finally ") ;	
		}
	}
```
<pre><code>
[result]
=======> catch inner exception 
[Ljava.lang.StackTraceElement;@15db9742
=======> try inner finally 
=======> Outer Source !!! 
=======> Outer Source !!! 
=======> Outer Source !!! 
=======> Outer Source !!! 
=======> try outer finally 
</code></pre>
