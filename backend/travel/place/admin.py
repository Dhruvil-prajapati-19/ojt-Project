from django.contrib import admin
from . import models
from .models import card
# Register your models here.

@admin.register(models.card)
class cardAdmin(admin.ModelAdmin):
    list_display = ['city','Country','price']
    search_fileds = ['city','Country']
