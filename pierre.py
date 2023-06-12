# Entrée : Deux ensembles finis M (d’hommes) et W (de femmes) de cardinal n ;
#          Une famille L de relations de préférences ;
# Sortie : Un ensemble S de couples engagés (homme ; femme) ;
# fonction mariageStable {
#     Initialiser tous les m ∈ M et w ∈ W à célibataire
#     tant que ∃ homme célibataire m qui peut se proposer à une femme w {
#        w = femme préférée de m parmi celles à qui il ne s'est pas déjà proposé
#        si w est célibataire
#          (m, w) forment un couple
#        sinon un couple (m', w) existe
#          si w préfère m à m'
#            (m, w) forment un couple
#             m' devient célibataire
#          sinon
#            (m', w) restent en couple
#     }
#     Retourner l’ensemble S des couples engagés
# }

def marriageStable(eleves, ecoles, preferences_eleves, preferences_ecoles):
    eleves_celibataires = {e for e in eleves}
    ecoles_celibataires = {ec for ec in ecoles}
    engagement = {}
    engagement_inverse = {}
    tour = 0

    while eleves_celibataires:
        eleve = eleves_celibataires.pop()  # Choisir un élève célibataire
        match_trouve = False  # Indicateur pour vérifier si un appariement a été trouvé pour l'élève

        for ecole in preferences_eleves[eleve]:  # Parcourir les écoles selon les préférences de l'élève
            places_restantes = ecoles[ecole]  # Nombre de places restantes à l'école

            if places_restantes > 0 and len(engagement_inverse.get(ecole, [])) < places_restantes:
                engagement[eleve] = ecole
                engagement_inverse.setdefault(ecole, []).append(eleve)
                ecoles[ecole] = places_restantes - 1
                match_trouve = True  # Un appariement a été trouvé pour l'élève
                break
            else:
                eleves_actuels = engagement_inverse.get(ecole, [])  # Les élèves actuellement engagés avec l'école
                index_eleve = preferences_ecoles[ecole].index(eleve)
                for eleve_actuel in eleves_actuels:
                    if preferences_ecoles[ecole].index(eleve_actuel) > index_eleve:
                        engagement[eleve] = ecole
                        engagement_inverse[ecole].remove(eleve_actuel)
                        engagement_inverse[ecole].append(eleve)
                        eleves_celibataires.add(eleve_actuel)
                        match_trouve = True  # Un appariement a été trouvé pour l'élève
                        break
        tour += 1

    return engagement, eleves_celibataires, tour

# Exemple d'utilisation
eleves = {'Pierre', 'Eliot', 'Alexis', 'Kylian'}
ecoles = {'ENSEEIHT': 1, 'X': 1, 'ENS UML': 1}
preferences_eleves = {
    'Pierre': ['ENSEEIHT', 'X', 'ENS UML'],
    'Eliot': ['X', 'ENSEEIHT', 'ENS UML'],
    'Alexis': ['ENSEEIHT', 'ENS UML', 'X'],
    'Kylian': ['X', 'ENSEEIHT', 'ENS UML'],
}
preferences_ecoles = {
    'ENSEEIHT': ['Pierre', 'Eliot', 'Alexis', 'Kylian'],
    'X': ['Eliot', 'Alexis', 'Pierre', 'Kylian'],
    'ENS UML': ['Alexis', 'Eliot', 'Pierre', 'Kylian'],
}

couples_engages, eleves_sans_match, tour = marriageStable(eleves, ecoles, preferences_eleves, preferences_ecoles)
print("Couples engagés:", couples_engages)
print("Élèves non appariés:", eleves_sans_match)
print("Nombre de tours:", tour)
