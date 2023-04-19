from turtle import home
from xml.etree.ElementInclude import include
from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static


######################################################################################################################
# app_name='movies'
from .views import index

# app_name = 'Dashboard'

urlpatterns = [
    path('', views.index, name='home'),
    path('contact/', views.contact, name = 'contact'),
    path('home/', views.home, name='home'),
    path('signup/', views.save, name='SignUp'),
    path('login/', views.signin, name='login'),
    path('profile/', views.profile, name='profile'),
    path('account/', views.logout, name='logout'),
    path('flights/', views.flights, name='flights'),
    path('reservation/', views.reservations, name='reservation'),
    path('ticket/', views.ticket, name='reservation'),
    ######################################################################################################################
    path('index1/', views.index1, name='index1'),
    path('index5/', views.index5, name='index5'),

    ######################################################################################################################
    path('<int:flight_id>/select_seat/', views.select_seat, name='select_seat'),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
