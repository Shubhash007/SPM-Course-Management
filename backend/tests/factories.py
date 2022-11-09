import factory, random, factory.fuzzy

from api.models import User_Role,Staff,Skill,Course,Registration,Job_Role,Requirements
from faker import Faker


fake = Faker()


class SkillFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Skill

    Skill_ID = 1000
    Skill_Name = 'testing pytest'
    Skill_Desc = 'for testing purposes used in factory model'

class CourseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Course

    Course_ID = "TEST001"
    Course_Name = fake.sentence(nb_words=1)
    Course_Desc = fake.sentence(nb_words=10)
    Course_Status = "Active"
    Course_Type = "Internal"
    Course_Category = "Core"

    @factory.post_generation
    def Skills(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for skill in extracted:
                self.Skills.add(skill)

class UserRoleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User_Role

    class Params:
    # Decide who the winner is; that field won't be passed to the `Match` model.
        user = random.choice([1,2,3,4])
    
    User_Role_ID = fake.random_element(elements=('1', '2', '3', '4'))
    User_Role_Name = ["Admin","User","Manager","Trainer"][int(User_Role_ID) - 1]

class JobRoleFactory(factory.django.DjangoModelFactory):
    Job_Role_ID = 20
    class Meta:
        model = Job_Role
        django_get_or_create = ('Job_Role_ID',)

    Job_Role_Name = fake.sentence(nb_words=2)
    Job_Role_Desc = fake.sentence(nb_words=10)
    Dept = fake.random_element(elements=('Sales','Ops','HR','Finance'))
    @factory.post_generation
    def Skills(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for skill in extracted:
                self.Skills.add(skill)

class StaffFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Staff

    Staff_ID = 1
    Staff_FName = fake.first_name()
    Staff_LName = fake.last_name()
    Dept = fake.random_element(elements=('Sales','Ops','HR','Finance'))
    Email = f"{Staff_FName}.{Staff_LName}@allinone.com.sg"
    User_Role = factory.SubFactory(UserRoleFactory)
    Job_Role = factory.SubFactory(JobRoleFactory)


class RegistrationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Registration

    Reg_ID = 9999
    Course = factory.SubFactory(CourseFactory)
    Staff = factory.SubFactory(StaffFactory)
    Reg_Status = 'Completed'
    Completion_Status = 'Registered'

class LjFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Requirements

    Job_Role= factory.SubFactory(JobRoleFactory)
    Staff = factory.SubFactory(StaffFactory)

    @factory.post_generation
    def Course_Registered(self, create, extracted, **kwargs):
        if not create:
            # Simple build, do nothing.
            return

        if extracted:
            # A list of groups were passed in, use them
            for c in extracted:
                self.Course_Registered.add(c)
