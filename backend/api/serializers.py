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
    class Meta:
        model = Course
        fields = ['Course_ID','Course_Name','Course_Desc','Course_Status','Course_Type','Course_Category']


class JobRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job_Role
        fields = ['Job_Role_ID','Job_Role_Desc','Job_Role_Name']