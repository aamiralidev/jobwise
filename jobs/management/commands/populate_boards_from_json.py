from typing import Any, Optional
from django.core.management import BaseCommand
from django.core.management.base import CommandParser
import json 
from jobs.utils import populate_boards_from_json

class Command(BaseCommand):

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('file', type=str, help='json file to extract boards from')
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        filepath = options['file']
        with open(filepath, 'r') as file:
            boards = json.load(file)
            populate_boards_from_json(boards)
        
        