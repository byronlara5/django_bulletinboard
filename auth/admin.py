from django.contrib import admin
#Register your models here.
from auth.models import Profile

admin.site.register(Profile)