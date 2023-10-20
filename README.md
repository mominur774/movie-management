## How to run

<br />

> Step 1: Clone the repository
```shell
$ git clone https://github.com/mominur774/movie-management.git # https
# or
$ git clone git@github.com:mominur774/movie-management.git # ssh
```
> Step 2: Change directory
```shell
$ cd movie-management
```
> Step 3: Create and activate virtual environment
```shell
# Create
$ python -m venv env 
# Activate
$ source env/bin/activate
```
>Step 4: Install the dependencies
```shell
$ pip install -r requirements.txt
```
>Step 5: Create `.env` in the root directory
```shell
SECRET_KEY=djkfdgfjgj
DEBUG=True
```
> Step 6: Migrate the database and create superuser
```shell
$ python manage.py migrate
$ python manage.py createsuperuser
```
> Step 7: Run the server
```shell
$ python manage.py runserver
```

The server will run http://127.0.0.1:8000/



https://github.com/mominur774/movie-management/assets/57674321/7a81aab1-4fc9-415a-90c3-a8c47610cffa

