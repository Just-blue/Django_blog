from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic import ListView, DetailView

from gallery.models import GalleryModel, CategoryModel


class GalleryView(ListView):
    model = GalleryModel
    template_name = 'blog/Gallery.html'
    context_object_name = 'gallery_list'
    paginate_by = 12

class ProjectView(DetailView):
    model = GalleryModel
    template_name = 'blog/project.html'
    context_object_name = 'gallery'

    def get_context_data(self, **kwargs):
        context = super(ProjectView, self).get_context_data(**kwargs)

        cate = get_object_or_404(CategoryModel, pk=self.kwargs.get('pk'))
        related_list = GalleryModel.objects.filter(category=cate).order_by('-time')
        context.update({
            'related_list': related_list
        })
        return context



