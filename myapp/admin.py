from django.contrib import admin
from myapp.models import *

# Register your models here.
admin.site.register(Genre)
admin.site.register(Music)
admin.site.register(Comment)
admin.site.register(Post)