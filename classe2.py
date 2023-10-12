class Pessoa:
    def __init__(self, nome, email, telefone):
        self.n = nome
        self.em = email
        self.tel = telefone
    def __str__(self): 
        return "O Nome é: " + self.n + "\n" + "Email: " + self.em + "\n" + "O Telefone é: " + self.tel
#criando pessoa
dadosa = Pessoa("Renata Arantes", "renaarantes@gmail.com", "47 991682796")
print(dadosa)
dados1 = Pessoa ("Júlia Amaral", "jufernanda@gmail.com", "47 88668675")
print(dados1)

class Motorista (Pessoa):
    def __init__(self, nome, email, telefone, CNH):
        super().__init__(nome, email, telefone)
        self.cnh = CNH
    def __str__(self): 
        return super().__str__() + "\n"  + "A CNH é: " + self.cnh
#criando pessoa
dadosb = Motorista("Roberta Rossi", "robretinha@gmail.com", "12653651", "123456789")
print(dadosb)
dados2 = Motorista("Juliano Borsch", "julianob@gmail.com", "47 66889900", "1011121314")
print(dados2)
class Vendedor (Pessoa):
    def __init__(self, nome, email, telefone, comissão):
        super().__init__(nome, email, telefone)
        self.com = comissão
    def __str__(self):
        return super().__str__() + "\n"  +  "A comissão é: " + self.com
dadosc = Vendedor("Ricardo Antunes", "ricardotunes@gmail.com", "47 991688975", "R$890.78")
print(dadosc)
dados3 = Vendedor("Tulio Moraes", "tuliomora@gmail.com", "47 88662211", "R$765,89")
print(dados3)


lista = []
lista.append(dadosa)
lista.append(dados1)
lista.append(dadosb)
lista.append(dados2)
lista.append(dadosc)
lista.append(dados3)
for e in lista:
    if isinstance (e, Motorista):
        print ("É motorista.", e.cnh)
    elif isinstance (e, Vendedor):
        print ("É vendedor.", e.com)
    else:
        print("É pessoa.")
    print(e)