from pickletools import read_long1
from wsgiref.validate import validator
from rest_framework import serializers
from .models import User_Role,Staff,Skill,Course,Registration,Job_Role,Requirements


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = "__all__"

        
class SkillSerializer(serializers.ModelSerializer):
    courses = serializers.StringRelatedField(many=True,read_only=True)
    class Meta:
        model = Skill
        fields = ['Skill_ID','Skill_Name','Skill_Desc','courses']
        extra_kwargs = {'courses': {'required': False, "allow_null": True}}

class CourseSerializer(serializers.ModelSerializer):
    Skills = SkillSerializer(many=True)
    class Meta:
        model = Course
        fields = "__all__"

class User_Role_Serializer(serializers.ModelSerializer):
    class Meta:
        model = User_Role
        fields = '__all__'

class Registration_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = "__all__"

class Job_Role_Serializer(serializers.ModelSerializer):
    Skills = SkillSerializer(many=True)
    class Meta:
        model = Job_Role
        fields = ['Job_Role_ID','Job_Role_Name','Job_Role_Desc','Dept','Skills']
        extra_kwargs = {'Skills': {'required': False, "allow_null": True}}

class Requirements_Serializer(serializers.ModelSerializer):
    Job_Role= Job_Role_Serializer(read_only=True)
    class Meta:
        model = Requirements
        fields = "__all__"