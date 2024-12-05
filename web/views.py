from django.shortcuts import render
from django.db.models import OuterRef,Exists
from rest_framework import generics
from .models import Food, FoodListSerializer,FoodCategory

# Create your views here.

class FoodsAPIView(generics.ListAPIView):
    serializer_class = FoodListSerializer

    def get_queryset(self):
        published_foods = Food.objects.filter(category=OuterRef('pk'), is_publish=True).order_by('id')
        return FoodCategory.objects.annotate(
            has_published_foods=Exists(published_foods)
        ).filter(has_published_foods=True).order_by('id')