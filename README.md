Create Environment

https://conda.io/docs/user-guide/tasks/manage-environments.html

conda create -n myenv python=3.4


C:\Program Files\Miniconda3\envs\pokeapp\Scripts\django-admin.py

Run below command from pokeapp dir
python "C:\Program Files\Miniconda3\envs\pokeapp\Scripts\django-admin.py" startproject pokemon .

python manage.py migrate

python manage.py runserver

python manage.py createsuperuser --username=john --email=john@thebeatles.com

Index page

create collections\templates directory

update collection views.py with index method

update pokemon urls.py

Creating data

Models.py

create the model

make viewable in admin

In Admin.py, create [table]Admin
Link tables through register method


python manage.py makemigrations

Apply migration