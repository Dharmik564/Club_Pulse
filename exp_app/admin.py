from django.contrib import admin
from exp_app import models

# Register your models here.
admin.site.register(models.User_Detail)
admin.site.register(models.Owner_Detail)
admin.site.register(models.Club_Detail)
admin.site.register(models.Club_Image)
admin.site.register(models.Contact)
admin.site.register(models.Subscriber)
admin.site.register(models.Club_Inquiry_Detail)
admin.site.register(models.Paid_Customer)