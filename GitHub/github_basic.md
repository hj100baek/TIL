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

 * #### commit :

   local만 반영되고 remote repository는 아직 반영되지 않은 상태
   
 * #### publish :

   local(commit상태) -> remote repository로 반영

### Stuff used to make this:

 * [GitHub Help](https://help.github.com/) help
