from django.db import models

# Create your models here.


class Blogs(models.Model):
    Blog_Tittle = models.CharField(max_length=50)
    Blog_Time = models.DateTimeField(auto_now=True)
    Blog_Description = models.CharField(max_length=350)
    Blog_AuthorName = models.CharField(max_length=30)

    def __str__(self):
        return self.Blog_Tittle
