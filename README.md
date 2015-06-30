분산환경에서 여러 대의 서버로 파일을 복사하거나 한번에  명령을 실행하고 싶을 때..유료 유틸만 방법일까요?

Python으로 리모트서버들을 접속하고 명령을 수행하고 scp로 put을 수행하는 유틸을 만들어봤음. 

Dependency 
* paramiko 
* scp 


Example) 

Change Mode 

* $ chmod util.py 


Run 
* $ ./util.py 

ssh> 


Add Host File 

* ssh> add_host_file file_name 


Run Command 

* ssh > run shell_command 



scp_put 

* ssh > scp_put file_name 
