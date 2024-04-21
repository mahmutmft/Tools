@echo off
setlocal enabledelayedexpansion

rem Set log file path
set "LOG_FILE=log.txt"

rem Clear screen
cls

rem Set color variables
set "COLOR_RESET=[0m"
set "COLOR_CYAN=[96m"
set "COLOR_YELLOW=[93m"
set "COLOR_RED=[91m"
set "COLOR_GREEN=[92m"

echo %COLOR_RED%==========================================================%COLOR_RESET%
echo %COLOR_YELLOW%             Rar Password Cracker by Mahmut%COLOR_RESET%
echo %COLOR_RED%==========================================================%COLOR_RESET%
echo.

if not exist "C:\Program Files\7-Zip\7z.exe" (
    echo %COLOR_RED%7-Zip Not Installed!%COLOR_RESET%
    pause
    exit
)

set /p archive="%COLOR_YELLOW%Enter Archive: %COLOR_RESET%"
if not exist "%archive%" (
    echo %COLOR_RED%Archive not Found!%COLOR_RESET%
    pause
    exit
)

set /p wordlist="%COLOR_YELLOW%Enter Wordlist: %COLOR_RESET%"
if not exist "%wordlist%" (
    echo %COLOR_RED%Wordlist not Found!%COLOR_RESET%
    pause
    exit
)

echo.
echo %COLOR_CYAN%Starting password cracking process...%COLOR_RESET%
echo.

rem Create or clear the log file
echo. > "%LOG_FILE%"

for /f %%a in (%wordlist%) do (
    set pass=%%a
    call :attempt
)
echo %COLOR_RED%Password not found in the wordlist.%COLOR_RESET%
pause
exit

:attempt
echo %COLOR_YELLOW%Testing password: !pass!%COLOR_RESET%
echo Testing password: !pass! >> "%LOG_FILE%"
"C:\Program Files\7-Zip\7z.exe" x -p"!pass!" "%archive%" -o"cracked" -y >nul 2>&1
if "%errorlevel%" EQU "0" (
    echo.
    echo %COLOR_RED%Password Found: !pass!%COLOR_RED%%COLOR_RESET%
    pause
    exit
) else (
    echo Password test failed. >> "%LOG_FILE%"
)

echo.
