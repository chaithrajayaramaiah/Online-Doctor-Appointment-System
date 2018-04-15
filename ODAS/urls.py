
from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    url(r'^',include('home.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^admin_login/', include('admin_login.urls')),
    url(r'^asr/', include('doctor_login.urls')),
    url(r'^patient_login/', include('patient_login.urls')),


]
