@echo off

cd mumo

set PATH=..\python26win32\ice\bin;%PATH%
set PYTHONPATH=..\python26win32\ice\python;%PYTHONPATH%

echo Running mumo...
..\python26win32\python mumo.py