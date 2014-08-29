from django.db import models
from django.contrib.auth.models import User
from django.utils.encoding import smart_unicode

# Create your models here.


class Type(models.Model):

    name = models.CharField(max_length=120, null=True, blank=True)

    def __unicode__(self):
        return smart_unicode(self.name)


class Source(models.Model):

    name = models.CharField(max_length=120, null=True, blank=True)

    def __unicode__(self):
        return smart_unicode(self.name)


class Document(models.Model):

    title = models.CharField(max_length=500, null=True, blank=True)
    author = models.CharField(max_length=120, null=True, blank=True)
    pub_info = models.CharField(max_length=120, null=True, blank=True, verbose_name="Published info")
    source_name = models.ForeignKey(Source, verbose_name="Source")
    type_name = models.ForeignKey(Type, verbose_name="Type")
    date = models.DateField(verbose_name="Published Date")
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.title)


class Contact(models.Model):
    title = models.CharField(max_length=20, null=True, blank=True)
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField()
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self):
        return smart_unicode(self.last_name)


class Note(models.Model):
    user = models.ForeignKey(User)
    pub_date = models.DateTimeField()
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __unicode__(self):
        return self.title