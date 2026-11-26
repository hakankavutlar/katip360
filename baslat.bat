@echo off
cd /d "%~dp0"
if not exist .venv\Scripts\python.exe (
    py -m venv .venv
    if errorlevel 1 goto :fail
)
.venv\Scripts\python.exe -m pip install -r requirements.txt
if errorlevel 1 goto :fail
.venv\Scripts\python.exe manage.py migrate
if errorlevel 1 goto :fail
echo Tarayicida http://127.0.0.1:8000 adresini acin.
.venv\Scripts\python.exe manage.py runserver 127.0.0.1:8000
pause
exit /b
:fail
echo Kurulum basarisiz. Python ve internet baglantisini kontrol edin.
pause
exit /b 1
