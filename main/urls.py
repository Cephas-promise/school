from django import views
from django.urls import path
import virtualenv
from. import views


urlpatterns = [
    path('',views.index, name='index' ),
    path('reg', views.reg, name='reg'),
    path('login', views.login, name='login'),
    path('studentprofile', views.studentprofile, name='studentprofile'),
    path('result', views.result, name='result'),
    path('updateprofile', views.updateprofile, name='updateprofile')
]
