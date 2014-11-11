 # -*- coding: utf-8 -*
from django.conf.urls import patterns, include, url
from django.contrib import admin
from djangoweb.view import hello,current_datetime,hours_ahead
from books import views #从app中导入视图文件
#from contact import views
 
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangoweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/', hello),
    url(r'^time/$', current_datetime),
    url(r'^auto/', current_datetime),
    url(r'^time/plus/(\d{1,2})/$',hours_ahead),
    url(r'^search_form/$',views.search_form),
    url(r'^search/$', views.search),
    #url(r'^contact/$', views.contact),
)
