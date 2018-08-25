### Thread 생성방법 2가지
##### 1) Thread class 상속
##### 2) Runnable interface 구현

```java
// 1)Thread를 상속받는 방법
public class SimpleThread extends Thread {
	public SimpleThread(String s) {
		super(s);
	}
	public void run() {
		for (int i=0; i < 5; i++) {
			System.out.println(getName());
			try { sleep((int)(Math.random() * 1000));
			
			} catch(Exception e) {}
		}
	}
}

class ThreadTest {
	public static void main(String[] a) {
		SimpleThread t1 = new SimpleThread("DisneyLand");
		SimpleThread t2 = new SimpleThread("\t\t HongKong");
		
		//start로 하면 순차적으로 실행되지 않는다. start는 thread를 생성하므로 서로 비동기적으로 실행되기 때문
		t1.start();  //creates a new thread
		t2.start();  //creates a new thread
		
		//run으로 하면 t1->t2순으로 실행된다.run은 존재하는 thread에서 실행되므로 동기적으로 실행되기 때문
		//t1.run();	  
		//t2.run();
		
	}
}
//==============================================================================
//start result
DisneyLand
		 HongKong
		 HongKong
		 HongKong
DisneyLand
		 HongKong
DisneyLand
DisneyLand
		 HongKong
DisneyLand

//run result
DisneyLand
DisneyLand
DisneyLand
DisneyLand
DisneyLand
		 HongKong
		 HongKong
		 HongKong
		 HongKong
		 HongKong
```

```java
//2) Runnable interface를 구현하는 방법
public class SimpleRun implements Runnable {
	String name;
	public SimpleRun(String str) {
		name = str;
	}
	
	@Override
	public void run() {
		for (int i=0; i < 5; i++) {
			System.out.println(this.name);
			try { Thread.sleep((int)(Math.random() * 1000));			
			} catch(Exception e) {}
		}		
	}

}

class RunnableTest {
	public static void main(String[] a) {
		SimpleRun r1 = new SimpleRun("DisneyLand1");
		SimpleRun r2 = new SimpleRun("\t\t HongKong1");
		
		Thread t1 = new Thread(r1);
		Thread t2 = new Thread(r2);
		
		t1.start();
		t2.start();
	}
}
```
