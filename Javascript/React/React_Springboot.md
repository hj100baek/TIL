#### React_Springboot
참고 : https://www.baeldung.com/spring-boot-react-crud

[개발환경]
NodeJs가 없다면 설치 후 npx , npm 으로 참고사이트에서 설치하라는 것 설치


- 예제에서 잘 안되는 것
  아무리 버튼을 클릭해도 화면이 바뀌지 않음.. 심지어 브라우저에 주소는 바꼈는데 !!
  ```js
  // index.js 에서  <React.StrictMode> 태그 제거하니 화면 이동 잘됨
  const root = ReactDOM.createRoot(document.getElementById('root'));
  root.render(
     
      <App />
  
  );
  ```
  
