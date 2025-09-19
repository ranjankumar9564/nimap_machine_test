
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Client, Project
from .serializers import ClientSerializer, ProjectCreateSerializer, ProjectListSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User

class ClientListCreateView(generics.ListCreateAPIView):
    queryset = Client.objects.all().order_by('-created_at')
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

class ClientDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = (IsAuthenticated,)

    def perform_update(self, serializer):
        serializer.save()  # updated_at handled automatically

class ProjectCreateForClientView(generics.CreateAPIView):
    serializer_class = ProjectCreateSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        client_id = self.kwargs.get('client_id')
        client = get_object_or_404(Client, pk=client_id)
        serializer.save(client=client, created_by=self.request.user)

class ProjectListForUserView(generics.ListAPIView):
    serializer_class = ProjectListSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Project.objects.filter(users=self.request.user).order_by('-created_at')
