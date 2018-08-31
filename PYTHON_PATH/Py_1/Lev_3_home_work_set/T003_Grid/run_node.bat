echo OFF
Setlocal EnableDelayedExpansion

set PATH_SERVER=d:\WORK_MC_21\Tester\Auto_Tester\Drivers
set BROWSER=%1
set IP=172.20.1.65:4444
set PORT=%2


rem Создаём центр - Node
IF %BROWSER%==chrome (
	java -Dwebdriver.chrome.driver=%PATH_SERVER%\chromedriver.exe -jar %PATH_SERVER%\selenium-server-standalone-3.14.0.jar -role webdriver -hub http://%IP%/grid/register -port %PORT% -browser browserName=chrome
) ELSE (
	IF %BROWSER%==firefox (
		java -Dwebdriver.firefox.driver=%PATH_SERVER%\geckodriver.exe -jar %PATH_SERVER%\selenium-server-standalone-3.14.0.jar -role webdriver -hub http://%IP%/grid/register -port %PORT% -browser browserName=firefox
	) ELSE (
		IF %BROWSER%==ie (
			java -Dwebdriver.ie.driver=%PATH_SERVER%\IEDriverServer.exe -jar %PATH_SERVER%\selenium-server-standalone-3.14.0.jar -role webdriver -hub http://%IP%/grid/register -port %PORT% -browser browserName=iexplorer
		)
	)
)