import pandas as pd
import sqlite3
conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()

role = pd.read_csv('backend\\backend\\RawData\\role.csv',error_bad_lines=False)
print(role)

course = pd.read_csv('backend\\backend\\RawData\\courses.csv',encoding ='unicode_escape')
print(course)

reg = pd.read_csv('backend\\backend\\RawData\\registration.csv',error_bad_lines=False)
print(reg)

staff = pd.read_csv('backend\\backend\\RawData\\staff.csv',error_bad_lines=False)
print(staff)


role.to_sql('roles', conn, if_exists='replace', index = False)

