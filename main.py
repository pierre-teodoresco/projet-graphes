# Description: This file contains the implementation of the Stable Marriage Problem
# Authors: Eliot Colomb & Pierre Teodoresco

# Stable Marriage Problem
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


# Example usage
def main():
    students = {
        'John': ['Stanford', 'Harvard', 'MIT'],
        'Emily': ['MIT', 'Harvard', 'Stanford'],
        'Michael': ['Stanford', 'MIT', 'Harvard'],
        'Sophia': ['MIT', 'Stanford', 'Harvard'],
        'David': ['MIT', 'Stanford', 'Harvard'],
        'Olivia': ['Stanford', 'Harvard', 'MIT'],
        'James': ['Stanford', 'MIT', 'Harvard'],
        'Emma': ['MIT', 'Stanford', 'Harvard'],
        'Daniel': ['Stanford', 'MIT', 'Harvard'],
        'Grace': ['MIT', 'Stanford', 'Harvard'],
    }

    colleges = {
        'MIT': ['John', 'Emily', 'Michael', 'Sophia', 'David', 'Olivia', 'James', 'Emma', 'Daniel', 'Grace'],
        'Stanford': ['John', 'Emily', 'Michael', 'Sophia', 'David', 'Olivia', 'James', 'Emma', 'Daniel', 'Grace'],
        'Harvard': ['John', 'Emily', 'Michael', 'Sophia', 'David', 'Olivia', 'James', 'Emma', 'Daniel', 'Grace'],
    }

    slots_per_college = 3  # Number of slots per college

    result, unmatched_students = stable_marriage(students, colleges, slots_per_college)
    for student, college in result.items():
        print(f"{student} is matched with {college}")

    print("Unmatched Students:")
    for student in unmatched_students:
        print(student)


if __name__ == "__main__":
    main()
