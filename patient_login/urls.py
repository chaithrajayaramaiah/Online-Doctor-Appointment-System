from django.conf.urls import url
from . import views
from django.contrib.auth.views import login,logout
from patient_login.views import schedule

urlpatterns = [
    url(r'^$', views.index3,name='index3'),
    url(r'^analytics$', views.analytics,name='analytics'),
    url(r'^(?P<doc_id>[0-9]+)/$',views.detail, name='detail'),
    url(r'^(?P<doc_id>[0-9]+)/schedule/$',schedule.as_view(), name='schedule'),
    url(r'^login/$',login, {'template_name':'patient_login/login.html'}),
    url(r'^register/$',views.register,name='register'),
    url(r'^profile/$',views.view_profile, name='view_profile'),
    url(r'^profile/edit/$',views.edit_profile, name='edit_profile'),
    url(r'^profile/change_password/$',views.change_password, name='change_password'),


    ]
