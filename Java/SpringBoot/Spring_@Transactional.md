```
@Transactional  

트랜잭션 처리를 위해 사용한다. 
그런데 동일 Bean에서 Amethod -> Bmethod 를 호출하면 원하는 대로 작동하지 않았다.

Bean을 분리해야 propagation이 제대로 작동하나 봄
```

```
//작동이 안된 케이스
//동일Bean 에 함수가 있었음.
//원한는 결과 : innerMthod에서 저장이 모두 성공하고, interFaceCall도 성공하면 전체 commit;
                innerMthod에서 저장이 모두 성공하고, interFaceCall이 실패하면 전체 rollback;   
                innerMthod에서 저장이 부분 성공하고, interFaceCall 성공하면 부분성공만 commit;
//작동 결과 : innerMthod에서 저장이 부분 성공하고, interFaceCall 성공하면 부분성공만 commit을 테스트해 보면
              ineerMthod에 롤백이 되지 않고 innserMethod에 RuntimeException 발생부분전까지가 commit되어 버린다.
              
class OuterService {

 @Transactional(propagation = Propagation.REQUIRED)
  public OuterMethod() {
      for () {
         innerMethod();
      }
      
     boolean rtnTF =  interFaceCall();
      if (rtnTF) {
      
      } else {
         throw new RuntimeException("인터페이스 오류, 전체 롤백");
      }
      
  }
 
 @Transactional(propagation = Propagation.NESTED, rollbackFor = Exception.class)
  public  innerMethod() {
      anotherCServer.insert();
      anotherCServer.insert2();
      
      throw new RuntimeException("정의된 오류");
      
      anotherDServer.insert();
      anotherDServer.insert2();
  }
    
}
```

```
//작동이 된 케이스
//Bean 분리 
//작동 결과 : innerMthod에서 저장이 부분 성공하고, interFaceCall 성공하면 부분성공 commit을 테스트해 보면
              innserMethod에 RuntimeException이 발생하면 에러 호출은 rollback처리되고
              다음건은 성공되어 commit처리 되고 , 전체 rollback결정은 outer에 의해 처리도됨
class OuterService {

 @Transactional(propagation = Propagation.REQUIRED)
  public OuterMethod() {
      for () {
         OuterSubService.innerMethod();
      }
      
     boolean rtnTF =  interFaceCall();
      if (rtnTF) {
      
      } else {
         throw new RuntimeException("인터페이스 오류, 전체 롤백");
      }
      
  }
}  
 class OuterSubService {
 
 @Transactional(propagation = Propagation.NESTED, rollbackFor = Exception.class)
  public  innerMethod() {
      anotherCServer.insert();
      anotherCServer.insert2();
      
      throw new RuntimeException("정의된 오류");
      
      anotherDServer.insert();
      anotherDServer.insert2();
  }
    
}
```
