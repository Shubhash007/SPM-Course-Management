from rest_framework import serializers
from .models import User_Role,Staff,Skill,Course,Registration,Job_Role,Requirements


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['Staff_ID','Staff_FName','Staff_LName','Dept','Email','User_Role']

        
class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skill
        fields = ['Skill_ID','Skill_Name','Skill_Desc']


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
        fields = "__all__"

class Requirements_Serializer(serializers.ModelSerializer):
    Job_Role= Job_Role_Serializer()
    Course = CourseSerializer()
    class Meta:
        model = Requirements
        fields = "__all__"


