# Spring_Mybatis 

 - pom.xml
 
  ```xml
   <!-- Mybatis log4j -->
  <dependency>
    <groupId>org.lazyluke</groupId>
    <artifactId>log4jdbc-remix</artifactId>
    <version>0.2.7</version>
   </dependency>
  ```
  
 - datasource.xml
  
    ```xml
    <!-- Mybatis log4j -->
     <bean id="dataSourceLog" class="net.sf.log4jdbc.Log4jdbcProxyDataSource">
	    <constructor-arg ref="dataSource" />
	    <property name="logFormatter">
	        <bean class="net.sf.log4jdbc.tools.Log4JdbcCustomFormatter">
	            <!-- <property name="loggingType" value="MULTI_LINE" />  --><!-- 여러줄에 출력하려고 하시면 코멘트 해제 -->
	            <property name="sqlPrefix" value="SQL         :  "/>
	        </bean>
	    </property>
	</bean>
    ```
