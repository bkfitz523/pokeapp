import os, sys
# import subprocess

# dj_admin = '"python "E:\Program Files\Miniconda3\envs\pokeapp\Scripts\django-admin.py" startproject pokemonapp ."'

dj_admin = 'python "E:\Program Files\Miniconda3\envs\pokeapp\Scripts\django-admin.py"'

command = 'startapp pokemon'


os.system(dj_admin + command)
