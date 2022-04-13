from django.db import models

# The Author model has been created for you
class Author(models.Model):
  name = models.CharField(max_length=50)
  # drawing = models.ForeignKey(Drawing, on_delete=models.CASCADE)

# # Create the Drawing model
# class Point(models.Model):
#   x = models.FloatField()
#   y = models.FloatField()
  
class Drawing(models.Model):
  title = models.CharField(max_length=50)
  author = models.CharField(max_length=50)
  points = models.CharField(max_length=1000000)

# class Drawings(models.Model):
#   drawings = models.ManyToManyField(Point)




