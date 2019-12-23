from django.contrib import admin
from .models import User,wareHouse,SessionAudit

admin.site.register(User)
admin.site.register(wareHouse)

admin.site.register(SessionAudit)

