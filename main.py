# Description: This file contains the implementation of the Stable Marriage Problem
# Authors: Eliot Colomb & Pierre Teodoresco

# Stable Marriage Problem with Gale-Shapley Algorithm
def stable_marriage(students, colleges, slots_per_college):
    students = {student: preferences for student, preferences in students.items()}
    colleges = {college: preferences for college, preferences in colleges.items()}
    student_engaged = {}
    college_slots = {college: slots_per_college for college in colleges}
    unmatched_students = {}

    while students and any(slots > 0 for slots in college_slots.values()):
        s = next(iter(students))
        college_list = students[s]

        for college in college_list:
            if college_slots[college] > 0:
                student_engaged[s] = college
                college_slots[college] -= 1
                del students[s]
                break

            current_partner = student_engaged.get(s)
            if current_partner is None:
                continue

            if colleges[college].index(s) < colleges[college].index(current_partner):
                student_engaged[s] = college
                student_engaged[current_partner] = None
                del students[s]
                break

            del students[s][0]

    for student in students:
        unmatched_students[student] = None

    return student_engaged, unmatched_students

# Example usage
def main():
    students = {
        'Emily': ['Harvard', 'MIT', 'Stanford'],
        'Marc': ['Harvard', 'Stanford', 'MIT'],
        'John': ['Stanford', 'Harvard', 'MIT'],
        'Kylian': ['Stanford', 'MIT', 'Harvard']
    }

    colleges = {
        'Harvard': ['Emily', 'Marc', 'John', 'Kylian'],
        'Stanford': ['Emily', 'Marc', 'John', 'Kylian'],
        'MIT': ['Emily', 'Marc', 'John', 'Kylian']
    }

    slots_per_college = 1

    result, unmatched_students = stable_marriage(students, colleges, slots_per_college)
    for student, college in result.items():
        print(f"{student} is matched with {college}")

    print("Unmatched Students:")
    for student in unmatched_students:
        print(student)


if __name__ == "__main__":
    main()
