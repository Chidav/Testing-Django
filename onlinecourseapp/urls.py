from django.urls import path
from . import views

app_name = "onlinecourseapp"

urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:price>/', views.post_detail, name='post_detail'),
]
