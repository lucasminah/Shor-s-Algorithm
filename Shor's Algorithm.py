from random import randrange
from math import floor

def euclid_algo(x, y):
    if x < y:
        return euclid_algo(y, x)

    while y != 0:
        (x, y) = (y, x % y)

    return x

def verificaIgualdade(num, lista):
    for number in lista:
        if number == num:
            return True
        
        return False

def contaFrequencia(number, lista):
    count = 0
    for num in lista:
        count += 1
        if num == number:
            return count

def descobrirFrequencia(rand, num, grandeza = 15):
    restosLista = []
    for x in range(grandeza):
    resto = (rand**x)%num
    if not verificaIgualdade(resto, restosLista):
    restosLista.append(resto)
    
    else:
    return contaFrequencia(resto, restosLista)

    return 0

def decodificar(num, grandeza):
    freq = 0
    factors = []
    
    while freq == 0 or not (freq%2 == 0):
        rand = randrange(2, num)
        freq = descobrirFrequencia(rand, num)
        
        
        guess = rand**(freq/2)
        
        factors.append(euclid_algo(guess+1,num))
        factors.append(euclid_algo(guess-1,num))
        
        
        if factors[0] == 1:
            factors[0] = num/factors[1]
            
        if factors[1] == 1:
            factors[1] = num/factors[0]
                
        if factors[0] == num or factors[1] == num:
            factors = decodificar(num, grandeza)
                    
    return factors
        
        
def main():
    num = int(input("The chosen number: "))
    grandeza = int(input("Number of trys: "))
    print(decodificar(num, grandeza))



if __name__ == '__main__':
     main()
