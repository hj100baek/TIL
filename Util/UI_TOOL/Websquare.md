```text

[그리드 관련]
  - 상태 변경 예외 처리
    바인딩된 dataList에 컬럼 속성 ignoreStatus = "true" 설정
    
  - 다단계 select
    select 1의 선택값에 따라 select 2가 나타나게 하기위해
    select 2의 전체 item을 담은 dataList에 대한 LinkedDataList를 정의하고 LinkedDataList의 FilterCondition을 정의
    ex)upCd == ref('data:dtl_Sel1.cd1')
    그리드에 select 2의 BindItemSet은 LinkedDataList로 설정
    select 1의 변경에 따른 select 2값 초기화 위해 dtl_Sel1 oncelldatachange이벤트에 data:dtl_Sel1.cd2 초기화 구현


```
