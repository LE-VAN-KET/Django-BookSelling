from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='index'),
    path('registration', views.registration, name='registration'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout')
]
