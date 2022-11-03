####  [ 1 개 파일에서 멀티 환경 설정 ]
##### A YAML file is actually a sequence of documents separated by --- lines, and each document is parsed separately to a flattened map
##### spring.profiles를 사용하면 멀티 설정 가능
##### spring.profiles.active=production 로 active 할 환경 지정 
##### 또는 application 실행시 java -jar -Dspring.profiles.active=production demo-0.0.1-SNAPSHOT.jar

```yml
server:
    address: 192.168.1.100
---
spring:
    profiles: development
server:
    address: 127.0.0.1
---
spring:
    profiles: production
server:
    address: 192.168.1.120
```
