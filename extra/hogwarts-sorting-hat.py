# Hogwarts Sorting Hat Algorithm - baseado em 101Computing
# https://www.101computing.net/hogwarts-sorting-hat-algorithm/

print(30*"=")
print("=                     ~")
print("=Chapéu Seletor UTFPR~")
print("=                     ~")
print(30*"=")
print()
print("Bem-vindo(a) a Hogwarts!")
print("Responda às perguntas com S/N.")
print()

gryffindor = 0
hufflepuff = 0
ravenclaw  = 0
slytherin  = 0

def res(msg):
    r = input(msg + " ").strip().lower()
    # aceita s/n/sim/nao/yes/no
    if r in ("s", "sim","S"):
        return True
    return False

##
if res("Você é corajoso(a)? [S/N]:"):
    gryffindor += 1  
##
if res("Você se considera paciente? [S/N]:"):
    hufflepuff += 1  
else:
    slytherin += 1   
##
if res("Você é focado(a) e estudioso(a)? [S/N]:"):
    ravenclaw += 1   
##
if res("Você tem uma mente criativa/inventiva? [S/N]:"):
    ravenclaw += 1 
##
if res("Você é organizado(a) e gosta de planejar com antecedência? [S/N]:"):
    ravenclaw += 1   
##
if res("Você preza pelo 'jogo limpo' (fair play)? [S/N]:"):
    hufflepuff += 1
    gryffindor += 1 
else:
    slytherin += 1   
##
if res("Você é leal? [S/N]:"):
    gryffindor += 1
    ravenclaw  += 1 
else:
    slytherin  += 1 

##
if res("Você é competitivo(a)? [S/N]:"):
    gryffindor += 1
    slytherin  += 1 
##
if res("Amizade é um valor muito forte para você? [S/N]:"):
    gryffindor += 1
    ravenclaw  += 1
    hufflepuff += 1  
else:
    slytherin  += 1  
##

if res("Você é gentil? [S/N]:"):
    hufflepuff += 1
    ravenclaw  += 1
    gryffindor += 1 
##

print("\nTotal de pontos:")
print(" - Gryffindor:", gryffindor)
print(" - Ravenclaw :", ravenclaw)
print(" - Hufflepuff:", hufflepuff)
print(" - Slytherin :", slytherin)  


if gryffindor >= ravenclaw and gryffindor >= hufflepuff and gryffindor >= slytherin:
    print("\n Parabéns, você pertence à Gryffindor!")
elif ravenclaw >= gryffindor and ravenclaw >= hufflepuff and ravenclaw >= slytherin:
    print("\n Parabéns, você pertence à Ravenclaw!")
elif hufflepuff >= ravenclaw and hufflepuff >= gryffindor and hufflepuff >= slytherin:
    print("\nParabéns, você pertence à Hufflepuff!")
elif slytherin >= ravenclaw and slytherin >= hufflepuff and slytherin >= gryffindor:
    print("\nParabéns, Você pertence à Slytherin!")  
