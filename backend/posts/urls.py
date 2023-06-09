from django.urls import path, include

from rest_framework import routers

from . import views


router = routers.DefaultRouter()
router.register('tweet', views.TweetViewSet, basename='tweet')
router.register('reaction_type', views.ReactionTypeViewSet)
# router.register(r'tweet/(?P<tweet_id>\d+)/reply', views.ReplyViewSet, basename='tweet-reply')


urlpatterns = [
    path('', include(router.urls)),
    path('tweet/<int:tweet_id>/reply/', views.ReplyListCreateAPIView.as_view()),
    path('tweet/<int:tweet_id>/reply/<int:pk>/', views.ReplyRetrieveUpdateDestroyAPIView.as_view()),
    path('tweet/<int:tweet_id>/reply/<int:reply_id>/reaction/', views.ReplyReactionCreateAPIView.as_view()),
    path('tweet/<int:tweet_id>/reaction/', views.ReactionCreateAPIView.as_view()),
]
