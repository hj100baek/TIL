### React useEffect
렌더러가 부수효과로 무언가를 수행하고 싶을 때 사용<br/>
부수효과란 UI 함수가 반환하는 값에 속하지 않는 어떤 것<br/>
렌더링이 끝난 다음 발생하는 함수<br/>
useEffect(이펙트함수, 의존성 배열);
```
 useEffect(() => {
    console.log(checked? "Yes, checked" : "No, not checked");
  });
```
