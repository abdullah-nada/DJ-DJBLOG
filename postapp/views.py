from django.shortcuts import render

from .models import Post
# Create your views here.


def show_all_posts(request):
    data=Post.objects.all()
    context={
        'var':data
    }
    return render(request,'posts\postlist.html',context)


def show_one_post(request,pk):
    data=Post.objects.get(id=pk)
    context={
        'var':data
    }
    return render(request,'posts\postdetail.html',context)
