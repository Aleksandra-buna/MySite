from django.urls import path
from . import views

urlpatterns = [
    path('', views.posts, name='posts'),  #name= nuzhno dlya ukazania link v html file
    path('<int:id_page>/', views.specific_id, name='id'),  #name= nuzhno dlya ukazania link v html file
]