from django.urls import path
from . import views

app_name = 'tracker'

urlpatterns = [
    path('', views.home, name='home'),
    path('add/', views.add_record, name='add_record'),
    path('report/', views.report, name='report'),
]
