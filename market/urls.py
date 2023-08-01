from django.urls import path

from market import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create_goods/', views.create_goods, name='create_goods'),
    path('deletegoods/<int:pk>/', views.deletegoods, name='deletegoods'),
    path('code_number/<str:code_number>/', views.code_number, name='code_number'),
    path('create_good/', views.create_good, name='create_good'),
    path('create_deliver/', views.create_deliver, name='create_deliver'),
    path('create_measure/', views.create_measure, name='create_measure'),
]