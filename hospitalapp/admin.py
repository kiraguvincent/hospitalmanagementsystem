from django.contrib import admin
from hospitalapp.models import users,Product,Member,Message,Appointment
# Register your models here.
admin.site.register(users)
admin.site.register(Product)
admin.site.register(Member)
admin.site.register(Message)
admin.site.register(Appointment)


