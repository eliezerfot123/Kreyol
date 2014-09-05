from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

from haystack.forms import ModelSearchForm
from haystack.query import SearchQuerySet
from haystack.views import SearchView, search_view_factory

admin.autodiscover()
sqs = SearchQuerySet().filter()

urlpatterns = patterns('',
    url('^select2/', include('django_select2.urls')),
    url(r'^$', 'documents.views.home', name='home'),
    url(r'^about/$', 'documents.views.about', name='about'),
    url(r'^corpus$', 'documents.views.corpus', name='corpus'),
    url(r'^contact/$', 'documents.views.contact', name='contact'),
    url(r'^thank-you/$', 'documents.views.thankyou', name='thankyou'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^search/', include('haystack.urls')),
    url(r'^select2/', include('django_select2.urls')),
   
#===== move search view to corpus ========#   
    
    url(r'^corpus/$', search_view_factory(
        view_class=SearchView,
        template='search/search.html',
        searchqueryset=sqs,
        form_class=ModelSearchForm
    ), name='haystack_search'),
)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_URL)
