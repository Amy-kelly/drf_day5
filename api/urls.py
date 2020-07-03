from django.urls import path

from api import views

urlpatterns = [
    path('user/',views.UserAPIView.as_view()),
    path('test/',views.TestPessionAPIView.as_view()),
    path('msg/',views.SendMsgAPIView.as_view()),
    path('login/',views.UserLoginOrReadOnly.as_view()),
]