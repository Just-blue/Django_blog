from datetime import timezone

from django import template
from django.db.models.aggregates import Count

from ..models import PostModel,CategoryModel,TagModel

register = template.Library()

@register.simple_tag
def get_recent_posts(num=3):
    return PostModel.objects.all().order_by('-time')[:num]

@register.simple_tag
def get_categories():
    # 记得在顶部引入 count 函数
    # Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称
    return CategoryModel.objects.annotate(num_posts=Count('postmodel')).filter(num_posts__gt=0)

@register.simple_tag
def get_tags():
    return TagModel.objects.annotate(num_posts=Count('postmodel')).filter(num_posts__gt=0)
