import django_filters
from .models import Job

class JobFilter(django_filters.FilterSet):
    company_name = django_filters.CharFilter(field_name='company_name', lookup_expr='exact')
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    career_level = django_filters.CharFilter(field_name='career_level', lookup_expr='exact')
    date_posted = django_filters.DateFilter(field_name='date_posted', lookup_expr='gte')
    degree = django_filters.CharFilter(field_name='degree', lookup_expr='exact')
    visa_sponsorship = django_filters.BooleanFilter(field_name='visa_sponsorship')
    relocation_support = django_filters.BooleanFilter(field_name='relocation_support')
    remote_from_anywhere = django_filters.BooleanFilter(field_name='remote_from_anywhere')
    job_role = django_filters.CharFilter(field_name='job_role', lookup_expr='icontains')
    skills = django_filters.CharFilter(field_name='skills', lookup_expr='icontains')
    language = django_filters.CharFilter(field_name='language', lookup_expr='icontains')
    commitment = django_filters.CharFilter(field_name='commitment', lookup_expr='exact')
    workplace_type = django_filters.CharFilter(field_name='workplace_type', lookup_expr='exact')
    location_region = django_filters.CharFilter(field_name='location_region', lookup_expr='exact')
    location_country = django_filters.CharFilter(field_name='location_country', lookup_expr='exact')
    location_state = django_filters.CharFilter(field_name='location_state', lookup_expr='exact')
    location_city = django_filters.CharFilter(field_name='location_city', lookup_expr='exact')

    class Meta:
        model = Job
        fields = []
