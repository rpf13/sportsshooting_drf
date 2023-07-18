from django.urls import path
from matches import views

urlpatterns = [
    path('matches/', views.MatchList.as_view()),
    path('matches/<int:pk>/', views.MatchDetail.as_view()),
]
