student_list = [
    {"name": "Bhumika", "subjects": {"PP": 90, "DBMS": 30, "Maths": 56}},
    {"name": "Vikram", "subjects": {"PP": 80, "DBMS": 70, "Maths": 60}},
    {"name": "Riya", "subjects": {"PP": 95, "DBMS": 85, "Maths": 75}}
]

def get_subject_wise_average(student_list):
    max_average = 0
    topper_name = ""
    for student in student_list:
        total_marks = sum(student["subjects"].values())
        average = total_marks / len(student["subjects"])
        if average > max_average:
            max_average = average
            topper_name = student["name"]
    return topper_name, max_average


def get_topper_list(student_list):
    topper_name, highest_average_marks = get_subject_wise_average(student_list)
    for student in student_list:
        print(f"{student['name']}: {student['subjects']}")
    print(f"\nTopper Name: {topper_name}")
    print(f"Topper's Highest Average Marks: {highest_average_marks}")


get_topper_list(student_list)
