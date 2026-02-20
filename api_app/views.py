from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from projects_app.models import Project
from contact_app.models import ContactMessage
from .serializers import ProjectSerializer, ContactSerializer
from django.shortcuts import get_object_or_404


# GET all projects
@api_view(['GET'])
@permission_classes([AllowAny])
def api_projects(request):

    projects = Project.objects.all().order_by('-created_date')

    serializer = ProjectSerializer(projects, many=True)

    return Response(serializer.data)


# GET single project by slug
@api_view(['GET'])
@permission_classes([AllowAny])
def api_project_detail(request, slug):

    project = get_object_or_404(Project, slug=slug)

    serializer = ProjectSerializer(project)

    return Response(serializer.data)


# POST new project (authenticated)
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_project_create(request):

    serializer = ProjectSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)


# POST contact message
@api_view(['POST'])
@permission_classes([AllowAny])
def api_contact_create(request):

    serializer = ContactSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors)
