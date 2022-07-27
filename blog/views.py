from ast import IsNot
from multiprocessing import context
from pkgutil import get_data
from django.views.generic import ListView, DetailView, UpdateView,CreateView
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post, Comment
from .forms import PostForm, CommentForm

# Create your views here.
# def blog(request):
#     posts = Post.objects.all().order_by('-pk')
#     return render(request, 'blog/blog.html', {'posts':posts})


class PostList(ListView):
    model = Post
    ordering = '-pk'
    template_name = 'blog/blog.html'

# def single_post(request, pk):
#     post = Post.objects.get(pk=pk)
#     return render(request, 'blog/single_post.html', {'post':post})


class PostDetail(DetailView):
    model = Post
    template_name = 'blog/single_post.html'

    def get_context_data(self, **kwargs):
        context = super(PostDetail, self).get_context_data()
        context['comment_form'] = CommentForm
        return context


class PostCreate(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_write.html'
    success_url = "/"


def new_comment(request, pk):
    # if request.user.is_authenticated:
    #     post=get_object_or_404(Post,pk=pk)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        post = get_object_or_404(Post, pk=pk)

        if post is None or not comment_form.is_valid():
            return redirect(post.get_absolute_url())

        else:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.author = comment.author
            comment.save()
            return redirect(comment.get_absolute_url())

    # else:
        # raise PermissionDenied


class CommentUpdate(UpdateView):
    model = Comment
    context_object_name = 'blog/comment_form.html'
    form_class = CommentForm
    success_url = '/'

    # def dispatch(self,request,*args,**kwargs):
    #     if request.user==self.get_object().author:
    #        return super(CommentUpdate,self).dispatch(request)

    def get_object(self):
        comment = get_object_or_404(Comment, pk=self.kwargs['pk'])
        return comment


def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    post = comment.post
    comment.delete()
    return redirect(post.get_absolute_url())
