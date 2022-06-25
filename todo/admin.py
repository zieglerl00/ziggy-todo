from django.contrib import admin

# Register your models here.
from todo.models import Importance, Status, Todo

admin.site.register(Importance)
admin.site.register(Status)
admin.site.register(Todo)
