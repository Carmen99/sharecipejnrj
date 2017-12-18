from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^posts/$', views.PostList.as_view(), name = "post-list"),
    url(r'^posts/(?P<pk>\d+)/$', views.PostDetail.as_view(), name = "post-detail"),
]
