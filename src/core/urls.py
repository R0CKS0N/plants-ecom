from django.urls import path
from .views import (
    SnippetList,
    ArticleDetails,
    GenericAPIView,
)

urlpatterns = [
    path('article/', SnippetList.as_view()),
    path('article/<int:id>/', ArticleDetails.as_view()),
    path('Generic/', GenericAPIView.as_view()),


]
