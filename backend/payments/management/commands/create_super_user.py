from django.contrib.auth.models import User
from django.core.management.base import BaseCommand

class Command(BaseCommand):

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        try:
            User.objects.create_superuser(username='admin', password='admin')
        except:
            print('Не удалось записать в базу items')
