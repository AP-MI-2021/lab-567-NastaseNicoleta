def creeaza_rezervare(id, nume, clasa, pret, checkin_facut):
    '''
    creeaza un dictionar pentru o rezervare facuta la o companie aeriana
    :param id: string
    :param nume: string
    :param clasa: string
    :param pret: float
    :param checkin_facut: string
    :return:

    '''

    return {
        "id": id,
        "nume": nume,
        "clasa": clasa,
        "pret": pret,
        "checkin_facut": checkin_facut

    }

def getId(rezervare):
    '''
    ia id-ul unei rezervari
    :param rezervare: un dictionar ce retine o rezervare
    :return: id-ul rezervarii
    '''
    return rezervare["id"]

def getNume(rezervare):
    '''
    ia numele folosit pentru o rezervare
    :param rezervare: un dictionare ce retine o rezervare
    :return: numele folosit pentru rezervare
    '''
    return rezervare["nume"]

def getClasa(rezervare):
    '''
    ia clasa unei rezervari
    :param rezervare: un dictionar ce retine o rezervare
    :return: clasa rezervarii
    '''
    return rezervare["clasa"]

def getPret(rezervare):
    '''
    ia pretul unei rezervari
    :param rezervare: un dictionar ce retine o rezervare
    :return: pretul rezervarii
    '''
    return rezervare["pret"]

def getCheckin_facut(rezervare):
    '''
    ia stadiul checkin-ului unei rezervari
    :param rezervare: un dictionar ce retine o rezervare
    :return: stadiul checkin-unului rezervarii
    '''
    return rezervare["checkin_facut"]

def toString(rezervare):
    return "Id: {}, Nume: {}, Clasa: {}, Pret: {}, Checkin_facut: {}".format(
        getId(rezervare),
        getNume(rezervare),
        getClasa(rezervare),
        getPret(rezervare),
        getCheckin_facut(rezervare)
    )
