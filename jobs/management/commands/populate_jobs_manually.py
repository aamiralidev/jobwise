from typing import Any, Optional
from django.core.management import BaseCommand
from django.core.management.base import CommandParser
from jobs.tasks.extractors import GreenHouseJobExtractor
from jobs.tasks.extractors import LeverBaseJobExtractor
from jobs.tasks.extractors import BreezyBaseJobExtractor
from jobs.tasks.extractors import AshbyBAseJobExtractor
from jobs.models import Job

class Command(BaseCommand):

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('provider', type=str, help='enter the job provider')
        parser.add_argument('identifier', type=str, help='enter the board identifier')

    def handle(self, *args: Any, **options: Any) -> str | None:
        provider = options['provider']
        identifier = options['identifier']
        print('populating with ' + identifier)
        if provider == 'greenhouse':
            extractor = GreenHouseJobExtractor(identifier)
            extractor.extract()
        if provider == 'lever':
            print('populating with ' + identifier)
            extractor = LeverBaseJobExtractor(identifier, 'https://jobs.lever.co/' + identifier)
            extractor.extract()
        if provider == 'breezy':
            Job.objects.all().delete()
            board_url = "https://nascent-xyz.breezy.hr"
            extractor = BreezyBaseJobExtractor(identifier, board_url)
            extractor.extract()
        if provider == 'ashbyhq':
            Job.objects.all().delete()
            board_url = "https://jobs.ashbyhq.com/irreducible"
            extractor = AshbyBAseJobExtractor(identifier, board_url)
            extractor.extract()
