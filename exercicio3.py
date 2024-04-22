import unittest


class sitema():
    def calculate(self,notas:list):
        sum = 0
        for nota in notas:
            if not isinstance(nota,float):
                return 'Error'
            sum += nota
        if len(notas) == 0:
            print("Não há notas para ser calculado")
            return 'Error'
        print(f'Média dos alunos: {sum/len(notas)}')
        return 'Sucess'
        

    def insert(self,notas:list):
        try:
            nota = float(input("Coloque a nota do aluno: "))
            if isinstance(nota,float):
                notas.append(nota)
                print("Sucesso na inserção da nota \n\n")
                return 'Sucess'
            elif nota < 0.0:
                print("\n------ERROR-------Nota inserida não pode ser negativa\n------ERROR-------\n\n")
                return 'Error'
                
        except ValueError:
            print("------ERROR-------\nNota inserida não é valida\n------ERROR-------\n\n")
            return 'Error'
      
    def run(self):  
        notas = []
        print(f"Bem vindo ao sistema de registro de nota dos alunos \n\n O que você gostaria de realizar?\n")
        while True:
            print("1- Adicionar nota do aluno \n2- Calcular média dos alunos\n3- Sair")
            inp = input("Escolha: ")
            match inp:
                case '1': 
                    self.insert(notas)
                case '2': 
                    self.calculate(notas)
                case '3':
                    return False
                case _:
                    print("Opção não valida")
    

class TestMethods(unittest.TestCase):
    
    def test_inserValid(self):
        sis = sitema()
        self.assertEqual(sis.insert([]),'Sucess')

    def test_insertInvalid(self):
        sis = sitema()
        self.assertEqual(sis.insert([]),'Error')
    
    def test_calculateInvalid(self):
        sis = sitema()
        self.assertEqual(sis.calculate(['A']),'Error')

    #CT4 e CT6 são a mesma coisa
    def test_calculateValid(self):
        sis = sitema()
        self.assertEqual(sis.calculate(['10,8']),'Sucess')

    def test_calculateEmpty(self):
        sis = sitema()
        self.assertEqual(sis.calculate([]),'Error')
    

if __name__ == '__main__':
    unittest.main()
