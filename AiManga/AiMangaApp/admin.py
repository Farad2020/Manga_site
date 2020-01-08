from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Manga)
admin.site.register(Volume)
admin.site.register(Chapter)
admin.site.register(Page)