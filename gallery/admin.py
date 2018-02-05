from django.contrib import admin

from .models import GalleryModel, ImageModel, CategoryModel


class ImageInline(admin.TabularInline):
    model = ImageModel

class GalleryAdmin(admin.ModelAdmin):
    inlines = [ImageInline]

admin.site.register(GalleryModel, GalleryAdmin)
admin.site.register(ImageModel)
admin.site.register(CategoryModel)