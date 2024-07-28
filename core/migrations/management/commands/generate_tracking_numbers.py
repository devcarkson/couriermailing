# new__core/management/commands/generate_tracking_numbers.py

import uuid
from django.core.management.base import BaseCommand
from core.models import Normalsender

def generate_unique_tracking_number():
    while True:
        tracking_number = str(uuid.uuid4())
        if not Normalsender.objects.filter(tracking_number=tracking_number).exists():
            return tracking_number

class Command(BaseCommand):
    help = 'Generate tracking numbers for existing Normalsender records without one'

    def handle(self, *args, **kwargs):
        senders_without_tracking = Normalsender.objects.filter(tracking_number__isnull=True)
        for sender in senders_without_tracking:
            sender.tracking_number = generate_unique_tracking_number()
            sender.save()
            self.stdout.write(self.style.SUCCESS(f'Generated tracking number for: {sender.name}'))
        self.stdout.write(self.style.SUCCESS('Successfully generated tracking numbers for all records without one'))
