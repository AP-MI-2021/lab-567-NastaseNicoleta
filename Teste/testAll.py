from Teste.testCRUD import testAdaugaRezervare, testStergereRezervare, testModificareRezervare
from Teste.testFunctionalitati import testTrecereLaClasaSuperioara, testIeftinirePretCuUnProcentajDat, testDeterminarePretMaximPeClasa
from Teste.testDomain import testRezervare


def runAllTests():
    testRezervare()
    testAdaugaRezervare()
    testStergereRezervare()
    testModificareRezervare()
    testTrecereLaClasaSuperioara()
    testIeftinirePretCuUnProcentajDat()
    testDeterminarePretMaximPeClasa()

