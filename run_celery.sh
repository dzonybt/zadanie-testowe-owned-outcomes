#!/bin/sh

# wait for RabbitMQ server to start
sleep 10

cd projekt_django  
su -m dzonybt -c "celery worker -A projekt_django.celeryconf -Q default -n default@%h"  