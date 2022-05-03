from django.contrib import admin
from .models import Project # Импорт моделей из текущей папки с классом project

admin.site.register(Project) # Регистрируем модели, которые хотим видеть в админке