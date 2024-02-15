from django.contrib import admin

# Register your models here.
from .models import Employee,Salary,ContactMessage

admin.site.register(Employee)
admin.site.register(Salary)
admin.site.register(ContactMessage)


