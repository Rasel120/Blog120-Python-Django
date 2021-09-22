from django.contrib import admin
# Register your models here.
from home.models import contact, information, about


@admin.register(contact)
class Contact(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'subject', 'timestamp']


@admin.register(information)
class Information(admin.ModelAdmin):
    list_display = ['email', 'call', 'location']


@admin.register(about)
class About(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'description']

