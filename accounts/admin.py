from django.contrib import admin

from accounts.models import User, Driver, Customer, Staff
# Register your models here.


admin.site.register(User)
admin.site.register(Driver)
admin.site.register(Customer)
admin.site.register(Staff)
