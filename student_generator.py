# your code goes here

import random

students_names = ["ROSIE MARIE MARTINEZ", "JOE NATALIIA LIU", "SALLY SUE", "BOB JOHNSON", "DELIA AGHO"]
student_names = []
students_ids = []
email_list = []
student_data = []

for student in students_names:
    student_data.append(dict([("name", student)]))


# creates random IDs and checks for duplicates
i = 0
while i < len(students_names):
    temp = random.randint(111111, 999999)
    # temp = random.randint(1, 9)
    if temp not in students_ids:
        students_ids.append(temp)
        i += 1


# generates e-mails
for i in range(0, len(students_names)):
    if len(students_names[i].split()) > 2:
        email_list.append(f"{students_names[i].split()[0][0]}{students_names[i].split()[1][0]}{(students_names[i].split()[-1]).upper()}{str(students_ids[i])[3:]}@example.org")
    else:
        email_list.append(f"{students_names[i].split()[0][0]}{(students_names[i].split()[-1]).upper()}{str(students_ids[i])[3:]}@example.org")


for i in range(len(student_data)):
    student_data[i]["ID"] = students_ids[i]
    student_data[i]["e-mail"] = email_list[i]

print(student_data)

print("-------------------------------")
print(students_names)
print(students_ids)
print("-------------------------------")

for i in range(len(student_data)):
    print(f"name:   {student_data[i]['name']}")
    print(f"id:     {student_data[i]['ID']}")
    print(f"e-mail: {student_data[i]['e-mail']}")
    print("-------------------------------")

