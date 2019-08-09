from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
import bars.views
# from users import views

urlpatterns = [
    path('', bars.views.home, name='home'),
    path('detail/<int:bar_id>', bars.views.bar_detail, name='bar_detail'),
    # path('detail/<int:bar_id>/reviews', users.views.create_review, name='bar_review')
    path('detail/<int:bar_id>/reviews',bars.views.bar_review, name='bar_detail_review'),
    path('detail/<int:bar_id>/menu',bars.views.bar_menu, name='bar_detail_menu'),
    path('bars_select', bars.views.bar_select, name='bars_select'),
    path('bars_detail/<int:bar_id>', bars.views.bar_detail, name='bar_detail'),
    path('bars_detail_detail/<int:bar_id>',bars.views.bar_detail_detail,name='bar_datail_detail'),
]

