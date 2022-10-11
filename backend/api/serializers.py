from rest_framework import serializers
from .models import User_Role,Staff,Skill,Course,Registration,Job_Role,Requirements


class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = ['Staff_ID','Staff_FName','Staff_LName','Dept','Email','User_Role']

        
    