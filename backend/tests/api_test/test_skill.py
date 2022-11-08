import pytest
from rest_framework.test import APIClient
from api.models import User_Role,Staff,Skill,Course,Registration,Job_Role,Requirements
from ..factories import SkillFactory,CourseFactory,StaffFactory,JobRoleFactory,UserRoleFactory,RegistrationFactory,LjFactory
client = APIClient()



@pytest.mark.django_db
def test_get_all_skills(create_skill):
    response = client.get("/skill/")

    data = response.data

    assert len(data) == Skill.objects.count()
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_1_skill(create_skill):
    response = client.get("/skill/1000/")

    data = response.data

    assert data["Skill_ID"] == 1000
    assert data["Skill_Name"] ==  'testing pytest'
    assert data["Skill_Desc"] ==  'for testing purposes used in factory model'
    assert data["courses"] ==  []
    assert response.status_code == 200

@pytest.mark.django_db
def test_post_skill_no_course():
    
    payload = {
    "Skill_ID": 1000,
    "Skill_Name": "test",
    "Skill_Desc": "lorem ipsum",
    }

    response = client.post("/skill/", payload)

    data = response.data

    assert data["Skill_ID"] == 1000
    assert data["Skill_Name"] ==  "test"
    assert data["Skill_Desc"] ==  "lorem ipsum"
    assert data["courses"] ==  []
    assert response.status_code == 201

@pytest.mark.django_db
def test_post_skill_exisitng_id(create_skill):
    payload = {
    "Skill_ID": 1000,
    "Skill_Name": "test",
    "Skill_Desc": "lorem ipsum",
    }

    response = client.post("/skill/",payload)
    # data = response.data
    assert response.status_code == 400
    assert response.data == {
        "Skill_ID": [
            "skill with this Skill ID already exists."
        ]
    }
@pytest.mark.django_db
def test_update_skill(create_skill):
    payload = {
        "Skill_Name": "a",
        "Skill_Desc": "b"
    }

    response = client.patch("/skill/1000/",payload)
    data = response.data
    assert response.status_code == 200
    assert data["Skill_Name"] == 'a'
    assert data["Skill_Desc"] == "b"


@pytest.mark.django_db
def test_delete_skill(create_skill):

    response = client.delete("/skill/1000/")
    # data = response.data
    assert response.status_code == 204
    assert response.data == None 

@pytest.mark.django_db
def test_delete_non_existant_skill(create_skill):

    client.delete("/skill/1000/")
    response = client.delete("/skill/1000/")
    # data = response.data
    assert response.status_code == 404
    assert response.data == {
                                "detail": "Not found."
                            } 


# @pytest.mark.django_db
# def test_all(lj_factory,create_skill,course_factory):
#     skill = create_skill
#     course = course_factory.create(Skills=(skill,))
#     #client.post('/skill_to_job_role/1000/20/')
#     lj_factory.create(Course_Registered = (course,))
#     print(list(Requirements.objects.all().values('Course_Registered')))
#     assert True
