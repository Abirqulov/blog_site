from django.contrib import admin
from .models import Contact
# Register your models here.


class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone']


admin.site.register(Contact, ContactUsAdmin)