# 10. Crie uma classe Forca que sorteie uma palavra de uma lista e permita que o jogador tente adivinhar, letra por letra, até acabar as tentativas ou acertar a palavra.
import random

class Forca:
    def __init__(self, palavras, tentativas=6):
        self.palavra = random.choice(palavras).upper()
        self.tentativas = tentativas
        self.letras_acertadas = set()
        self.letras_erradas = set()

    def adivinhar(self, letra):
        letra = letra.upper()
        if letra in self.palavra:
            self.letras_acertadas.add(letra)
            return True
        else:
            self.letras_erradas.add(letra)
            self.tentativas -= 1
            return False

    def mostrar_palavra(self):
        return ' '.join([letra if letra in self.letras_acertadas else '_' for letra in self.palavra])

    def jogo_terminado(self):
        return self.tentativas <= 0 or all(letra in self.letras_acertadas for letra in self.palavra)

    def venceu(self):
        return all(letra in self.letras_acertadas for letra in self.palavra)
