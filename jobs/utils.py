from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlunparse
import tldextract
from jobs.models import BoardProvider, JobBoard

def extract_links_from_bookmarks(content):
    soap = BeautifulSoup(content, 'html.parser')
    links = [x.get('href') for x in soap.find_all('a')]
    return links

def extract_boards_from_links(links):
	existing_identifiers = set(BoardProvider.objects.values_list('identifier', 'identifier_by_prefix'))
	existing_identifiers = {item[0]: item[1] for item in existing_identifiers}
	extracted_boards = []
	for link in links:
		extracted = tldextract.extract(link)
		if extracted.domain in existing_identifiers:
			if existing_identifiers[extracted.domain]:
				provider = extracted.domain
				identifier = extracted.subdomain
				if not identifier:
					continue
				company_name = identifier
				board_url = link.split(urlparse(link).hostname)[0] + urlparse(link).hostname
			else:
				provider = extracted.domain
				parsed_url = urlparse(link)
				identifier = parsed_url.path.split('/')[1]
				if not identifier:
					continue
				company_name = identifier
				board_url = link.split(identifier)[0] + identifier

			extracted_boards.append(
				{
					'identifier': identifier,
					'provider': provider,
					'company_name': company_name,
					'board_url': board_url
				}
			)
	return extracted_boards


def extract_boards_from_bookmarks(content):
	links = extract_links_from_bookmarks(content)
	boards = extract_boards_from_links(links)
	return boards

def populate_boards_from_json(boards):
	boards = list(map(lambda x: JobBoard(**x), boards))
	try:
		created_boards = JobBoard.objects.bulk_create(boards, ignore_conflicts=True)
	except Exception as e:
		pass

def populate_boards_from_bookmarks(content):
	boards = extract_boards_from_bookmarks(content)
	populate_boards_from_json(boards)