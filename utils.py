# fonction moyenne 

def moyenne(l):

    # permet de stopper le script directement 

    if len(l) == 0:
        raise "Division by zero"

    return sum(l)/len(l) 