@echo off
REM Prompt the user to enter their username
echo Please login LXPlus first
set /p username=Please enter lxplus username:

ssh -o ProxyJump=%username%@lxplus.cern.ch %username%@dbloader-hgcal 'echo -e "\n\n    Login Successfully \n\n"'
pause
