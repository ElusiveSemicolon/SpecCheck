To setup the Django server and run it, run the following commands inside the src folder where manage.py is located:

```bash
$ python manage.py migrate
$ python manage.py runserver
```

Make sure pip is installed and, if necessary:

```bash
$ pip install django
$ pip install django-machina
$ pip install django-braces
$ pip install django-bootstrap3
$ pip install misaka
$ pip install django-select2
$ pip install django-select2-forms
$ pip install django-chosen
$ pip install django-simple-autocomplete
$ pip install igdb-api-python
```

If game database is empty, install igdb-api-python and then run:

```bash
$ python manage.py update_database
```


Just in case missing modules are still detected, here are all the python packages I had installed when it was working:

```bash
cffi (1.11.2)
Django (1.11.6)
django-appconf (1.0.2)
django-bootstrap3 (9.1.0)
django-braces (1.11.0)
django-chosen (0.1)
django-haystack (2.6.1)
django-machina (0.5.6)
django-mptt (0.8.7)
django-select2 (6.0.0)
django-select2-forms (2.0.2)
django-simple-autocomplete (1.11)
django-sortedm2m (1.5.0)
django-widget-tweaks (1.4.1)
markdown2 (2.3.5)
misaka (2.1.0)
olefile (0.44)
Pillow (4.3.0)
pip (9.0.1)
pycparser (2.18)
pytz (2017.2)
setuptools (28.8.0)
```
