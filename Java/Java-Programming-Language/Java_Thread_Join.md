```java
public class SimpleThreadJoin extends Thread {
	public SimpleThreadJoin(String s) {
		super(s);
	}
	public void run() {
		for (int i=0; i < 5; i++) {
			if(getName().equals("DisneyLand"))
				ThreadJoinTest.tour = 0;
			else
				ThreadJoinTest.tour = 1;
			try { sleep((int)(Math.random() * 1000));
			
			} catch(Exception e) {}
		}
	}
}

class ThreadJoinTest {
	static int tour;
	public static void main(String[] a) {
		SimpleThreadJoin t1 = new SimpleThreadJoin("DisneyLand");
		SimpleThreadJoin t2 = new SimpleThreadJoin("\t\t HongKong");
		
		//start로 하면 순차적으로 실행되지 않는다. start는 thread를 생성하므로 서로 비동기적으로 실행되기 때문
		t1.start();  //creates a new thread
		t2.start();  //creates a new thread
		
		//join을 사용하지 않으면 main도 별도 thread이기 때문에 main이 먼저 끝날수도 있다.
		try{
			t1.join();   //main thread가 t1이 종료할때까지 대기하게 한다.
			t2.join();   //main thread가 t2이 종료할때까지 대기하게 한다.
		} catch(Exception e) {
			e.printStackTrace();
		}
		
		if(tour == 0 ) System.out.println("Let's go! DesineyLand");
		else 		   System.out.println("Let's go! HongKong");	
		
	}
}

```
