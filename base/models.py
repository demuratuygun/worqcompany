from django.db import models

class User(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)

    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=20)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name+" "+self.surname


class Platform(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=0)
    url = models.CharField(max_length=2083)
    platform = models.CharField(max_length=200)
