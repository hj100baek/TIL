### Mybatis

```
1) list로 in 조건 만들때
 <choose>
    <when test="sampleList.size != 0">
     and columnA in 
       <foreach collection="sampleList" item="item" index="index" separator=","  open="(" close=")">
          #{item}
        </foreach>
 </choose>

2) SelectKey property : 구문이 실행된 전후(order 옵션)에 따른 값을 조회한다. 
                       아래 예는 insert된후 id값을 keyProperty="id" 로 조회한다.

 <insert id="insertUser" parameterClass="XXX.User"> 
          insert into user (name,password) 
         values (#{id},#{name},#{password}) 
          <selectKey resultClass="long" keyProperty="id" order="after">  
             SELECT LAST_INSERT_ID() AS ID  
        </selectKey>  
 </insert> 


``` 
