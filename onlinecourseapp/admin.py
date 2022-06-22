from django.contrib import admin
from .models import gallery
from .models import Contact
from .models import pricing


# Register your models here.
admin.site.register(gallery)
admin.site.register(Contact)
admin.site.register(pricing)
