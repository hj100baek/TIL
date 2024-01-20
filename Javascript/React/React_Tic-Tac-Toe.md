https://react.dev/learn/tutorial-tic-tac-toe
Making an interactive component 
```txt
[ App.js]
  Component를 생성한다/
  Component는 재사용가능한 code의 조각
```
```javascript
/*
export - function을 이 파일의 외부에서 access 가능하게 한다.
default - main function을 의미. 기본으로 내보내는 함수를 지정
<button> - JSX element. JSX element = Javascript code + HTML tags
*/

export default function Square() {
  return <button className="square">X</button>;
}
```
