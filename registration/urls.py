# registration/urls.py
from django.urls import path
from .views import exam_registration, success_view

urlpatterns = [
    path('', exam_registration, name='exam_registration'),
    path('success/', success_view, name='success'),
]
