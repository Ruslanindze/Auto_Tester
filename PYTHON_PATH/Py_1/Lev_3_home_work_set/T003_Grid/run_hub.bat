echo OFF
set PATH_SERVER=d:\WORK_MC_21\Tester\Auto_Tester\Drivers\selenium-server-standalone-3.14.0.jar
set PORT=4444
set IP=172.20.1.150
rem set IP=%1

rem Создаём узел 
java -jar %PATH_SERVER% -host %IP% -port %PORT% -role hub

rem Check on http://172.20.1.150:4444/grid/console
pause