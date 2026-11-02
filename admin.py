from django.contrib import admin

from app.models import UserData
from .models import ContactMessage, Appointment, Newsletter

# Register your models here.
admin.site.register(ContactMessage)
admin.site.register(Appointment)
admin.site.register(Newsletter)
admin.site.register(UserData)