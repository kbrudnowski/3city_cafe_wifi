from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('add_new/', views.add_cafe, name='add_new'),
    path('delete/<id>/', views.delete_cafe, name='delete_cafe'),

]