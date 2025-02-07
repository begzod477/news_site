from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    published_date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='news_images/', null=True, blank=True)

    def __str__(self):
        return self.title

