from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=100)  # ограничеваем количество символов
    description = models.CharField(max_length=250)  # значение для короткого описания проекта
    image = models.ImageField(upload_to='portfolio/images/')  # Откуда будут браться изображения
    url = models.URLField(blank=True)  # Позволяет открывать страницу на новой вкладке браузера

    def __str__(self):
        return self.title