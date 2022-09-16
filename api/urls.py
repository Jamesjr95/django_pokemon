from email.mime import base
from django.urls import path

from rest_framework.routers import DefaultRouter
from . import views  


router = DefaultRouter()

router.register('pokemon', views.PokemonViewSet, basename='pokemon')
router.register('types', views.TypeViewSet, basename='types')
router.register('users', views.UserViewSet, basename='users')

urlpatterns = router.urls + [
    path('current-user/', views.CurrentUserViewSet.as_view())
]
