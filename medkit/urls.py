from django.urls import path
from . import views

urlpatterns = [
    path('', views.order, name='order'),
    path('dashboard/', views.Dashboard, name="order_dashboard"),
    path('dashboard/<int:order_id>', views.Dashboard, name="order_dashboard"),
    path('dashboard/<int:order_id>/<str:taken>', views.taken, name="order_dashboard")
]
