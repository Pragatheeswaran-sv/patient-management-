from django.urls import path
from . import views


urlpatterns = [
    path('form/', views.form),
    path('slot/', views.availabe_slots),
    path('confirm/', views.get_details),
]