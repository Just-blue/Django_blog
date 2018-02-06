from django.db import models

class MessageModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=250)
    web = models.URLField(null=True,blank=True)
    content = models.TextField()
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.content[:20]