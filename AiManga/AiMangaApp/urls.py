from django.contrib import admin
from django.urls import path
from . import views
app_name = "AiMangaApp"

urlpatterns = [
    path("", views.index, name="index"),
    path('admin/', admin.site.urls),
]