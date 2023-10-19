###
참고
  https://www.toptal.com/spring/spring-security-tutorial <br/>
  https://stackoverflow.com/questions/72381114/spring-security-upgrading-the-deprecated-websecurityconfigureradapter-in-spring
  
```java
@Configuration
@EnableConfigurationProperties(RedisProperties.class)
public class RedisConfig {
    @Bean
    public RedisTemplate<?, ?> redisTemplate(RedisConnectionFactory connectionFactory) {
        RedisTemplate<?, ?> template = new RedisTemplate<>();
        template.setConnectionFactory(connectionFactory);
        // Add some specific configuration here. Key serializers, etc.
        return template;
    }
}
```

```txt
## application.properties
spring.data.redis.host=localhost
spring.data.redis.port=6379
```
