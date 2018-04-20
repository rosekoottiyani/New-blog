
from django.db import models
from django.utils import timezone
# Create your models here.
class register(models.Model):
    username=models.CharField(default="",max_length=100,unique= True)
    password=models.CharField(default="",max_length=100)
    name=models.CharField(default="",max_length=100)
    email=models.EmailField(default="",max_length=100)
    mobile=models.CharField(default="",max_length=100)
    question=models.CharField(default="",max_length=100)
    answer=models.CharField(default="",max_length=100)


class blog(models.Model):
    username=models.CharField(default="",max_length=100)
    author = models.CharField(default="",max_length=100)
    title = models.CharField(default="",max_length=100)
    blogpost=models.TextField(default="")


class Comment(models.Model):
    post = models.ForeignKey('blog', related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
