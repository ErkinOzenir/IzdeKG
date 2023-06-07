from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter
from rest_framework import renderers
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="IzdeKG API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

user_list = (UserViewSet.as_view({
    'get': 'list'
}))
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

router = DefaultRouter()
router.register(r'users', UserViewSet, basename="user")
router.register(r'posts', PostViewSet, basename="post")
router.register(r'saved-posts', SavedPostViewSet, basename="saved-post")
router.register(r'reviews', ReviewViewSet, basename="review")

urlpatterns = [
  path('', include(router.urls)),
  path('register',RegisterUserAPIView.as_view()),
  path('login/', LoginAPIView.as_view()),
  path('logout', LogoutView.as_view()),
  path('posts', PostViewSet.as_view({'get': 'list'})),
  path('saved-posts', SavedPostViewSet.as_view({'get': 'list'})),
  path('reviews', ReviewViewSet.as_view({'get': 'list'})),
  path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]