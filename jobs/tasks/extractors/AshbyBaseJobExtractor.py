from .BaseJobExtractor import BaseJobExtractor
import requests 
from bs4 import BeautifulSoup

class AshbyBAseJobExtractor(BaseJobExtractor):
    def __init__(self, identifier, board_url) -> None:
        super().__init__()
        self.base_url = "https://jobs.ashbyhq.com/"
        self.identifier = identifier
        self.board_url = board_url
    
    def set_company_name(self, board):
        self.company_name = self.identifier

    def get_board(self):
        payload = {
            "operationName": "ApiJobBoardWithTeams",
            "variables": {
                "organizationHostedJobsPageName": self.identifier
            },
            "query": "query ApiJobBoardWithTeams($organizationHostedJobsPageName: String!) {\n  jobBoard: jobBoardWithTeams(\n    organizationHostedJobsPageName: $organizationHostedJobsPageName\n  ) {\n    teams {\n      id\n      name\n      parentTeamId\n      __typename\n    }\n    jobPostings {\n      id\n      title\n      teamId\n      locationId\n      locationName\n      employmentType\n      secondaryLocations {\n        ...JobPostingSecondaryLocationParts\n        __typename\n      }\n      compensationTierSummary\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment JobPostingSecondaryLocationParts on JobPostingSecondaryLocation {\n  locationId\n  locationName\n  __typename\n}".replace('BOARD_IDENTIFIER', self.identifier)
        }
        response = requests.post('https://jobs.ashbyhq.com/api/non-user-graphql?op=ApiJobBoardWithTeams', json=payload)
        if response.status_code != 200:
            raise ConnectionError("get_board: response code is not 200")
        return response.json()

    def get_job_page(self, url):
        payload = {
            "operationName": "ApiJobPosting",
            "variables": {
                "organizationHostedJobsPageName": self.identifier,
                "jobPostingId": url
            },
            "query":"query ApiJobPosting($organizationHostedJobsPageName: String!, $jobPostingId: String!) {\n  jobPosting(\n    organizationHostedJobsPageName: $organizationHostedJobsPageName\n    jobPostingId: $jobPostingId\n  ) {\n    id\n    title\n    departmentName\n    locationName\n    employmentType\n    descriptionHtml\n    isListed\n    isConfidential\n    teamNames\n    applicationForm {\n      ...FormRenderParts\n      __typename\n    }\n    surveyForms {\n      ...FormRenderParts\n      __typename\n    }\n    secondaryLocationNames\n    compensationTierSummary\n    compensationTiers {\n      id\n      title\n      tierSummary\n      __typename\n    }\n    applicationDeadline\n    compensationTierGuideUrl\n    scrapeableCompensationSalarySummary\n    compensationPhilosophyHtml\n    applicationLimitCalloutHtml\n    shouldAskForTextingConsent\n    candidateTextingPrivacyPolicyUrl\n    __typename\n  }\n}\n\nfragment JSONBoxParts on JSONBox {\n  value\n  __typename\n}\n\nfragment FileParts on File {\n  id\n  filename\n  __typename\n}\n\nfragment FormFieldEntryParts on FormFieldEntry {\n  id\n  field\n  fieldValue {\n    ... on JSONBox {\n      ...JSONBoxParts\n      __typename\n    }\n    ... on File {\n      ...FileParts\n      __typename\n    }\n    ... on FileList {\n      files {\n        ...FileParts\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n  isRequired\n  descriptionHtml\n  isHidden\n  __typename\n}\n\nfragment FormRenderParts on FormRender {\n  id\n  formControls {\n    identifier\n    title\n    __typename\n  }\n  errorMessages\n  sections {\n    title\n    descriptionHtml\n    fieldEntries {\n      ...FormFieldEntryParts\n      __typename\n    }\n    isHidden\n    __typename\n  }\n  sourceFormDefinitionId\n  __typename\n}".replace('BOARD_IDENTIFIER', self.identifier).replace('JOB_ID', url)}
        response = requests.post('https://jobs.ashbyhq.com/api/non-user-graphql?op=ApiJobPosting', json=payload)
        if response.status_code != 200:
            raise ConnectionError("get_board: response code is not 200")
        return response.json()
    
    def get_job_element(self, page):
        return page['data']['jobPosting']
    
    def get_job_description(self, job_element):
        return job_element['descriptionHtml']
    
    def get_job_title(self, job_element):
        return job_element['title']
    
    def get_job_location(self, job_element):
        return job_element['locationName']
    
    def get_job_company(self, job_element):
        return self.company_name
    
    def get_board_url(self, job_element):
        return self.board_url
    
    def get_company_website(self, job_element):
        return self.company_website
    
    def get_commitment(self, job_element):
        try:
            return job_element['employmentType']
        except:
            return ''
        
    def get_job_role(self, job_element):
        return job_element['departmentName']

    def extract_job_id(self, job):
        return job['id']
    
    def extract_job_ids(self, board):
        job_listings = board['data']['jobBoard']['jobPostings']
        jobs = list(map(self.extract_job_id, job_listings))
        return jobs
    
