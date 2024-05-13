from rest_framework import serializers
from company.models import JobOpening

class JobOpeningSerializer(serializers.ModelSerializer):
    company_name = serializers.CharField(source='company.company_name', read_only=True)
    class Meta:
        model = JobOpening
        fields = '__all__'