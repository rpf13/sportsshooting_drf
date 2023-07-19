from django.urls import path
from usermessages import views

urlpatterns = [
    path('usermessages/', views.UsermessageList.as_view()),
    path('usermessages/<int:pk>/', views.UsermessagesDetail.as_view()),
]
