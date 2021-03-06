```java

//중복된 key가 있으면 긴것부터 처리하도록 로직 추가

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Comparator;
import java.util.LinkedHashMap;
import java.util.List;
import java.util.Map;
import java.util.Map.Entry;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public class MultipleReplace3 {

	static String findReplacefilePath = "C:/convertemp/find_replace3.txt"; // 변환대상 ASIS:TOBE
	static String targetfileName = "find_replace3"; // 변환결과 파일명
	static String targetfilePath = "C:/convertemp/" + targetfileName + ".xml";
	static Map<String, String> findReplaceMap = null;
	static Map<String, String> tableMap = null;
	static Map<String, String> columnMap = null;
	static LinkedHashMap<String, String> columnMap2 = null;

	public static void main(String[] args) {
		// 파일명을 변수로 받고 싶다면
		if (args.length == 1) {
		  targetfileName = args[0];
		  String targetfilePath = "C:/convertemp/" + targetfileName + ".xml";
		}
		
		readFindReplaceFile();
		replaceFile();
	}

	private static void readFindReplaceFile() {

		try {
			Stream<String> stream = Files.lines(Paths.get(findReplacefilePath));
			findReplaceMap = stream

					.filter(s -> s.contains(":")).map(s -> s.replace(" ", ""))
					.collect(Collectors.toMap(k -> String.valueOf(k.split(":")[0]),
							v -> String.valueOf(v.split(":")[1]), (asis, tobe) -> asis))

			;

			stream.close();

			System.out.println(findReplaceMap);

			tableMap = findReplaceMap.entrySet().stream().filter(map -> map.getKey().contains("TB_"))
					.collect(Collectors.toMap(map -> map.getKey(), map -> map.getValue()));

			columnMap = findReplaceMap.entrySet().stream().filter(map -> !map.getKey().contains("TB_"))
					// .sorted((e1, e2) -> Integer.compare(e2.getKey().length(),
					// e1.getKey().length()))
					// .sorted(new StringLengthComparator().reversed())
					.collect(Collectors.toMap(map -> map.getKey(), map -> map.getValue()))

			;

			System.out.println(tableMap);
			System.out.println(columnMap);
			System.out.println(columnMap2);

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
		String convertline = "";  //중복키값때문에 추가

		try {
			while ((line = file.readLine()) != null) {
				convertline = line;
				
				// original
				inputBuffer.append(line);
				inputBuffer.append('\n');

				// convert - column
				if (line.contains("TB_")) {

					for (Map.Entry<String, String> entry : tableMap.entrySet()) {
						convertline = convertline.replaceAll("(?i)" + entry.getKey(), entry.getValue().toLowerCase());
						convertline = convertline.replaceAll("[$]\\{", "#{");
					}
				} else {
					for (Map.Entry<String, String> entry : columnMap.entrySet()) {
          
						Map<String, String> sameStartCols = columnMap.entrySet().stream()
								.filter(s -> s.getKey().startsWith(s.getKey())).collect(Collectors.toMap(map -> map.getKey(), map -> map.getValue()));
						
						List<Map.Entry<String, String>> sorted = sameStartCols.entrySet().stream().sorted(new StringLengthComparator2()).collect(Collectors.toList());
						
						if (sorted.size() > 0) {
							for (Map.Entry<String, String> entry2 : sorted) {
								//System.out.println("-------------sorted line:" + line + "\n");
								//System.out.println("-------------sorted getKey:" +  entry2.getKey() + "\n");
								convertline = convertline.replaceAll("(?i)" + entry2.getKey(), entry2.getValue().toLowerCase());
								convertline = convertline.replaceAll("[$]\\{", "#{");
								
								if (!convertline.equals(line)) {
									System.out.println("-------------sorted convertline line:" + convertline + "\n");
									break;
								}
								System.out.println("-------------sorted after line:" + line + "\n");
							}
						
						} else {
					
							convertline = convertline.replaceAll("(?i)" + entry.getKey(), entry.getValue().toLowerCase());
							convertline = convertline.replaceAll("[$]\\{", "#{");
						}
					}
				}

				convertBuffer.append(convertline);
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
			fileOut = new FileOutputStream("C:/convertemp/" + targetfileName + "_conv.xml");
		} catch (FileNotFoundException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
		try {
			// fileOut.write(inputStr.getBytes());
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

class StringLengthComparator2 implements Comparator<Entry<String, String>> {

	@Override
	public int compare(Entry<String, String> o1, Entry<String, String> o2) {
		//System.out.println("o1:" + o1);
		//System.out.println("o2:" + o2);
		return o2.getKey().length() - o1.getKey().length();// compare length of Strings
	}

}


```
