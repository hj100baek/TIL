### Context API
```
1. 사용이유 : 컴포넌트에서 props로 부모 자식간에 데이터를 전달한다면 컴포넌트 깊이가 깊어질수록 복잡도 증가 (Props Drilling)
           
2. Context API
  - Context를 이용하면 단계마다 props를 넘겨주지 않고도 컴포넌트 트리 전체에 데이터 제공 가능
  - Context: 데이터 저장 공간
  - Provider: 데이터 제공, Context의 변화를 감지
  - Consumer: Context를 사용, Context를 구독 

```
```
// Context
import { createContext } from 'react';

const ThemeContext = createContext('light');

// Provider
<ThemeContext.Provider value="dark"> //React19 이전
   <Page />
</ThemeContext.Provider>

<ThemeContext value="dark"> //React19 이후 - .Provider 없이 컨텍스트 객체를 직접 사용
    <Page />
</ThemeContext>


// Consumer
import { useContext } from 'react';

function MyComponent() {
  const theme = useContext(ThemeContext);
  // ...
```
