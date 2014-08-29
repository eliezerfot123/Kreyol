from django.contrib import admin

# Register your models here.

from .models import Document
from .models import Source
from .models import Type
from .models import Contact
from .models import Note


class DocumentAdmin(admin.ModelAdmin):
    class Meta:
        model = Document

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
