```java


import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class MultipleReplace {



	static String findReplacefilePath = "C:/convertemp/find_replace3.txt";  //변환대상 ASIS:TOBE
	static String targetfileName = "find_replace3";                         //변환결과 파일명
	static String targetfilePath = "C:/convertemp/"+ targetfileName +".xml";
	static Map<String, String> findReplaceMap = null;
	static Map<String, String> tableMap = null;
	static Map<String, String> columnMap = null;
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		readFindReplaceFile() ;
		replaceFile();
	}
	
	
	private static void readFindReplaceFile() {

		try {
			Stream<String> stream = Files.lines(Paths.get(findReplacefilePath));
			findReplaceMap = stream
					                .collect(Collectors.toMap(k-> String.valueOf(k.split(":")[0]), v->String.valueOf(v.split(":")[1]),
					            		   (asis, tobe)-> asis));
			
			stream.close();
			
			System.out.println(findReplaceMap);
		
			tableMap = findReplaceMap.entrySet() 
			          .stream() 
			          .filter(map -> map.getKey().contains("TB_")) 
			          .collect(Collectors.toMap(map -> map.getKey(), map -> map.getValue()));  
			
			columnMap = findReplaceMap.entrySet() 
			          .stream() 
			          .filter(map -> !map.getKey().contains("TB_")) 
			          .collect(Collectors.toMap(map -> map.getKey(), map -> map.getValue())); 
			 
				System.out.println(tableMap);
				System.out.println(columnMap);
			
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	}
	
	private static void replaceFile() {
		 BufferedReader file = null;
		try {
			file = new BufferedReader(new FileReader(targetfilePath));
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
	        StringBuffer inputBuffer = new StringBuffer();
	        StringBuffer convertBuffer = new StringBuffer();
	        String line;

	        try {
				while ((line = file.readLine()) != null) {
				    
					//original
					inputBuffer.append(line);
				    inputBuffer.append('\n');
				    
				    //convert - column
				    if(line.contains("TB_")){
				    	 
				    	 for (Map.Entry<String, String> entry : tableMap.entrySet() ) {
						    	line = line.replaceAll("(?i)"+entry.getKey(), entry.getValue().toLowerCase());
						    	line = line.replaceAll("[$]\\{", "#{");
						    }	
				    }else {
				    	  for (Map.Entry<String, String> entry : columnMap.entrySet() ) {
						    	line = line.replaceAll("(?i)"+entry.getKey(), entry.getValue().toLowerCase());
						    	line = line.replaceAll("[$]\\{", "#{");
						    }
				    }
				  
					convertBuffer.append(line);
					convertBuffer.append('\n');
				    
				}
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
	        try {
				file.close();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
	        String inputStr = inputBuffer.toString();
	        
	        System.out.println(inputStr); // display the original file for debugging
	        
	       
	      
	        System.out.println("----------------------------------\n" + convertBuffer);
	        
	        // write the new string with the replaced line OVER the same file
	        FileOutputStream fileOut = null;
			try {
				fileOut = new FileOutputStream("C:/convertemp/"+ targetfileName +"_conv.xml");
			} catch (FileNotFoundException e1) {
				// TODO Auto-generated catch block
				e1.printStackTrace();
			}
	        try {
				//fileOut.write(inputStr.getBytes());
				fileOut.write(convertBuffer.toString().getBytes());
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
	        try {
				fileOut.close();
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
	}

}


```
