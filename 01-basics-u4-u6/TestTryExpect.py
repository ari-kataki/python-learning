try:
    numeroUtente = int(input("insert name: "))
    print(numeroUtente)
except ValueError as errore:
    print(f"insert a whole number, Salmon! {errore}")
else:
    print(numeroUtente)
finally:
    pass