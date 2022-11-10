import pytest,json
from rest_framework.test import APIClient
from api.models import User_Role,Staff,Skill,Course,Registration,Job_Role,Requirements
from ..factories import SkillFactory,CourseFactory,StaffFactory,JobRoleFactory,UserRoleFactory,RegistrationFactory,LjFactory
from api.serializers import SkillSerializer,CourseSerializer,Job_Role_Serializer,Requirements_Serializer
client = APIClient()


@pytest.mark.django_db
def test_get_all_lj(api_client,lj_factory,create_skill,course_factory):

    course = course_factory.create(Skills=(create_skill,))
    lj_factory.create(Course_Registered = (course,))

    response = api_client().get("/req/",format='json')
    data = response.data
    assert response.status_code == 200
    assert data == Requirements_Serializer(Requirements.objects.all(),many=True).data
    assert response.json()[0]["Course_Registered"] == [course.Course_ID]

@pytest.mark.django_db
def test_get_all_lj_1_staff(api_client,lj_factory,create_skill,course_factory):

    course = course_factory.create(Skills=(create_skill,))
    lj_factory.create(Course_Registered = (course,))

    response = api_client().get("/req/1/",format='json')
    data = response.data
    assert response.status_code == 200
    assert data == Requirements_Serializer(Requirements.objects.filter(Staff_id = 1),many=True).data
    assert response.json()[0]["Course_Registered"] == [course.Course_ID]   

@pytest.mark.django_db
def test_post_lj_with_course(api_client,create_job_role,create_staff,create_course):

    payload = {
                "Course_Registered": [
                    "TEST001"
                ]
            }
    response = api_client().post(f"/req/{create_staff.Staff_ID}/{create_job_role.Job_Role_ID}/",data=payload,format='json')
    data = response.data
    assert response.status_code == 200
    assert data == json.loads(json.dumps(Requirements_Serializer(Requirements.objects.filter(Staff_id = 1),many=True).data))[0]
    assert data["Course_Registered"] == ["TEST001"]

@pytest.mark.django_db
def test_update_lj_with_course(api_client,create_course,lj_factory):
    lj_factory.create(Course_Registered = (create_course,))
    Course.objects.create( Course_ID = "TEST002",
    Course_Name = 'work please',
    Course_Desc = "the lazy dog",
    Course_Status = "Active",
    Course_Type = "Internal",
    Course_Category = "Core")

    print(Course.objects.get(pk="TEST002"))
    payload = {
                "Course_Registered": [
                    "TEST001",
                    "TEST002"
                ]
            }
    response = api_client().put(f"/req/1/20/",data=payload,format='json')
    data = response.data
    print(data)
    assert response.status_code == 200
    assert data == json.loads(json.dumps(Requirements_Serializer(Requirements.objects.filter(Staff_id = 1),many=True).data))[0]
    assert data["Course_Registered"] == ["TEST001","TEST002"]
    assert data['Job_Role']['Job_Role_ID'] == 20

@pytest.mark.django_db
def test_delete_lj(api_client,create_course,lj_factory):
    lj_factory.create(Course_Registered = (create_course,))
    response = api_client().delete(f"/req/1/20/")
    data = response.data
    print(data)
    assert response.status_code == 200

############################################################################################################################
######################################Negative Test Cases###################################################################

@pytest.mark.django_db
def test_get_all_lj_missing_staff(api_client,lj_factory,create_skill,course_factory):

    course = course_factory.create(Skills=(create_skill,))
    lj_factory.create(Course_Registered = (course,))

    response = api_client().get("/req/2/",format='json')
    data = response.data
    assert response.status_code == 404
    assert response.data == {
                                "detail": "Not found."
                            }


# @pytest.mark.django_db
# def test_get_all_lj_missing_course(api_client,lj_factory,create_skill,course_factory):

#     course = course_factory.create(Skills=(create_skill,))
#     lj_factory.create(Course_Registered = (course,))

#     api_client().delete('/course/TEST001/')
#     response = api_client().get("/req/1/",format='json')
#     data = response.data
#     assert response.status_code == 404
#     assert response.data == {
#                                 "detail": "Not found."
#                             }

