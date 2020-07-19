from django.contrib import admin

from . import models

from autres.actions import Action


# Register your models here.
class ProfileAdmin(Action):
    list_display = ('user', 'contact',
                    'date_birthday')
    list_filter = ('user', )
    search_fields = ('user', )
   


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Profile, ProfileAdmin)