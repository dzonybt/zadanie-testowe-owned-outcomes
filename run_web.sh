#!/bin/sh

# wait for PSQL server to start
sleep 15

cd projekt_django
su -m dzonybt -c "python manage.py syncdb --noinput"
su -m dzonybt -c "python manage.py makemigrations projekt_django"  
su -m dzonybt -c "python manage.py migrate" 
su -m dzonybt -c "echo \"from django.contrib.auth.models import User; User.objects.create_superuser(username='admin', password='admin_pass', email='admin@gmail.com')\" | python manage.py shell "
su -m dzonybt -c "python manage.py runserver 0.0.0.0:8000"