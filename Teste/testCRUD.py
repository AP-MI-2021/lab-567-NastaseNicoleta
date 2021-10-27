from Domain.rezervare import getId, getNume, getClasa, getPret, getCheckin_facut
from Logic.CRUD import adaugaRezervare, getById, stergeRezervare


def testAdaugaRezervare():
    lista = []
    lista = adaugaRezervare("454", "Costachescu", "business", 400, "da", lista)
    assert len(lista) == 1
    assert getId(getById("454", lista)) == "454"
    assert getNume(getById("454", lista)) == "Costachescu"
    assert getClasa(getById("454", lista)) == "business"
    assert getPret(getById("454", lista)) == 400
    assert getCheckin_facut(getById("454", lista)) == "da"

def testStergereRezervare():
    lista = []
    lista = adaugaRezervare("454", "Costachescu", "business", 400, "da", lista)
    lista= adaugaRezervare("325", "Grigore", "economy", 230, "nu", lista)

    lista = stergeRezervare("454", lista)
    assert len(lista) == 1
    assert getById("454", lista) is None
    assert getById("325", lista) is not None

    lista = stergeRezervare("101", lista)
    assert len(lista) == 1
    assert getById("325", lista) is not None


