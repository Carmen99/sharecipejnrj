from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', auth_views.login, {'template_name': 'list/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'list/logout.html'}, name='logout'),
    url(r'^post/recipes/$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/contact', views.contact, name='contact'),
    url(r'^post/(?P<pk>\d+)/delete/$', views.post_delete, name='post_delete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
