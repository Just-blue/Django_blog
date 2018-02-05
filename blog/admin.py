from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import PostModel, CategoryModel, TagModel


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'time', 'category', 'author']


list_display = ('image_img', 'product',)
readonly_fields = ('image_img',)
fields = ('image_img',)


# 把新增的 PostAdmin 也注册进来
admin.site.register(PostModel,PostAdmin)
admin.site.register(CategoryModel)
admin.site.register(TagModel)


