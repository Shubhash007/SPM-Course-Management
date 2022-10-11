from atexit import register
from django.contrib import admin
from .models import User_Role,Staff,Skill,Course,Registration,Job_Role,Requirements

# Register your models here.
admin.site.register(User_Role)
admin.site.register(Staff)
admin.site.register(Skill)
admin.site.register(Course)
admin.site.register(Registration)
admin.site.register(Job_Role)
admin.site.register(Requirements)