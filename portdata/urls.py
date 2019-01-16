from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'data', views.DataViewSet)

urlpatterns = [
    url('^api/', include(router.urls)),
    path('', views.index, name='index'),
    path('upload/', views.upload, name='upload'),
]
