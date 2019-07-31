from django.db import models

class TeluguactorsData(models.Model):
    name=models.CharField(max_length=30)
    rating=models.IntegerField()
    date=models.DateTimeField(max_length=100)
    feedback=models.TextField(max_length=500)
    location=models.CharField(max_length=50)
    salary=models.IntegerField()
    email=models.EmailField(max_length=100)






