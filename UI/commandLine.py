from Logic.CRUD import adaugaRezervare, stergeRezervare, modificaRezervarea
from UI.console import showAll


def mainCommandLine(listaNoua):
    while True:
        mesaj = input()
        if mesaj == "Ajutor":
            print("Adauga, Id, Nume, Clasa, Pret, Checkin_facut - adauga un element nou in lista de rezervari a companiei")
            print("Sterge, Id, Nume, Clasa, Pret, Checkin_facut - sterge un element din lista de rezervari a companiei cu un anumit id")
            print("Modifica, Id, Nume, Clasa, Pret, Checkin_facut - modifica un element din lista de rezervari a companiei cu un anumit id")
            print("Afiseaza - afiseaza toate elementele din lista de rezervari")
            print("Stop - opreste programul")
        else:
            string = mesaj.split(";")
            if string[0] == "Stop":
                break
            else:
                for elemente in string:
                    elementNou = elemente.split(",")
                    if elementNou[0] == "Adauga":
                        try:
                            if len(elementNou) != 6:
                                raise ValueError("Trebuie sa introduceti exact 5 date adica id, nume, clasa, pret, checkin facut! ")
                            ID = elementNou[1]
                            nume = elementNou[2]
                            clasa = elementNou[3]
                            pret = float(elementNou[4])
                            checkin_facut = elementNou[5]
                            listaNoua = adaugaRezervare(ID, nume, clasa, pret, checkin_facut, listaNoua)
                        except ValueError:
                            print("Eroare! Nu ati introdus un numar zecimal pentru pretul rezervarii. Reincercati!")
                    elif elementNou[0] == "Sterge":
                        ID = elementNou[1]
                        listaNoua = stergeRezervare(ID, listaNoua)
                    elif elementNou[0] == "Modifica":
                        try:
                            if len(elementNou) != 6:
                                raise ValueError("Trebuie sa introduceti exact 5 date adica id, nume, clasa, pret, checkin facut! ")
                            ID = elementNou[1]
                            nume = elementNou[2]
                            clasa = elementNou[3]
                            pret = float(elementNou[4])
                            checkin_facut = elementNou[5]
                            listaNoua = modificaRezervarea(ID, nume, clasa, pret, checkin_facut, listaNoua)
                        except ValueError:
                            print("Eroare! Nu ati introdus un numar zecimal pentru pretul rezervarii. Reincercati!")
                    elif elementNou[0] == "Afiseaza":
                        showAll(listaNoua)
                    else:
                        print("Optiune gresita! Va rugam, reincercati:")

listaNoua = []
mainCommandLine(listaNoua)



