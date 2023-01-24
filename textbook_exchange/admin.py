from django.contrib import admin
from .models import *

# Register your models here.
from .models import Department
admin.site.register(Department)
admin.site.register(FriendRequest)
admin.site.register(Book)
admin.site.register(FriendsList)
admin.site.register(FavoriteBooks)