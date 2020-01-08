from django.contrib import admin
from .models import *

# Register your models here.
admin.register(Manga)
admin.register(Volume)
admin.register(Chapter)
admin.register(Page)