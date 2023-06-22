from django.urls import path, include
from . import views

urlpatterns = [
    path('lung_cancer', views.lung_cancer),
    path('skin_disease', views.skin_disease),
    path('brain_tumor', views.brain_tumor),
    path('diabetes', views.diabetes),
    path('pneumonia', views.pneumonia),
]
