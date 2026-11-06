def addizione(a, b):
    """esc 3"""
    if type(a) != int and type(a) != float and type(b) != int and type(b) != float:
        raise ValueError
    else:
        return a + b
    
def sottrazione(a, b):
    """esc 3"""
    if type(a) != int and type(a) != float and type(b) != int and type(b) != float:
        raise ValueError
    else:
        return a + b

def multiplicazione(a, b):
    """esc 3"""
    if type(a) != int and type(a) != float and type(b) != int and type(b) != float:
        raise ValueError
    else:
        return a + b
    
def divisione(a, b):
    """esc 3"""
    if type(a) != int and type(a) != float and type(b) != int and type(b) != float:
        raise ValueError
    elif b == 0:
        print("Attenzione: divisione per 0!")
    else:    
        return a / b
    
if __name__ == "__name__":
    while True:
        comandoUtente = input("insert 's' if you want to do an operation")

        if comandoUtente.lower() == "s":
            numeroA = float(input("insert the number for the operation:  "))
            numeroB = float(input("insert the number for the operation:  "))
            operatore = input("insert an operator (+ = addizione; - = sottrazione; * = moltiplicazione; / = divisione): ")

            match operatore:
                case "+":
                    print(f"Risultato operazione {numeroA} + {numeroB} = {addizione(numeroA, numeroB)}")
            match operatore:
                case "-":
                    print(f"Risultato operazione {numeroA} - {numeroB} = {sottrazione(numeroA, numeroB)}")
            match operatore:
                case "*":
                    print(f"Risultato operazione {numeroA} * {numeroB} = {multiplicazione(numeroA, numeroB)}")
            match operatore:
                case "/":
                    print(f"Risultato operazione {numeroA} / {numeroB} = {divisione(numeroA, numeroB)}")