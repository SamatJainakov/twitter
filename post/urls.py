from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TweetViewSet, ReplyViewSet

router = DefaultRouter()
router.register('tweets', TweetViewSet)
router.register('reply', ReplyViewSet)


urlpatterns = [
    # path('viewset/tweets/', TweetViewSet.as_view(
    #     {'get': 'list', 'post': 'create'}
    # )),
    # path('viewset/tweets/<int:pk>/', TweetViewSet.as_view(
    #     {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
    # )),
    #
    # path('viewset/posts/', ReplyViewSet.as_view(
    #     {'get': 'list', 'post': 'create'}
    # )),
    # path('viewset/posts/<int:pk>/', ReplyViewSet.as_view(
    #     {'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}
    # )),
    path('viewset/', include(router.urls))
]