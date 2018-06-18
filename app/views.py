
from django.http.response import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from app.models import Project
from app.serializers import ProjectSerializer
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class ProjectListAPIView(APIView):

    def get(self, request):
        all_projects = Project.objects.all()
        serialized_projects = ProjectSerializer(all_projects, many=True)
        return Response(serialized_projects.data)

    def post(self, request):
        print(request.POST)
        title = request.POST['title']
        technologies_used = request.POST['technologies_used']
        github_link = request.POST['github_link']
        project_desription = request.POST['project_desription']

        Project.objects.create(title=title, technologies_used=technologies_used,
                               github_link=github_link, project_desription=project_desription)
        return Response({})


class ProjectDetailAPIView(APIView):

    def get(self, request, pk):
        project = Project.objects.get(id=pk)
        serialized_project = ProjectSerializer(project)
        return Response(serialized_project.data)

    def put(self, request, pk):
        project = Project.objects.get(id=pk)
        project.title = request.POST['title']
        project.technologies_used = request.POST['technologies_used']
        project.github_link = request.POST['github_link']
        project.project_description = request.POST['project_description']
        project.save()
        serialized_project = ProjectSerializer(project)
        return Response(serialized_project.data)

    def delete(self, request, pk):
        project = Project.objects.get(id=pk)
        project.delete()
        return Response({})


"""class ProjectListCreateAPIView(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer"""
