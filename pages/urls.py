from django.urls import path

from . import views

app_name = 'pages'

urlpatterns = [
    path('contact/',views.contact_page_views,name='contact'),
    path('about/',views.about_page_views,name='about'),
    path('',views.home_page_views,name='home'),
]