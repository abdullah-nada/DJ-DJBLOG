from django.shortcuts import render ,redirect

from .models import Post

from django.views.generic import ListView ,DetailView

from .forms import Postform

# Create your views here.


# def show_all_posts(request):
#     data=Post.objects.all()
#     context={
#         'var':data
#     }
#     return render(request,'posts\postlist.html',context)


def show_one_post(request,post_id):
    data=Post.objects.get(id=post_id)
    context={
        'var':data
    }
    return render(request,'posts\postdetail.html',context)


class Postlist(ListView):
    model=Post 
    template_name = "posts/post_list.html"
    context_object_name = "posts"



class PostDetail(DetailView):
    model=Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"



def create_post(request):
    if request.method == 'POST':
        form=Postform(request.POST,request.FILES)
        if form.is_valid():
            form.save() 
            return redirect('/posts/')
    else:
        form = Postform()
    
    
    return render(request,'posts/new.html',{'form':form})