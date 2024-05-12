from rest_framework import viewsets
from .models import Job
from .serializers import JobSerializer
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from .filters import JobFilter
from django_filters.rest_framework import DjangoFilterBackend


class CustomPagination(PageNumberPagination):
    page_size_query_param = 'page_size'
    max_page_size = 50
    page_size = 10


class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = CustomPagination
    filter_backends = [DjangoFilterBackend]
    filterset_class = JobFilter

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [permissions.IsAuthenticated()]
        return super().get_permissions()

