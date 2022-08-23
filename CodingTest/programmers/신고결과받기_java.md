``` java
/**
 * 1차 실패 : 실패 (시간 초과) 
 * 정확성: 75.0
 * 합계: 75.0 / 100.0
 *
 */
public class BadUser {
	public static void main(String[] args) {
	
		
		
		String[] id_list = {"muzi", "frodo", "apeach", "neo"};
		String[] report = {"muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"};
		int k = 2;
		
		System.out.println(solution(id_list, report, k));
			
   }
		
	 public static int[] solution(String[] id_list, String[] report, int k) {
	        int[] answer = new int[id_list.length];
	    
	        Map<String, Map<String, Integer>> idBadUserMap = new LinkedHashMap<>();
	        Map<String, Integer> badUserCount = new HashMap<String, Integer>();
	        
	      //신고자 - 불량자 맵 생성
			for (int i=0; i < id_list.length ; i++) {
				Map<String, Integer> id_map = new HashMap<String, Integer>(); 
				
				for (int j=0; j < report.length; j++){
					String[] tmpIds = report[j].split(" ");
					String id = tmpIds[0]; 
					String badId= tmpIds[1];
					if (id_list[i].equals(id)) {
						id_map.put(badId, 0);					
					}
					
					idBadUserMap.put(id_list[i], id_map);				   
				}
			}	
	        
		    //불량자 - 신고당한 횟수
			 for( Entry<String, Map<String, Integer>> elem : idBadUserMap.entrySet() ){
		          System.out.println( String.format("키 -> %s, 값 -> %s", elem.getKey(), elem.getValue()) );
		           for(Entry<String, Integer> elem2 : elem.getValue().entrySet() ){
		        	   System.out.println( String.format("키 -> %s, 값 -> %s", elem2.getKey(), elem2.getValue()));
		        	   Integer prevCnt =  badUserCount.get(elem2.getKey()) == null ? 0 : badUserCount.get(elem2.getKey()) ;
		        	   badUserCount.put(elem2.getKey(), prevCnt + 1);
		           }
		      }
		    
           //최종결과 
			 int z = 0;
			 for( Entry<String, Map<String, Integer>> elem : idBadUserMap.entrySet() ){
				  for(Entry<String, Integer> elem2 : elem.getValue().entrySet() ){
					 if (badUserCount.containsKey(elem2.getKey())) {
						if ( badUserCount.get(elem2.getKey()) >= k) {
						 answer[z] = answer[z] + 1 ;
						}
					 }
				  }
				  
				  z++;
			 }
			
			System.out.println(idBadUserMap);
			System.out.println(badUserCount);
			
			for(int i = 0; i < answer.length; i++) {
			       System.out.println(answer[i]);
			}
			
	        return answer;
	    }		
		

}
```

