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
                            listaNoua = adaugaRezervare(elementNou[1], elementNou[2], elementNou[3], float(elementNou[4]), elementNou[5])
                        except ValueError:
                            print("Eroare! Nu ati introdus un numar zecimal pentru pretul rezervarii. Reincercati!")
                    elif elementNou[0] == "Sterge":
                        listaNoua = stergeRezervare(elementNou[1], listaNoua)
                    elif elementNou[0] == "Modifica":
                        try:
                            listaNoua = modificaRezervarea(elementNou[1], elementNou[2], elementNou[3], float(elementNou[4]), elementNou[5])
                        except ValueError:
                            print("Eroare! Nu ati introdus un numar zecimal pentru pretul rezervarii. Reincercati!")
                    elif elementNou[0] == "Afiseaza":
                        showAll(listaNoua)
                    else:
                        print("Optiune gresita! Va rugam, reincercati:")

listaNoua = []
mainCommandLine(listaNoua)


