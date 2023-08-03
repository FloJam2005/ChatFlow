# social_app

## Setup

The requirements in the requirements.txt can be installed using the command:
```bash
pip install -r requirements.txt
```

Then you need to run the migrations to set up the sqlite database:
```bash
python manage.py migrate
```

Additionally, you can add an admin user:
```bash
python manage.py createsuperuser
```
With this user you can access the [admin page](http://localhost:8000/admin) that is provided by Django after you started the application.


## Starting the application

In PyCharm, you should get the green triangle run configuration for `social-media-app` automatically after the project import.
If not, you can also start the app via

```bash
python manage.py runserver
```
