from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from data import models


def home(request):
    return render(request, 'two_list.html')


def two_list(request):
    if request.method == "POST":
        cars = request.POST.get('cars')
        News_Paper = request.POST.get('News_Paper')
        add1 = models.list.objects.create(cars=cars,)
        add2 = models.list.objects.create(News_Paper=News_Paper)
        add1, add2.save()

    return render(request, 'user_view.html')
