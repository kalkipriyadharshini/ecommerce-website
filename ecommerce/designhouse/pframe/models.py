from django.db import models

   
class Datas(models.Model):
  Name=models.CharField(max_length=20,default="")
  Age=models.IntegerField(default="")
  Contect=models.IntegerField(default="")
  Address=models.CharField(max_length=50,default="")
  Mail=models.CharField(max_length=50,default="")

