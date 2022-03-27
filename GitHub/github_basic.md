# GitHub Basic

 * ### git 구조
 ```
  working directory - staging area - local repository - remote repository
  <-------------------------- local -----------------> <------ remote ---->
                   git add        git commit        git push  
 ``` 
 
 * ### git 설치 :
   git bash 설치 (https://git-scm.com/downloads) 
   
 * ### git 설정 :
  1)  username 설정  
  ```
     git config --global user.name "Mona Lisa"   //username 설정  
     git config --global user.name               //username 설정 확인
  ```
  2)  email 설정
  ```
     git config --global user.email "email@example.com"
     git config --global user.email
  ```
  
  * ### git remote 설정 :
  1)  리모트 저장소 추가 (워킹 디렉토리에 새 리모트 저장소 추가)
  ```
     git remote add <단축이름> <url>
     git remote add origin https://github.com/xxx/test-gitproject.git
     
  ```
  2)  branch 설정
  ```
     git branch -M main
  ```
  3)  push 
  ```
     git push -u origin main
     git push <리모트 저장소 이름> <브랜치 이름>
  ```

 * #### commit :

   local만 반영되고 remote repository는 아직 반영되지 않은 상태
   
 * #### publish :

   local(commit상태) -> remote repository로 반영

### Stuff used to make this:

 * [GitHub Help](https://help.github.com/) help
