import pandas as pd
import sqlite3

conn = sqlite3.connect('../db.sqlite3')
c = conn.cursor()

role = pd.read_csv('role.csv',error_bad_lines=False)
role.columns = ['User_Role_ID','User_Role_Name']
print(role)
role.to_sql('api_user_role', conn, if_exists='append', index = False)

course = pd.read_csv('courses.csv',encoding ='unicode_escape')
print(course)
course.to_sql('api_course', conn, if_exists='append', index = False)

reg = pd.read_csv('registration.csv',error_bad_lines=False)
print(reg)
reg.to_sql('api_registration', conn, if_exists='append', index = False)

staff = pd.read_csv('staff.csv',error_bad_lines=False)
staff.rename(columns = {'Role':'User_Role_id'}, inplace=True)
print(staff)
staff.to_sql('api_staff', conn, if_exists='append', index = False)

skill = pd.read_json('skills.json')
skill.columns = ['Skill_ID','Skill_Name','Skill_Desc']
print(skill)
skill.to_sql('api_skill', conn, if_exists='append', index = False)


