from rest_framework import serializers
from projects_app.models import Project
from contact_app.models import ContactMessage


class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactMessage
        fields = '__all__'
