from django.db import models

# Create your models here.


class Blogs(models.Model):
    Blog_Tittle = models.CharField(max_length=50, default='0')
    Blog_Time = models.DateTimeField(auto_now=True)
    Blog_Description = models.TextField(max_length=350, default='0')
    Blog_AuthorName = models.CharField(max_length=30)

    def __str__(self):
        return self.Blog_Tittle
