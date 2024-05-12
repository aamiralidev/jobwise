from rest_framework.routers import DefaultRouter
from jobs.views import JobViewSet

job_router = DefaultRouter()
job_router.register(r'jobs', JobViewSet)
