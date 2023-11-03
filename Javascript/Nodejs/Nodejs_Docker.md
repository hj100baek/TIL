### Docker에서 Node.js 실행하기 환경설정
- window에 nodejs 다운로드 및 설치 (https://nodejs.org/)
   
 - 프로젝트 폴더 생성 후 생성한 경로로 이동<br/>
   mkdir testnode <br/>
   cd testnode<br/>
    
 -   JavaScript 프로젝트에 필요한 패키지 설치 , package.json 생성<br/>
     npm install -y

-  express 설치<br/>
     npm install express --save

-  package.json에서 "main" : 수정<br/>
     "main" : "index.js"   ->  "main" : "server.js"

-  server.js 파일 생성

  ```javascript
const PORT = 3000;
const HOST = '0.0.0.0';

const express = require('express'); 
const app = express();

app.get('/', (req, res) => {
  res.send('Hello World!');
})

app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);
   ```
-  Dockerfile 파일 생성
  ```docker
FROM node:20

WORKDIR /usr/src/node_app

COPY package*.json /usr/src/node_app

RUN npm install

COPY . /usr/src/node_app

EXPOSE 3000

CMD ["node" , "server.js"]
  ```

-  .dockerignore 파일 생성
```docker
node_modules
npm.debug.log
```

 - docker image 생성<br/>
   docker build -t  mydockerid/test_node:1.0 .

  - docker container 실행<br/>
   docker run --name local_node -p 3001:3000 mydockerid/test_node:1.0


refer: https://www.youtube.com/watch?v=PsWeSg38XFY </br>
       https://riptutorial.com/docker/example/27294/running-a-basic-node-js-application-inside-a-container
   
   
