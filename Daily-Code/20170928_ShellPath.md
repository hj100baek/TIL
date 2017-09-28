# Shell 내에서 환경변수 설정시

CLASSPATH, LD_LIBRARY_PATH 등이 그냥 변수가 아니라 OS에 따라 정해져있다.


AIX 운영 체제에서 라이브러리 경로 설정:
export LIBPATH=INSTALL_PATH/lib:$LIBPATH

HP-UX 운영 체제에서 라이브러리 경로 설정:
export SHLIB_PATH=INSTALL_PATH/lib:$SHLIB_PATH

기타 UNIX 운영 체제 및 Linux 운영 체제에서 라이브러리 경로 설정:
export LD_LIBRARY_PATH=INSTALL_PATH/lib:$LD_LIBRARY_PATH


SQLJ, JDBC, JCC 드라이버에서 사용할 환경 변수:
export CLASSPATH=INSTALL_PATH/java/db2jcc.jar:$CLASSPATH
export CLASSPATH=INSTALL_PATH/java/sqlj.zip:$CLASSPATH

참고:https://www.ibm.com/support/knowledgecenter/ko/SSEPGG_10.1.0/com.ibm.db2.luw.apdv.gs.doc/doc/c0006321.html
