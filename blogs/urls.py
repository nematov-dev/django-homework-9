from django.urls import path

from blogs import views

app_name = 'blogs'

urlpatterns = [
    path('<int:pk>/', views.blog_detail_view, name='detail'),
    path('<int:pk>/comment/', views.blog_comment_view, name='comment'),
    path('', views.blog_list_view, name='list'),
]