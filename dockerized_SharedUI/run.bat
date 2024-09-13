@echo off
:: Check docker desktop running or not
docker info >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo Docker is not running. Starting Docker Desktop...
    start "" "C:\Program Files\Docker\Docker\Docker Desktop.exe"
    echo Waiting for Docker Desktop standby...
    timeout /t 30

    :: Check again
    docker info >nul 2>&1
    if %ERRORLEVEL% neq 0 (
        echo [ERROR]
        echo [ERROR] Unable to activate Docker Desktop... Please run Docker Desktop manually.
        echo [ERROR]
        pause
        exit /b 1
    )
)

set "scriptPath=%~dp0"
set "parentPath=%scriptPath:~0,-1%"
for %%i in ("%parentPath%") do set parentPath=%%~dpi
set "configFile=%parentPath%config.xlaunch"


:: Check VcXsrv running or not
tasklist /FI "IMAGENAME eq vcxsrv.exe" | find /I "vcxsrv.exe" > nul
if %ERRORLEVEL% neq 0 (
    echo "[INFO] VcXsrv is not running. Starting VcXsrv..."
    start "" "%configFile%"
)
:: Check again
tasklist /FI "IMAGENAME eq vcxsrv.exe" | find /I "vcxsrv.exe" > nul
if %ERRORLEVEL% neq 0 (
    echo [ERROR]
    echo [ERROR] Unable to activate VcXsrv, run VcXsrv manually.
    echo [ERROR]
    pause
    exit /b 1
)



docker run -it --rm ^
  --env="DISPLAY=host.docker.internal:0" ^
  --env="QT_X11_NO_MITSHM=1" ^
  --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" ^
  --volume="%cd%\filemanager_data:/SharedUI/filemanager_data" ^
  --volume "%USERPROFILE%\.ssh:/root/.ssh:rw" ^
  --name shared-ui-container shared-ui-image

echo FINISHED
pause
