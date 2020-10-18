# dictionaries

import random

students_names = ["ROSIE MARTINEZ", "JOE LIU", "SALLY SUE", "BOB JOHNSON", "DELIA AGHO"]
student_names = []
students_ids = []
email_list = []


# # promps the user for 5 names
# for i in range(5):
#   students_names[i]=input(f"Enter {i+1} student's name: ")

# creates random IDs and checks for duplicates
i = 0
while i < len(students_names):
    temp = random.randint(111111, 999999)
    # temp = random.randint(1, 9)
    if temp not in students_ids:
        students_ids.append(temp)
        i += 1
    # else:
    #   print(f'{temp} is duplicate')

# # students_ids = [random.randint(111111, 999999) for i in range (0, len(students_names))]

for i in range(0, len(students_names)):
    if len(students_names[i].split()) > 2:
        email_list.append(
            f"{students_names[i].split()[0][0]}{students_names[i].split()[1][0]}{(students_names[i].split()[-1]).upper()}{str(students_ids[i])[3:]}@example.org")
    else:
        email_list.append(
            f"{students_names[i].split()[0][0]}{(students_names[i].split()[-1]).upper()}{str(students_ids[i])[3:]}@example.org")

# email_list = [f"{students_names[i].split()[0][0]}{students_names[i].split()[1][0]}{(students_names[i].split()[-1]).upper()}{str(students_ids[i])[3:]}@example.org"
#               for i in range (0, len(students_names))]

print("-------------------------------")
print(students_names)
print(students_ids)
print("-------------------------------")

for i in range(0, len(students_names)):
    print(f"name:   {students_names[i]}")
    print(f"id:     {students_ids[i]}")
    print(f"e-mail: {email_list[i]}")
    print("-------------------------------")

