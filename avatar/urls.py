from django.conf.urls import url

from avatar import views

app_name = 'avatar'


urlpatterns = [
    url(r'^add/$', views.add, name='add'),
    url(r'^change/$', views.change, name='change'),
    url(r'^delete/$', views.delete, name='delete'),
    url(r'^render_primary/(?P<user>[\w\d\@\.\-_]+)/(?P<size>[\d]+)/$',
        views.render_primary,
        name='render_primary'),
]
