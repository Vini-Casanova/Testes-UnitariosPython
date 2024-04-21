import unittest

class Eleitores:

    def __init__(self,idade:int,has_vote:bool) -> None:
        self._idade = idade
        self._has_vote = has_vote

    def status(self):
        if self._has_vote : return "Eleitor já votou"
        else: return "Eleitor ainda não votou"

    def eleitor_type(self):
        if self._idade >= 18 or self._idade <= 69: return True
        else: return False



class TestStringMethods(unittest.TestCase):
    
    def test_datatype(self):
        eleitor = Eleitores(17,False)
        self.assertIsInstance(eleitor._idade, int,"Tipo de dado inserido incorreto")

    def test_obrigatorio(self):
        eleitor = Eleitores(43,True)
        self.assertTrue(eleitor.eleitor_type,"Eleitor não é obrigado")

    def test_not_obrigatorio(self):
        eleitor = Eleitores(17,False)
        self.assertFalse(eleitor.eleitor_type,"Eleitor é obrigado")

    def test_has_vote(self):
        eleitor = Eleitores(53,True)
        self.assertEqual(eleitor.status,"Eleitor já votou", "Eleitor ainda não havia votado")

    def test_has_not_vote(self):
        eleitor = Eleitores(21,False)
        self.assertEqual(eleitor.status,"Eleitor não votou", "Eleitor já havia votado")

if __name__ == '__main__':
    unittest.main()
