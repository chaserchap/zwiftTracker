# zwiftTracker

## To get running:

### Setup Python
Clone this repo to a directory, then change into that directory.

```python3 -m venv venv
source venv/bin/activate
pip install requirements.txt
python manage.py makemigrations
python manage.py migrate
```

### Setup django admin
```
python manage.py createsuperuser
```
Follow prompts.

### Setup DB

```
sqlite3
.mode csv
.import routes_fixed.csv rides_route
.quit
```

### Run server
```
python manage.py runserver
```

You can now access your zwifttracker at https://localhost:8000
