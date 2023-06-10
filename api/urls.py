from rest_framework import routers
from .views import  *
from django.urls import include, path

router = routers.DefaultRouter()                                                                       

urlpatterns = [
    path('', include(router.urls)),
    path('stars/', StarTestView.as_view(), name="starlist"),
]