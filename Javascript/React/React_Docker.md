### Docker에서 React 실행하기 환경설정
- window에 nodejs 다운로드 및 설치 (https://nodejs.org/)
- React apps 생성 후 생성한 경로로 이동<br/>
   npx create-react-app my-app <br/>
   cd my-app<br/>   
  
-  개발환경용 도커파일 Dockerfile.dev 생성
  ```docker
FROM node:20

WORKDIR /usr/src/node_app

COPY package*.json /usr/src/node_app

RUN npm install

COPY . /usr/src/node_app

CMD ["npm" , "run",  "start"]
  ```

-  .dockerignore 파일 생성
```docker
node_modules
npm.debug.log
```

 - docker image 생성<br/>
   docker build -t mydockerid/test_react:1.0 -f Dockerfile.dev .

  - docker container 실행<br/>
   docker run --name local_react -p 3000:3000 -v /usr/src/node_app/node_modules -v D:\workspace_node\my-app:/usr/src/node_app -e WATCHPACK_POLLING=true mydockerid/test_react:1.0

   
