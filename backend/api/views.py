import json
from urllib import response
from django.shortcuts import render
from django.http import JsonResponse, HttpResponse, Http404
from .models import User_Role,Staff,Skill,Course,Registration,Job_Role,Requirements
from .serializers import CourseSerializer, Registration_Serializer, StaffSerializer,SkillSerializer,Requirements_Serializer,User_Role_Serializer, Job_Role_Serializer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status,mixins,generics
from django.db import IntegrityError



# Create your views here.
# @api_view(['GET', 'POST'])
# @csrf_exempt
# def staff_list(request):
#     #get all staff
#     if request.method == 'GET':
#         staffs = Staff.objects.all()
#         serializer = StaffSerializer(staffs, many=True)
#         return Response({'staff': serializer.data},status = status.HTTP_200_OK)

#     if request.method == 'POST':
#         serializer = StaffSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)
class staff_list(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):

    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)
    

class staff_detail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# @api_view(['GET', 'PUT', 'DELETE'])
# @csrf_exempt
# def staff_detail(request, query):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         staff = Staff.objects.get(Staff_ID=query)
#     except Staff.DoesNotExist:
#         return Response(data = "Cannot find user",status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = StaffSerializer(staff)
#         return Response(serializer.data, status = status.HTTP_200_OK)

#     elif request.method == 'PUT':
#         serializer = StaffSerializer(staff, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         staff.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



##########################SKILLS############################
class skill_list(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)
    

class skill_detail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


##########################COURSE#####################################################

class course_list(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self,request,*args,**kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)
    

class course_detail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

#####################################################################################

