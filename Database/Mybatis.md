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
                       
== insert된후 id값을 keyProperty="id" 로 조회한다.
 <insert id="insertUser" parameterClass="XXX.User"> 
          insert into user (name,password) 
         values (#{id},#{name},#{password}) 
          <selectKey resultClass="long" keyProperty="id" order="after">  
             SELECT LAST_INSERT_ID() AS ID  
        </selectKey>  
 </insert> 
 
 == insert 전 max+1 조회 
 <insert id="insertUser" parameterClass="XXX.User"> 
            <selectKey resultClass="long" keyProperty="id" order="before">  
               select max(id)+1 from user
            </selectKey>
    insert into user (id, name,password) 
    values (#{id},#{name},#{password}) 

 </insert>
 

3) useGeneratedKeys, keyProperty : 자동 생성키를 지원하는 경우 insert 후 key값을 리턴 받을 수 있다.
 <insert id="insertUser" parameterType="DataClass" useGeneratedKeys="true"   keyProperty="id">

     inser into user (name,password) 
     values (#{name},#{password}) 
</insert>

4) trim , prefix : 쿼리문에 문자열을 추가 또는 제거해준다.
update user 
  <trim prefix="SET"  prefixOverrides="OR">          //set을 넣어준다.  prefixOverrides 쿼리 중에 'OR' 텍스트를 찾고, 찾게 되면 'OR' 텍스트를 제거
  username=#{username}
  ,password=#{password}
  </trim>

``` 
