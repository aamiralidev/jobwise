from abc import ABC, abstractmethod
from jobs.models import Job

# NOTE: it is a better idea to extract information from job page related to job as it makes better hirarchi


##### greenhouse boards

# https://bitso.com/jobs                // this one embeds greenhouse
# https://array.com/company/careers#open-roles  // partially greenhouse. job board is personal while job details is greenhouse


##### Paylocity
# https://recruiting.paylocity.com/recruiting/jobs/All/cab4161a-b9de-40e7-85e8-27920748af9d/OCHIN


class BaseJobExtractor(ABC):

    def set_company_website(self, board):
        self.company_website = '' 

    @abstractmethod
    def set_company_name(self, board):
        self.company_name = ''

    @abstractmethod
    def get_board(self):
        pass
    
    @abstractmethod
    def get_job_page(self, url):
        pass

    @abstractmethod
    def get_job_element(self, page):
        pass

    @abstractmethod
    def get_job_description(self, job_element):
        pass
    
    @abstractmethod
    def get_job_title(self, job_element):
        pass

    @abstractmethod
    def get_job_location(self, job_element):
        pass

    @abstractmethod
    def get_job_company(self, job_element):
        pass
    
    def get_company_website(self, job_element):
        return ''
    
    @abstractmethod
    def get_board_url(self, job_element):
        pass
    
    @abstractmethod
    def extract_job_id(self, job):
        pass

    @abstractmethod
    def extract_job_ids(self, board):
        pass

    def get_existing_job_ids(self):
        return Job.objects.filter(board_url=self.get_board_url(None)).values_list('original_id', flat=True)

    def get_career_level(self, job_element):
        return ''
    
    def get_degree_required(self, job_element):
        return ''
    
    def get_visa_sponsorhip(self, job_element):
        return False 
    
    def get_remote_from_anywhere(self, job_element):
        return False 
    
    def get_relocation_support(self, job_element):
        return False
    
    def get_job_role(self, job_element):
        return ''
    
    def get_language(self, job_element):
        return ''
    
    def get_contract(self, job_element):
        return ''
    
    def get_commitment(self, job_element):
        return ''
    
    def get_workplace_type(self, job_element):
        return ''
    
    def get_open_status(self, job_element):
        return True

    def extract_job(self, job_id):
        job_page = self.get_job_page(job_id)
        job_element = self.get_job_element(job_page)
        url = job_id
    
        return Job(
                original_id=url,
                url=url,
                title=self.get_job_title(job_element), 
                company_name=self.get_job_company(job_element),
                company_website = self.get_company_website(job_element),
                board_url=self.get_board_url(job_element),
                career_level=self.get_career_level(job_element),
                degree=self.get_degree_required(job_element),
                visa_sponsorship = self.get_visa_sponsorhip(job_element),
                remote_from_anywhere = self.get_remote_from_anywhere(job_element),
                relocation_support = self.get_relocation_support(job_element),
                job_role = self.get_job_role(job_element),
                language=self.get_language(job_element),
                contract=self.get_contract(job_element),
                commitment=self.get_commitment(job_element),
                workplace_type=self.get_workplace_type(job_element),
                location=self.get_job_location(job_element),
                job_description=self.get_job_description(job_element),
                open=self.get_open_status(job_element),
            )
    
    def extract(self):
        board = self.get_board()
        self.set_company_name(board)
        self.set_company_website(board)
        job_ids = set(self.extract_job_ids(board))
        existing_job_ids = set(self.get_existing_job_ids())
        closed_jobs = existing_job_ids - job_ids
        new_jobs = job_ids - existing_job_ids
        if closed_jobs:
            closed_jobs_queryset = Job.objects.filter(original_id__in=closed_jobs)
            closed_jobs_queryset.update(open=False)
        jobs = list(map(self.extract_job, new_jobs))
        if jobs:
            Job.objects.bulk_create(jobs, ignore_conflicts=True)