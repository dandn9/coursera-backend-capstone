from django.contrib import admin
from . import models

# Register your models here.
admin.register(models.Booking, models.Menu)
admin.site.register([models.Booking, models.Menu])
