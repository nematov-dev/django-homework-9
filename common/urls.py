from django.urls import path
from . import views

app_name = 'common'

urlpatterns = [
    path('recipies/',views.recipies_page_views,name='recipies'),
    path('blog/',views.blog_page_views,name='blog'),
    path('category/',views.category_page_views,name='category'),
    path('submit/',views.submit_page_views,name='submit'),
    path('login/',views.login_page_views,name='login'),
]
