#ese 4
print("\nesc 6")
try:
    a = int(input("Insert value of a: "))
    b = int(input("Insert value of b: "))
    k = int(input("Insert value of k: "))

    # precondizioni: a < b e k > 0
    if a < b and k > 0:
        print(f"Numebers between {a} and {b} divide per {k}:")


        # b + 1
        for i in range(a, b + 1):
            if i % k == 0:
                print(i)
    else:
        print("input not valid")

except ValueError:
    print("Error: insert only whole numbers.")

#esc 5 
print ("\nesc 5")
    
quantity = int(input("Quantity of numbers to insert? "))

if quantity <= 0:
    print("empty list")

else:
    firstnumber = int(input("Insert 1° number: "))
    
    min = firstnumber
    max = firstnumber

    for i in range(1, quantity):
        number = int(input(f"input {i+1}° number: "))
        
        if number > max:
            max = number

        if number < min:
            min = number

    print(f"Minimum: {min}")
    print(f"Maximum: {max}")

#esc 6
print ("\nesc 6")

quantity = int(input("Quantity of numbers to insert? "))

firstnumber = int(input("Insert 1° number: "))

odd =  0
evan = 0
if firstnumber % 2 == 0:
    evan += 1
else:
    odd += 1
for i in range(1, quantity):
    number = int(input(f"input {i+1}° number: "))
    
    if number % 2 == 0:
        evan += 1
    else:
        odd += 1
print(f"Odd numbers: {odd} Evan numbers: {evan}")

#esc 7
print ("\nesc 7")
input_utente = input("Insert real numbers: ")
L = [float(x) for x in input_utente.split()]
print(f"Lista originale: {L}")

L.sort()

D = []

for i in range(len(L) - 1):
    differenza = L[i+1] - L[i]
    D.append(differenza)

print("\nElementi di L (in order):")
for numero in L:
    print(numero)

print("\nElementi di D (consuicative differences):")
for diff in D:
    #.2f per le decimali
    print(f"{diff:.2f}")

#esc 8
print ("\nesc 8")
# Input: strings
input_strings = input("Enter strings separated by commas: ")

# Creating the list L
L = [s.strip() for s in input_strings.split(",")]

# Calculating the sum of lengths
total_length = sum(len(s) for s in L)

# Results
print(f"L = {L}")
print(f"Sum of lengths: {total_length}")

#esc 9
print ("\nesc 9")

righe = int(input("Inserisci il numero di righe: "))
colonne = int(input("Inserisci il numero di colonne: "))

tabella = []

for i in range(righe):
    riga_corrente = []
    print(f"\n--- Inserimento dati per la riga {i+1} ---")
    for j in range(colonne):
        stringa = input(f"Inserisci la stringa per la posizione [{i}][{j}]: ")
        riga_corrente.append(stringa)
    tabella.append(riga_corrente)

print("\n--- Risultati ---")
for indice, riga in enumerate(tabella):
    somma_lunghezze = sum(len(stringa) for stringa in riga)
    print(f"Riga {indice}: la somma delle lunghezze è {somma_lunghezze}")