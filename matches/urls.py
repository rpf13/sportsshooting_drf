from django.urls import path
from matches import views

urlpatterns = [
    path('matches/', views.MatchList.as_view()),
]
