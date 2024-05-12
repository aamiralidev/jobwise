from typing import Any, Optional
from django.core.management.base import BaseCommand, CommandParser 
import requests
import json
from jobs.utils import extract_boards_from_links

class Command(BaseCommand):
    
	def add_arguments(self, parser: CommandParser) -> None:
		parser.add_argument('filepath', type=str, help='path to the bookmarks.html file')
		parser.add_argument('output_path', type=str, nargs='?', help='path to the bookmarks.html file', default='boards.json')

	def handle(self, *args: Any, **options: Any) -> str | None:
		filepath = options['filepath']
		output_path = options.get('output_path')
		with open(filepath, 'r', encoding='utf-8') as file:
			links = file.readlines()
		boards = extract_boards_from_links(links)
		with open(output_path, 'w') as file:
			json.dump(boards, file)
