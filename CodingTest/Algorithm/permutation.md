### permutation(순열)
#### 서로 다른 n개의 원소에서 r개를 중복없이 순서에 상관있게 선택하는 혹은 나열하는 것
#### 순서도 중요하다. {1, 2, 3}와 {1, 3, 2}는 순서가 다르기 때문에 다른 값이다.
#### 재귀함수를 사용한다.

```java
public class PremutationTest {

	public static void main(String[] args) {
		String str = "ABC";
		int choose = 0;
		permutations("", str, choose);
	}
	
	public static void permutations(String target, String source, int choose) {
		System.out.println("\n=====permutations choose:"+ choose);
		if (source == null) {
			return;
		}
		
		if (source.length() == 0) {
			System.out.println("======source.length()==="+target);
		}
		
		for (int i=0; i < source.length(); i++) {
			String newTarget = target + source.charAt(i);  // 누적된 기준값 + 원본 source에서 choose값
			System.out.println("======newTarget"+i +"==="+newTarget);
			String newSource = source.substring(0, i) + source.substring(i+1);  //원본 source에서 choose값을 제외한 나머지들
			System.out.println("======newSource"+i +"==="+newSource);
			
			
			permutations(newTarget, newSource, choose++);
						
		}
	}

}
```
```
[실행결과]

=====permutations choose:0
======newTarget0===A
======newSource0===BC

=====permutations choose:0
======newTarget0===AB
======newSource0===C

=====permutations choose:0
======newTarget0===ABC
======newSource0===

=====permutations choose:0
======source.length()===ABC
======newTarget1===AC
======newSource1===B

=====permutations choose:1
======newTarget0===ACB
======newSource0===

=====permutations choose:1
======source.length()===ACB
======newTarget1===B
======newSource1===AC

=====permutations choose:1
======newTarget0===BA
======newSource0===C

=====permutations choose:1
======newTarget0===BAC
======newSource0===

=====permutations choose:1
======source.length()===BAC
======newTarget1===BC
======newSource1===A

=====permutations choose:2
======newTarget0===BCA
======newSource0===

=====permutations choose:2
======source.length()===BCA
======newTarget2===C
======newSource2===AB

=====permutations choose:2
======newTarget0===CA
======newSource0===B

=====permutations choose:2
======newTarget0===CAB
======newSource0===

=====permutations choose:2
======source.length()===CAB
======newTarget1===CB
======newSource1===A

=====permutations choose:3
======newTarget0===CBA
======newSource0===

=====permutations choose:3
======source.length()===CBA

```
