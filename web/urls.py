from django.urls import path
from . import views

urlpatterns = [
    path('v1/foods/', views.FoodsAPIView.as_view()),
]