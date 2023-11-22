### React LifeCycle
##### 클래스에서 Lifecycle
```
ReactDOM.render() : React 애플리케이션이 시작될 때,최초의 렌더링을 수행,
                    React 엘리먼트를 가상 DOM에 렌더링하고, 이후에 실제 DOM에 반영

 // 최초 mouting :  컴포넌트가 처음으로 생성되고 실제 DOM에 추가되는 과정
componentWillMount (): mounting이 발생하기 전에 호출된다. UNSAFE
render () : Virtual DOM node를 반환한다.
componentDidMount () : 컴포넌트가 마운트(inserted into the tree) 된 후 즉시 호출된다.
                       컴포넌트가 실제 DOM에 추가된 직후에 호출되는 메서드 

// updateing
shouldComponentUpdate (): 새로운 props or state 가 수신됬을때 rendering() 전에 호출된다.
componentWillUpdate () : 새로운 props or state 가 수신됬을때 rendering() 전에 호출된다. UNSAFE
render () : Virtual DOM node를 반환한다.
componentDidUpdate () : updating이 발생 된 후 즉시 호출된다. 

```

##### 함수에서 Lifecycle
함수형 Component에서는 hook을 이용함
```
 useEffect(() => {
   //컴포넌트 렌더링 후에 실행
    const connection = createConnection(serverUrl, roomId);
    connection.connect();

   // 정리(clean-up) 함수 반환 (선택적)
    return () => {   
      connection.disconnect();
    };
  }, [serverUrl, roomId]);
    //[] 의존성 배열 : 이 배열에 포함된 상태나 속성이 변경될 때마다 useEffect가 재실행됨
                       빈 배열 []을 전달하면, useEffect는 컴포넌트가 처음 마운트될 때만 실행

```
