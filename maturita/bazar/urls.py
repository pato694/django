from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('list', views.AutoListView.as_view(), name='list'),
    path('detail/<int:pk>', views.AutoDetailView.as_view(), name='detail'),
]