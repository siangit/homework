from django.urls import path
from . import views

app_name = 'feeds'

urlpatterns = [
    path("", views.Feeds.as_view()),
    path("<int:feed_id>", views.FeedDetail.as_view()),
]