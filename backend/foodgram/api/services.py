from django.conf import settings
from django.db.models import Sum
from django.http import HttpResponse

from .models import IngredientAmount


def download_shopping_cart(self, request):
    ingredients = IngredientAmount.objects.filter(
        recipe__shopping_cart__user=request.user).values(
        'ingredient__name',
        'ingredient__measurement_unit').annotate(total=Sum('amount'))
    content = 'Cписок покупок:\n\n'
    for number, ingredient in enumerate(ingredients, start=1):
        content += (
            f'[{number}] '
            f'{ingredient["ingredient__name"]} - '
            f'{ingredient["total"]} '
            f'{ingredient["ingredient__measurement_unit"]}\n')
    response = HttpResponse(content, content_type='text/plain')
    response['Content-Disposition'] = (
            f'attachment;'f'filename={settings.FILENAME_SHOP}')
    return response
