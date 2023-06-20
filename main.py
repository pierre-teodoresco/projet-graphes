import argparse
from gale_shapley import gale_shapley
import json

def main(json_file, studentBiding):
    # Convertir la valeur de l'argument en booléen
    studentBiding = studentBiding.lower() == 'true'

    # Charger les données du fichier JSON
    with open(json_file) as file:
        data = json.load(file)

    # Appeler la fonction gale_shapley avec les données du fichier JSON
    matchings, rounds, students_without_school = gale_shapley(
        data['students_preferences'],
        data['schools_preferences'],
        data['school_seats'],
        studentBiding
    )

    # Afficher les résultats
    print("Matchings:")
    for school, students in matchings.items():
        print(f"{school}: {students}")
    print(f"Number of rounds: {rounds}")
    print("Unmatched:")
    print(students_without_school)

if __name__ == '__main__':
    # Créer un analyseur d'arguments
    parser = argparse.ArgumentParser(description='Gale-Shapley Script')
    
    # Ajouter les arguments
    parser.add_argument('json_file', type=str, help='Chemin vers le fichier JSON')
    parser.add_argument('--studentBiding', type=str, default='True', help='True si eleves proposent, False sinon')
    
    # Parser les arguments de la ligne de commande
    args = parser.parse_args()

    # Appeler la fonction main avec les arguments fournis
    main(args.json_file, args.studentBiding)
