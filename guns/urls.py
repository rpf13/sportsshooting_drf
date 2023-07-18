from django.urls import path
from guns import views

urlpatterns = [
    path('guns/', views.GunList.as_view()),
    path('guns/<int:pk>/', views.GunDetail.as_view()),
]
