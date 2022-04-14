from django.contrib import admin

from .models import hello
# Register your models here.


@admin.register(hello)
class helloadmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'city']
