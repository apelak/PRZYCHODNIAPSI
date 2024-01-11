from rest_framework import routers
from .views import Dokumentacja_medycznaViewSet
from django.urls import include, path

router = routers.DefaultRouter()
router.register(r'dokumentacja_medyczna', Dokumentacja_medycznaViewSet)
app_name = 'dokumentacja_medyczna'

urlpatterns = [
    path('api/', include(router.urls)),
    path('api_auth/', include('rest_framework.urls', namespace='rest_framework')),

]