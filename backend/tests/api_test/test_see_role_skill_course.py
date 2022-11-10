import pytest,json
from rest_framework.test import APIClient
from api.models import User_Role,Staff,Skill,Course,Registration,Job_Role,Requirements
from ..factories import SkillFactory,CourseFactory,StaffFactory,JobRoleFactory,UserRoleFactory,RegistrationFactory,LjFactory
from api.serializers import SkillSerializer,CourseSerializer,Job_Role_Serializer
client = APIClient()


# @pytest.mark.django_db
# def test_course(create_skill,course_factory):
#     course_factory.create(Skills=(create_skill,))
#     #print(list(Course.objects.filter(pk='TEST001').values('Skills')))
#     assert True

@pytest.mark.django_db
def test_get_job_role_skill_course(api_client,create_skill,course_factory,lj_factory,job_role_factory):
    course = course_factory.create(Skills=(create_skill,))
    job_role_factory.create(Skills=(create_skill,))

    Course.objects.create( Course_ID = "TEST002",
    Course_Name = 'work please',
    Course_Desc = "the lazy dog",
    Course_Status = "Active",
    Course_Type = "Internal",
    Course_Category = "Core")

    Skill.objects.create( Skill_ID = 1001,
    Skill_Name = 'leading the way',
    Skill_Desc = 'learn how to be a leader')

    api_client().post("/skill_to_job_role/1001/20/")
    api_client().post("/skill_to_course/1000/TEST002/")
    api_client().post("/skill_to_course/1001/TEST002/")

    response = api_client().get("/job_role/20/")

    data = response.data
    all_skills = json.loads(json.dumps(response.data['Skills']))
    print(data)
    assert all_skills[0]['Skill_ID'] == 1000
    assert all_skills[1]['Skill_ID'] == 1001

    course_id = []
    for i in all_skills[0]['courses']:
        data = i.split(',')[0]
        course_id.append(data)
    assert course_id[0] == 'TEST001'
    assert course_id[1] == 'TEST002'  

    course_id = []
    for i in all_skills[1]['courses']:
        data = i.split(',')[0]
        course_id.append(data)
    assert course_id[0] == 'TEST002'

@pytest.mark.django_db
def test_get_job_role_no_skill(api_client,create_skill,course_factory,lj_factory,create_job_role):
    course = course_factory.create(Skills=(create_skill,))

    response = api_client().get("/job_role/20/")

    data = response.data
    #all_skills = json.loads(json.dumps(response.data['Skills']))
    print(data)
    assert len(data["Skills"]) ==  0

@pytest.mark.django_db
def test_get_job_role_skill_no_course(api_client,create_skill,course_factory,lj_factory,job_role_factory):
    #course = course_factory.create(Skills=(create_skill,))
    job_role_factory.create(Skills=(create_skill,))

    response = api_client().get("/job_role/20/")

    data = response.data
    all_skills = json.loads(json.dumps(response.data['Skills']))
    print(data)
    assert len(all_skills[0]['courses']) == 0

# @pytest.mark.django_db
# def test_get_1_job_role(api_client,create_job_role):
#     response = api_client().get("/job_role/20/")

#     data = response.data

#     assert data == Job_Role_Serializer(Job_Role.objects.get(pk=20)).data
#     assert data["Skills"] ==  []
#     assert response.status_code == 200


# @pytest.mark.django_db
# def test_post_job_role_no_skill(api_client):
    
#     payload = dict(
#     Job_Role_ID=100,
#     Job_Role_Desc="a",
#     Job_Role_Name="b",
#     Dept="b",
#     Skills=[])
    
#     response = api_client().post("/job_role/", data=payload,format='json')

#     data = response.data
#     #print(data)
#     assert data["Job_Role_ID"] == 100
#     assert data[ "Job_Role_Desc"] ==  "a"
#     assert data["Job_Role_Name"] ==  "b"
#     assert data["Dept"] ==  'b'
#     assert len(data["Skills"]) ==  0
#     assert response.status_code == 200

# @pytest.mark.django_db
# def test_post_job_role_with_skill(create_skill,api_client):
    
#     payload = dict(
#     Job_Role_ID=100,
#     Job_Role_Desc="a",
#     Job_Role_Name="b",
#     Dept="b",
#     Skills=[1000])
    
#     response = api_client().post("/job_role/", data=payload,format='json')

#     data = response.data
    
#     assert data["Job_Role_ID"] == 100
#     assert data[ "Job_Role_Desc"] ==  "a"
#     assert data["Job_Role_Name"] ==  "b"
#     assert data["Dept"] ==  'b'
#     assert json.loads(json.dumps(data["Skills"])) ==  [SkillSerializer(Skill.objects.get(pk=1000)).data]
#     assert response.status_code == 200

# @pytest.mark.django_db
# def test_post_job_role_with_non_existent_skill(api_client):
    
#     payload = dict(
#     Job_Role_ID=100,
#     Job_Role_Desc="a",
#     Job_Role_Name="b",
#     Dept="b",
#     Skills=[5])
    
#     response = api_client().post("/job_role/", data=payload,format='json')

#     data = response.data
#     print(data)
#     assert response.status_code == 404

# @pytest.mark.django_db
# def test_post_job_role_with_exisitng_id(api_client,create_job_role):
    
#     payload = dict(
#     Job_Role_ID=20,
#     Job_Role_Desc="a",
#     Job_Role_Name="b",
#     Dept="b",
#     Skills=[5])
    
#     response = api_client().post("/job_role/", data=payload,format='json')

#     data = response.data
#     print(data)
#     assert response.status_code == 400
#     assert data == {'msg': 'Job ID already exists'}

# @pytest.mark.django_db
# def test_update_job_role_not_skill(create_skill,job_role_factory,api_client):
#     skill = create_skill
#     job_role_factory.create(Skills=(skill,))

#     payload = {
#         "Job_Role_Desc": "asdfsdf",
#         "Job_Role_Name": "bdsfsf",
#         "Dept": "bsdfsf"
#     }
#     response = api_client().put("/job_role/20/",data=payload,format='json')
#     data = response.data
#     assert response.status_code == 200
#     assert data["Job_Role_Desc"] == "asdfsdf"
#     assert data["Job_Role_Name"] == "bdsfsf"

# @pytest.mark.django_db
# def test_update_job_role_only_skill(create_skill,create_job_role,api_client):
#     payload = {
#         "Skills":[1000]
#     }
#     response = api_client().put("/job_role/20/",data=payload,format='json')
#     data = response.data
#     assert response.status_code == 200
#     assert data["Job_Role_ID"] == 20
#     assert json.loads(json.dumps(data["Skills"])) ==  [SkillSerializer(Skill.objects.get(pk=1000)).data]

# @pytest.mark.django_db
# def test_update_job_role_only_invalid_skill(create_skill,create_job_role,api_client):
#     payload = {
#         "Skills":[13]
#     }
#     response = api_client().put("/job_role/20/",data=payload,format='json')
#     data = response.data
#     assert response.status_code == 404
#     assert data == {
#                     "detail": "Not found."
#                     }

# @pytest.mark.django_db
# def test_delete_job_role(api_client,create_job_role):

#     response = api_client().delete("/job_role/20/")
#     # data = response.data
#     assert response.status_code == 204
#     assert response.data == None 

# @pytest.mark.django_db
# def test_delete_non_existent_job_role(api_client):

#     response = api_client().delete("/job_role/20/")
#     # data = response.data
#     assert response.status_code == 404
#     assert response.data == {
#                                 "detail": "Not found."
#                             }

