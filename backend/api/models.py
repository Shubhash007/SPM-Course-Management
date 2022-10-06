from django.db import models

# Create your models here.
class Role(models.Model):
    """Model definition for Role."""
    Role_ID = models.IntegerField(primary_key=True, null=False)
    Role_Name = models.CharField(null=False,max_length=20)
    

    class Meta:
        """Meta definition for Role."""
        verbose_name = 'Role'

    def __str__(self):
        return f'{self.Role_ID} : {self.Role_Name}'


class Staff(models.Model):
    """Model definition for Staff."""
    Staff_ID = models.IntegerField(primary_key=True, null=False)
    Staff_FName = models.CharField(null=False,max_length=50)
    Staff_LName = models.CharField(null=False,max_length=50)
    Dept = models.CharField(null=False,max_length=50)
    Email = models.EmailField(null=False,max_length=50)
    Role = models.ForeignKey(Role,on_delete=models.CASCADE)
    class Meta:
        """Meta definition for Staff."""
        verbose_name =  'Staff'

    def __str__(self):
        return f"{self.Staff_ID}"


class Course(models.Model):
    """Model definition for Courses."""
    Course_ID = models.CharField(primary_key=True, null=False,max_length=20)
    Course_Name = models.CharField(null=False,max_length=50)
    Course_Desc = models.CharField(max_length=255)
    Course_Status = models.CharField(max_length=15)
    Course_Type = models.CharField(max_length=10)
    Course_Category = models.CharField(max_length=50)


    class Meta:
        """Meta definition for Courses."""
        verbose_name = 'Course'


    def __str__(self):
        return f'{self.Course_ID} : {self.Course_Name},{self.Course_Status},{self.Course_Category}'

class Registration(models.Model):
    """Model definition for Registration."""
    # TODO: Define fields here
    Registration_ID = models.IntegerField(primary_key=True, null=False)
    Course_ID = models.ForeignKey(Course,on_delete=models.CASCADE)
    Staff_ID = models.ForeignKey(Staff,on_delete=models.CASCADE)
    Reg_Status = models.CharField(max_length=20)
    Completion_Status = models.CharField(max_length=20)

    class Meta:
        """Meta definition for Registration."""
        verbose_name = 'Registration'

    def __str__(self):
        """Unicode representation of Registration."""
        pass

