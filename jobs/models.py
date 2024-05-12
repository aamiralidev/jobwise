from django.db import models

class BoardProvider(models.Model):
    identifier = models.CharField(max_length=255, primary_key=True)
    domain = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    identifier_by_prefix = models.BooleanField(default=False)

class JobBoard(models.Model):
    provider = models.CharField(max_length=255, blank=True)
    identifier = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    board_url = models.CharField(max_length=255)

    # Ensure unique combination of provider and identifier
    class Meta:
        unique_together = ('provider', 'identifier')

class Job(models.Model):
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
    original_id = models.CharField(max_length=255, blank=True)
    url = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    company_website = models.URLField(blank=True)
    board_url = models.CharField(max_length=255)
    company_logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    # career_level = models.CharField(max_length=50, choices=CAREER_LEVEL_CHOICES, blank=True)
    career_level = models.CharField(max_length=50, blank=True)
    experience_level_min = models.IntegerField(default=-1)
    experience_level_max = models.IntegerField(default=-1)
    date_posted = models.DateField(auto_now_add=True)
    # degree = models.CharField(max_length=50, choices=DEGREE_CHOICES, default='no_degree_required')
    degree = models.CharField(max_length=50, blank=True)
    visa_sponsorship = models.BooleanField(default=False)
    remote_from_anywhere = models.BooleanField(default=False)
    relocation_support = models.BooleanField(default=False)
    job_role = models.CharField(max_length=100, blank=True)
    skills = models.CharField(max_length=255, blank=True)
    language = models.CharField(max_length=100, blank=True)
    # contract = models.CharField(max_length=50, choices=[('temporary', 'Temporary'), ('permanent', 'Permanent')], default='permanent')
    contract = models.CharField(max_length=50, blank=True)
    # commitment = models.CharField(max_length=50, choices=[('part-time', 'Part-time'), ('full-time', 'Full-time')], default='full-time')
    commitment = models.CharField(max_length=255, blank=True)
    # workplace_type = models.CharField(max_length=50, choices=[('on-site', 'On-site'), ('remote', 'Remote'), ('hybrid', 'Hybrid'), ('remote-across-borders', 'Remote across Borders')], default='on-site')
    workplace_type = models.CharField(max_length=50, blank=True)
    region = models.CharField(max_length=255, blank=True)
    country = models.CharField(max_length=255, blank=True)
    state = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    location = models.CharField(max_length=255, blank=True)
    job_description = models.TextField(blank=True)
    open = models.BooleanField(default=True)

    def __str__(self):
        return self.title

