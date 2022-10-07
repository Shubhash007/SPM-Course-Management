from email.policy import default
from django.db import models

# Create your models here.
class User_Role(models.Model):
    """Model definition for User_Role."""
    User_Role_ID = models.IntegerField(primary_key=True)
    User_Role_Name = models.CharField(null=False,max_length=20)
    
    class Meta:
        """Meta definition for User_Role."""
        verbose_name = 'User_Role'

    def __str__(self):
        return f'{self.User_Role_ID} : {self.User_Role_Name}'
###############################################################################
class Staff(models.Model):
    """Model definition for Staff."""
    Staff_ID = models.IntegerField(primary_key=True)
    Staff_FName = models.CharField(null=False,max_length=50)
    Staff_LName = models.CharField(null=False,max_length=50)
    Dept = models.CharField(null=False,max_length=50)
    Email = models.EmailField(null=False,max_length=50)
    User_Role = models.ForeignKey(User_Role,on_delete=models.CASCADE)

    class Meta:
        """Meta definition for Staff."""
        verbose_name =  'Staff'

    def __str__(self):
        return f"{self.Staff_ID}"
##############################################################################
class Skill(models.Model):
    """Model definition for Skill."""
    Skill_ID = models.IntegerField(primary_key=True)
    Skill_Name = models.CharField(null=False,max_length=50) 
    Skill_Desc = models.CharField(max_length=255)

    class Meta:
        """Meta definition for Skill."""
        verbose_name = 'Skill'

    def __str__(self):
        return f'{self.Skill_ID},{self.Skill_Name},{self.Skill_Desc}'


################################################################################
class Course(models.Model):
    """Model definition for Courses."""
    Course_ID = models.CharField(primary_key=True,max_length=20)
    Course_Name = models.CharField(null=False,max_length=50)
    Course_Desc = models.CharField(max_length=255)
    Course_Status = models.CharField(max_length=15)
    Course_Type = models.CharField(max_length=10)
    Course_Category = models.CharField(max_length=50)
    Skills = models.ManyToManyField(Skill)

    class Meta:
        """Meta definition for Courses."""
        verbose_name = 'Course'


    def __str__(self):
        return f'{self.Course_ID} : {self.Course_Name},{self.Course_Status},{self.Course_Category}'
################################################################################
class Registration(models.Model):
    """Model definition for Registration."""
    # TODO: Define fields here
    Registration_ID = models.IntegerField(primary_key=True)
    Course_ID = models.ForeignKey(Course,on_delete=models.CASCADE)
    Staff_ID = models.ForeignKey(Staff,on_delete=models.CASCADE)
    Reg_Status = models.CharField(max_length=20)
    Completion_Status = models.CharField(max_length=20)

    class Meta:
        """Meta definition for Registration."""
        verbose_name = 'Registration'

    def __str__(self):
        return f'{self.Registration_ID},{self.Course_ID},{self.Staff_ID},{self.Completion_Status}'
###################################################################################
class JobRole(models.Model):
    """Model definition for Job_Role."""
    # TODO: Define fields here
    Job_Role_ID = models.IntegerField(primary_key=True)
    Job_Role_Desc = models.CharField(max_length=255)
    Staff = models.ForeignKey(Staff,on_delete=models.CASCADE,null=True)

    class Meta:
        """Meta definition for Job_Role."""
        verbose_name = 'Job_Role'

    def __str__(self):
        return f'{self.Job_Role_ID}:{self.Job_Role_Desc}'
###################################################################################
class Requirements(models.Model):
    """Model definition for Requirements."""
    Skill_ID = models.OneToOneField(Skill,on_delete=models.CASCADE)
    Job_Role_ID = models.OneToOneField(JobRole,on_delete=models.CASCADE)
    Staff_ID = models.OneToOneField(Staff,on_delete=models.CASCADE)
    Reg_Status = models.IntegerField(default=1,null=False)
    Completion_Status = models.CharField(max_length=15)


    class Meta:
        """Meta definition for Requirements."""
        unique_together = ['Skill_ID','Job_Role_ID', 'Staff_ID']
        verbose_name = 'Requirements'

    def __str__(self):
        pass
