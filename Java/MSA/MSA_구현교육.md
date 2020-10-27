## MSA교육

```
db: Postgre 설치 , postgresql-12.4-1-windows-x64.exe 설치,  기본으로 설치하다 컴포넌트 선택창에서 스택빌더 선택 지우고 설치진행

postgres=# pg_ctl start
postgres=# pg_ctl status
postgres=# pg_ctl restart
postgres=# pg_ctl start company
postgres=# pg_ctl status

spring boot
과거의 방식은 작은 개발에도 많은 기본 환경 설정(WAS , Container, Context, web-inf/lib)이 필요.
runtime방식의 framework.  

spring cloud
spring f/w와 spring boot를 포함하는 더 큰 개념

Hystrix 
Circuit breaker
Hystrix is a latency and fault tolerance library designed to isolate points of access to remote systems, services and 3rd party libraries, stop cascading failure and enable resilience in complex distributed systems where failure is inevitable.

API Gateway
Channel(폰, PC, 태블릿 등등)과 Service사이에 작동한다.
EndPoint의 단일화 역할.
인증/인가 처리가 가능

Service Mesh
MSA서비스들 사이에서 작동한다.(서비스들 사이에 Routing, Discovery-Eureka, Load Balance-Ribbon, Fail over-Hystrix)
최근에는 Eureka보다는 쿠버네티스를 사용한다.

Backing Service
데이터 처리. 캐시 등등

CI/CD: Deploy, delivery

Telemetry
Log, Trace, monitoring 등 

```
