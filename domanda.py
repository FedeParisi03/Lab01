import random

class Domanda:

    def __init__(self, testo: str, difficolta: int, risposta_esatta: str, opzioni : list):
        self.testo = testo
        self.difficolta = difficolta
        self.risposta_esatta = risposta_esatta
        self.opzioni = opzioni

    def fornisciDomanda(self):
        print(f"difficoltà {self.difficolta}\n")
        print(self.testo)
        random.shuffle(self.opzioni)
        print("scegli tra le seguenti risposte: ")
        for o in self.opzioni:
            print(o)