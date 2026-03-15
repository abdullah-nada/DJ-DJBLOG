from django.shortcuts import render ,redirect

from .models import Post

from django.views.generic import ListView ,DetailView ,CreateView ,UpdateView ,DeleteView

from .forms import Postform

# Create your views here.

#fun show all posts

def show_all_posts(request):
    data=Post.objects.all()
    context={
        'var':data
    }
    return render(request,'posts\postlist.html',context)


def show_one_post(request,post_id):
    data=Post.objects.get(id=post_id)
    context={
        'var':data
    }
    return render(request,'posts\postdetail.html',context)


#creat post from mointor

def create_post(request):
    if request.method == 'POST':
        form=Postform(request.POST,request.FILES)
        if form.is_valid():
            my_form=form.save(commit=False) 
            my_form.author=request.user
            my_form.save()
            return redirect('/posts/')
    else:
        form = Postform()
    
    
    return render(request,'posts/new.html',{'form':form})


#edit function

def edit_post(request,pk):
    post=Post.objects.get(id=pk)
    if request.method == 'POST':
        form=Postform(request.POST,request.FILES,instance=post)
        if form.is_valid():
            my_form=form.save(commit=False) 
            my_form.author=request.user
            my_form.save()
            return redirect('/posts/')
    else:
        form = Postform(instance=post)
    
    
    return render(request,'posts/edit.html',{'form':form})


def delete_post(request,pk):
    post=Post.objects.get(id=pk)
    post.delete()
    return redirect('/posts/')



#CBV

class Postlist(ListView):
    model=Post 
    template_name = "posts/post_list.html"
    context_object_name = "posts"



class PostDetail(DetailView):
    model=Post
    template_name = "posts/post_detail.html"
    context_object_name = "post"


class Addpost(CreateView):
    model=Post
    fields='__all__'
    template_name = "posts/post_form.html"
    success_url='/posts/'


class Editview(UpdateView ):
    model=Post
    fields='__all__'
    template_name = "posts/edit.html"
    success_url='/posts/'


class Deletepost(DeleteView):
    model=Post
    template_name ="posts/post_confirm_delete.html"
    success_url='/posts/'







