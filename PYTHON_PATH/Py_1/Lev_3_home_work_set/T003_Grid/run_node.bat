echo OFF
Setlocal EnableDelayedExpansion

set PATH_SERVER=d:\WORK_MC_21\Tester\Auto_Tester\Drivers
set BROWSER=%1
set IP=172.20.1.150:4444
set PORT=%2


rem Create a connection Node -> Hub
IF %BROWSER%==chrome (
	java -Dwebdriver.chrome.driver=%PATH_SERVER%\chromedriver.exe -jar %PATH_SERVER%\selenium-server-standalone-3.14.0.jar -role webdriver -hub http://%IP%/grid/register -port %PORT% -browser browserName=chrome,platform=WINDOWS
) ELSE (
	IF %BROWSER%==firefox (
		rem java -Dwebdriver.firefox.driver=%PATH_SERVER%\geckodriver.exe -jar %PATH_SERVER%\selenium-server-standalone-3.14.0.jar -role webdriver -hub http://%IP%/grid/register -port %PORT% -browser browserName=firefox
        java -Dwebdriver.gecko.driver=%PATH_SERVER%\geckodriver.exe -jar %PATH_SERVER%\selenium-server-standalone-3.14.0.jar -role webdriver -hub http://%IP%/grid/register -port %PORT% -browser browserName=firefox,platform=WINDOWS
	) ELSE (
		IF %BROWSER%==ie (
			java -Dwebdriver.ie.driver=%PATH_SERVER%\IEDriverServer.exe -jar %PATH_SERVER%\selenium-server-standalone-3.14.0.jar -role webdriver -hub http://%IP%/grid/register -port %PORT% -browser browserName=iexplorer,platform=WINDOWS
		)
	)
)
rem Check on http://172.20.1.150:4444/grid/console