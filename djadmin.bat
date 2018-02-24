ECHO off

SET djpath="E:\Program Files\Miniconda3\envs\pokeapp\Scripts\django-admin.py"

ECHO %djpath% %1 %2 %3

CALL python %djpath% %1 %2 %3