from django.urls import path
from guns import views

urlpatterns = [
    path('guns/', views.GunList.as_view()),
]
