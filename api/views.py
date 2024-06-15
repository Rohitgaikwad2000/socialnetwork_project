from django.contrib.auth import authenticate, login
from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from .models import User, FriendRequest
from .serializers import UserSerializer, FriendRequestSerializer


class UserSignupView(generics.CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        print(self.request.data)
        serializer.save(password=self.request.data["email"])


class UserLoginView(views.APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get("email").lower()
        password = request.data.get("password")
        user = authenticate(request, email=email, password=password)
        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({"token": token.key}, status=status.HTTP_200_OK)
        return Response(
            {"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST
        )


class UserSearchView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        query = self.request.query_params.get("q", "")
        return User.objects.filter(
            Q(email__iexact=query) | Q(username__icontains=query)
        )


class FriendRequestView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        to_user_id = request.data.get("to_user_id")
        to_user = User.objects.get(id=to_user_id)
        if FriendRequest.objects.filter(
            from_user=request.user, to_user=to_user
        ).exists():
            return Response(
                {"error": "Friend request already sent"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        friend_request = FriendRequest(from_user=request.user, to_user=to_user)
        friend_request.save()
        return Response(
            {"status": "Friend request sent"}, status=status.HTTP_201_CREATED
        )

    def put(self, request, *args, **kwargs):
        request_id = request.data.get("request_id")
        action = request.data.get("action")
        friend_request = FriendRequest.objects.get(id=request_id)
        if friend_request.to_user != request.user:
            return Response(
                {"error": "Permission denied"}, status=status.HTTP_403_FORBIDDEN
            )

        if action == "accept":
            friend_request.accepted = True
            friend_request.save()
            return Response(
                {"status": "Friend request accepted"}, status=status.HTTP_200_OK
            )
        elif action == "reject":
            friend_request.delete()
            return Response(
                {"status": "Friend request rejected"}, status=status.HTTP_200_OK
            )
        return Response({"error": "Invalid action"}, status=status.HTTP_400_BAD_REQUEST)


class FriendsListView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return User.objects.filter(
            Q(sent_requests__to_user=self.request.user, sent_requests__accepted=True)
            | Q(
                received_requests__from_user=self.request.user,
                received_requests__accepted=True,
            )
        )


class PendingFriendRequestsView(generics.ListAPIView):
    serializer_class = FriendRequestSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        print(f"User object: {self.request.user}")
        return FriendRequest.objects.filter(to_user=self.request.user, accepted=False)
