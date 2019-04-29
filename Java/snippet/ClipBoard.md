```java

import java.awt.Toolkit;
import java.awt.datatransfer.Clipboard;
import java.awt.datatransfer.DataFlavor;
import java.awt.datatransfer.StringSelection;
import java.awt.datatransfer.UnsupportedFlavorException;
import java.io.IOException;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
/*
 * clipBoard로 원하는 문자만 추출하기
 * 원하는 문자열을 ctl+c한 후 소스를 실행하면 console에 결과값이 나타남
 * 
 * */

public class ClipBoard {
	
	public static void main(String args[]) {
		paste();	
	}
	
	private static void copy() {
		System.out.println("copy()=====================================");
	    Clipboard clipboard = Toolkit.getDefaultToolkit().getSystemClipboard();
	    String text = "value";
	    StringSelection selection = new StringSelection(text);
	    clipboard.setContents(selection, null);
	    
	    
	  }

	private static void paste() {
		System.out.println("paste()=====================================");
	    Clipboard clipboard = Toolkit.getDefaultToolkit().getSystemClipboard();
	    DataFlavor flavor = DataFlavor.stringFlavor;
	    if (clipboard.isDataFlavorAvailable(flavor)) {
	      try {
	        String text = (String) clipboard.getData(flavor);
	        System.out.println(text);
	        
	        exractConvert(text) ; 
	        
	      } catch (UnsupportedFlavorException e) {
	        System.out.println(e);
	      } catch (IOException e) {
	        System.out.println(e);
	      }
	    }
	  }
	
	
	private static void exractConvert(String text) {
		System.out.println("exractConvert()=====================================");
	  // [name] = value 와 같은 패턴으로 되어 있는 문자열을 검색하는 정규표현
	 // 2개의 그룹을 포함한 정규표현식 
        //Pattern groupPattern = Pattern.compile("\\[(\\w+)] = (.+)"); //[name] = value 와 같은 패턴
        //Pattern groupPattern = Pattern.compile("\"header\": . \"(text)\": \"(.+)\""); // "header": { "text": "재고합계" },
        Pattern groupPattern = Pattern.compile("\"header\"\\s{0,}: .\\s{0,}\"(text)\"\\s{0,}: \"([가-힣a-zA-Z0-9/\\s()*n\\\\]+)\""); //   , "header" : {"text" : "수량"} 
		Matcher groupMatcher = groupPattern.matcher(text);
		
		
		//text 
		while(groupMatcher.find()) {
			String name = groupMatcher.group(1);  // 첫번째 그룹에 일치한 문자열을 구함
	        String value = groupMatcher.group(2); // 두번째 그룹에 일치한 문자열을 구함
	        //System.out.println(String.format("이름:%s, 값:'%s'", name, value));        //이름:text, 값:'수 '
	  
	        //text
	        System.out.println(String.format("'%s',", value));
		}
		
		System.out.println("==============================================================");
		
		//fieldName 
         //groupPattern = Pattern.compile("\"(fieldName)\": \"(.+)\""); //  "fieldName": "amountTotal",
         groupPattern = Pattern.compile("\"(fieldName)\"\\s{0,}: \"(\\w+)\""); //    "fieldName" : "abcAmount", 
         groupMatcher = groupPattern.matcher(text);
         
     	while(groupMatcher.find()) {
     		String name = groupMatcher.group(1);  // 첫번째 그룹에 일치한 문자열을 구함
	        String value = groupMatcher.group(2); // 두번째 그룹에 일치한 문자열을 구함
   
	        //fieldName 
	        String con_value = value.replaceAll("([A-Z]{1})", "_$1"); // aaaBbbCcc -> aaa_Bbb_Ccc
	        con_value = con_value.toUpperCase();   // aaa_Bbb_Ccc -> AAA_BBB_CCC
	        //System.out.println(String.format("%s", con_value));
	        System.out.println(String.format("%s", value));
     	}
		
		
	}

}
```
