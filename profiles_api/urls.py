from django.urls import path

from profiles_api import views


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()) #call to convert our api view class to be rendered by our urls
]
