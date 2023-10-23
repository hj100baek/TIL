#### Spring Security 
###### authentication (who are you?) and authorization (what are you allowed to do?)
###### 웹단에서 Srping Security는 Servlet Filters에 기반한다.

1) Deprecate WebSecurityConfigurerAdapter 이전 <br>
https://www.youtube.com/watch?v=VVn9OG9nfH0
https://github.com/getarrays/userservice/tree/main/src/main/java/io/getarrays/userservice
```java
@Configuration @EnableWebSecurity @RequiredArgsConstructor
public class SecurityConfig extends WebSecurityConfigurerAdapter{

.....

 	@Override
 	protected void configure(HttpSecurity http) throws Exception {
          http
            .authorizeHttpRequests((authz) -> authz
                .anyRequest().authenticated()
            )
            .httpBasic(withDefaults());
  }

}
```
 
#### CSRF (Cross Site Request Forgery)
```
```
