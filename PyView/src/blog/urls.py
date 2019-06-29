from django.conf.urls import url
from .views import (post_model_list_view, login_required_view,  post_model_detail_view, post_model_create_view, post_model_update_view, post_model_delete_view)
urlpatterns = [
    url(r'^list/$', post_model_list_view, name ="list"),
    url(r'^login_required_view/$', login_required_view, name ="login"),
    url(r'^detail/(?P<id>\d+)/$', post_model_detail_view, name ="detail"),
    url(r'^create/$', post_model_create_view, name ="create"),
    url(r'^(?P<id>\d+)/edit/$', post_model_update_view, name ="update"),
    url(r'^(?P<id>\d+)/delete/$', post_model_delete_view, name ="delete"),
    #/(?P<id>\d+)/
]
