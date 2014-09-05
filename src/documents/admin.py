from django.contrib import admin

# Register your models here.

from .models import Document
from .models import Source
from .models import Type
from .models import Contact
from .models import Note


#updated = models.DateTimeField(auto_now_add=False, auto_now=True)
class DocumentAdmin(admin.ModelAdmin):
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
    class Meta:
        model = Contact

admin.site.register(Contact, ContactAdmin)


class NoteAdmin(admin.ModelAdmin):
    class Meta:
        model = Note

admin.site.register(Note, NoteAdmin)
