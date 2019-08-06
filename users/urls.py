from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
import users.views


urlpatterns =[
    path('', users.views.home, name='users'),
    path('login/', users.views.login, name='login'),
    path('signup/', users.views.signup, name='signup'),
    path('signup_owner/', users.views.signup_owner, name='signup_owner'),
    path('logout/', users.views.logout, name='logout'),
    path('<int:user_id>/messages', users.views.message_post, name='message_post'),
    path('<int:message_id>/messages/detail', users.views.message_detail, name='message_detail'),
    # path('messages/<str:type>', users.views.message_box, name='message_box'),
    path('messages/box', users.views.message_box, name='message_box'),
    path('messages/box/<int:user_id>', users.views.message_room, name='message_room'),
    path('<int:message_id>/messages/delete', users.views.message_delete, name='message_delete'),
    path('detail/<int:bar_id>/reviews', users.views.create_review, name='bar_review')

]


