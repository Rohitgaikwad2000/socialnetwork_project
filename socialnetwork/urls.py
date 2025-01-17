"""
URL configuration for socialnetwork project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from django.contrib import admin
from api.views import (
    UserSignupView,
    UserLoginView,
    UserSearchView,
    FriendRequestView,
    FriendsListView,
    PendingFriendRequestsView,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/signup/", UserSignupView.as_view(), name="signup"),
    path("api/login/", UserLoginView.as_view(), name="login"),
    path("api/search/", UserSearchView.as_view(), name="search"),
    path("api/friend-request/", FriendRequestView.as_view(), name="friend-request"),
    path("api/friends/", FriendsListView.as_view(), name="friends"),
    path(
        "api/pending-requests/",
        PendingFriendRequestsView.as_view(),
        name="pending-requests",
    ),
]
