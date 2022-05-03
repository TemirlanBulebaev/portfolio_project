from django.shortcuts import render
from .models import Project # импортируем модели из базы данных
def home(request):
    projects = Project.objects.all() # так джанго импортирует данные из базы данных
    return render(request, 'portfolio/home.html', {'projects': projects}) #Передаем словарь в шаблон
