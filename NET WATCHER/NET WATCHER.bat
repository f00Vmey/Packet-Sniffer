@echo off >nul
title Net Watcher - Foomey
chcp 65001>nul

:banner
cls
echo.
echo                   [93md8b   db d88888b d888888b  [0mdb   d8b   db  .d8b.  d888888b  .o88b. db   db d88888b d8888b. 
echo                   [93m888o  88 88'     `~~88~~'  [0m88   I8I   88 d8' `8b `~~88~~' d8P  Y8 88   88 88'     88  `8D 
echo                   [93m88V8o 88 88ooooo    88     [0m88   I8I   88 88ooo88    88    8P      88ooo88 88ooooo 88oobY' 
echo                   [93m88 V8o88 88~~~~~    88     [0mY8   I8I   88 88~~~88    88    8b      88~~~88 88~~~~~ 88`8b   
echo                   [93m88  V888 88.        88     [0m`8b d8'8b d8' 88   88    88    Y8b  d8 88   88 88.     88 `88. 
echo                   [93mVP   V8P Y88888P    YP      [0m`8b8' `8d8'  YP   YP    YP     `Y88P' YP   YP Y88888P 88   YD 
echo.                     
goto commands

:commands
echo       note:
echo    Press ctrl+c to end process.
echo.
echo       options:
echo    "-ps" - ( ps = packetsniffer) sniffs packets, see any activity on the network youre connected to.
echo    "-ns" - ( ns = netstat) powerful tool that provides information about network connections, routing tables, etc. 
echo    "-t"  - ( t = traceroute) valuable tool for monitoring, and analysis.
echo    "-bwt"  - ( bwt = BandWith Test) process used to measure the data transfer speed of a network connection.
echo    "$e"  - "( e = exit)" Exits Net Watcher.
echo    "$h" - ( h = help) Comes back to the page. (Not useful)
echo.
goto prompt

:prompt
for /f %%A in ('"prompt $H &echo on &for %%B in (1) do rem"') do set BS=%%A

set /p input="[30m.[0m    Input$:  %BS%"

if /I %input% EQU T goto banner
if /I %input% EQU -ps goto -ps
if /I %input% EQU -ns goto -ns
if /I %input% EQU -t goto -t
if /I %input% EQU -bwt goto -bwt
if /I %input% EQU $e goto $e
if /I %input% EQU $h goto $help

:$help
goto banner

:$e
exit

:-bwt
cd C:\Users\NET WATCHER\scripts\crit
python bwt.py

:-t
cd C:\Users\NET WATCHER\scripts\crit
python traceroute.py

:-ns 
netstat - an
goto -nsc

:-nsc
set /p inp="[30m.[0m    NetstatCmd$:  %BS%"
netstat %inp%
pause>nul
goto banner

:-ps
cd C:\Users\NET WATCHER\scripts\crit
python main.py