class skill_assign_course_detail(APIView):
    def get_object(self,pk):
        try:
            return Skill.objects.get(pk=pk)
        except Skill.DoesNotExist:
            raise Http404

    def get_course(self,pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        skill = self.get_object(pk)

        courses = skill.course_set.all()
        course_serializer = CourseSerializer(courses,many=True)
        return Response(course_serializer.data)
        #return Response({'error':"No Courses attached to skill"},status=status.HTTP_204_NO_CONTENT)

    def post(self,request,skill,course,format=None):
        skill_1 = self.get_object(skill)
        course_1 = self.get_course(course)
    
        course_1.Skills.add(skill_1)
        msg = f"course:{course_1.Course_ID} assigned to skill:{skill_1.Skill_ID}"
        return Response({'msg': msg},status = status.HTTP_201_CREATED)

    def delete(self,request,skill,course,formar=None):
        skill_1 = self.get_object(skill)
        course_1 = self.get_course(course)

        if skill_1 in course_1.Skills.all():
            course_1.Skills.remove(skill_1)
            course_1.save()
            msg = f"skill:{skill_1.Skill_ID} assignment to course:{course_1.Course_ID} has been removed"
            return Response({'msg': msg},status = status.HTTP_200_OK)
        return Response({"msg":f"skill:{skill_1.Skill_ID} not assigned to course:{course_1.Course_ID}"},status=status.HTTP_404_NOT_FOUND)
##############################User_Role###############################################

class user_role_list(mixins.RetrieveModelMixin,
                generics.GenericAPIView):

    queryset = User_Role.objects.all()
    serializer_class = User_Role_Serializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

####################Registration##################################################

class registration_list(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):

    queryset = Registration.objects.all()
    serializer_class = Registration_Serializer

    def get(self,request,*args,**kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)


class registration_detail(generics.GenericAPIView,
                        mixins.UpdateModelMixin,
                        mixins.CreateModelMixin,
                        mixins.DestroyModelMixin):

    queryset = Registration.objects.all()
    serializer_class = Registration_Serializer

    def get_staff(self,pk):
        try:
            return Staff.objects.get(pk=pk)
        except Staff.DoesNotExist:
            raise Http404

    def get_course(self,pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404

    def get(self,request,pk,format=None):
        if isinstance(pk, int):
            staff = self.get_staff(pk)
            registrations = staff.registration_set.all()
            registration_serializer = Registration_Serializer(registrations,many=True)
            return Response(registration_serializer.data)
        
        if isinstance(pk, str):
            course = self.get_course(pk)
            registrations = course.registration_set.all()
            registration_serializer = Registration_Serializer(registrations,many=True)
            return Response(registration_serializer.data)


    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

######################################JOB_ROLE######################################################
class job_role_list(mixins.ListModelMixin,
                mixins.CreateModelMixin,
                generics.GenericAPIView):

    queryset = Job_Role.objects.all()
    serializer_class = Job_Role_Serializer

    def get(self,request,*args,**kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self,request,*args,**kwargs):
        return self.create(request, *args, **kwargs)
    

class job_role_detail(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):

    queryset = Job_Role.objects.all()
    serializer_class = Job_Role_Serializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
########################################################################################

class job_assign_skill_detail(APIView):
    def get_job_role(self,pk):
        try:
            return Job_Role.objects.get(pk=pk)
        except Job_Role.DoesNotExist:
            raise Http404

    def get_skill(self,pk):
        try:
            return Skill.objects.get(pk=pk)
        except Skill.DoesNotExist:
            raise Http404

    def post(self,request,skill,job_role,format=None):
        skill_1 = self.get_skill(skill)
        job_role_1 = self.get_job_role(job_role)

        job_role_1.Skills.add(skill_1)
        msg = f"skill:{skill_1.Skill_Name} assigned to Job Role:{job_role_1.Job_Role_Name}"
        return Response({'msg': msg},status = status.HTTP_201_CREATED)

    def delete(self,request,skill,job_role,format=None):
        skill_1 = self.get_skill(skill)
        job_role_1 = self.get_job_role(job_role)

        if skill_1 in job_role_1.Skills.all():
            job_role_1.Skills.remove(skill_1)
            job_role_1.save()
            msg = f"skill:{skill_1.Skill_ID} assignment to Job Role:{job_role_1.Job_Role_ID} has been removed"
            return Response({'msg': msg},status = status.HTTP_200_OK)
        return Response({"msg":f"skill:{skill_1.Skill_Name} not assigned to Job Role:{job_role_1.Job_Role_Name}"},status = status.HTTP_404_NOT_FOUND)

################################Requirements##################################################################
class requirements_list(APIView):
    def get_job_role(self,pk):
        try:
            return Job_Role.objects.get(pk=pk)
        except Job_Role.DoesNotExist:
            raise Http404

    def get_staff(self,pk):
        try:
            return Staff.objects.get(pk=pk)
        except Staff.DoesNotExist:
            raise Http404

    def get_course(self,pk):
        try:
            return Course.objects.get(pk=pk)
        except Course.DoesNotExist:
            raise Http404

    def get(self,request,staff_id,format=None):
        staff = self.get_staff(staff_id)

        search = Requirements.objects.filter(Staff_id=staff.Staff_ID)
        serializer = Requirements_Serializer(search,many=True)
        return Response(serializer.data,status = status.HTTP_200_OK)

    def post(self,request,staff_id,job_role_id,course_id,format=None):
        staff = self.get_staff(staff_id)
        job_role = self.get_job_role(job_role_id)
        course = self.get_course(course_id)

        if Requirements.objects.filter(Staff_id=staff.Staff_ID,Job_Role_id=job_role.Job_Role_ID,Course_id=course.Course_ID).exists():
            return Response({'msg': f'This {course.Course_Name} has already been assigned to {staff.Staff_FName} with job role {job_role.Job_Role_Name}'},status=status.HTTP_404_NOT_FOUND)
        else:
            Requirements.objects.create(Course_id=course.Course_ID,Job_Role_id=job_role.Job_Role_ID,Staff_id=staff.Staff_ID)
            return Response(f"{staff} with {job_role} has {course} saved",status=status.HTTP_200_OK)
            

    def delete(self,request,staff_id,job_role_id,course_id,format=None):
        staff = self.get_staff(staff_id)
        job_role = self.get_job_role(job_role_id)
        course = self.get_course(course_id)
        
        req = Requirements.objects.filter(Staff_id=staff.Staff_ID,Job_Role_id=job_role.Job_Role_ID,Course_id=course.Course_ID)
        if req.exists():
            req.delete()
            return Response({'msg':f"{staff.Staff_ID},{course.Course_ID},{job_role.Job_Role_ID} has been removed"},status=status.HTTP_200_OK)
        return Response({'msg':f"{staff.Staff_ID},{course.Course_ID},{job_role.Job_Role_ID} dosent exist"},status=status.HTTP_404_NOT_FOUND)
