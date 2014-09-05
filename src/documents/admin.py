from django.contrib import admin

# Register your models here.

from .models import Document
from .models import Source
from .models import Type
from .models import Contact
from .models import Note


#updated = models.DateTimeField(auto_now_add=False, auto_now=True)
class DocumentAdmin(admin.ModelAdmin):

    '''
    def suit_row_attributes(self, obj, request):
        css_class = {
            True: 'success',
            False: 'error',
        }.get(int(obj.updated))
        if css_class:
            return {'class': css_class}
        '''
    fieldsets = [
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ['title', 'author', 'pub_info']
        }),

        ('type & source & date', {
            'classes': ('suit-tab suit-tab-type',),
            'fields': ['type_name', 'source_name', 'date',]}),

        ('Content', {
            'classes': ('suit-tab suit-tab-content',),
            'fields': ['text',]}),
    ]
    
    suit_form_tabs = (('general', 'General'), ('type', u'Type and Date'),('content', u'Content Docs')) 

    select_related=False
    list_display = ('date', 'title', 'author',)#'get_carnicos', 'get_quimicos', 'get_otros')
    search_fields = ['text',]
    list_filter = ['author',]

admin.site.register(Document, DocumentAdmin)


class SourceAdmin(admin.ModelAdmin):
    class Meta:
        model = Source

admin.site.register(Source, SourceAdmin)


class TypeAdmin(admin.ModelAdmin):
    class Meta:
        model = Type

admin.site.register(Type, TypeAdmin)


class ContactAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ['title', 'first_name', 'last_name', 'email']
        }),

        (None, {
            'classes': ('suit-tab suit-tab-message',),
            'fields': ['message',]}),
    ]
    
    suit_form_tabs = (('general', 'General'), ('message', u'Message')) 
    select_related=False
    list_display = ('title', 'first_name', 'last_name', 'email', 'updated', 'message')
    search_fields = ['first_name', 'last_name', 'email']
admin.site.register(Contact, ContactAdmin)


class NoteAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'classes': ('suit-tab suit-tab-general',),
            'fields': ['user', 'pub_date', 'title']
        }),

        (None, {
            'classes': ('suit-tab suit-tab-body',),
            'fields': ['body',]}),
    ]
    
    suit_form_tabs = (('general', 'General'), ('body', u'Body of Note')) 
    select_related=False
    list_display = ('pub_date', 'user', 'title', 'body')
    search_fields = ['title', 'body']
    list_filter = ['user',]
admin.site.register(Note, NoteAdmin)
