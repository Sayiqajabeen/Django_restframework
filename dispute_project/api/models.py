from django.db import models

# Create your models here.
from django.db import models

class DisputeRequest(models.Model):
    payment_status = models.IntegerField()
    account_status = models.CharField(max_length=50)
    creditor_remark = models.TextField()
    dispute_letter_generated = models.BooleanField(default=False)





# django-admin startproject dispute_project
# cd dispute_project
# python manage.py startapp api
# INSTALLED_APPS = [
#     ...
#     'rest_framework',
#     'api',
# ]
# python manage.py makemigrations
# python manage.py migrate
# python manage.py runserver
# http://127.0.0.1:8000/api/process/?payment_status=30&account_status=open&creditor_remark=Some+Remark
