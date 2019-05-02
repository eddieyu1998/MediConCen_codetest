# MediConCen_codetest

Dependencies needed:

* python 3.5 or above

* django 2.1/2.2

To run the server: `python3 manage.py runserver`

To invoke the django interactive shell: `python3 manage.py shell`

data can be loaded into the database from the shell, or on the admin page 127.0.0.1:8000/admin if local host is used.
A superuser has to be created first, this can also be done in the shell.

To load the data, in the shell type `from content.models import *` and then paste the data script into the shell.

default port is 8000

## Login
User can login or register via this page.

## Homepage
User can view the dataset as a table. Create new entries, update or delete entries from the table.

To create, fill in the fields at the bottom of the page and hit create.

To delete an entry, hit delete on the row to be deleted

To update, hit update after modifying the fields in the row

At this stage, the system does not support:

* sorting of entries
* user account management
* concurrency issues prevention
* aesthetic
