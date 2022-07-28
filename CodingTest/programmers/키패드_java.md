```java

/**
 * 결과 : 60/ 100
 * 원인: 1차원적 접근 . 직선형으로만 숫자차이 생각함 . 2차원 배열만들기 싫어서 center 라인만 어떻게 해보려함.
 */
public class KeyPad {
	public static void main(String[] args) {
				
		int[] numbers = {0, 2, 9, 8, 5};  
		System.out.println(solution(numbers, "left"));
	}
	
	 public static String solution(int[] numbers, String hand) {	        
	        int last_left_number = 10; //*
	        int last_right_numer = 12; //#
	        int current_number = 0;	        
	        String answer = "";
	        for (int idx=0 ; idx< numbers.length; idx++) {
	        	current_number = numbers[idx];
	            if (current_number == 1 || current_number == 4 || current_number == 7) {
	                answer = answer + "L";
	                last_left_number = numbers[idx];
	            } else if  (current_number == 3 ||current_number == 6 || current_number == 9) {
	                answer = answer + "R";
	                last_right_numer = numbers[idx];
	            } else {
	              	            	
	             
	              int left_gap = Math.abs((current_number == 0 ? 11 : current_number)- (last_left_number == 0 ? 11 :  last_left_number));
	              int right_gap = Math.abs((current_number == 0 ? 11 : current_number) - (last_right_numer == 0 ? 11 :  last_right_numer));
	              
	              if (centerNumberChck(current_number) && !centerNumberChck(last_left_number)  && !centerNumberChck(last_right_numer) ) {
	            	
	            	  if (left_gap >= 3) {
	            		  left_gap = (int) Math.ceil(left_gap / (3 * 1.0));  
	            	  }
	            	  if (right_gap >= 3) {
	            		  right_gap = (int)Math.ceil(right_gap / (3 * 1.0)); 
	            	  }	            	
	            	
	              } else {
	            	   
		              if (centerNumberChck(last_left_number)) {
		            	  if (left_gap >= 3) {
		            		  left_gap = (int) Math.ceil(left_gap / (3 * 1.0));  
		            	  }
		              }
		              
		              if (centerNumberChck(last_right_numer)) {
		            	  if (right_gap >= 3) {
		            		  right_gap = (int)Math.ceil(right_gap / (3 * 1.0)); 
		            	  }
		              }
	              }
	            	
	            
	          
	               if (left_gap < right_gap)  {
	                   answer = answer + "L";
	                   last_left_number = numbers[idx];
	               } else if  (left_gap > right_gap)  {
	                   answer = answer + "R";
	                   last_right_numer = numbers[idx];
	               } else {
	            	   if (centerNumberChck(current_number) && !centerNumberChck(last_left_number)  && !centerNumberChck(last_right_numer) ) {
	            		   int left_line_gap =  Math.abs(numberLine((current_number == 0 ? 11 : current_number)) -  numberLine((last_left_number == 0 ? 11 :  last_left_number))) ;
		            	   int right_line_gap = Math.abs(numberLine((current_number == 0 ? 11 : current_number)) -  numberLine((last_right_numer == 0 ? 11 :  last_right_numer))) ;
			            	   if (left_line_gap < right_line_gap) {
			            		   answer = answer + "L";
				                   last_left_number = numbers[idx];
			            	   } else if (left_line_gap > right_line_gap) {
			            		   answer = answer + "R";
			            		   last_right_numer = numbers[idx];
			            	   } else {
		            	   
				                   if (hand.equals("left")) {
				                        answer = answer + "L";
				                        last_left_number = numbers[idx];
				                   } else {
				                        answer = answer + "R";
				                        last_right_numer = numbers[idx];
				                   }
			            	   }
	            	   } else {
	            		   if (hand.equals("left")) {
		                        answer = answer + "L";
		                        last_left_number = numbers[idx];
		                   } else {
		                        answer = answer + "R";
		                        last_right_numer = numbers[idx];
		                   }
	            	   }
	            	  
	               }
	            }
	            
	        }
	        
	        
	        return answer;
	    }
	 
	 public static boolean centerNumberChck(int num) {
		 return (num == 2 || num == 5 || num == 8 || num == 0) ;
	 }
	
	 public static int numberLine(int num) {
		 return (int) Math.ceil(num/(3*1.0));
		 
	 }
	
}

```

```java
/**
 * 결과 : 100/ 100
 * 원인: 2차원적 접근. X축(1~3)과 Y축(1~4) 의 차이를 모두 구해서 차이를 구함
  */ 
public class KeyPad2 {
	public static void main(String[] args) {
		
	
		int[] numbers = {7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2};  // left LRLLRRL L LR R - pass
		//LRLLRRLLLRR
		//LRLLRRLLLRR
		System.out.println(solution(numbers, "left"));
	
	}
	
	 public static String solution(int[] numbers, String hand) {	        
	        int last_left_number = 10; //*
	        int last_right_numer = 12; //#
	        int current_number = 0;	        
	        String answer = "";
	        for (int idx=0 ; idx< numbers.length; idx++) {
	        	current_number = numbers[idx];
	            if (current_number == 1 || current_number == 4 || current_number == 7) {
	                answer = answer + "L";
	                last_left_number = numbers[idx];
	            } else if  (current_number == 3 ||current_number == 6 || current_number == 9) {
	                answer = answer + "R";
	                last_right_numer = numbers[idx];
	            } else {
	              	            	
	             
	              int x_left_gap = Math.abs(numberXLine(numberZeroConvert(current_number)) - numberXLine(numberZeroConvert(last_left_number)));
	              int y_left_gap = Math.abs(numberYLine(numberZeroConvert(current_number)) - numberYLine(numberZeroConvert(last_left_number)));	              
	              int left_gap = x_left_gap + y_left_gap;
	              
	              int x_right_gap = Math.abs(numberXLine(numberZeroConvert(current_number)) - numberXLine(numberZeroConvert(last_right_numer)));
	              int y_right_gap = Math.abs(numberYLine(numberZeroConvert(current_number)) - numberYLine(numberZeroConvert(last_right_numer)));	              
	              int right_gap = x_right_gap + y_right_gap;
	           
	          
	               if (left_gap < right_gap)  {
	                   answer = answer + "L";
	                   last_left_number = numbers[idx];
	               } else if  (left_gap > right_gap)  {
	                   answer = answer + "R";
	                   last_right_numer = numbers[idx];
	               } else {
	
	            		   if (hand.equals("left")) {
		                        answer = answer + "L";
		                        last_left_number = numbers[idx];
		                   } else {
		                        answer = answer + "R";
		                        last_right_numer = numbers[idx];
		                   }
	               }
	            }
	            
	        }
	        
	        
	        return answer;
	    }
	 
	 public static int numberZeroConvert(int num) {
		 return (num == 0) ? 11 : num;
		 
	 }

	 public static int numberXLine(int num) {
		 return (num % 3 == 0) ? 3 : (num % 3);
		 
	 }
	 public static int numberYLine(int num) {
		 return (int) Math.ceil(num/(3*1.0));
		 
	 }
}
```
