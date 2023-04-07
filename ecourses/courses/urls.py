from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'subject', views.SubjectViewSet, basename='MySubject')
router.register(r'user', views.UserViewSet, basename='MyUser')

urlpatterns = [
    path('', include(router.urls)),
]
