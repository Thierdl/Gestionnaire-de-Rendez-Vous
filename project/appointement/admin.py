from django.contrib import admin
from .models import Appointement, Patient

# Register your models here.
admin.site.register(Appointement),
admin.site.register(Patient)
