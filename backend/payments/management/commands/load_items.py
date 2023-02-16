from django.core.management.base import BaseCommand

from payments.models import Item

list_items = [
    {'name': 'Молоко', "description": 'Свежее', 'price': 2},
    {'name': 'Хлеб', "description": 'Мягкий', 'price': 1.3},
    {'name': 'Печенье', "description": 'С арахисом', 'price': 3},
]


class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        try:

            for item in list_items:
                Item.objects.get_or_create(name = item.get('name'),
                                           description = item.get('description'),
                                           price=item.get('price'))
        except:
            print('Не удалось записать в базу items')