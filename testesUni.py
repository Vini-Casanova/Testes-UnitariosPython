import unittest

class Eleitores:
    def __init__(self,idade) -> None:
        self._idade = idade



class TestStringMethods(unittest.TestCase):
    
    @unittest.expectedFailure
    def test_lower(self):
        eleitor = Eleitores(17)
        self.assertGreaterEqual(eleitor._idade,18,"Idade Invalida")

    def test_okay1(self):
        eleitor = Eleitores(21)
        self.assertGreaterEqual(eleitor._idade,18,"Idade Invalida")

    def test_okay2(self):
        eleitor = Eleitores(69)
        self.assertLessEqual(eleitor._idade,69,"Idade Invalida")
    
    @unittest.expectedFailure
    def test_higher(self):
        eleitor = Eleitores(71)
        self.assertLessEqual(eleitor._idade,69,"Idade Invalida")

if __name__ == '__main__':
    unittest.main()
