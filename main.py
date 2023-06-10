# Description: This file contains the implementation of the Stable Marriage Problem
# Authors: Eliot Colomb & Pierre Teodoresco

import random


# Stable Marriage Problem with Gale-Shapley Algorithm
def stable_marriage(students_prefs, colleges_prefs, slots_per_college):
    students_prefs = {student: preferences for student, preferences in students_prefs.items()}
    colleges_prefs = {college: preferences for college, preferences in colleges_prefs.items()}
    student_engaged = {}
    college_slots = {college: slots_per_college for college in colleges_prefs}
    unmatched_students = {}

    while students_prefs and any(slots > 0 for slots in college_slots.values()):
        s = next(iter(students_prefs))
        college_list = students_prefs[s]

        for college in college_list:
            if college_slots[college] > 0:
                student_engaged[s] = college
                college_slots[college] -= 1
                del students_prefs[s]
                break

            current_partner = student_engaged.get(s)
            if current_partner is None:
                continue

            if colleges_prefs[college].index(s) < colleges_prefs[college].index(current_partner):
                student_engaged[s] = college
                student_engaged[current_partner] = None
                del students_prefs[s]
                break

            del students_prefs[s][0]

    for student in students_prefs:
        unmatched_students[student] = None

    return student_engaged, unmatched_students


def generate_random_data(num_students, num_colleges, slots_per_college):
    students = {}
    colleges = {}
    college_slots = {}

    for i in range(num_students):
        student_name = f"Student{i + 1}"
        student_prefs = random.sample(range(1, num_colleges + 1), num_colleges)
        students[student_name] = student_prefs

    for i in range(num_colleges):
        college_name = i + 1
        college_prefs = random.sample(range(1, num_students + 1), num_students)
        colleges[college_name] = college_prefs
        college_slots[college_name] = slots_per_college

    return students, colleges


# Example usage
def main():
    num_students = 10
    num_colleges = 4
    slots_per_college = 2

    students, colleges = generate_random_data(num_students, num_colleges, slots_per_college)

    result, unmatched_students = stable_marriage(students, colleges, slots_per_college)
    for student, college in result.items():
        print(f"{student} is matched with {college}")

    print("Unmatched Students:")
    for student in unmatched_students:
        print(student)


if __name__ == "__main__":
    main()
