from .BaseJobExtractor import BaseJobExtractor
import requests 
from bs4 import BeautifulSoup
from jobs.models import Job

class BreezyBaseJobExtractor(BaseJobExtractor):
    def __init__(self, identifier, board_url) -> None:
        super().__init__()
        self.base_url = "https://boards.greenhouse.io/"
        self.identifier = identifier
        self.board_url = board_url
    
    def set_company_name(self, board):
        self.company_name = board.find('a', class_='brand').find('img').get('alt')
    
    def set_company_website(self, board):
        self.company_website = ''

    def get_board(self):
        response = requests.get(self.board_url)
        if response.status_code != 200:
            raise ConnectionError("get_board: response code is not 200")
        return BeautifulSoup(response.content, 'html.parser')

    def get_job_page(self, url):
        response = requests.get(url)
        if response.status_code != 200:
            raise ConnectionError("get_board: response code is not 200")
        return BeautifulSoup(response.content, 'html.parser')
    
    def get_job_element(self, page):
        return page
    
    def get_job_description(self, job_element):
        return str(job_element.find('div', class_='description'))
    
    def get_job_title(self, job_element):
        return job_element.find('h1').text.strip()
    
    def get_job_location(self, job_element):
        return job_element.find('li', class_='location').text.strip()
    
    def get_job_company(self, job_element):
        return self.company_name
    
    def get_board_url(self, job_element):
        return self.board_url
    
    def get_company_website(self, job_element):
        return self.company_website
    
    def get_commitment(self, job_element):
        try:
            commitment = job_element.find('li', class_='type').find('span', class_='polygot').text.strip()
            return commitment[21:-1]
        except:
            return ''

    def extract_job_id(self, job):
        return self.board_url + job.find('a').get('href')
    
    def extract_job_ids(self, board):
        job_listings = board.find_all('li', class_='position transition')
        jobs = list(map(self.extract_job_id, job_listings))
        return jobs
    
    def get_existing_job_ids(self):
        return Job.objects.filter(board_url=self.board_url).values_list('original_id', flat=True)