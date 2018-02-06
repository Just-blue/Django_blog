from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView

from message.forms import MessageForm

def message(request):
    if request.method == 'POST' :
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save()
            message.save()
            return redirect('blog:contact')
        else:
            context = { 'form':form }
            return render(request, 'blog/contact.html', context=context)
    return redirect('blog:ContactView.as_view()')
