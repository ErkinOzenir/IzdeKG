from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from .models import *

class PriceFilter(admin.SimpleListFilter):
    title = _('Price Filter')
    parameter_name = 'price'

    def lookups(self, request, model_admin):
        return (
            ('asc', _('Low to High')),
            ('desc', _('High to Low')),
        )
    def queryset(self, request, queryset):
        if self.value() == 'asc':
            return queryset.order_by('price')
        if self.value() == 'desc':
            return queryset.order_by('-price')

class PostAdmin(admin.ModelAdmin):

    search_fields = ['title']
    list_display = ['title']
    list_filter = ['post_type', 'city', 'room_number', PriceFilter]

class SavedPostAdmin(admin.ModelAdmin):
    search_fields = ['user']
    list_display = ['user']
    list_filter = ['user']

class ReviewAdmin(admin.ModelAdmin):
    search_fields = ['user']
    list_display = ['post']
    list_filter = ['post']

admin.site.register(Tag)
admin.site.register(Attachment)
admin.site.register(Post, PostAdmin)
admin.site.register(SavedPost, SavedPostAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Currency)
