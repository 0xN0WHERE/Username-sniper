@echo off
title Username sniper - Setup

python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo Python is NOT installed!
    echo Please install Python and add it to PATH.
    pause
    exit
)

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

IF %ERRORLEVEL% NEQ 0 (
    echo Failed to install requirements!
    pause
    exit
)

python main.py

pause
