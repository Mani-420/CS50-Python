# with open("student.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         print(f"{row[0]} lives in {row[1]}")


# --------------------------------------------------------------


# with open("student.csv") as file:
#     for line in file:
#         name, place = line.rstrip().split(",")
#         print(f"{name} lives in {place}")


# --------------------------------------------------------------


# students = []

# with open("student.csv") as file:
#     for line in file:
#         name, place = line.rstrip().split(",")
#         students.append(f"{name} lives in {place}")

# for student in sorted(students):
#     print(f"{student}")


# --------------------------------------------------------------


# students = []

# with open("student.csv") as file:
#     for line in file:
#         name, place = line.rstrip().split(",")
#         # student = {}
#         # student["name"] = name
#         # student["place"] = place
#         student = {"name": name, "place": place}
#         students.append(student)

# for student in students:
#     print(f"{student['name']} is in {student['place']}.")


# --------------------------------------------------------------


students = []

with open("student.csv") as file:
    for line in file:
        name, place = line.rstrip().split(",")
        student = {"name": name, "place": place}
        students.append(student)


def get_name(student):
    return student["name"]


for student in sorted(students, key=get_name, reverse=True):
    print(f"{student['name']} is in {student['place']}.")