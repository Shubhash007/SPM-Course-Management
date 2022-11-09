import pytest
from rest_framework.test import APIClient
from pytest_factoryboy import register
from .factories import SkillFactory,CourseFactory,StaffFactory,JobRoleFactory,UserRoleFactory,RegistrationFactory,LjFactory

register(SkillFactory)
register(CourseFactory)
register(UserRoleFactory)
register(JobRoleFactory)
register(StaffFactory)
register(RegistrationFactory)
register(LjFactory)

@pytest.fixture
def api_client():
    return APIClient

@pytest.fixture
def create_skill(db,skill_factory):
    skill = skill_factory.create()
    return skill

@pytest.fixture
def create_course(db,course_factory):
    course = course_factory.create()
    return course

@pytest.fixture
def create_staff(db,staff_factory):
    staff = staff_factory.create()
    return staff

@pytest.fixture
def create_user_role(db,user_role_factory):
    user_role = user_role_factory.create()
    return user_role

@pytest.fixture
def create_job_role(db,job_role_factory):
    job_role = job_role_factory.create()
    return job_role

@pytest.fixture
def create_registration(db,registration_factory):
    reg = registration_factory.create()
    return reg

@pytest.fixture
def create_lj(db,lj_factory):
    lj = lj_factory.create()
    return lj





