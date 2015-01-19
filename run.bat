@ECHO OFF

:loop

python class_alert.py

REM Timeout in seconds (7200 = 2 hours).
timeout /t 7200 /nobreak

goto loop
