from rest_framework import serializers

from api.apps.companies.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        depth = 1
        fields = '__all__'
