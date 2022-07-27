from . import views
from django.urls import path

urlpatterns = [
    # path('', views.blog, name='blog'),
    path('', views.PostList.as_view(), name='blog'),
    # path('<int:pk>/', views.single_post, name='single_post')
    path('<int:pk>/', views.PostDetail.as_view()),
    path('write/', views.PostCreate.as_view()),
    path('<int:pk>/new_comment/',views.new_comment),
    path('<int:pk>/CommentUpdate/',views.CommentUpdate.as_view()),
    path('<int:pk>/delete_comment/',views.delete_comment),
]