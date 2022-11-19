from django.urls import path
from . import views

urlpatterns = [
    path("api/", views.Home),
    path('api/get-all-actors/', views.get_all_actors_present),
    path('api/get-quot-by-actor/', views.get_quote_by_actor),
]