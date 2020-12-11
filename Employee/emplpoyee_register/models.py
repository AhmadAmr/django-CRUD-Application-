from django.db import models

class Postion(models.Model):
    pos=models.CharField(max_length=50)

    def __str__(self):
        return self.pos
class create(models.Model):
    name=models.CharField(max_length=20)
    title=models.CharField(max_length=20)
    age=models.IntegerField()
    postion=models.ForeignKey(Postion,on_delete=models.CASCADE)