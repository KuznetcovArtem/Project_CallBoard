from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .forms import PostForm, ReviewPostForm, ReviewPostStatusForm
from .models import Post, Category, Review
from .filters import PostFilter


# Create your views here.
class PostList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'posts.html'
    context_object_name = 'posts'
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class PostDetail(LoginRequiredMixin, DetailView):
    raise_exception = True
    model = Post
    template_name = 'post_detail.html'
    context_object_name = 'post_detail'


class PostCreate(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostEdit(LoginRequiredMixin, UpdateView):
    raise_exception = True
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'


class PostDelete(LoginRequiredMixin, DeleteView):
    raise_exception = True
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')


class ReviewPost(LoginRequiredMixin, CreateView):
    raise_exception = True
    form_class = ReviewPostForm
    model = Review
    template_name = 'review_post.html'


class CategoryListView(LoginRequiredMixin, ListView):
    raise_exception = True
    model = Post
    template_name = 'category_list.html'
    context_object_name = 'category_post_list'

    def get_queryset(self):
        self.postCategory = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(postCategory=self.postCategory).order_by('-dateCreation')
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filterset'] = self.filterset
        return context


class ReviewList(ListView):
    model = Review
    template_name = 'review_list.html'
    context_object_name = 'review_post_list'
    paginate_by = 10

    def get_queryset(self):
        current_user = self.request.user
        if current_user.is_authenticated:
            return Review.objects.filter(reviewPost__author__authorUser=current_user)
        else:
            return Review.objects.none()


    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class ReviewChangeStatus(LoginRequiredMixin, UpdateView):
    raise_exception = True
    form_class = ReviewPostStatusForm
    model = Review
    template_name = 'review_post_edit.html'


class ReviewPostDelete(LoginRequiredMixin, DeleteView):
    raise_exception = True
    model = Review
    template_name = 'review_post_delete.html'
    success_url = reverse_lazy('review_list')
