import pandas as pd
import sqlite3

conn = sqlite3.connect('../db.sqlite3')
c = conn.cursor()

role = pd.read_csv('role.csv',error_bad_lines=False)
print(role)

course = pd.read_csv('courses.csv',encoding ='unicode_escape')
print(course)

reg = pd.read_csv('registration.csv',error_bad_lines=False)
print(reg)

staff = pd.read_csv('staff.csv',error_bad_lines=False)
print(staff)



role.to_sql('api_user_role', conn, if_exists='replace', index = False)
reg.to_sql('api_registration', conn, if_exists='replace', index = False)
staff.to_sql('api_staff', conn, if_exists='replace', index = False)
course.to_sql('api_course', conn, if_exists='replace', index = False)