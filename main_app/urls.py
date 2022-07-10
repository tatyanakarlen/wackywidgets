from django.urls import path
from . import views

urlpatterns = [
 path('', views.home, name='home'), 
 path('wackywidgets/', views.index, name='wacky_widgets'),
 path('wackywidgets/new_widget/', views.widget_create.as_view(), name='widget_create'),
 path('wackywidgets/<int:pk>/delete/', views.widget_delete.as_view(), name='widget_delete'), 
]