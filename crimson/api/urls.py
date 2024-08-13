from django.urls import path
from django.views.generic import TemplateView
from .views import SalaView, SalaInsert, main

urlpatterns = [
    path('ver_sala', SalaView.as_view()),
    path('adi_sala', SalaInsert.as_view()),
    path('home', main),
    # path('apis', TemplateView.as_view(template_name='apis.html'), name='apis')
]