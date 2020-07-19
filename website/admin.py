from django.contrib import admin

# Register your models here.
from . import models

from django.utils.safestring import mark_safe

from autres.actions import Action




class PresentationAdmin(Action):
    list_display = ('images_view', 'nom', 'date_add',
                    'date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info Presentation', {'fields': ['nom', 'description', 'image', 'slogan']}),
                 ('Standard', {'fields': ['status']})
                 ]

    def images_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.image.url))


class SocialAccountAdmin(Action):
    list_display = ('nom', 'lien', 'date_add',
                    'date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['lien']
    ordering = ['nom']
    list_per_page = 10

    fieldsets = [
        ('Info SocialAccount', {
            'fields': ['nom', 'lien', 'icon']
        }),
        ('Standare', {
            'fields': ['status']
        })
    ]

class GallerieAdmin(Action):
    list_display = ('images_view', 'nom', 'date_add',
                    'date_update', 'status')
    list_filter = ('nom', )
    search_fields = ('nom', )
    date_hierarchy = 'date_add'
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    fieldsets = [('Info Gallerie', {'fields': ['nom', 'image']}),
                 ('Standard', {'fields': ['status']})
                 ]

    def images_view(self, obj):
        return mark_safe('<img src="{url}" style="height:50px; width:100px">'.format(url=obj.image.url))



def _register(model, admin_class):
    admin.site.register(model, admin_class)

_register(models.SocialAccount, SocialAccountAdmin)
_register(models.Presentation, PresentationAdmin)
_register(models.Gallerie, GallerieAdmin)
