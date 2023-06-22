from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.departmentlist, name='firstpage'),
    path('<str:department>', views.Appointment, name='appointment'),
    path('dashboard/', views.Dashboard, name='dashboard'),
    path('dashboard/<int:booking_id>', views.Dashboard, name='dashboard')
]