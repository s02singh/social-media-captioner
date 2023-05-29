from django.urls import path
from . import views

app_name = 'caption_generator'

urlpatterns = [
    path('', views.generate_caption, name='generate_caption'),
    
]
