from Teste.testCRUD import testAdaugaRezervare, testStergereRezervare
from Teste.testDomain import testRezervare


def runAllTests():
    testRezervare()
    testAdaugaRezervare()
    testStergereRezervare()
