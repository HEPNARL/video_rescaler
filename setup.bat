@echo off
echo Checking for Python...
echo.

python --version >nul 2>&1

if %ERRORLEVEL%==0 (
    echo Python is installed:
    python --version
    pip install -r requirements.txt
) else (
    echo Python is NOT installed.
    echo Please install Python from:
    echo https://www.python.org/downloads/
    echo and run the setup again
)

echo.

