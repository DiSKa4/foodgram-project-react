from recipes.models import (Ingredient, Recipe, Tag)
from rest_framework import viewsets
from .mixins import CreateListViewSet
from api.serializers import (
    RecipeSerializers,
    IngredientSerializers,
    TagSerializers,
    FollowSeriallizer
)
from .filters import IngredientFilter, RecipeFilter
from rest_framework.permissions import (
    IsAuthenticated,
)
from .pagination import CustomPagination


class TagViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializers
    pagination_class = None


class IngredientsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializers
    pagination_class = None
    filterset_class = IngredientFilter


class RecipeViewSet(viewsets.ModelViewSet):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializers
    pagination_class = CustomPagination
    filterset_class = RecipeFilter

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FollowViewSet(CreateListViewSet):
    serializer_class = FollowSeriallizer
    permission_classes = [IsAuthenticated]
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
