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
              
##### packaging
```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
                      http://maven.apache.org/xsd/maven-4.0.0.xsd">
  ...
  <packaging>war</packaging>
  ...
</project>
```
예어서 packaing가 선언되지 않았다면 org.codehaus.mojo:my-project:1.0 이 jar로 패키징 된다.  
위의 예에서는 war로 선언했으므로 war로 패키징 된다.  
패키 values는 pom, jar, maven-plugin, ejb, war, ear, rar 가 있다.

#### POM Relationships
Maven의 강력한 면중 하나는 프로젝트 relationshps를 핸들링하는 것이다.  
이것은 dependencies, inheritance, aggregation을 포함한다.  
dependency 관리는 복잡한 것이라는 전통을 가진다.  
"Jarmaggeddon"는 크고 복잡하게 되어진 dependency tree로써 빠르게 발생한다.  
"Jar Hell"은 dependencies version이 동일하지 않게 개발되거나 유사한 이름의 jar 사이에 버전충돌이 있다.  
Maven은 이런 문제들을 해결한다.

##### Dependencies
POM의 핵심은 dependency이다. 대부분 프로젝트는 빌드하고 실행하기 위해 다른것을 의존한다.  
Maven이 이 리스트를 모두 관리한다면 큰 이득을 얻는다.  
Maven은 dependencies를 다운로드하고 링크한다.  
```
<project xmlns="http://maven.apache.org/POM/4.0.0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
                      https://maven.apache.org/xsd/maven-4.0.0.xsd">
  ...
  <dependencies>
    <dependency>
      <groupId>junit</groupId>
      <artifactId>junit</artifactId>
      <version>4.12</version>
      <type>jar</type>
      <scope>test</scope>
      <optional>true</optional>
    </dependency>
    ...
  </dependencies>
  ...
</project>
```

##### Inheritance
Maven의 강력한 추가 기능중 하나는 프로젝트 상속 개념이다.  
Maven은 pom에 명시적으로 프로젝트 상속을 만드는 추가단계를 가진다.
```xml

<project xmlns="http://maven.apache.org/POM/4.0.0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
                      https://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
 
  <groupId>org.codehaus.mojo</groupId>
  <artifactId>my-parent</artifactId>
  <version>2.0</version>
  <packaging>pom</packaging>
</project>
```
packaging type은 parent를 위해 __pom__ 이 요구된다.

```xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
                      https://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>
 
  <parent>
    <groupId>org.codehaus.mojo</groupId>
    <artifactId>my-parent</artifactId>
    <version>2.0</version>
    <relativePath>../my-parent</relativePath>
  </parent>
 
  <artifactId>my-project</artifactId>
</project>
```
relativePath 요소는 요구되지 않지만 사용된다면  
프로젝트 parent를 위해 첫번째 검색을 위한 의미로 사용된다.  

객체지향 프로그래밍의 객체 상속과 유사하게 모든 POM은 Super POM을 상속한다.


