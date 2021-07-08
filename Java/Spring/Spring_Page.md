### Srping에서 페이징
```java
public calss AAA {

public Page<SampleResDTO> retrieveQry(SampleSrchReqPageDTO param){
   return xxxxx
}

public Page<SampleResDTO> retrieveTot(SampleSrchReqPageDTO param){
  //다른 클래스(AAA)에서 호출
  TotalPageSample<SampleSrchReqPageDTO, SampleResDTO> totalPageSample = new TotalPageSample<>(this::retrieveQry, 100);
  return totalPageSample.readTableTotalPage(param);
}

// 관련 클래스 Page, Pageable , PageRequest
public class TotalPageSample<T extends PagingVO, R extends BaseModel> {

private Function<T, Page<R>> serviceFunction;
private int ROW_SIZE = 100;

public TotalPageSample(Function<T, Page<R>> serviceFunction, int rowSize) {
  this.serviceFunction = serviceFunction;
  this.ROW_SIZE = rowSize;
}

/** ROW_SIZE 단위로 전체 페이지 조회
// T: paging 요청정보를 가지고 있어야 함
// R: paging 전체 결과 
public Page<R> readTableTotalPage(T t) {
  int totRecord = 0;
  Pageable pageable = PageRequest.of(0, this.ROW_SIZE);
  Pageable lastPageble = null;
  List<R> pageTotalList = new ArrayList<R>();
  
  do {
     if (lastPageble != null) {
       pageable = lastPageble;
     }  
       t.setPageNo(pageable.getPageNumber() + 1);
       t.setRowSize(pageable.getPageSize());
       t.setTotalRecord(totRecord);
       
       Page<R> pageList = this.serviceFunction.apply(t);
       pageTotalList.addAll(pageList.toList());
       
       lastPageble = pageList.nextOrLastPageble();
       totRecord = (int)pageList.getTotalElements();
           
  } while (!lastPageble.equals(pageable));
  
  Page<R> totalPage = new PageImpl<R>(pageTotalList, PageRequest.of(0, this.ROW_SIZE), totRecord);
  
  return totalPage;
}

```
