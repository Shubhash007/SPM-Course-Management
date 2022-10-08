import json
import sqlite3

connection = sqlite3.connect('../db.sqlite3')
cursor = connection.cursor()

traffic = json.load(open('skills.json'))
columns = ['No','Skill','Desc']
for row in traffic:
    keys= tuple(row[c] for c in columns)
    cursor.execute('insert into api_skill values(?,?,?)',keys)
    print(f'{row["Skill"]} data inserted')

connection.commit()
connection.close()