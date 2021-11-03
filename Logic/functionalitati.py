from Domain.rezervare import getClasa, getPret, getCheckin_facut, getId, getNume, creeaza_rezervare, toString


def trecereLaClasaSuperioara(nume, lista):
    '''
    trece o rezervare facuta pe un nume la o clasa superioara
    :param nume: un nume dat
    :param lista: o lista
    :return: noile rezervari
    '''

    listaNoua = []

    for rezervare in lista:
        if getNume(rezervare) == nume :
            if getClasa(rezervare) == "economy":
                clasaNoua = "economy plus"
            elif getClasa(rezervare) == "economy plus":
                clasaNoua = "business"
            elif getClasa(rezervare) == "business":
                clasaNoua = "business"
            rezervareClasaModificata = creeaza_rezervare(
                getId(rezervare),
                getNume(rezervare),
                clasaNoua,
                getPret(rezervare),
                getCheckin_facut(rezervare)
            )
            listaNoua.append(rezervareClasaModificata)
        else:
            listaNoua.append(rezervare)

    return listaNoua

def ieftinireRezervariCuCheckinFacut(procentaj :float, lista: list):
    '''
    Ieftineste rezervarile care au checkin-ul facut cu un procentaj dat
    :param procentaj:procentajul dat
    :param lista: o lista de rezervari
    :return: lista cu rezervarile modificate
    '''
    listaNoua = []
    for rezervare in lista:
        if getCheckin_facut(rezervare) == "da":
            pretNou = getPret(rezervare) - (procentaj / 100 * getPret(rezervare))
            rezervareNoua = creeaza_rezervare(
                getId(rezervare),
                getNume(rezervare),
                getClasa(rezervare),
                pretNou,
                getCheckin_facut(rezervare)
            )
            listaNoua.append(rezervareNoua)
        else:
            listaNoua.append(rezervare)
    return listaNoua

def determinarePretMaximPeClasa(lista):
    '''
    Determina pretul maxim pentru fiecare clasa
    :param lista: lista de rezervari
    :return: pretul maxim
    '''
    pretMaxEconomy = 0
    pretMaxEconomyPlus = 0
    pretMaxBusiness = 0

    for rezervare in lista:
        if getClasa(rezervare) == "economy" and getPret(rezervare) > pretMaxEconomy:
            pretMaxEconomy = getPret(rezervare)
        elif getClasa(rezervare) == "economy plus" and getPret(rezervare) > pretMaxEconomyPlus:
            pretMaxEconomyPlus = getPret(rezervare)
        elif getClasa(rezervare) == "business" and getPret(rezervare) > pretMaxBusiness:
            pretMaxBusiness = getPret(rezervare)

    return pretMaxEconomy, pretMaxEconomyPlus, pretMaxBusiness







