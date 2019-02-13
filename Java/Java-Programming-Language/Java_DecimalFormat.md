```java
package com.test;

import java.text.DecimalFormat;
import java.text.NumberFormat;
import java.util.ArrayList;
import java.util.List;
import java.util.Locale;

/**
 * The preceding example created a DecimalFormat object for the default Locale. 
 * If you want a DecimalFormat object for a nondefault Locale, you instantiate a NumberFormat and then cast it to DecimalFormat
 *    
 * */
public class DecimalFormatTest {

	private static final String DEFAULT_COLUMN_NAME_PREFIX = "AB";
	private static final double DEFAULT_NUMBER = 12345.67;

	public static void main(String[] args) {
		System.out.println("getDummyHeader():" + getDummyHeader(3));  //[AB0001, AB0002, AB0003]
		
		String pattern = "###,###.###";
		DecimalFormat myFormatter = new DecimalFormat(pattern);
		String output = myFormatter.format(DEFAULT_NUMBER);
		System.out.println(DEFAULT_NUMBER + " " + pattern + " " + output); //12345.67 ###,###.### 12,345.67

		pattern = "###.##";
		myFormatter = new DecimalFormat(pattern);
	    output = myFormatter.format(DEFAULT_NUMBER);
		System.out.println(DEFAULT_NUMBER + " " + pattern + " " + output); //12345.67 ###.## 12345.67
		
		pattern = "000000.000";
		myFormatter = new DecimalFormat(pattern);
	    output = myFormatter.format(DEFAULT_NUMBER);
		System.out.println(DEFAULT_NUMBER + " " + pattern + " " + output); //12345.67 000000.000 012345.670
		
		pattern = "\uFFE6###,###.###";
		myFormatter = new DecimalFormat(pattern);
	    output = myFormatter.format(DEFAULT_NUMBER);
		System.out.println(DEFAULT_NUMBER + " " + pattern + " " + output); //12345.67 ￦###,###.### ￦12,345.67
		
		
		Locale currentLocale = Locale.getDefault();
		System.out.println(currentLocale.toString());                      //ko_KR
		System.out.println(currentLocale.getDisplayLanguage());            //한국어
		
		NumberFormat nf = NumberFormat.getNumberInstance(currentLocale);
		DecimalFormat df_local = (DecimalFormat)nf;
		pattern = "###,###.###";
		df_local.applyPattern(pattern);
		output = df_local.format(DEFAULT_NUMBER);
		System.out.println(DEFAULT_NUMBER + " " + pattern + " " + output);  //12345.67 ###,###.### 12,345.67
	}

	private static List<String> getDummyHeader(int maxColumns){
		List<String> dummy = new ArrayList<String>(maxColumns);
		DecimalFormat df = new DecimalFormat("0000");
		for (int i = 0; i < maxColumns; i++) {
			dummy.add(DEFAULT_COLUMN_NAME_PREFIX + df.format(i + 1));
		}
		return dummy;
	}
	
    

}

```
