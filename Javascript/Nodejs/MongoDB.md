#### windows에서 mongodb 설치 후 시작 방법
```
   -- MongoDB start
    cmd> mongod --dbpath /Users/userid/database/local   
    
   -- MongoDB shell
   새로운 cmd창 오픈 후 
    cmd> mongo
    cmd> use local     -- local db사용
    cmd> show collections    -- colleciton 목록 조회
    cmd> db.users.find().pretty()        --users colleciton 조회
    
```    
    
    
