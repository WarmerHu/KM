from django.conf.urls import patterns, url

#制定url以及对应的函数
urlpatterns = patterns('',
#    url(r'^k_means/page/', 'showkm.views.kmAjax'),
    url(r'^km$', 'showkm.views.lastkm'),
    url(r'^km/(\d{1})', 'showkm.views.kmshow'),
    
)
