from django.conf import settings
from django.contrib import admin
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from haystack.forms import ModelSearchForm
from haystack.query import SearchQuerySet
from haystack.views import SearchView, search_view_factory

from documents.views import MultilineSearchView

admin.autodiscover()
sqs = SearchQuerySet().filter()

urlpatterns = patterns('',
    url('^select2/', include('django_select2.urls')), 
  # url(r'^blog/', include('blog.urls')),

#===== Kreyol Pages ========#
    url(r'^$', 'documents.views.akey', name='akey'),
  # url(r'^pib/$', 'documents.views.pib', name='pib'),
    url(r'^ekip$','documents.views.ekip', name='ekip'),
  # url(r'^dict/$', 'documents.views.dict', name='dict'),
    url(r'^pwoje$', 'documents.views.pwoje', name='pwoje'),
    url(r'^kontak/$', 'documents.views.kontak', name='kontak'),
  
#===== English Pages ========#
    url(r'^en$', 'documents.views.home', name='home'),
    url(r'^team$', 'documents.views.team', name='team'),
    url(r'^project$', 'documents.views.project', name='project'),
    url(r'^contact$',  'documents.views.contact', name='contact'),
    
    url(r'^thank-you$', 'documents.views.thankyou', name='thankyou'),
 
    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', MultilineSearchView(), name='corpus'),   
    url(r'^select2/', include('django_select2.urls')),  
   
)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_URL)
