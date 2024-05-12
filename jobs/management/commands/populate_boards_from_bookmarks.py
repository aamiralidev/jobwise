from typing import Any, Optional
from django.core.management import BaseCommand
from django.core.management.base import CommandParser
from jobs.utils import populate_boards_from_bookmarks

class Command(BaseCommand):

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('file', type=str, help='bookmarks.html file')
    
    def handle(self, *args: Any, **options: Any) -> str | None:
        filepath = options['file']
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            populate_boards_from_bookmarks(content)
            