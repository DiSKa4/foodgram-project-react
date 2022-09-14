import json

from django.conf import settings
from django.core.management.base import BaseCommand

from api.models import Ingredient


class Command(BaseCommand):
    Ingredient.objects.all().delete()

    def handle(self, *args, **kwargs):
        with open(f'{settings.BASE_DIR}/data/ingredients.json', 'rb') as f:
            data = json.load(f)
        for d in data:
            Ingredient.objects.get_or_create(
                name=str(d['name']),
                measurement_unit=str(d['measurement_unit'])
            )
