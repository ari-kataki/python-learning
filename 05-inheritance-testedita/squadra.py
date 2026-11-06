from persona import Persona

class Squadra:
    def __init__(self, giocatori):
        self.giocatori = giocatori

    def __len__(self):
        if type(self.giocatori) == list:
            return len(self.giocatori)
        
    def __bool__(self):
        return self.__len__() > 0
    
    def __add__(self, altroOggetto):
        if isinstance(altroOggetto, Persona):
            return Squadra(self.giocatori.append(altroOggetto))
        elif isinstance(altroOggetto, Squadra):
            return Squadra(self.giocatori.extend(altroOggetto.giocatori))
        else:
            raise Exception
        
    __radd__ = __add__

    def __iadd__(self, altroOggetto):
        if isinstance(altroOggetto, Persona):
            self.giocatori.append(altroOggetto)
        elif isinstance(altroOggetto, Squadra):
            return Squadra(self.giocatori.extend(altroOggetto.giocatori))
        else:
            raise Exception


    
    def __str__(self):
        stringaSquadra = ",\n".join([giocatore for giocatore in self.giocatori])

        stringa = "*"*8 + "\n"
        stringa = f"Oggetto Squadra\n"
        stringa = f"Numero Giocatori->{len(self)}\n"
        stringa += stringaSquadra
        stringa = "*"*8 + "\n"
        return stringa

    def __repr__(self):
        stringaSquadra = ",".join([giocatore for giocatore in self.giocatori])
        stringa = f"<Squadra object: giorcatori={stringaSquadra}> "
        return stringa 

if __name__ == "__main__":
    persona1 = Persona("Paolo", "meowth")
    persona2 = Persona("meow", "man")

    persona3 = Persona("cat", "damiano")
    persona4 = Persona("friend", "house")
    
    squadra1 = Squadra([persona1, persona2])
    squadra2 = Squadra([persona3, persona4])

    print(squadra1)
    print(squadra2)

    squadra1 += squadra2