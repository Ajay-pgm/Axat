from django.db import models
from django.db import models
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend


class Register(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    number = models.CharField(max_length=10)

    class Meta:
        db_table = 'Register'


admin, status = Group.objects.get_or_create(name='admin')
teacher, status = Group.objects.get_or_create(name='teacher')
student, status = Group.objects.get_or_create(name='student')


class dashboard(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='media', default='')

    class Meta :
        db_table = 'dashdb'


'''
Hii there! I try  my level best to implement email authentication but not success so i only built
user authentication sys 
'''



#
# class EmailBackend(ModelBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         UserModel = get_user_model()
#         user = UserModel.objects.get(email=username)
#         return None
#

# Create your models here.
