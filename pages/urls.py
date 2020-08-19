from django.urls import path
from .views import HomPageView, AboutPageView

urlpatterns = [
    path('', HomPageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
]
