from django.urls import include, path
from rest_framework import routers
from blog import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostViewSet)

urlpatterns = [
    # ... otras URL de la aplicación ...
    path('api/', include(router.urls)),
]