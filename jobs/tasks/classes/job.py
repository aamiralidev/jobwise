from dataclasses import dataclass
from typing import Optional
# from django.db import models

@dataclass
class Job:
    original_id: Optional[str] = None
    title: str = ''
    company_name: str = ''
    company_website: str = ''
    company_logo: str = ''
    url: str = ''
    career_level: str = ''
    experience_level_min: int = -1
    experience_level_max: int = -1
    date_posted: str = ''
    degree: str = 'no_degree_required'
    visa_sponsorship: bool = False
    remote_from_anywhere: bool = False
    relocation_support: bool = False
    job_role: str = ''
    skills: str = ''
    language: str = ''
    contract: str = 'permanent'
    commitment: str = 'full-time'
    workplace_type: str = 'on-site'
    region: str = ''
    country: str = ''
    state: str = ''
    city: str = ''
    location: str = ''
    job_description: str = ''
    board_url: str = ''
    open: bool = True
    

    CAREER_LEVEL_CHOICES = [
        ('intern', 'Intern'),
        ('apprenticeship', 'Apprenticeship'),
        ('freshgrad', 'Fresh Graduate'),
        ('associate', 'Associate'),
        ('entry', 'Entry'),
        ('mid', 'Mid'),
        ('senior', 'Senior'),
        ('staff', 'Staff'),
        ('director', 'Director'),
        ('executive', 'Executive'),
    ]

    DEGREE_CHOICES = [
        ('bachelors', "Bachelor's"),
        ('masters', "Master's"),
        ('phd', 'PhD'),
        ('diploma', 'Diploma'),
        ('no_degree_required', 'No Degree Required'),
    ]

    CONTRACT_CHOICES = [
        ('temporary', 'Temporary'),
        ('permanent', 'Permanent')
    ]

    COMMITMENT_CHOICES = [
        ('part-time', 'Part-time'),
        ('full-time', 'Full-time')
    ]

    WORKPLACE_TYPE_CHOICES = [
        ('on-site', 'On-site'),
        ('remote', 'Remote'),
        ('hybrid', 'Hybrid'),
        ('remote-across-borders', 'Remote across Borders')
    ]

    @classmethod
    def from_django_model(cls, job_instance):
        return cls(
            original_id=job_instance.original_id,
            title=job_instance.title,
            company_name=job_instance.company_name,
            company_website=job_instance.company_website,
            company_logo=job_instance.company_logo.url if job_instance.company_logo else '',
            career_level=job_instance.career_level,
            experience_level_min=job_instance.experience_level_min,
            experience_level_max=job_instance.experience_level_max,
            date_posted=str(job_instance.date_posted),
            degree=job_instance.degree,
            visa_sponsorship=job_instance.visa_sponsorship,
            remote_from_anywhere=job_instance.remote_from_anywhere,
            relocation_support=job_instance.relocation_support,
            job_role=job_instance.job_role,
            skills=job_instance.skills,
            language=job_instance.language,
            contract=job_instance.contract,
            commitment=job_instance.commitment,
            workplace_type=job_instance.workplace_type,
            region=job_instance.region,
            country=job_instance.country,
            state=job_instance.state,
            city=job_instance.city,
            location=job_instance.location,
            job_description=job_instance.job_description
        )

    # def to_django_model(self):
    #     job_instance = models.Job()
    #     job_instance.original_id = self.original_id
    #     job_instance.title = self.title
    #     job_instance.company_name = self.company_name
    #     job_instance.company_website = self.company_website
    #     job_instance.company_logo = self.company_logo
    #     job_instance.career_level = self.career_level
    #     job_instance.experience_level_min = self.experience_level_min
    #     job_instance.experience_level_max = self.experience_level_max
    #     job_instance.date_posted = self.date_posted
    #     job_instance.degree = self.degree
    #     job_instance.visa_sponsorship = self.visa_sponsorship
    #     job_instance.remote_from_anywhere = self.remote_from_anywhere
    #     job_instance.relocation_support = self.relocation_support
    #     job_instance.job_role = self.job_role
    #     job_instance.skills = self.skills
    #     job_instance.language = self.language
    #     job_instance.contract = self.contract
    #     job_instance.commitment = self.commitment
    #     job_instance.workplace_type = self.workplace_type
    #     job_instance.region = self.region
    #     job_instance.country = self.country
    #     job_instance.state = self.state
    #     job_instance.city = self.city
    #     job_instance.location = self.location
    #     job_instance.job_description = self.job_description

    #     return job_instance
