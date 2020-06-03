from django.urls import path
from .views import MediaViewSet, like_post, UserViewSet, follow_user, GalleryViewSet

app_name = 'imageapi'

urlpatterns = [
    path('', MediaViewSet, name='post-list'),
    path('', UserViewSet, name='user-details'),
    path('gallery', GalleryViewSet, name='gallery-list'),
    path('searchResults', UserViewSet, name='search-results'),
    path('like/', like_post, name="like-post"),
    path('follow/', follow_user, name="follow-user")
]