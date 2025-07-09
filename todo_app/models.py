from django.db import models


###if there is any change in modelpy run following
#python manage.py makemigrations
#python manage.py migrate

# Create your models here.
class Todo(models.Model): # PascalCase
    title = models.CharField(max_length = 200) #varchar, char

    def __str__(self): #agadi pachadi double underlone ho
        return self.title



