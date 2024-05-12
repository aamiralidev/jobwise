from typing import Any, Optional
from django.core.management import BaseCommand
from django.core.management.base import CommandParser
from jobs.models import BoardProvider
import os
import json

identifier = 'identifier'
domain = 'domain'
name = 'name'
identifier_by_prefix = 'identifier_by_prefix'


class Command(BaseCommand):

    def add_arguments(self, parser):
        command_dir = os.path.dirname(os.path.abspath(__file__))
        default_filepath = os.path.join(command_dir, 'providers.json')
        parser.add_argument('file', nargs='?', type=str, help='Path to JSON file', default=default_filepath)

    def handle(self, *args: Any, **options: Any) -> str | None:
        existing_identifiers = set(BoardProvider.objects.values_list('identifier', flat=True))
        filepath = options.get('file')

        with open(filepath, 'r') as file:
            providers = json.load(file)
        
        new_board_providers = []
        
        for provider in providers:
            if provider['identifier'] not in existing_identifiers:
                new_board_providers.append(BoardProvider(**provider))
        
        if new_board_providers:
            BoardProvider.objects.bulk_create(new_board_providers)
        
        self.stdout.write(self.style.SUCCESS('BoardProviders populated successfully.'))