@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo Submitting site URLs to Bing / IndexNow ...
python "_admin\notify_search_engines.py"
echo.
pause
