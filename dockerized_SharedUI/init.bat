@echo off

:: Check if Docker is running
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

docker rmi shared-ui-image
docker build -t shared-ui-image .

echo FINISHED
pause
