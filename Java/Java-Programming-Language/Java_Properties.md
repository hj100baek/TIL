```java
import java.io.IOException;
import java.util.Properties;

public class MainTest {
	
	public static void main(String[] args) {
			Properties properties  = new Properties();
			
			try {
				properties.load(new FileInputStream("project.properties"));
			} catch (FileNotFoundException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
			
			for (String key : properties.stringPropertyNames()) {
				String value = properties.getProperty(key);
				System.out.println(key + "=> " + value);
			}
			
			System.out.println(properties.getProperty("undefined"));  
	}

}
```
<pre><code>
#result
test.home2=> r2.txt
test.home1=> r1.txt
null

#project.properties file
test.home1=r1.txt
test.home2=r2.txt
</code></pre>
