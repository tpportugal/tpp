from rest_framework import viewsets

from api.apps.companies.models import Company
from api.apps.companies.serializer import CompanySerializer


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