@pytest.mark.django_db
def test_post_lj_with_missing_course(api_client,create_job_role,create_staff):

    payload = {
                "Course_Registered": [
                    "TEST001"
                ]
            }
    response = api_client().post(f"/req/1/20/",data=payload,format='json')
    data = response.data
    assert response.status_code == 404
    assert response.data == {
                                "detail": "Not found."
                            }

@pytest.mark.django_db
def test_post_lj_with_missing_staff(api_client,create_job_role,create_course):

    payload = {
                "Course_Registered": [
                    "TEST001"
                ]
            }
    response = api_client().post("/req/1/20/",data=payload,format='json')
    data = response.data
    assert response.status_code == 404
    assert response.data == {
                                "detail": "Not found."
                            }

@pytest.mark.django_db
def test_post_lj_with_missing_job_role(api_client,create_staff,create_course):

    payload = {
                "Course_Registered": [
                    "TEST001"
                ]
            }
    response = api_client().post("/req/1/21/",data=payload,format='json')
    data = response.data
    assert response.status_code == 404
    assert response.data == {
                                "detail": "Not found."
                            }

@pytest.mark.django_db
def test_update_lj_with_missing_course(api_client,create_course,lj_factory):
    lj_factory.create(Course_Registered = (create_course,))
    Course.objects.create( Course_ID = "TEST002",
    Course_Name = 'work please',
    Course_Desc = "the lazy dog",
    Course_Status = "Active",
    Course_Type = "Internal",
    Course_Category = "Core")

    print(Course.objects.get(pk="TEST002"))
    payload = {
                "Course_Registered": [
                    "TEST001",
                    "TEST003"
                ]
            }
    response = api_client().put(f"/req/1/20/",data=payload,format='json')
    data = response.data
    assert response.status_code == 404
    assert response.data == {
                                "detail": "Not found."
                            }

@pytest.mark.django_db
def test_update_lj_with_invalid_staff(api_client,create_course,lj_factory):
    lj_factory.create(Course_Registered = (create_course,))
    Course.objects.create( Course_ID = "TEST002",
    Course_Name = 'work please',
    Course_Desc = "the lazy dog",
    Course_Status = "Active",
    Course_Type = "Internal",
    Course_Category = "Core")

    print(Course.objects.get(pk="TEST002"))
    payload = {
                "Course_Registered": [
                    "TEST001",
                    "TEST003"
                ]
            }
    response = api_client().put(f"/req/2/20/",data=payload,format='json')
    data = response.data
    assert response.status_code == 404
    assert response.data == {
                                "detail": "Not found."
                            }

@pytest.mark.django_db
def test_update_lj_with_invalid_job_role(api_client,create_course,lj_factory):
    lj_factory.create(Course_Registered = (create_course,))
    Course.objects.create( Course_ID = "TEST002",
    Course_Name = 'work please',
    Course_Desc = "the lazy dog",
    Course_Status = "Active",
    Course_Type = "Internal",
    Course_Category = "Core")

    print(Course.objects.get(pk="TEST002"))
    payload = {
                "Course_Registered": [
                    "TEST001",
                    "TEST003"
                ]
            }
    api_client().delete('/job_role/20/')
    response = api_client().put(f"/req/1/20/",data=payload,format='json')
    data = response.data
    assert response.status_code == 404
    assert response.data == {
                                "detail": "Not found."
                            }

@pytest.mark.django_db
def test_delete_lj_missing_staff(api_client,create_course,lj_factory):
    lj_factory.create(Course_Registered = (create_course,))
    response = api_client().delete(f"/req/2/20/")
    data = response.data
    assert response.status_code == 404
    assert response.data == {
                                "detail": "Not found."
                            }

@pytest.mark.django_db
def test_delete_lj_missing_job_role(api_client,create_course,lj_factory):
    lj_factory.create(Course_Registered = (create_course,))
    response = api_client().delete(f"/req/1/21/")
    data = response.data
    assert response.status_code == 404
    assert response.data == {
                                "detail": "Not found."
                            }

