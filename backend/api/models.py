from email.policy import default
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class User_Role(models.Model):
    """Model definition for User_Role."""
    User_Role_ID = models.IntegerField(primary_key=True)
    User_Role_Name = models.CharField(null=False,max_length=20)
    
    class Meta:
        """Meta definition for User_Role."""
        verbose_name_plural = 'User_Roles'

    def __str__(self):
        return f'{self.User_Role_ID} : {self.User_Role_Name}'
##############################################################################
class Skill(models.Model):
    """Model definition for Skill."""
    Skill_ID = models.IntegerField(primary_key=True)
    Skill_Name = models.CharField(null=False,max_length=50) 
    Skill_Desc = models.CharField(max_length=255)

    class Meta:
        """Meta definition for Skill."""
        verbose_name_plural = 'Skills'

    def __str__(self):
        return f'{self.Skill_ID},{self.Skill_Name}'

###################################################################################
class Job_Role(models.Model):
    """Model definition for Job_Role."""
    # TODO: Define fields here
    Job_Role_ID = models.IntegerField(primary_key=True)
    Job_Role_Name = models.CharField(max_length=200,default="")
    Job_Role_Desc = models.CharField(max_length=255)
    Dept = models.CharField(max_length=30,default="")
    #Staff = models.ForeignKey(Staff, to_field = 'Staff_ID',on_delete=models.CASCADE,null=True)
    Skills = models.ManyToManyField(Skill, blank=True, related_name='jb_skills')

    class Meta:
        """Meta definition for Job_Role."""
        verbose_name_plural = 'Job_Roles'

    def __str__(self):
        return f'{self.Job_Role_ID}:{self.Job_Role_Name}:{self.Dept}'
###############################################################################
class Staff(models.Model):
    """Model definition for Staff."""
    Staff_ID = models.BigIntegerField(primary_key=True)
    Staff_FName = models.CharField(null=False,max_length=50)
    Staff_LName = models.CharField(null=False,max_length=50)
    Dept = models.CharField(null=False,max_length=50)
    Email = models.EmailField(null=False,max_length=50)
    User_Role = models.ForeignKey(User_Role,on_delete=models.CASCADE)
    Job_Role = models.ForeignKey(Job_Role,on_delete=models.CASCADE, default=None, null=True, blank= True)

    class Meta:
        """Meta definition for Staff."""
        verbose_name_plural =  'Staffs'

    def __str__(self):
        return f"{self.Staff_ID}"
################################################################################
class Course(models.Model):
    """Model definition for Courses."""
    Course_ID = models.CharField(primary_key=True,max_length=20)
    Course_Name = models.CharField(null=False,max_length=50)
    Course_Desc = models.CharField(max_length=255)
    Course_Status = models.CharField(max_length=15)
    Course_Type = models.CharField(max_length=10)
    Course_Category = models.CharField(max_length=50)
    Skills = models.ManyToManyField(Skill, related_name = 'courses')

    class Meta:
        """Meta definition for Courses."""
        verbose_name_plural = 'Courses'


    def __str__(self):
        return f'{self.Course_ID},{self.Course_Name},{self.Course_Status},{self.Course_Category}'
################################################################################
class Registration(models.Model):
    """Model definition for Registration."""
    # TODO: Define fields here
    Reg_ID = models.IntegerField(primary_key=True)
    Course = models.ForeignKey(Course,on_delete=models.CASCADE)
    Staff = models.ForeignKey(Staff,on_delete=models.CASCADE)
    Reg_Status = models.CharField(max_length=20,null=True,default="")
    Completion_Status = models.CharField(max_length=20,null=True,default="")

    class Meta:
        """Meta definition for Registration."""
        verbose_name_plural = 'Registrations'
        unique_together = [['Reg_ID', 'Course', 'Staff']]

    def __str__(self):
        return f'{self.Reg_ID},{self.Course},{self.Staff},{self.Completion_Status}'
###################################################################################
class Requirements(models.Model):
    """Model definition for Requirements."""
    Course_Registered = models.ManyToManyField(Course,related_name='ljcourses')
    Job_Role= models.ForeignKey(Job_Role,on_delete=models.CASCADE)
    Staff = models.ForeignKey(Staff,on_delete=models.CASCADE)
    # Registration = models.OneToOneField(Registration,on_delete=models.CASCADE,null=True)
    # Reg_Status = models.IntegerField(default=1,null=False)
    # Completion_Status = models.CharField(max_length=15)


    class Meta:
        """Meta definition for Requirements."""
        unique_together = [[ 'Job_Role', 'Staff']]
        verbose_name_plural = 'Requirements'
        managed = True

    def __str__(self):
        return f'Job_Role:{self.Job_Role.Job_Role_ID},Staff_ID:{self.Staff.Staff_ID}'
    