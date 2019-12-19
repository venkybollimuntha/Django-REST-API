createProject -- django-admin startproject projectname
cd projectname

py manage.py startapp appname

open settings.py file and add app name in installed apps

create a table in database using models
create SQL query from models -- py manage.py makemigrations
execute/commit models -- py manage.py migrate

register those models with admin panel to see in console.(localhost:8000/admin)

create a super user to login to console -- py manage.py createsuperuser

add records manually in the student table.

then continue to write logic in views.py


Mixin: calss
-- uses for code reusability
-- independent class to get the child classes directly.
-- can't create object for mixin classes.


