# file: algo.py

# Description: This file contains the implementation of the Stable Marriage Problem
# Authors: Eliot Colomb & Joe Teodoresco

class Serenade:
    def __init__(self, name, preferences):
        self.name = name
        self.preferences = preferences
        self.engaged = None

    def __str__(self):
        return f"{self.name} - {self.engaged}"
    
    def reset(self):
        self.engaged = None

    def engage_balcony(self, balcony):
        self.engaged = balcony
    
    def disengage_balcony(self):
        if self.engaged is not None:
            self.engaged.disengage_serenade(self)
            self.engaged = None
    
    def reset_preferences(self):
        self.preferences = self.preferences[::-1]  # Reverse the preferences order for the next round

class Balcony:
    def __init__(self, name, preferences, slots):
        self.name = name
        self.preferences = preferences
        self.slots = slots
        self.engaged = []

    def __str__(self):
        return f"{self.name} - {self.engaged}"
    
    def reset(self):
        self.engaged = []

    def has_slots_available(self):
        return len(self.engaged) < self.slots

    def engage_serenade(self, serenade):
        if self.has_slots_available():
            if self.engaged:
                self.engaged[0].disengage_balcony()
            self.engaged = [serenade]
            serenade.engage_balcony(self)

    def disengage_serenade(self, serenade):
        if serenade in self.engaged:
            self.engaged.remove(serenade)


    def get_least_preferred_serenade(self):
        return min(self.engaged, key=lambda serenade: self.preferences.index(serenade.name))

    def replace_serenade(self, new_serenade, old_serenade):
        self.engaged.remove(old_serenade)
        self.engaged.append(new_serenade)

    def prefers_serenade(self, new_serenade, current_serenade):
        return self.preferences.index(new_serenade.name) < self.preferences.index(current_serenade.name)

    def disengage_balcony(self):
        for serenade in self.engaged:
            serenade.engaged = None
        self.engaged = []

    def reset_preferences(self):
        self.preferences = self.preferences[::-1]  # Reverse the preferences order for the next round


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
# Gale-Shapley stable marriage solver
def stable_marriage(serenades, balconies):
    # Initialisation
    nbr_of_rounds = 0
    for serenade in serenades:
        serenade.reset()
    for balcony in balconies:
        balcony.reset()

    # While there are still serenades without a balcony
    while still_unmatched(serenades):
        for serenade in serenades:
            if serenade.engaged is None:
                preferred_balcony = serenade.preferences.pop(0)  # Get the next preferred balcony
                balcony = get_balcony_by_name(preferred_balcony, balconies)
                if balcony.has_slots_available():
                    balcony.engage_serenade(serenade)
                    serenade.engage_balcony(balcony)
                else:
                    current_partner = balcony.get_least_preferred_serenade()
                    if balcony.prefers_serenade(serenade, current_partner):
                        balcony.replace_serenade(serenade, current_partner)
                        serenade.engage_balcony(balcony)
                        current_partner.disengage_balcony()
                        current_partner.reset_preferences()

        nbr_of_rounds += 1

    return nbr_of_rounds



def still_unmatched(serenades):
    for serenade in serenades:
        if serenade.engaged == None:
            return True
    return False

def get_balcony_by_name(balcony_name, balconies):
    for balcony in balconies:
        if balcony.name == balcony_name:
            return balcony
    return None


# Jeu de test 1
def test1():
    students = [
        Serenade("Esteban", ["IMT", "INSA", "N7"]),
        Serenade("Joe", ["N7", "IMT", "INSA"]),
        Serenade("Pablo", ["N7", "INSA", "IMT"])
    ]

    colleges = [
        Balcony("IMT", ["Esteban", "Pablo", "Joe"], 1),
        Balcony("N7", ["Joe", "Esteban", "Pablo"], 1),
        Balcony("INSA", ["Esteban", "Joe", "Pablo"], 1)
    ]

    nbr_of_rounds = stable_marriage(students, colleges)

    ### WANTED RESULTS ###
    # Joe - N7
    # Esteban - INSA
    # Pablo - IMT
    # nbr_of_rounds = 3

    print("Test 1")
    print("-------")
    for serenade in students:
        print(serenade)
    print("-------")
    print("Number of rounds: ", nbr_of_rounds)
    print("-------")

test1()