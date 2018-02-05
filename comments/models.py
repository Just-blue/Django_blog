from django.db import models

from blog.models import PostModel


class CommentModel(models.Model):

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=250)
    url = models.URLField(null=True,blank=True)
    text = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(PostModel,on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.text[:20]