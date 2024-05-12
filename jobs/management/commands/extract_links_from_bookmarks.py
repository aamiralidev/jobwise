from django.core.management.base import BaseCommand, CommandParser 
from bs4 import BeautifulSoup
from jobs.utils import extract_links_from_bookmarks

class Command(BaseCommand):

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('filepath', type=str, help='path to the bookmarks.html file')
        parser.add_argument('output_path', type=str, nargs='?', help='path to the bookmarks.html file', default='links.txt')

    def handle(self, *args, **options):
        filepath = options['filepath']
        output_path = options.get('output_path')
        with open(filepath, 'r', encoding='utf-8') as file:
            links = extract_links_from_bookmarks(file.read())
        with open(output_path, 'w', encoding='utf-8') as file:
            for link in links:
                file.write(f'{link}\n')
