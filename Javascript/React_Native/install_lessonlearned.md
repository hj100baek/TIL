#### 설치시 주의 사항 (on Windows , Android)
###### https://facebook.github.io/react-native/docs/getting-started 에서 보고하다가 안된 것들

```
1) choco install -y nodejs.install python2 jdk8
   --> choco따위는 내 환경에 없었음
       nodejs,jdk8은 설치된 상태였고 python3만 깔려있어 python2만 설치가 필요했음
       python2설치 : python 사이트가서 Windows x86 MSI installer 다운로드 후 설치
2) npm install -g react-native-cli
3) Install Android Studio
   --> 설치 가이드에서 시키는 대로 Android 6.0 (Marshmallow)도 체크해서 선택
4) ANDROID_HOME 환경변수에 추가 
5) react-native init AwesomeProject
6)cd AwesomeProject
  react-native run-android
  --> 실행하니 ANDROID_HOME 에러발생! 
      원인: command창을 4)번 환경변수 추가 후  재시작하지 않음, 환경변수 추가한다음에는 command창을 다시 띄워서 하자!
      
7) command 창을 다시 띄워서 react-native run-android
  --> 실행하니 또 에러발생!
      원인: Android device가 virtual이건 physical이건 뭔가 떠 있는 상태에서 실행시켜 줘야함.
      
8) virtual device 를 띄운후 react-native run-android실행 .. 결국 안되서 다른 버전 재설치!
 --> 실행하니 또 에러발생. AccessibilityInfo 에러 
     원인: reactive-native  0.56 버그라고함. 
     해결: command창에서 react-native -v 로 버전확인
           npm uninstall react-native
           npm uninstall -g react-native-cli
           npm install react-native@0.55.4
           npm install -g react-native-cli@1.2.0
           react-native init --version="0.55.4" myprojectname
 9) virtual device 를 띄운후 react-native run-android실행 성공
 10) virtual device 닫고 react-native 종료
 11) physical device 실행준비
    - device에서 Enable USB Debugging Mode 로 변경해줌
    - 새 command창에서  Android SDK Manger -> Platform Tools 로 이동
    - command > adb devices 명령어로 device확인. 
      만약 기기가  unauthorized라면 USB 디버깅 권한 승인 취소
      command > adb kill-server
      command > adb start-server
      command > adb reverse tcp:8081 tcp:8081
  12) 다시 react-native run-android실행
  13) physical device에서 화면이 나타남. android경우 새로 고침하고 싶으면 메뉴키를 길게 눌러주면 리로드 가능한 메뉴가 나타남.    

```
