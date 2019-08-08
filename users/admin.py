from django.contrib import admin
from users.models import User, Message, Review, Route
# Register your models here.

admin.site.register(User)
admin.site.register(Message)
admin.site.register(Review)
admin.site.register(Route)