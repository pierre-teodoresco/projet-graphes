# Authors : Eliot Colomb & Pierre Teodoresco

# Gale-Shapley algorithm implementation for the stable marriage problem between students and schools
def gale_shapley(students_preferences, schools_preferences, school_seats):
    # Initialize variables
    proposals = {}
    for (student, preferences) in students_preferences.items():
        proposals[student] = iter(preferences)

    school_queues = {}
    for school in schools_preferences.keys():
        school_queues[school] = []
    
    # Set of free students filled with all students names
    free_students = set(students_preferences.keys())
    rounds = 0

    # Run the algorithm until there are no more free students
    while free_students:
        rounds += 1
        # Process free students and add them to the school queues
        for student in free_students.copy():
            # Get the next school in the student's preferences
            try:
                school = next(proposals[student])
            except StopIteration:
                # Student has exhausted all school preferences
                free_students.remove(student)
                continue
            school_queues[school].append(student)
            # Sort the school queue by the school's preferences
            school_queues[school].sort(key=lambda x: schools_preferences[school].index(x))

        # Process school queues
        for school, queue in school_queues.items():
            # Remove students from the queue until the school is full
            while len(queue) > school_seats[school]:
                rejected_student = queue.pop()
                free_students.add(rejected_student)

        # Update free students
        for school, queue in school_queues.items():
            for student in queue:
                if student in free_students:
                    free_students.remove(student)

    # Create the final matchings
    matchings = {}
    for (school, queue) in school_queues.items():
        if queue:
            matchings[school] = queue

    # Create the list of students without a school
    students_without_school = []
    for student in students_preferences.keys():
        # if student is not matched to any school (not in the queue of any school)
        if not any(student in values for values in matchings.values()):
            students_without_school.append(student)

    return matchings, rounds, students_without_school
