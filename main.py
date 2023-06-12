# Stable Marriage Problem with Gale-Shapley Algorithm
def stable_marriage(students, colleges, slots_per_college):
    students = {student: preferences for student, preferences in students.items()}  # Convertit la liste d'étudiants en dictionnaire
    colleges = {college: preferences for college, preferences in colleges.items()}  # Convertit la liste de collèges en dictionnaire
    student_engaged = {}  # Dictionnaire pour stocker les engagements des étudiants
    college_slots = {college: slots_per_college for college in colleges}  # Dictionnaire pour stocker les places disponibles par collège
    unmatched_students = {}  # Dictionnaire pour stocker les étudiants non appariés

    # Tant qu'il reste des étudiants et qu'il y a des places disponibles dans les collèges
    while students and any(slots > 0 for slots in college_slots.values()):
        s = next(iter(students))  # Sélectionne un étudiant
        college_list = students[s]  # Récupère les préférences de ce dernier

        for college in college_list:
            if college_slots[college] > 0:  # S'il y a des places disponibles dans le collège
                student_engaged[s] = college  # L'étudiant s'engage avec le collège
                college_slots[college] -= 1  # Réduit le nombre de places disponibles dans le collège
                del students[s]  # Supprime l'étudiant des candidats
                break

            current_partner = student_engaged.get(s)  # Récupère le partenaire actuel de l'étudiant
            if current_partner is None:
                continue

            if colleges[college].index(s) < colleges[college].index(current_partner):  # Si le collège préfère l'étudiant actuel à l'étudiant courant
                student_engaged[s] = college  # L'étudiant s'engage avec le collège
                student_engaged[current_partner] = None  # L'ancien partenaire devient célibataire
                del students[s]  # Supprime l'étudiant des candidats
                break

            del students[s][0]  # Supprime le collège actuel de la liste des préférences de l'étudiant

    for student in students:
        unmatched_students[student] = None  # Ajoute les étudiants restants dans la liste des non appariés

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

    # Affichage des appariements
    for student, college in result.items():
        print(f"{student} is matched with {college}")

    # Affichage des étudiants non appariés
    print("Unmatched Students:")
    for student in unmatched_students:
        print(student)


if __name__ == "__main__":
    main()
