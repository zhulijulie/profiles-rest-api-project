from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views


router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()), #call to convert our api view class to be rendered by our urls
    path('', include(router.urls)),
    #as you register new routes with our router it generates a list of URLs
    #that are associated for our view set it figures out the URLs that are required
    #for all of the functions that we add to our view set and then it generates this URLs
    #list which we can pass in to using the path function and the include function to our URL patterns
]
