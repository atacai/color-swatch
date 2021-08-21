from django.urls import path
from .views import ColorSpaceAPIView

app_name = 'colors'
urlpatterns = [
    path('colors/', ColorSpaceAPIView.as_view(), name='index')
]
