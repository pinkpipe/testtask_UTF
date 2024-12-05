from django.contrib import admin

from web.models import FoodCategory, Food

# Register your models here.

admin.site.register(Food)
admin.site.register(FoodCategory)