from django.shortcuts import render

from bars.models import Bar
# from .bars import models

# Create your views here.


def home(request):
    bars=Bar.objects.all()
    return render(request, 'maps_home.html',{'bars':bars})