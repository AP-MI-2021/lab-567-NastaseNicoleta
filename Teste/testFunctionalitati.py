from Domain.rezervare import getClasa, getPret
from Logic.CRUD import adaugaRezervare
from Logic.functionalitati import trecereLaClasaSuperioara, ieftinireRezervariCuCheckinFacut, \
    determinarePretMaximPeClasa


def testTrecereLaClasaSuperioara():
    lista = []
    lista = adaugaRezervare("454", "Costachescu", "business", 400, "da", lista)
    lista = adaugaRezervare("325", "Grigore", "economy", 230, "nu", lista)

    lista = trecereLaClasaSuperioara("Grigore", lista)

    assert getClasa(lista[0]) == "business"
    assert getClasa(lista[1]) == "economy plus"

    lista = trecereLaClasaSuperioara("Costachescu", lista)

    assert getClasa(lista[0]) == "business"

def testIeftinirePretCuUnProcentajDat():
    lista = []
    lista = adaugaRezervare("454", "Costachescu", "business", 400, "da", lista)
    lista = adaugaRezervare("325", "Grigore", "economy", 230, "nu", lista)

    lista = ieftinireRezervariCuCheckinFacut(20, lista)

    assert getPret(lista[0]) == 320.0
    assert getPret(lista[1]) == 230.0

def testDeterminarePretMaximPeClasa():
    lista = []
    lista = adaugaRezervare("454", "Costachescu", "business", 400, "da", lista)
    lista = adaugaRezervare("325", "Grigore", "economy", 230, "nu", lista)
    lista = adaugaRezervare("57", "Galateanu", "business", 456, "da", lista)
    lista = adaugaRezervare("276", "Marin", "economy", 124, "nu", lista)
    lista = adaugaRezervare("973", "Calin", "economy plus", 250, "da", lista)
    lista = adaugaRezervare("100", "Georgescu", "economy plus", 224, "da", lista)

    pretMaximEconomy, pretMaximEconomyPlus, pretMaximBusiness = determinarePretMaximPeClasa(lista)
    assert pretMaximEconomy == 230
    assert pretMaximEconomyPlus == 250
    assert pretMaximBusiness == 456