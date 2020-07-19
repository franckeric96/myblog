from django.contrib import admin

# Register your models here.

from . import models

from autres.actions import Action


class ContactAdmin(Action):
    list_display = ('nom', 'email', 'website',
                    'date_add', 'date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['date_add']
    list_per_page = 15
    fieldsets = [('Info Contact', {'fields': ['nom', 'email', 'website', 'message']}),
                 ('Standard', {'fields': ['status']})
                 ]



def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Contact, ContactAdmin)