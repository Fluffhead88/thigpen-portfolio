
from rest_framework import serializers

from app.models import Project 

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'title', 'technologies_used', 'github_link', 'project_desription']
