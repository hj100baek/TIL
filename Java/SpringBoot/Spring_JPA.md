#### Spring JPA

##### @Entity
###### - db에 저장된 테이블을 표현한다. 해당 클래스가 JPA의 엔티티임을 의미한다.
###### - @Entity(name = "Student") : 엔티티명을 표현한다.


##### @Table
###### - optional, @Table annotation이 없으면 @Entity를 기본값으로 사용한다.
###### - @Table(name = "student") : db에서 테이블명으로 사용된다.

##### 객체 연관관계 vs 테이블 연관관계
```txt
객체  :   참조(주소)로 연관관계 (member.getTeam())
          단방향 (만약 양쪽에서 서로 참조한다면?  이것은 양방향 관계가 아니라 서로 다은 단방향 관계 2개다.)
          
테이블 : 외래키로 연관관계 (JOIN)
          양방향
```

##### JPQL
```txt
JPQL : Java Persistence Query Language
엔티티 객체를 조회하는 객체지향 쿼리
SQL을 추상화해서 특정 db에 의존하지 않음
```
