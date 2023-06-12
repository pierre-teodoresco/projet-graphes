from gale_shapley import gale_shapley

import json

def main():
    # Charger les données du fichier JSON
    with open('tests/test_1.json') as file:
        data = json.load(file)

    # Appeler la fonction gale_shapley avec les données du fichier JSON
    matchings, rounds, students_without_school = gale_shapley(
        data['students_preferences'],
        data['schools_preferences'],
        data['school_seats']
    )

    # Afficher les résultats
    print("Matchings:")
    for school, students in matchings.items():
        print(f"{school}: {students}")
    print(f"Number of rounds: {rounds}")
    print("Students without a school:")
    print(students_without_school)

if __name__ == '__main__':
    main()