```java
package com.devb.test;

import java.util.HashMap;
import java.util.LinkedHashMap;
import java.util.Map;
import java.util.Map.Entry;

/**
 * 2차 실패 : 실패 (시간 초과) 
 * 정확성: 75.0
 * 합계: 75.0 / 100.0
 *
 */
public class BadUser2 {
	public static void main(String[] args) {
	
		
		
		String[] id_list = {"muzi", "frodo", "apeach", "neo"};
		String[] report = {"muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"};
		int k = 2;
		
	
/*		String[] id_list = {"con", "ryan"};
		String[] report = {"ryan con", "ryan con", "ryan con", "ryan con"};
		int k = 3;
*/		
		System.out.println(solution(id_list, report, k));
			
   }
		
	 public static int[] solution(String[] id_list, String[] report, int k) {
	        int[] answer = new int[id_list.length];
	    
	        Map<String, Map<String, String>> idBadUserMap = new LinkedHashMap<>();
	        Map<String, Integer> badUserCount = new HashMap<String, Integer>();
	        
	      //신고자 - 불량자 맵 생성
			for (int i=0; i < id_list.length ; i++) {
				Map<String, String> id_map = new HashMap<String, String>(); 
				
				for (int j=0; j < report.length; j++){
					String[] tmpIds = report[j].split(" ");
					String id = tmpIds[0]; 
					String badId= tmpIds[1];
					if (id_list[i].equals(id)) {
						
						//중복제거 
						if (!id_map.containsValue(report[j])) {
						  id_map.put(badId, report[j]);
						  Integer prevCnt =  badUserCount.get(badId) == null ? 0 : badUserCount.get(badId) ;
						  badUserCount.put(badId, prevCnt + 1);
						}
					}
					
					idBadUserMap.put(id_list[i], id_map);				   
				}
			}	
	        
		
		    
           //최종결과 
			 int z = 0;
			 for( Entry<String, Map<String, String>> elem : idBadUserMap.entrySet() ){
				  for(Entry<String, String> elem2 : elem.getValue().entrySet() ){
					 if (badUserCount.containsKey(elem2.getKey())) {
						if ( badUserCount.get(elem2.getKey()) >= k) {
						 answer[z] = answer[z] + 1 ;
						}
					 }
				  }
				  
				  z++;
			 }
			
			System.out.println(idBadUserMap);
			System.out.println(badUserCount);
			
			for(int i = 0; i < answer.length; i++) {
			       System.out.println(answer[i]);
			}
			
	        return answer;
	    }		
		
		
}

```
```java
package com.devb.test;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/*
 * 3차 실패 : 실패 (시간 초과) , 중복을 For을 이용해 건건이 처리해서 더 느려짐
 * 정확성: 66.7
 * 합계: 66.7 / 100.0
 */
public class BadUser3 {
public static void main(String[] args) {
	
		
		
		String[] id_list = {"muzi", "frodo", "apeach", "neo"};
		String[] report = {"muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"};
		int k = 2;
		
	/*
		String[] id_list = {"con", "ryan"};
		String[] report = {"ryan con", "ryan con", "ryan con", "ryan con"};
		int k = 3;
	*/	
		System.out.println(solution(id_list, report, k));
			
   }
		
	 public static int[] solution(String[] id_list, String[] report, int k) {
	        int[] answer = new int[id_list.length];
	    
	        List<String> idBadUserList = new ArrayList<String>();   //중복제거한 report
	        Map<String, Integer> badUserCount = new HashMap<String, Integer>();
	        
	      
	        
	     
	    for(int i =0; i <id_list.length ; i++){
		   //중복제거 및 불량자 개수 카운트	
			for (int j=0; j < report.length; j++){
				String[] tmpIds = report[j].split(" ");
				String id = tmpIds[0]; 
				String badId= tmpIds[1];
				
				if (id.equals(id_list[i]) && !idBadUserList.contains(report[j])) {
					idBadUserList.add(report[j]);
					Integer prevCnt =  badUserCount.get(badId) == null ? 0 : badUserCount.get(badId) ;
					badUserCount.put(badId, prevCnt + 1);
				}
							   
			}
		
	    }     
			
		    
           //최종결과 		
	         int lastIdIdx = 0;
	         loop1:
			 for(int i = 0; i <id_list.length ; i++){
				loop2:
				 for (int j=lastIdIdx; j < idBadUserList.size(); j++){
					 String[] tmpIds = idBadUserList.get(j).split(" ");
					 String id = tmpIds[0]; 
					 String badId= tmpIds[1];
					
					 if (id.equals(id_list[i])) { 
						if ( badUserCount.containsKey(badId) && badUserCount.get(badId) >= k) {
							 answer[i] = answer[i] + 1 ;
						}
										
					 } else {
						 lastIdIdx = j ;		
						 continue loop1;
					 }
					 
					
				 }

			 }
		
			System.out.println(idBadUserList); 
			System.out.println(badUserCount);
			
			for(int i = 0; i < answer.length; i++) {
			       System.out.println(answer[i]);
			}
			
	        return answer;
	    }		
}
```

```java
/*
 * 4차 성공 : 중복제거 시 HashSet 사용. 대량건이 되면 일반 for문 처리와 속도차이나 나는듯. 
 *           최종결과 설정시 실패했을 경우는 중복제거한 report를 중심으로 for문 처리. report가 가장 데이터 양이 많으므로 사용하지 않도록 수정
 * 정확성: 100.0
합계: 100.0 / 100.0
 */
public class BadUser4 {
public static void main(String[] args) {
	
		
		
		String[] id_list = {"muzi", "frodo", "apeach", "neo"};
		String[] report = {"muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"};
		int k = 2;
		
	/*
		String[] id_list = {"con", "ryan"};
		String[] report = {"ryan con", "ryan con", "ryan con", "ryan con"};
		int k = 3;
	*/	
		System.out.println(solution(id_list, report, k));
			
   }
		
	 public static int[] solution(String[] id_list, String[] report, int k) {
	      int[] answer = new int[id_list.length];
		    
	      //  List<String> idBadUserList = new ArrayList<String>();   //중복제거한 report
	        Map<String, Integer> badUserCount = new HashMap<String, Integer>();
	        
	
         //중복제거 		
	     
			 List<String> list = Arrays.asList(report);
			 HashSet<String> idBadUserSet = new HashSet<>(list);
			 for (String tmpId : idBadUserSet) {
				 String[] tmpIds = tmpId.split(" ");
				 String id = tmpIds[0]; 
				 String badId= tmpIds[1];
				 Integer prevCnt =  badUserCount.get(badId) == null ? 0 : badUserCount.get(badId) ;
				 badUserCount.put(badId, prevCnt + 1);
			 }
			 
			 
			 
			 
		//최종결과 		
	     
			 for(int i = 0; i <id_list.length ; i++){
				 
				 for(Entry<String, Integer> elem : badUserCount.entrySet() ){					
					if (elem.getValue() >= k && idBadUserSet.contains(id_list[i]+" "+elem.getKey() )) {
						 answer[i] = answer[i] + 1 ;
						 idBadUserSet.remove(id_list[i]+" "+elem.getKey());
					}
				}
				  

			 }
			 
			 
		
			System.out.println(idBadUserSet); 
			System.out.println(badUserCount);
			
			for(int i = 0; i < answer.length; i++) {
			       System.out.println(answer[i]);
			}
			
	        return answer;
	    }	
	 
	  

}
```
