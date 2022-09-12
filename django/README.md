```shell
pipenv install Django
pipenv shell # opcional caso vc não queria digitar 'pipenv run'
pipenv run python -m django --version
pipenv run django-admin startproject desafio21diaspython
cd desafio21diaspython
pipenv install
pipenv install Django
pipenv run python manage.py runserver
pipenv run python manage.py migrate
pipenv run python manage.py mysqlclient
mysql -uroot -p
create database desafio21dias_python_django;
pipenv run python manage.py createsuperuser
pipenv run python manage.py startapp web


```

