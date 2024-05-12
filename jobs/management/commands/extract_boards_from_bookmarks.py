from typing import Any, Optional
from django.core.management import BaseCommand
from django.core.management.base import CommandParser
from jobs.utils import extract_boards_from_bookmarks
import json 

class Command(BaseCommand):
    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('file', type=str, help='bookmarks.html file path')
        parser.add_argument('output_path', type=str, nargs='?', help='bookmarks.html file path', default='boards.json')

    def handle(self, *args: Any, **options: Any) -> str | None:
        filepath= options['file']
        output_path= options.get('output_path')
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            boards = extract_boards_from_bookmarks(content)
        with open(output_path, 'w', encoding='utf-8') as file:
            json.dump(boards, file)
        
