class Pessoa:
    def __init__(self,nome, sobrenome, idade, cidade):
        self.nome = nome 
        self.sobrenome = sobrenome
        self.idade = idade
        self.cidade = cidade
        

    def saida_info(self):
        print(f"{self.nome} {self.sobrenome}, voce vem da cidade {self.cidade} e tem a idade {self.idade}")

pessoa1= Pessoa(input("Qual seu nome?"), input("Qual seu sobrenome?"), input("Qual sua idade?"), input("Qual sua cidade?"))
pessoa2= Pessoa(input("Qual seu nome?"), input("Qual seu sobrenome?"), input("Qual sua idade?"), input("Qual sua cidade?"))
pessoa3= Pessoa(input("Qual seu nome?"), input("Qual seu sobrenome?"), input("Qual sua idade?"), input("Qual sua cidade?"))
pessoa4= Pessoa(input("Qual seu nome?"), input("Qual seu sobrenome?"), input("Qual sua idade?"), input("Qual sua cidade?"))
        
pessoa1.saida_info()
pessoa2.saida_info()
pessoa3.saida_info()
pessoa4.saida_info()