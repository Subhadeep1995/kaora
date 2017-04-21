from django.conf.urls import url
from django.contrib.auth.views import login
from .import views

urlpatterns = [
    url(r'^login/$', login, {'template_name':'login.html'}),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^logout/$', views.logout_view, name='logout'),

]
