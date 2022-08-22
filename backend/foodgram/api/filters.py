from django_filters.rest_framework import (
    CharFilter,
    FilterSet,
    AllValuesMultipleFilter
)

from recipes.models import Ingredient, Recipe


class IngredientFilter(FilterSet):
    name = CharFilter(field_name='name', lookup_expr="startswith")

    class Meta:
        model = Ingredient
        fields = ('name',)


class RecipeFilter(FilterSet):
    tags = AllValuesMultipleFilter(
        field_name='tags__slug',
        lookup_expr='exact',
    )

    class Meta:
        model = Recipe
        fields = ('author', 'tags',)
