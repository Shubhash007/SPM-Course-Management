import pytest,json
from api.models import User_Role,Staff,Skill,Course,Registration,Job_Role,Requirements
from ..factories import SkillFactory,CourseFactory,StaffFactory,JobRoleFactory,UserRoleFactory,RegistrationFactory,LjFactory
from api.serializers import SkillSerializer,CourseSerializer
# @pytest.mark.django_db
# def test_course(create_skill,course_factory):
#     course_factory.create(Skills=(create_skill,))
#     #print(list(Course.objects.filter(pk='TEST001').values('Skills')))
#     assert True

@pytest.mark.django_db
def test_get_all_courses_for_1_skill(api_client,create_skill,course_factory):
    course_factory.create(Skills=(create_skill,))

    response = api_client().get("/skill_to_course/1000/")

    data = response.data
    #print(json.dumps(data))
    assert data == CourseSerializer(Course.objects.filter(pk='TEST001'),many=True).data
    assert response.status_code == 200

@pytest.mark.django_db
def test_post_assign_1_skill_1_course(api_client,create_skill,create_course):

    response = api_client().post("/skill_to_course/1000/TEST001/")

    data = response.data
    #print(json.dumps(data))
    assert data == {
        "msg": "course:TEST001 assigned to skill:1000"
    }
    assert response.status_code == 201

@pytest.mark.django_db
def test_delete_1_skill_from_1_course(api_client,create_skill,course_factory):
    course_factory.create(Skills=(create_skill,))

    response = api_client().delete("/skill_to_course/1000/TEST001/")

    data = response.data
    #print(json.dumps(data))
    assert data == {'msg': f"skill:1000 assignment to course:TEST001 has been removed"}
    assert response.status_code == 200


##########################################################################################################
@pytest.mark.django_db
def test_get_all_courses_for_1_missing_skill(api_client,):

    response = api_client().get("/skill_to_course/1000/")

    data = response.data
    #print(json.dumps(data))
    assert data == {
    "detail": "Not found."
    }
    assert response.status_code == 404

@pytest.mark.django_db
def test_post_assign_missing_skill_1_course(api_client,create_course):

    response = api_client().post("/skill_to_course/1000/TEST001/")

    data = response.data
    #print(json.dumps(data))
    assert data == {
    "detail": "Not found."
    }
    assert response.status_code == 404


@pytest.mark.django_db
def test_post_assign_1_skill_missing_course(api_client,create_skill):

    response = api_client().post("/skill_to_course/1000/TEST001/")

    data = response.data
    #print(json.dumps(data))
    assert data == {
    "detail": "Not found."
    }
    assert response.status_code == 404

@pytest.mark.django_db
def test_delete_missing_skill_from_1_course(api_client,create_course):

    response = api_client().delete("/skill_to_course/1000/TEST001/")

    data = response.data
    #print(json.dumps(data))
    assert data == {
    "detail": "Not found."
    }
    assert response.status_code == 404

@pytest.mark.django_db
def test_delete_1_skill_from_missing_course(api_client,create_skill,):

    response = api_client().delete("/skill_to_course/1000/TEST001/")

    data = response.data
    #print(json.dumps(data))
    assert data == {
    "detail": "Not found."
    }
    assert response.status_code == 404

################################################################################
############################JOB ROLE ASSIGN SKILL###############################

@pytest.mark.django_db
def test_post_assign_1_skill_1_job_role(api_client,create_job_role,create_skill):

    response = api_client().post("/skill_to_job_role/1000/20/")

    data = response.data
    print(json.dumps(data))
    assert data == {
        "msg": f"skill:{create_skill.Skill_Name} assigned to Job Role:{create_job_role.Job_Role_Name}"
    }
    assert response.status_code == 201

@pytest.mark.django_db
def test_delete_1_skill_from_1_job_role(api_client,create_skill,job_role_factory):
    job_role_factory.create(Skills=(create_skill,))

    response = api_client().delete("/skill_to_job_role/1000/20/")

    data = response.data
    #print(json.dumps(data))
    assert data == {'msg': f"skill:{create_skill.Skill_ID} assignment to Job Role:{Job_Role.objects.get(pk=20).Job_Role_ID} has been removed"}
    assert response.status_code == 200

################################################################################################################################
@pytest.mark.django_db
def test_post_assign_1_skill_missing_job_role(api_client,create_skill):

    response = api_client().post("/skill_to_job_role/1000/20/")

    data = response.data
    #print(json.dumps(data))
    assert data == {
    "detail": "Not found."
    }
    assert response.status_code == 404

@pytest.mark.django_db
def test_post_assign_missing_skill_1_job_role(api_client,create_job_role):

    response = api_client().post("/skill_to_job_role/1000/20/")

    data = response.data
    #print(json.dumps(data))
    assert data == {
    "detail": "Not found."
    }
    assert response.status_code == 404

@pytest.mark.django_db
def test_delete_1_skill_from_missing_job_role(api_client,create_skill):

    response = api_client().delete("/skill_to_job_role/1000/20/")

    data = response.data
    #print(json.dumps(data))
    assert data == {
    "detail": "Not found."
    }
    assert response.status_code == 404

@pytest.mark.django_db
def test_delete_missing_skill_from_1_job_role(api_client,create_job_role):

    response = api_client().delete("/skill_to_job_role/1000/20/")

    data = response.data
    #print(json.dumps(data))
    assert data == {
    "detail": "Not found."
    }
    assert response.status_code == 404

