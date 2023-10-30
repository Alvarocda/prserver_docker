@echo off

cd mumo\tools

set PATH=..\..\python26win32\ice\bin;%PATH%
set PYTHONPATH=..\..\python26win32\ice\python;%PYTHONPATH%

..\..\python26win32\python prbf2setup.py -s prmurmurpassword -i "..\..\PRMurmur.ice"

cd ..\..

pause