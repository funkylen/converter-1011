from django.urls import path

from .views import get_conversion_result

urlpatterns = [
    path('test/', get_conversion_result),
]