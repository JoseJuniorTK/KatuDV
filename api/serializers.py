from rest_framework import serializers
from .models import BillerServicesUploads


class FileUpload(serializers.ModelSerializer):
    class Meta:
        model = BillerServicesUploads
        fields = '__all__'
