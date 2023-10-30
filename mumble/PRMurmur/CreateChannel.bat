@echo off

cd mumo\tools

set PATH=..\..\python26win32\ice\bin;%PATH%
set PYTHONPATH=..\..\python26win32\ice\python;%PYTHONPATH%

SET /P CHANNEL_NAME="Name of Channel (i.e. Awesome PR Server): "
SET /P CHANNEL_ID="Unique Channel ID (i.e. awesome): "
SET /P IP="Server IP (i.e. 123.123.123.123): "
SET /P PORT="Server Game Port (i.e. 16567): "

..\..\python26win32\python prbf2man.py -c "%CHANNEL_ID%" -n "%CHANNEL_NAME%" -f %IP%:%PORT% -b 1 -o "..\modules-enabled\prbf2.ini" -s prmurmurpassword -i "..\..\PRMurmur.ice"

cd ..\..

pause