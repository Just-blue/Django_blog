from django.shortcuts import render, get_object_or_404, redirect

from blog.models import PostModel
from .models import CommentModel
from .forms import CommentForm


def post_comment(request, post_pk):
    post = get_object_or_404(PostModel, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)

        # 当调用 form.is_valid() 方法时，Django 自动帮我们检查表单的数据是否符合格式要求。
        if form.is_valid():
            # 检查到数据是合法的，调用表单的 save 方法保存数据到数据库，
            # commit=False 的作用是仅仅利用表单的数据生成 Comment 模型类的实例，但还不保存评论数据到数据库。

            comment = form.save(commit=False)

            # 将评论和被评论的文章关联起来。
            comment.post = post

            comment.save()

            # 重定向到 post 的详情页，实际上当 redirect 函数接收一个模型的实例时，它会调用这个模型实例的 get_absolute_url 方法，
            # 然后重定向到 get_absolute_url 方法返回的 URL。
            return redirect(post)
        else:
            # 因此使用 post.commentmodel_set.all() 反向查询全部评论。

            comment_list = post.commentmodel_set.all()
            context = {'post': post,
                       'form': form,
                       'comment_list': comment_list
                       }
            return render(request, 'blog/detail.html', context=context)
            # 不是 post 请求，说明用户没有提交数据，重定向到文章详情页。
        return redirect(post)
