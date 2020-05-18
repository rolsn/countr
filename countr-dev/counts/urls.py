from django.urls import path

from . import views

app_name='counts'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:counter_id>/', views.detail, name='detail'),
]
