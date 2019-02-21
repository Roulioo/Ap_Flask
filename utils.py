# fonction moyenne 

def moyenne(l):

    # permet de stopper le script directement 

    if len(l) == 0:
        raise "Division by zero"

    return round(sum(l)/len(l))

def moyenne_max(users):
    
    maximum, name = 0, ''

    for user in users:

        m = moyenne(user['notes'])

        if m > maximum:
            maximum, name = m, user['name']
    
    return maximum, name