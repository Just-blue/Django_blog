
from django.db.models import Q
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from blog.models import PostModel, CategoryModel, TagModel
from django.views.generic import ListView, DetailView
from comments.forms import CommentForm

# 主页视图
from gallery.models import GalleryModel
from message.forms import MessageForm


class IndexView(ListView):
    model = PostModel
    template_name = 'blog/index.html'
    context_object_name = 'post_list'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        gallery_list = GalleryModel.objects.all().order_by('-time')[:3]
        context.update({'gallery_list': gallery_list})
        return context


# 博客主页视图
class BlogView(ListView):
    model = PostModel
    template_name = 'blog/blog.html'
    context_object_name = 'post_list'
    paginate_by = 3

    # def get_queryset(self):
    #     year = self.kwargs.get('year')
    #     month = self.kwargs.get('month')
    #     return super(BlogView, self).get_queryset().filter(time__year=year,
    #                                                        time__month=month
    #                                                        )


# 分类标签视图
class CategoryView(BlogView):
    def get_queryset(self):
        cate = get_object_or_404(CategoryModel, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate).order_by('-time')

    '''
        等价：
        cate = get_object_or_404(CategoryModel, pk=pk)
        post_list = PostModel.objects.filter(category=cate).order_by('-time')
        return render(request, 'blog/blog.html', context={'post_list': post_list})
    '''


# Tag标签视图
class TagView(BlogView):
    def get_queryset(self):
        tag = get_object_or_404(TagModel, pk=self.kwargs.get('pk'))
        return super(TagView, self).get_queryset().filter(tags=tag)


# 详情页面视图
class PostDetailView(DetailView):
    # 这些属性的含义和 ListView 是一样的
    model = PostModel
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get(self, request, *args, **kwargs):
        # 覆写 get 方法的目的是因为每当文章被访问一次，就得将文章阅读量 +1
        # get 方法返回的是一个 HttpResponse 实例
        # 之所以需要先调用父类的 get 方法，是因为只有当 get 方法被调用后，
        # 才有 self.object 属性，其值为 Post 模型实例，即被访问的文章 post
        response = super(PostDetailView, self).get(request, *args, **kwargs)

        # 将文章阅读量 +1
        # 注意 self.object 的值就是被访问的文章 post
        self.object.increase_views()

        # 视图必须返回一个 HttpResponse 对象
        return response

    # def get_object(self, queryset=None):
    #     # 覆写 get_object 方法的目的是因为需要对 post 的 body 值进行渲染
    #     post = super(PostDetailView, self).get_object(queryset=None)
    #     post.body = markdown.markdown(post.body,
    #                                   extensions=[
    #                                       'markdown.extensions.extra',
    #                                       'markdown.extensions.codehilite',
    #                                   ])
    #     return post

    def get_context_data(self, **kwargs):
        # 覆写 get_context_data 的目的是因为除了将 post 传递给模板外（DetailView 已经帮我们完成），
        # 还要把评论表单、post 下的评论列表传递给模板。
        context = super(PostDetailView, self).get_context_data(**kwargs)
        form = CommentForm()

        # post = super(PostDetailView, self).get_object(queryset=None)
        # comment_list = CommentModel.objects.filter(post=post)

        comment_list = self.object.commentmodel_set.all()
        context.update({
            'form': form,
            'comment_list': comment_list
        })
        return context


def search(request):
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = "请输入关键词"
        return render(request, 'blog/blog.html', {'error_msg': error_msg})

    post_list = PostModel.objects.filter(Q(title__icontains=q) | Q(body__icontains=q))
    return render(request, 'blog/blog.html', {'error_msg': error_msg,
                                              'post_list': post_list})


def page(request):
    return render(request, 'blog/page.html')


class ContactView(IndexView):
    template_name = 'blog/contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        form = MessageForm()
        context.update({'form': form})
        return context


def project(request):
    return render(request, 'blog/project.html')
