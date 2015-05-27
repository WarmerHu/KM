from django.conf.urls import patterns, url


urlpatterns = patterns('',
    url(r'^k_means/', 'showkm.views.showkm'),
)
