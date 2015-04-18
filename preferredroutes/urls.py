from django.conf.urls import patterns, include, url
from django.contrib import admin
from .views import HomePageView
from .views import RouteWXView, StoriesView

from .views import StuffView, TracksView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'preferredroutes.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', HomePageView.as_view(), name='home'),
    #url(r'^routewx', RouteWXView.as_view(), name='routewx'),
    url(r'^stuff', StuffView.as_view(), name='stuff'),
    url(r'^tracks', TracksView.as_view(), name='tracks'),
    url(r'^stories', StoriesView.as_view(), name='stories'),
    url(r'^s3direct/', include('s3direct.urls')),
    
)
