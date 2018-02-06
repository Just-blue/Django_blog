from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

from gallery.files_handle import ThumbnailImageField


class CategoryModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class GalleryModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    time = models.DateTimeField()
    category = models.ForeignKey(CategoryModel, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User,on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['-time']

    def __str__(self):
        return self.title

    def get_month(self):
        return self.time.strftime("%b")

    def get_absolute_url(self):
        return reverse('gallery:project', kwargs={'pk': self.pk})


class ImageModel(models.Model):

    gallery = models.ForeignKey(GalleryModel,on_delete=models.SET_NULL, null=True)

    image = ThumbnailImageField(upload_to='./gallery/')
