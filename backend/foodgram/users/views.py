from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.mixins import ListModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from api.pagination import CustomPagination
from .models import Follow, User
from .serializers import FollowSerializer, UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = CustomPagination

    @action(
        detail=True,
        permission_classes=[IsAuthenticated],
        methods=['POST', 'DELETE']
    )
    def subscribe(self, request, pk=None):
        user = request.user
        author = get_object_or_404(User, id=pk)
        if self.request.method == 'POST':
            follow = Follow.objects.create(user=user, author=author)
            serializer = FollowSerializer(
                follow, context={'request': request}
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        if Follow.objects.filter(user=user, author=author).exists():
            follow = get_object_or_404(Follow, user=user, author=author)
            follow.delete()
            return Response(
                'Подписка успешно удалена',
                status=status.HTTP_204_NO_CONTENT
            )


class FollowListViewSet(ListModelMixin, viewsets.GenericViewSet):
    permissions_classes = [IsAuthenticated]
    serializer_class = FollowSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        user = self.request.user
        return Follow.objects.filter(user=user)
