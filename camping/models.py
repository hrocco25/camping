from django.db import models


class Camp(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=150)
    description = models.TextField()
    road = models.CharField(default="Paved, Gravel, Dirt, or 4x4", max_length=100)
    management = models.CharField(max_length=100, default="Public or Private Land")
    number_of_campsites = models.PositiveIntegerField()
    number_of_days = models.PositiveIntegerField()
    image=models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name

class Review(models.Model):
    title = models.CharField(max_length= 200)
    content= models.TextField()
    author= models.CharField(max_length=200)
    camp = models.ForeignKey(Camp, on_delete = models.CASCADE, related_name = 'reviews')

    def __str__(self):
        return self.title