from django.urls import path
from .views import upload_media, upload_success

urlpatterns = [
    path('upload/', upload_media, name='upload_media'),
    path('upload/success/', upload_success, name='upload_success'),
]