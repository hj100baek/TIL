### 비동기 호출방법
```java
//http://localhost:8080/callExternalApi?param=1  을 호출하면 화면단에는 바로 OK1이 나타나지만
//서버단에서는 callExternalApiSync 가 계속 수행된다.
@Controller
public class MyController {

  @Autowired
  MyService myService;

  @RequestMapping("/callExternalApi")
  @ResponseBody
  public String callExternalApi(@RequestParam("param") String param) {

    myService.callAsycModel(param);

    return "OK" + param;
  }
}


@Service
public class MyService {

  public void callAsycModel(String param) {
    final ExecutorService executorService = Executors.newFixedThreadPool(1);
    executorService.submit(new Runnable() {
      @Override
      public void run() {
        // 외부 API를 비동기적으로 호출하고 결과를 deferredResult에 설정합니다.
        String apiResult = callExternalApiSync(param); // 외부 API 호출 (동기적으로 호출하는 메서드)
        // deferredResult.setResult(apiResult); // 결과 저장
      }
    });

    // return deferredResult;
    // return "OK";
  }

  // 실제로는 외부 API를 동기적으로 호출하는 메서드
  private String callExternalApiSync(String param) {
    // 외부 API 호출 로직 구현
    // ...
    for (int i = 0; i < 1000000; i++) {
      System.out.println(param + ": [" + i + "]");
    }
    return "External API Result";
  }
}
```
