from django.urls import path
from .views import PostList, PostDetail, PostCreate, PostEdit, PostDelete, ReviewPost, CategoryListView, ReviewList

urlpatterns = [
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/edit/', PostEdit.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('<int:pk>/review/', ReviewPost.as_view(), name='review_post'),
    path('categories/<int:pk>', CategoryListView.as_view(), name='category_list'),
    path('reviewlist/', ReviewList.as_view(), name='review_list')
]
