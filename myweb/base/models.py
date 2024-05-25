from django.db import models

from django.contrib.auth.models import User

class Topic(models.Model):
    name= models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Room(models.Model):
    topic=models.CharField(Topic, max_length=200)
    name=models.CharField(max_length=200)
    description=models.TextField(null=True,blank=True) #null=True მონაცემთა ბაზამ რომ არ დააეროროს და blank=True html ფორმამ რომ არ დაეროროს როცა ცარიელი იქნება.
    created=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name

#class Meal(models.Model):
    #name = models.CharField(max_length=100)
   # description = models.TextField()
   # picture = models.ImageField(upload_to='meal_pictures/', null=True, blank=True)
   # room = models.ForeignKey(Room, on_delete=models.CASCADE)
    #created = models.DateTimeField(auto_now_add=True)
   # class Meta:
        #ordering=['-created']

   # def __str__(self):
      #  return self.name