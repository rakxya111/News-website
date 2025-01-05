from datetime import timezone
from datetime import datetime, timezone
from django.utils.timezone import now
from django.shortcuts import render
from newspaper.models import Post,Tag,Category
from django.views.generic import ListView , DetailView , CreateView , UpdateView , View,TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from newspaper.forms import PostForm,TagForm,CategoryForm
from django.shortcuts import redirect

class dashboardView(LoginRequiredMixin,ListView):
    model = Post
    template_name = "aznews/dashboard/index.html"
    context_object_name = "posts"

    def get_queryset(self):
        post = Post.objects.filter(published_at__isnull=False,status="active").order_by("-published_at")
        return post

# class dashboardd(LoginRequiredMixin,TemplateView):
   
#     template_name = "aznews/dashboard/header.html"
    
class PostlistView(LoginRequiredMixin,ListView):
    model = Post
    template_name = "aznews/dashboard/index.html"
    context_object_name = "posts"

    def get_queryset(self):
        post = Post.objects.filter(published_at__isnull=False,status="active").order_by("-published_at")
        return post

class PostDeleteView(LoginRequiredMixin,View):

    def get(self,request,pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect("post-list-view")
    
class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = "aznews/dashboard/post_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        queryset = Post.objects.filter(pk=self.kwargs["pk"])
        return queryset

class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    template_name = "aznews/dashboard/post_create.html"
    form_class = PostForm

    def get_success_url(self):
        post = self.get_object()
        return reverse_lazy("dash-post-detail",kwargs={"pk" : post.pk}) 

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    template_name = "aznews/dashboard/post_create.html"
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy("dash-post-detail",kwargs={"pk" : self.object.pk })
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class TaglistView(LoginRequiredMixin,ListView):
    model = Tag
    template_name = "aznews/dashboard/tags.html"
    context_object_name = "tags"

class TagDeleteView(LoginRequiredMixin,View):

    def get(self,request,pk):
        tag = Tag.objects.get(pk=pk)
        tag.delete()
        return redirect("tag-list")
    
class TagUpdateView(LoginRequiredMixin,UpdateView):
    model = Tag
    template_name = "aznews/dashboard/create_tag.html"
    form_class = TagForm

    def get_success_url(self):
        post = self.get_object()
        return reverse_lazy("tag-list")

class TagCreateView(LoginRequiredMixin,CreateView):
    model = Tag
    template_name = "aznews/dashboard/create_tag.html"
    form_class = TagForm

    def get_success_url(self):
        return reverse_lazy("tag-list")

class CategorylistView(LoginRequiredMixin,ListView):
    model = Category
    template_name = "aznews/dashboard/categories.html"
    context_object_name = "categoriess"  

class CategoryDeleteView(LoginRequiredMixin,View):

    def get(self,request,pk):
        category = Category.objects.get(pk=pk)
        category.delete()
        return redirect("category-list") 

class CategoryUpdateView(LoginRequiredMixin,UpdateView):
    model = Category
    template_name = "aznews/dashboard/create_category.html"
    form_class = CategoryForm

    def get_success_url(self):
        catgory = self.get_object()
        return reverse_lazy("category-list")

class CategoryCreateView(LoginRequiredMixin,CreateView):
    model = Category
    template_name = "aznews/dashboard/create_category.html"
    form_class = CategoryForm

    def get_success_url(self):
        return reverse_lazy("category-list")

class PostPublishView(LoginRequiredMixin,View):

    def get(self,request,pk):
        post = Post.objects.get(pk=pk)
        
        post.save()
        return redirect("post-list-view")

class DraftListView(LoginRequiredMixin,ListView):
    model = Post
    template_name = "aznews/dashboard/draft_list.html"
    context_object_name = "postss"

    def get_queryset(self):
        post = Post.objects.filter(published_at__isnull=True,status="active")
        return post


class DraftPublishView(LoginRequiredMixin,View):

    def get(self,request,pk):
        post = Post.objects.get(pk=pk)
        post.published_at = datetime.now(timezone.utc)
        post.save()
        return redirect("draft-list-view")

class DraftUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    template_name = "aznews/dashboard/post_create.html"
    form_class = PostForm

    def get_success_url(self):
        post = self.get_object()
        return reverse_lazy("draft-detail-view",kwargs={"pk" : post.pk}) 

class DraftDeleteView(LoginRequiredMixin,View):

    def get(self,request,pk):
        post = Post.objects.get(pk=pk)
        post.delete()
        return redirect("draft-list-view")

class DraftDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = "aznews/dashboard/draft_detail.html"
    context_object_name = "post"

    def get_queryset(self):
        queryset = Post.objects.filter(pk=self.kwargs["pk"],published_at__isnull=True)
        return queryset   


class InactivePostListView(ListView):
    model = Post
    template_name = 'aznews/dashboard/inactive_post_list.html' 
    context_object_name = 'posts1'          

    def get_queryset(self):
        queryset =  Post.objects.filter(published_at__isnull=True,status='in_active')
        return queryset
    
class MakeActiveView(LoginRequiredMixin,View):
    def get(self,request,pk):
        post = Post.objects.get(pk=pk,status='in_active')
        post.status = 'active'
        post.save()
        return redirect('inactive-post-view')

class DeActiveView(LoginRequiredMixin,View):
    def get(self,request,pk):
        post = Post.objects.get(pk=pk,published_at__isnull=False,status='active')
        post.published_at = None
        post.status = 'in_active'
        post.save()
        return redirect('inactive-post-view')
