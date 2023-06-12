# Authors : Eliot Colomb & Pierre Teodoresco

# Gale-Shapley algorithm implementation for the stable marriage problem between students and schools
def gale_shapley(students_preferences, schools_preferences, school_seats):
    # Initialize variables
    proposals = {student: iter(preferences) for student, preferences in students_preferences.items()}
    school_queues = {school: [] for school in schools_preferences.keys()}
    free_students = set(students_preferences.keys())
    rounds = 0

    # Run the algorithm until there are no more free students
    while free_students:
        rounds += 1
        for student in free_students.copy():
            try:
                school = next(proposals[student])
            except StopIteration:
                # Student has exhausted all school preferences
                free_students.remove(student)
                continue
            school_queues[school].append(student)
            school_queues[school].sort(key=lambda x: schools_preferences[school].index(x))

        # Process school queues
        for school, queue in school_queues.items():
            while len(queue) > school_seats[school]:
                rejected_student = queue.pop()
                free_students.add(rejected_student)

        # Update free students
        for school, queue in school_queues.items():
            for student in queue:
                if student in free_students:
                    free_students.remove(student)

    # Create the final matchings
    matchings = {school: queue for school, queue in school_queues.items() if queue}

    # Create the list of students without a school
    students_without_school = [student for student in students_preferences.keys() if student not in sum(matchings.values(), [])]

    return matchings, rounds, students_without_school
