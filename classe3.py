#criando as questões
class Questao1:
    def __init__(self, enunciado, autor, datacadastro):
        self.enun = enunciado
        self.aut = autor
        self.datac = datacadastro
    def __str__(self):
        return "\n" + self.enun + "A autora é: " + self.aut + "\n" + "Data de Cadastro: " + self.datac
#ajustando a questão
q = Questao1("Quanto é 2+2?: ", "Júlia Amaral", "8/03/2023")
print (q)

class Questao2 (Questao1):
    def __init__(self, enunciado, autor, datacadastro, alternativas):
        super().__init__(enunciado, autor, datacadastro)
        self.alternativas = alternativas
    def __str__(self):
        alts = ""
        for i in (self.alternativas):
            alts = alts + "\n" +  i           
        return super().__str__() +alts
#ajustando a questão
q2 = Questao2("Quanto é 2+2?: ", "Júlia Amaral", "8/03/2023", ["a)3", "b)5", "***c)4***"])
print (q2)

class Questao3 (Questao1):
    def __init__(self, enunciado, autor, datacadastro, respostalacuna):
        super().__init__(enunciado, autor, datacadastro)
        self.rl = respostalacuna
    def __str__(self):
        rls = ""
        for i in (self.rl):
            rls = rls + "\n" + i 
        return super().__str__() + rls
#ajustando a questão
q3 = Questao3 ("2+3 é igual a _______, enquanto 2*3 é igual a ______ ", "Júlia Amaral", "8/03/2023", ["5", "6"])
print(q3)
#q4 = Questao3 ("Quanto é 5+5?: ")