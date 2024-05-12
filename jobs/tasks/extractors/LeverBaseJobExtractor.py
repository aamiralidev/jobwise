from .BaseJobExtractor import BaseJobExtractor
import requests
from bs4 import BeautifulSoup
from jobs.models import Job

class LeverBaseJobExtractor(BaseJobExtractor):
    def __init__(self, identifier, board_url) -> None:
        super().__init__()
        self.base_url = "https://jobs.lever.co/"
        self.identifier = identifier
        self.board_url = board_url

    def set_company_website(self, board):
        self.company_website = self.board_url

    def set_company_name(self, board):
        self.company_name = self.identifier
        

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
        job_description_element = job_element.find('div', class_='section-wrapper page-full-width')
        if job_description_element.children:
            list(job_description_element.children)[-1].decompose()
        return str(job_description_element)
    
    def get_job_title(self, job_element):
        return job_element.find('h2').text.strip()

    def get_job_location(self, job_element):
        return job_element.find(class_='location').text.strip()
    
    def get_workplace_type(self, job_element):
        return job_element.find(class_='workplaceTypes').text.strip()
    
    def get_commitment_type(self, job_element):
        return job_element.find(class_='commitment').text.strip()
    
    def get_job_company(self, job_element):
        return self.identifier
    
    def get_board_url(self, job_element):
        return self.board_url
    
    def extract_job_id(self, job):
        return job.find('a').get('href')
    
    def extract_job_ids(self, board):
        job_listings = board.find_all('div', class_='posting')
        jobs = list(map(self.extract_job_id, job_listings))
        return jobs
    
    def get_existing_job_ids(self):
        return Job.objects.filter(board_url=self.board_url).values_list('original_id', flat=True)
