# Programme test

# Initiation des variables #
n1 = 0
n2 = 0
n3 = 0

# Fonctions #
def calcul():
    global n1
    global n2
    global n3
    
    result = int(n1) + int(n2) + int(n3)
    return result

def inputNombre():
    global n1
    global n2
    global n3
    
    n1 = input ("Veuillez entrez la valeur du premier nombre : ")
    n2 = input ("Veuillez entrez la valeur du deuxième nombre : ")
    n3 = input ("Veuillez entrez la valeur du troisième nombre : ")
    
def programme():
    inputNombre()
    print("Voici le resultat du calcul : " + str(calcul()))
    
# Test pour un deuxième commit

# nouvelle-Fonctionnalité 

def salutation():
    print("Salut mon chère")   

# Main #
salutation()
programme() 

    