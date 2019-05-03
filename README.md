# MediConCen_codetest

Dependencies needed:

* python 3.5 or above

* django 2.1/2.2

Set up the database for the first time: `python3 manage.py makemigrations` , followed by `python3 manage.py migrate`

Subsequent changes to the models require the above steps.

To invoke the django interactive shell: `python3 manage.py shell`

data can be loaded into the database from the shell, or on the admin page 127.0.0.1:8000/admin if local host is used.
A superuser has to be created first, this can be done by `python3 manage.py createsuperuser`.

To load the data, in the shell type `from content.models import *` and then paste the data script into the shell.

To run the server: `python3 manage.py runserver`

default port is 8000

## Login
User can login or register via this page.

## Homepage
User can view and operate on his files

To upload new files, hit choose file and uplaod.

To download or delete files, hit the corresponding button

To update a file, hit the update button on the specific row, change the file name or upload a new file, then hit update.

At this stage, the system does not contains:

* user files scanning
* sorting of entries
* user account management
* duplicate file name prevention
* aesthetic
