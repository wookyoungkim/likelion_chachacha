from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
import users.views


# urlpatterns =[
#     path('', users.views.home, name='users'),
#     path('login/', users.views.login, name='login'),
#     path('signup/', users.views.signup, name='signup'),
#     path('signup_owner/', users.views.signup_owner, name='signup_owner'),
#     path('logout/', users.views.logout, name='logout'),
#     path('<int:user_id>/messages', users.views.message_post, name='message_post'),
#     path('<int:message_id>/messages/detail', users.views.message_detail, name='message_detail'),
#     # path('messages/<str:type>', users.views.message_box, name='message_box'),
#     path('messages/box', users.views.message_box, name='message_box'),
#     path('messages/box/<int:user_id>', users.views.message_room, name='message_room'),
#     path('<int:message_id>/messages/delete', users.views.message_delete, name='message_delete'),
#     path('detail/<int:bar_id>/reviews', users.views.create_review, name='bar_review'),

# ]


urlpatterns =[
    path('', users.views.home, name='users'),
    path('select_signup/',users.views.select_signup, name='select_signup'),
    path('login/', users.views.login, name='login'),
    path('signup/', users.views.signup, name='signup'),
    path('signup_owner/', users.views.signup_owner, name='signup_owner'),
    path('login/success',users.views.login_success, name='login_success'),
    path('logout/', users.views.logout, name='logout'),
    path('<int:user_id>/messages', users.views.message_post, name='message_post'),
    path('<int:message_id>/messages/detail', users.views.message_detail, name='message_detail'),
    # path('messages/<str:type>', users.views.message_box, name='message_box'),
    path('messages/box', users.views.message_box, name='message_box'),
    path('messages/box/<int:user_id>', users.views.message_room, name='message_room'),
    path('<int:message_id>/messages/delete', users.views.message_delete, name='message_delete'),
    path('detail/<int:bar_id>/reviews', users.views.create_review, name='bar_review'),
    path('<int:bar_id>/heart/', users.views.heart_bar, name='user_heart'),
    path('select', users.views.select, name='select'),
    path('done_select', users.views.done_select, name='done_select'),
    path('mypage_bars/', users.views.mypage_bars, name='mypage_bars'),
    path('mypage', users.views.mypage, name='mypage'),
    path('route_detail/<int:route_id>', users.views.route_detail, name='route_detail'),
    path('', users.views.loading, name='loading'),
    path('mypage_home', users.views.mypage_home, name='mypage_home'),
    path('about', users.views.about, name='about'),

]


# urlpatterns =[
#     path('', users.views.home, name='users'),
#     path('login/', users.views.login, name='login'),
#     path('signup/', users.views.signup, name='signup'),
#     path('signup_owner/', users.views.signup_owner, name='signup_owner'),
#     path('logout/', users.views.logout, name='logout'),
#     path('<int:user_id>/messages', users.views.message_post, name='message_post'),
#     path('<int:message_id>/messages/detail', users.views.message_detail, name='message_detail'),
#     # path('messages/<str:type>', users.views.message_box, name='message_box'),
#     path('messages/box', users.views.message_box, name='message_box'),
#     path('messages/box/<int:user_id>', users.views.message_room, name='message_room'),
#     path('<int:message_id>/messages/delete', users.views.message_delete, name='message_delete'),
#     path('detail/<int:bar_id>/reviews', users.views.create_review, name='bar_review'),
#     path('heart_bar/', users.views.heart_show, name='heart_bar'),
#     #path('route/', users.views.route, name='route'),
#     path('done_select', users.views.done_select, name='done_select'),
#     path('select', users.views.select, name='select'),
#     path('mypage', users.views.mypage, name='mypage'),
#     path('route_detail/<int:route_id>', users.views.route_detail, name='route_detail')

# ]