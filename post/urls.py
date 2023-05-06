from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TweetViewSet, ReplyViewSet

router = DefaultRouter()
router.register('tweets', TweetViewSet)
router.register('replies', ReplyViewSet)


urlpatterns = [
    # path('viewset/tweets/', TweetViewSetAPIView.as_view(
    #     {'get': 'list', 'post': 'create'}
    # )),
    # path('viewset/tweets/<int:pk>/', TweetViewSetAPIView.as_view(
    #     {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
    # )),
    #
    # path('viewset/posts/', ReplyViewSetAPIView.as_view(
    #     {'get': 'list', 'post': 'create'}
    # )),
    # path('viewset/posts/<int:pk>/', ReplyViewSetAPIView.as_view(
    #     {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
    # )),
    path('viewset/', include(router.urls))
]