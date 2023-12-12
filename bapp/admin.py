from django.contrib import admin
from .models import Books,Buy,BookRent,Review,User,UserProfile

# Register your models here.
admin.site.register(Books)

admin.site.register(Buy)
admin.site.register(BookRent)

admin.site.register(UserProfile)