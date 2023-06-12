# Authors: Eliot Colomb & Pierre Teodoresco

import json

# Stable Marriage Problem with Gale-Shapley Algorithm
def stable_marriage(students, colleges, slots_per_college):
    students = {student: preferences for student, preferences in students.items()}  # Convertit la liste d'étudiants en dictionnaire
    colleges = {college: preferences for college, preferences in colleges.items()}  # Convertit la liste de collèges en dictionnaire
    student_engaged = {}  # Dictionnaire pour stocker les engagements des étudiants
    college_slots = slots_per_college.copy()  # Dictionnaire pour stocker les places disponibles par collège
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

def read_students_from_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    students = {}
    for item in data:
        name = item['name']
        preferences = item['preferences']
        students[name] = preferences
    return students

def read_colleges_from_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    colleges = {}
    slots_per_college = {}
    for item in data:
        name = item['name']
        preferences = item['preferences']
        slots = item['slots']
        colleges[name] = preferences
        slots_per_college[name] = slots
    return colleges, slots_per_college

# Example usage
def main():
    students = read_students_from_json('students.json')
    colleges, slots_per_college = read_colleges_from_json('colleges.json')

    result, unmatched_students = stable_marriage(students, colleges, slots_per_college)
    for student, college in result.items():
        print(f"{student} is matched with {college}")

    print("Unmatched Students:")
    for student in unmatched_students:
        print(student)


if __name__ == "__main__":
    main()
