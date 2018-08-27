### Thread.yield() 
##### 현재 실행 중인 스레드의 시행을 일시 중단하여 다른 스레드가 실행가능하도록 한다.

```java
package com.devb.test;

class S10 implements Runnable {
	public void run() {
		System.out.println("S10");
		//Thread.yield();
		System.out.println("S10");
		//Thread.yield();
		System.out.println("S10");
		//Thread.yield();
	}
}

class S20 implements Runnable {
	public void run() {
		System.out.println("S20");
		//Thread.yield();
		System.out.println("S20");
		//Thread.yield();
		System.out.println("S20");
		//Thread.yield();
	}
}

class S30 implements Runnable {
	public void run() {
		System.out.println("S30");
		//Thread.yield();
		System.out.println("S30");
		//Thread.yield();
		System.out.println("S30");
		//Thread.yield();
	}
}

public class ThreadYield {
	public static void main(String[] args) {
		Thread s = new Thread(new S10());
		Thread t = new Thread(new S20());
		Thread u = new Thread(new S30());
		
		s.start();
		t.start();
		u.start();	
	}

}



==================================================
output
==================================================
//yield 주석일 경우

S20
S20
S20
S30
S30
S30
S10
S10
S10

//yield 주석해제 경우

S20
S30
S10
S30
S30
S20
S10
S10
S20
```
