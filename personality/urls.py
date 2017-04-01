from django.conf.urls import url
from . import views

app_name = "personality"
urlpatterns = [
    url(r'^$', views.index,name ="index"),
    url(r'^review$', views.review, name='review'),
]