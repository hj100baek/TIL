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
``` 
