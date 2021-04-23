from django.urls import path
from . import views

urlpatterns= [
    path("", views.index),
    path('register', views.register),
    path("login", views.login),
    path("main", views.main),
    path("logout", views.logout),
    path("view_stats", views.view_stats),
    path("make_a_wish", views.make_a_wish),
    path('wish_list', views.wish_list),
    path("remove", views.remove),
    path('edit', views.edit),
    path('granted_wishes', views.granted_wishes),
    path('like', views.like),
    path('cancel', views.cancel),
    path('submit', views.submit)
]