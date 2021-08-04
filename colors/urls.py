from django.urls import path
from .views import ColorAPIView

app_name = 'colors'
urlpatterns = [
    path('colors/', ColorAPIView.as_view(), name='index')
]
