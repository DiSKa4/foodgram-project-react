import json

from django.core.management.base import BaseCommand

from api.models import Ingredient


class Command(BaseCommand):
    Ingredient.objects.all().delete()

    def handle(self, *args, **options):
        with open(
            'C:\\Dev\\foodgram-project-react\\api\\',
            'management\\commands\\ingredients.json',
            'r',
            encoding='utf-8'
        ) as f:
            data = json.load(f)
        for d in data:
            Ingredient.objects.get_or_create(
                name=str(d['name']),
                measurement_unit=str(d['measurement_unit'])
            )
