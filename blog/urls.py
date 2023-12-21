# blog/urls.py
from django.urls import path
from .views import create_blog_post, doctor_posts, patient_posts, edit_blog_post, read_blog_post, like_post

urlpatterns = [
    path('create/', create_blog_post, name='create_blog_post'),
    path('edit_blog_post/<int:post_id>/',
         edit_blog_post, name='edit_blog_post'),
    path('read_blog_post/<int:post_id>/',
         read_blog_post, name='read_blog_post'),
    path('doctor_posts/', doctor_posts, name='doctor_posts'),
    path('patient_posts/', patient_posts, name='patient_posts'),
    path('like_post/<int:post_id>/', like_post, name='like_post')
]
