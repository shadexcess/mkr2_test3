from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Image(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='gallery/')
    categories = models.ManyToManyField(Category)
    created_date = models.DateField(auto_now_add=True)
    age_limit = models.PositiveIntegerField()

    def __str__(self):
        return self.title