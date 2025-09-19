from rest_framework import serializers
from .models import Client, Project
from django.contrib.auth.models import User

class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email')

class ProjectListSerializer(serializers.ModelSerializer):
    users = UserSimpleSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = ('id', 'project_name', 'users', 'client', 'created_at', 'created_by')

class ProjectCreateSerializer(serializers.ModelSerializer):
    users = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)
    
    class Meta:
        model = Project
        fields = ('id', 'project_name', 'users')  # removed 'client'

    def create(self, validated_data):
        users = validated_data.pop('users', [])
        project = Project.objects.create(**validated_data)
        project.users.set(users)
        return project

class ClientSerializer(serializers.ModelSerializer):
    created_by = UserSimpleSerializer(read_only=True)
    projects = ProjectListSerializer(many=True, read_only=True)
    
    class Meta:
        model = Client
        fields = ('id', 'client_name', 'projects', 'created_at', 'updated_at', 'created_by')
