from django.core.management.base import BaseCommand, CommandError
from view_result.models import models
from django.apps import apps
import csv

class Command(BaseCommand):
    help ="Global label base commands"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='This will help you to input file path')
        parser.add_argument('model_name', type=str, help='This will help you to input model name')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        model_name = kwargs['model_name']

        model = None
        for app in apps.get_app_configs():
            try:
                model = apps.get_model(app.label, model_name)
                break
            except LookupError:
                continue
        if not model:
            raise CommandError
        
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                email = row['email']
                existing_email = model.objects.filter(email=email).exists()
                if not existing_email:
                    model.objects.create(**row)
                    self.stdout.write(self.style.SUCCESS(f"Succefully inserted all data at {model}"))
                else:
                    self.stdout.write(self.style.WARNING(f"The input data is already exists!"))
            
