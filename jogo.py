# PERSONAGEM : classe mãe
# Heroi : controlado pelo usr
# Inimigo : adversario do heroi

from random import randint

class Personagem:
    def __init__(self, nome, vida, nivel) -> None:
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome
    def get_vida(self):
        return self.__vida
    def get_nivel(self):
        return self.__nivel

    def __str__(self):
        return f"\nNome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}"

    def receber_dano(self, dano):
        self.__vida -= dano
        if self.__vida <= 0:
            self.__vida = 0
            return "\nFIM DE JOGO"

    def atacar(self, alvo):
        faixa = self.__nivel // 5
        minimo = 5 + (faixa * 10)
        maximo = 10 + (faixa * 10)
        dano = randint(minimo, maximo)
        alvo.receber_dano(dano)
        print(f"\n{self.get_nome()} atacou o {alvo.get_nome()} e causou {dano} de dano")
        print(f"\nVida atual do {alvo.get_nome()}: {alvo.get_vida()}")

        


class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade

    @classmethod
    def personagem_supremo(cls):
        return cls("HEROI-SUPREMO", 200, 50,"SUPER HABILIDADE")

    def get_hability(self):
        return self.__habilidade

    def __str__(self):
        return f"{super().__str__()}\nHabilidade: {self.get_hability()}\n"

    def ataque_especial(self, alvo):
        faixa = self.get_nivel() // 5 
        minimo = 5 + (faixa * 20)
        maximo = 10 + (faixa * 20)
        dano = randint(minimo, maximo)
        alvo.receber_dano(dano)
        print(f"\n{self.get_nome()} atacou com {self.get_hability()} o {alvo.get_nome()} e causou {dano} de dano")
        print(f"\nVida atual do {alvo.get_nome()}: {alvo.get_vida()}")

class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo

    def __str__(self):
        return f"{super().__str__()}\nTipo: {self.get_tipo()}\n"



class Jogo:
    """"CLASSE ORQUESTRADORA DO JOGO"""

    def __init__(self) -> None:
        self.heroi = Heroi(nome="Ryan", vida=100, nivel=10, habilidade="cagar descalço")
        self.inimigo = Inimigo(nome="Morcego", vida=50, nivel=3, tipo="Voador")

    def iniciarbatalha(self):
        """GESTÃO DA BATALHA EM TURNOS"""
        print("Iniciando batalha")
        while self.heroi.get_vida() > 0 and self.inimigo.get_vida() > 0:
            print("\nDetalhes dos personagens:")
            print(self.heroi)
            print(self.inimigo)

            input("Pressione Enter para atacar...")
            escolha = input("Escolha (1 - ATAQUE NORMAL, 2 - ATAQUE ESPECIAL): ")

            if escolha == "1":
                self.heroi.atacar(self.inimigo)
            elif escolha == "2":
                self.heroi.ataque_especial(self.inimigo)
            elif escolha == "q":
                break
            else:
                print("Escolha invpalida. Escolha novamente.")

            if self.inimigo.get_vida() > 0:
                #INIMIGO ATACA O HEROI
                self.inimigo.atacar(self.heroi)
        if self.heroi.get_vida() > 0:
            print(f"O HEROI {self.heroi.get_nome()} VENCEU!")
        else:
            print(f"O INIMIGO {self.inimigo.get_nome()} VENCEU!")

            


heroi_s = Heroi.personagem_supremo()
print(heroi_s)
