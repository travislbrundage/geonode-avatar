from django.conf.urls import include, url

app_name = 'tests'


urlpatterns = [
    url(r'^avatar/', include('avatar.urls')),
]
