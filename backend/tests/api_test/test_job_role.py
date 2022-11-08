import pytest
from rest_framework.test import APIClient
from api.models import User_Role,Staff,Skill,Course,Registration,Job_Role,Requirements
from ..factories import SkillFactory,CourseFactory,StaffFactory,JobRoleFactory,UserRoleFactory,RegistrationFactory,LjFactory
client = APIClient()


# @pytest.mark.django_db
# def test_course(create_skill,course_factory):
#     course_factory.create(Skills=(create_skill,))
#     #print(list(Course.objects.filter(pk='TEST001').values('Skills')))
#     assert True

@pytest.mark.django_db
def test_get_all_job_roles(create_job_role):
    response = client.get("/job_role/")

    data = response.data

    assert len(data) == Job_Role.objects.count()
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_1_job_role(create_job_role):
    response = client.get("/job_role/20/")

    data = response.data

    assert data["Job_Role_ID"] == 20
    assert data["Skills"] ==  []
    assert response.status_code == 200


@pytest.mark.django_db
def test_post_job_role_no_skill(api_client):
    
    payload = dict(
    Job_Role_ID=100,
    Job_Role_Desc="a",
    Job_Role_Name="b",
    Dept="b",
    Skills=[])
    
    response = api_client().post("/job_role/", data=payload,format='json')

    data = response.data
    #print(data)
    assert data["Job_Role_ID"] == 100
    assert data[ "Job_Role_Desc"] ==  "a"
    assert data["Job_Role_Name"] ==  "b"
    assert data["Dept"] ==  'b'
    assert len(data["Skills"]) ==  0
    assert response.status_code == 200

@pytest.mark.django_db
def test_post_job_role_with_skill(create_skill,api_client):
    
    payload = dict(
    Job_Role_ID=100,
    Job_Role_Desc="a",
    Job_Role_Name="b",
    Dept="b",
    Skills=[1000])
    
    response = api_client().post("/job_role/", data=payload,format='json')

    data = response.data
    print(Skill.objects.all())
    print(data)
    assert data["Job_Role_ID"] == 100
    assert data[ "Job_Role_Desc"] ==  "a"
    assert data["Job_Role_Name"] ==  "b"
    assert data["Dept"] ==  'b'
    assert len(data["Skills"]) ==  1
    assert response.status_code == 200

@pytest.mark.django_db
def test_post_job_role_with_non_existent_skill(api_client):
    
    payload = dict(
    Job_Role_ID=100,
    Job_Role_Desc="a",
    Job_Role_Name="b",
    Dept="b",
    Skills=[5])
    
    response = api_client().post("/job_role/", data=payload,format='json')

    data = response.data
    print(data)
    assert response.status_code == 404

@pytest.mark.django_db
def test_post_job_role_with_exisitng_id(api_client,create_job_role):
    
    payload = dict(
    Job_Role_ID=20,
    Job_Role_Desc="a",
    Job_Role_Name="b",
    Dept="b",
    Skills=[5])
    
    response = api_client().post("/job_role/", data=payload,format='json')

    data = response.data
    print(data)
    assert response.status_code == 400
    assert data == {'msg': 'Job ID already exists'}

@pytest.mark.django_db
def test_update_job_role_not_skill(create_skill,job_role_factory,api_client):
    skill = create_skill
    job_role_factory.create(Skills=(skill,))

    payload = {
        "Job_Role_Desc": "asdfsdf",
        "Job_Role_Name": "bdsfsf",
        "Dept": "bsdfsf"
    }
    response = api_client().put("/job_role/20/",data=payload,format='json')
    data = response.data
    assert response.status_code == 200
    assert data["Job_Role_Desc"] == "asdfsdf"
    assert data["Job_Role_Name"] == "bdsfsf"

@pytest.mark.django_db
def test_update_job_role_only_skill(create_skill,create_job_role,api_client):
    payload = {
        "Skills":[1000]
    }
    response = api_client().put("/job_role/20/",data=payload,format='json')
    data = response.data
    assert response.status_code == 200
    assert data["Job_Role_ID"] == 20
    assert len(data['Skills']) == 1

# @pytest.mark.django_db
# def test_delete_skill(create_skill):

#     response = client.delete("/skill/1000/")
#     # data = response.data
#     assert response.status_code == 204
#     assert response.data == None 

# @pytest.mark.django_db
# def test_delete_non_existent_skill(create_skill):

#     client.delete("/skill/1000/")
#     response = client.delete("/skill/1000/")
#     # data = response.data
#     assert response.status_code == 404
#     assert response.data == {
#                                 "detail": "Not found."
#                             }

