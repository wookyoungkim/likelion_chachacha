from django.shortcuts import render
from .models import Loc
# from .bars import models

# Create your views here.


def home(request):
    locs=Loc.objects.all()
    return render(request, 'maps_home.html',{'locs':locs})
