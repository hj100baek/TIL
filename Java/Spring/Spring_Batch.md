### Spring Batch

#### [annotation]

```
@JobScope
: @Bean과 함께 사용한다. 스프링 애플리케이션이 실행되는 시점이 아닌 Job 실행시점에 Bean이 생성된다.(LateBinding)
 
@StepScope
: Step 구현은 Chunk 또는 Tasklet 방식으로 가능하다. 
  Step을 구성하는 ItemReader, ItemWriter, ItemProcessor에서 사용가능하다.
  Chunk 방식 - ItemReader, ItemWriter, ItemProcessor 를 지정하여 chunkSize에 따라  처리. Read와 Writer 개수가 일치해야함
  Tasklet 방식 - ItemReader, ItemWriter 구조가 맞지 않는 배치나 단순구조일 경우 사용

@Bean
@JobScope
public Step xxxxStep01() throw Exception{
...
}

@Bean
@StepScope
public MyBatisPagingItemReader xxxxReader() throw Exception{
...
}

@Bean
@StepScope
public MyBatisPagingItemWriter xxxxWriter() throw Exception{
...
}
```
