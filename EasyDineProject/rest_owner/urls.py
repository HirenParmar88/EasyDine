from django.contrib import admin
from django.urls import path
from . import views
from rest_owner import views as rest_owner_views
from .views import addrestaurant
# from django.conf.urls.static import static

from .views import dashboard

urlpatterns = [
    path("", rest_owner_views.index, name='index'),
    path("payment.html", rest_owner_views.payment, name='payment'),
    path("dashboard.html", rest_owner_views.dashboard, name='dashboard'),
    path("login.html", rest_owner_views.login, name='login'),
    path("feedback.html", rest_owner_views.feedback, name='feedback'),
    path("addrestaurant.html", rest_owner_views.addrestaurant, name='addrestaurant'),
    path("editrestaurant.html", rest_owner_views.editrestaurant, name='editrestaurant'),
    path("signup.html", rest_owner_views.signup, name='signup'),
    # for add restaurant store data on database
    path("addrestaurant.html/", rest_owner_views.addrestaurant, name='addrestaurant'),
    path('dashboard/', dashboard, name='dashboard'),

]