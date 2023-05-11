from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('user_login/', views.user_login, name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('user_register/', views.user_register, name='user_register'),
    path('details/<int:pk>/', views.details, name='details'),
    path('categories/', views.categories, name='categories'),
    path('all_posts/', views.all_posts, name='all_posts'),
    path('search/', views.search, name='search'),
    path('category/<int:pk>/', views.category, name='category'),
]