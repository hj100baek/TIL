### Thread 실행 취소 방법
##### 1) 비동기적 취소 : stop()메소드를 사용하여 스레드를 즉시 중단 시키는 것. 갑자기 실행중단이 되므로 교착상태가 발생할 수 있다.
##### 2) 연기된 취소: 실행중인 스레드가 중단되어야 하는지 주기적으로 체크한다.

```java
// 1) 비동기적 취소
class StoppedThread implements Runnable {
	public void run() {
		while(true) {
			StopThread.sum = StopThread.sum + 1;
		}
	}
}

public class StopThread  {
	static public long sum=0;
	
	public static void main(String[] args) {
		Thread worker = new Thread(new StoppedThread());
		worker.start();
		
		try{
			Thread.sleep(2000);
		} catch (InterruptedException ie) {
			
		}
		
		worker.stop(); //stop worker thread
		
		System.out.println("workder thread stopped: sum = "+ sum);
	}

}

//===========================================
//result
//===========================================
 workder thread stopped: sum = 475108384
```

```java
//2) 연기된 취소
class InterrupterThread implements Runnable {

	@Override
	public void run() {
		while (true) {
			if (Thread.currentThread().isInterrupted()) {
				System.out.println("I'm interrupted!");
				break;
			}
		}
		
	}

}

public class Interrupter {
	public static void main(String[] args) {
		Thread worker = new Thread(new InterrupterThread());
		worker.start();
		
		try { Thread.sleep(3000);
		}catch(InterruptedException ie) {}
		
		worker.interrupt();
		}
	}

//===========================================
//result
//===========================================
I'm interrupted!

```
