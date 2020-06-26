#### What is the POM?
POM은 "Project Object Model"를 나타낸다.  
pom.xml로 작성된 파일을 가진 Maven 프로젝트의 XML 표현이다.  
프로젝트는 configuration files, roqkfwkemf, 시스템 트래킹 , 라이센스등등이  
code life로 수행된다.
프로젝트에 관련된 모든것이 one-stop-shop이다.  
사실, Maven world에서 프로젝트는 모든것이 어떤 code로 포함될 필요가 없다, 단지 pom.xml

#### The Basics
POM은 project에 필요한 모든 정보를 포함한다.  
build lifecycle가 when, how 동안 who, what, where의 선언적 표현이다.
저것이 POM이 lifecycle의 흐름에 영향을 미칠수 없다고 말하는것은 아니다.  

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
                      http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
 
  <groupId>org.codehaus.mojo</groupId>
  <artifactId>my-project</artifactId>
  <version>1.0</version>
</project>
```
* Maven 프로젝트에 coordinate sysmtem : 3개 필드
  + __groupid__ : 조직 또는 프로젝트에서 유니크하다. dot 표기가 필수는 아니다. dot 표기가 패키지 구조와 일치하지 않아도 된다.  
              그러나 따르는 것이 좋다.
  + __artifactId__ : 프로젝트명 
  + __version__ : 네이밍 퍼즐의 마지막 조각. groupId:artifactId가 single 프로젝트를 나타낼수 있지만 프로젝트의 구체화를 표현 할 수 없다.  
              코드가 변경되면 변경된 것들이 version되어 진다. 버전을 분리하기위해 repository에서 사용된다. $M2_REPO/org/codehaus/mojo/my-project/1.0
              

  
