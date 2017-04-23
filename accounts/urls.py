from django.conf.urls import url
from django.contrib.auth.views import login
from .import views

urlpatterns = [
    url(r'^login/$', login, {'template_name':'login.html'}, name='login'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
    #url(r'^register/$', views.register_view, name='register'),

]
