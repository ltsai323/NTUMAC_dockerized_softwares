@echo off

:: BatchGotAdmin
:-------------------------------------
REM  --> Check for permissions
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params = %*:"=""
    echo UAC.ShellExecute "cmd.exe", "/c %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
:--------------------------------------

python3 -m pip install --upgrade pip
python3 -m pip install numpy PyQt5 jinja2 pytest pexpect wexpect psutil requests setuptools
 



REM Go to current directory at Administrator mode
cd /d "%~dp0"

rmdir /S /Q "SharedUI"
git clone https://github.com/IncandelaLab/SharedUI.git

REM get the absolute path of filemanager_data
for /f "delims=" %%i in ('powershell -command "(Get-Item -Path .\filemanager_data).FullName"') do set ABSOLUTE_PATH=%%i

mklink /D .\SharedUI\filemanager_data "%ABSOLUTE_PATH%"

cd .\SharedUI\
git checkout c6f1d7ba54df1560a15b30ca9f83f5870dbe85e5
