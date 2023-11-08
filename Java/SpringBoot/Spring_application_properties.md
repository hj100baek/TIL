#### application.properties

``` txt
# docker-jpa-mysql용
spring.datasource.url=jdbc:mysql://${MYSQL_HOST:localhost}:3306/mydb
spring.datasource.username=username
spring.datasource.password=password
spring.jpa.hibernate.ddl-auto=create-drop
spring.jpa.show-sql=true
spring.jpa.properties.hibernate.dialect = org.hibernate.dialect.MySQL8Dialect
spring.jpa.properties.hibernate.format_sql=true

```
