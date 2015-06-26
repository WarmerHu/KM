from django.conf.urls import patterns, url


urlpatterns = patterns('',
#    url(r'^k_means/page/', 'showkm.views.kmAjax'),
    url(r'^k_means/(.+)', 'showkm.views.showkm'),
    url(r'^k_means', 'showkm.views.lastkm'),
)
