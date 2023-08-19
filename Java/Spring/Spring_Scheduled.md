##### controller 에서 스케쥴 호출 방법
```
https://stackoverflow.com/questions/23996173/spring-scheduled-task-triggered-through-the-controller-and-websocket
https://github.com/Charlynux/task-scheduling/tree/master/src/main/java/demo
```
```java
@Controller
public class MyController {

    private ScheduledExecutorService executorService;

    @RequestMapping("/start")
    public String start() {
        executorService = Executors.newSingleThreadScheduledExecutor();
        executorService.scheduleAtFixedRate(new Runnable() {
            @Override
            public void run() {
                // do something
            }
        }, 0, 1, TimeUnit.SECONDS);

        return "index";
    }

    @RequestMapping("/stop")
    public String stop() {
        if (executorService != null) {
            executorService.shutdown();
        }

        return "index";
    }
}
```
```java
@Controller
public class MyController {

    @Autowired
    private TaskScheduler taskScheduler;

    @RequestMapping("/start")
    public String start() {
        taskScheduler.scheduleAtFixedRate(new Runnable() {
            @Override
            public void run() {
                // do something
            }
        }, 0, 1, TimeUnit.SECONDS);

        return "index";
    }

    @RequestMapping("/stop")
    public String stop() {
        if (taskScheduler != null) {
            taskScheduler.shutdown();
        }

        return "index";
    }
}
```
