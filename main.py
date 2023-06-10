# Stable marriage problem solver

# Simple static example
def stable_marriage(serenades_prefs, balconies_prefs):
    # create dictionaries of preferences for both serenades and balconies
    serenades_prefs = {serenade: preferences for serenade, preferences in serenades_prefs.items()}
    balconies_prefs = {balcony: preferences for balcony, preferences in balconies_prefs.items()}
    # create a dictionary of engaged serenades initialized to None
    serenade_engaged = {}
    # create a dictionary of available balconies initialized to 1
    balcony_slots = {balcony: 1 for balcony in balconies_prefs}

    # while there are still serenades without a balcony
    while serenades_prefs:
        # get the first serenade in the list of serenades
        b = next(iter(serenades_prefs))
        # get the list of balconies that the serenade prefers
        balcony_list = serenades_prefs[b]

        # for each balcony in the list of balconies that the serenade prefers
        for balcony in balcony_list:
            # if the balcony has a slot available
            if balcony_slots[balcony] > 0:
                # the serenade is engaged to the balcony
                serenade_engaged[b] = balcony
                # the balcony has one less slot available
                balcony_slots[balcony] -= 1
                # remove the serenade from the list of serenades
                del serenades_prefs[b]
                # break out of the loop
                break

            # get the current partner of the serenade
            current_partner = serenade_engaged.get(b)
            # if the serenade has no partner
            if current_partner is None:
                # continue to the next balcony
                continue

            # if the serenade prefers the current balcony to the current partner
            if balconies_prefs[balcony].index(b) < balconies_prefs[balcony].index(current_partner):
                # the serenade is engaged to the balcony
                serenade_engaged[b] = balcony
                # the current partner is no longer engaged
                serenade_engaged[current_partner] = None
                # remove the serenade from the list of serenades
                del serenades_prefs[b]
                # break out of the loop
                break

            # remove the current balcony from the list of preferences
            del serenades_prefs[b][0]

    # return the dictionary of engaged serenades
    return serenade_engaged


# Example usage

def __main__():
    men = {
        'A': ['Alpha', 'Beta', 'Gamma'],
        'B': ['Beta', 'Alpha', 'Gamma'],
        'C': ['Alpha', 'Beta', 'Gamma']
    }

    women = {
        'Alpha': ['B', 'A', 'C'],
        'Beta': ['A', 'B', 'C'],
        'Gamma': ['B', 'C', 'A']
    }

    result = stable_marriage(men, women)
    for serenade, balcony in result.items():
        print(f"{serenade} is matched with {balcony}")


if __name__ == "__main__":
    __main__()

