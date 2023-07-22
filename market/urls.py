from django.urls import path

from market import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>/', views.prihod_to_rashod, name='prihod_to_rashod'),
    path('rashod/', views.rashod, name='rashod'),
    path('create_prihod/', views.create_prihod, name='create_prihod'),
    path('create_good/', views.create_good, name='create_good'),
    path('create_goods/', views.create_goods, name='create_goods'),
    path('counterparty/', views.counterparty, name='create_counterparty'),
    path('create_measure/', views.create_measure, name='create_measure'),
]