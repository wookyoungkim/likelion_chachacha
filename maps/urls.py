from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

import maps.views

urlpatterns =[
    path('', maps.views.home),
    
]

