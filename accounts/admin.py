from django.contrib import admin
from django.utils.safestring import mark_safe
from accounts.models import Signup
from django.http import HttpResponse

class SignupAdmin(admin.ModelAdmin):
    list_display = (
            'name',
            'nickname',
            'email',
            'created_on',
            )
    pass

admin.site.register(Signup, SignupAdmin)
