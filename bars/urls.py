from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
import bars.views
# from users import views

urlpatterns = [
    path('', bars.views.home),
    path('detail/<int:bar_id>', bars.views.bar_detail, name='bar_detail'),
    # path('detail/<int:bar_id>/reviews', users.views.create_review, name='bar_review')
]

