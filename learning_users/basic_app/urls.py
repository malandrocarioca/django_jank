from django.conf.urls import urls
from basic_app import views
# template URLs
app_name = 'basic_app'

urlpatterns [
url(r'^register/$', views.register, name= 'Register')

]
