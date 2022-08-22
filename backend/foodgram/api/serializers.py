from rest_framework import serializers

from recipes.models import Tag, Ingredient, Recipe
from recipes.models import Follow
from rest_framework.validators import UniqueTogetherValidator


class TagSerializers(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class IngredientSerializers(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = '__all__'


class RecipeSerializers(serializers.ModelSerializer):

    class Meta:
        model = Recipe
        fields = '__all__'


class FollowSeriallizer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username',
        default=serializers.CurrentUserDefault())

    author = serializers.SlugRelatedField(
        queryset=Follow.objects.all(),
        slug_field='username'
    )

    class Meta:
        model = Follow
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=('user', 'author')
            ),
        ]

    def validate_following(self, following):
        if self.context['request'].user == following:
            raise serializers.ValidationError(
                "Нельзя подписаться на самого себя"
            )
        return following
