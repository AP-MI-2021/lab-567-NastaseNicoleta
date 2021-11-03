from Domain.rezervare import toString
from Logic.CRUD import adaugaRezervare, stergeRezervare, modificaRezervarea
from Logic.functionalitati import trecereLaClasaSuperioara, ieftinireRezervariCuCheckinFacut, \
    determinarePretMaximPeClasa


def printMenu():
    print("1. Adauga rezervare")
    print("2. Sterge rezervare")
    print("3. Modifica rezervare")
    print("4. Trecere rezervare cu un nume dat la o clasa superioara")
    print("5. Ieftinire pret rezervari, care au checkin-ul facut, cu un procentaj dat ")
    print("6. Determinare pret maxim pe clase")
    print("a. Afisare rezervari")
    print("x. Iesire")


def uiAdaugareRezervare(lista):
    id = input("Dati id-ul: ")
    nume = input("Dati numele: ")
    clasa = input("Dati clasa: ")
    pret = float(input("Dati pretul: "))
    checkin_facut = input("Dati stadiul checkin-ului: ")
    return adaugaRezervare(id, nume, clasa, pret, checkin_facut, lista)


def uiStergereRezervare(lista):
    id = input("Dati id-ul rezervarii de sters: ")
    return stergeRezervare(id, lista)


def uiModificareRezervare(lista):
    id = input("Dati id-ul rezervarii de modificat: ")
    nume = input("Dati noul nume: ")
    clasa = input("Dati noua clasa: ")
    pret = float(input("Dati noul pret: "))
    checkin_facut = input("Dati noul stadiu al checkin-ului: ")
    return modificaRezervarea(id, nume, clasa, pret, checkin_facut, lista)

def uiTrecereLaClasaSuperioara(lista):
    try:
        nume = input("Dati numele pentru care doriti sa se modifice clasa:")
        return trecereLaClasaSuperioara(nume, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiIeftinirePretRezervariCuCheckinFacut(lista):
    try:
        procentaj = float(input("Dati procentajul cu care doriti sa se faca ieftinirea:"))
        return ieftinireRezervariCuCheckinFacut(procentaj, lista)
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista

def uiDeterminarePretMaximPeClasa(lista):
    try:
        pretMaximEconomy, pretMaximEconomyPlus, pretMaximBusiness = determinarePretMaximPeClasa(lista)
        print("Pretul maxim la clasa economy este " + str(pretMaximEconomy))
        print("Pretul maxim la clasa economy_plus este " + str(pretMaximEconomyPlus))
        print("Pretul maxim la clasa business este " + str(pretMaximBusiness))
    except ValueError as ve:
        print("Eroare: {}".format(ve))
        return lista



def showAll(lista):
    for rezervare in lista:
        print(toString(rezervare))


def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")

        if optiune == "1":
            lista = uiAdaugareRezervare(lista)
        elif optiune == "2":
            lista = uiStergereRezervare(lista)
        elif optiune == "3":
            lista = uiModificareRezervare(lista)
        elif optiune == "4":
            lista = uiTrecereLaClasaSuperioara(lista)
        elif optiune == "5":
            lista = uiIeftinirePretRezervariCuCheckinFacut(lista)
        elif optiune == "6":
            lista=uiDeterminarePretMaximPeClasa(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita! Reincercati: ")






