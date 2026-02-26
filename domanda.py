import random

class Domanda:

    def __init__(self, testo: str, difficolta: int, risposta_esatta: str, opzioni : list):
        self.testo = testo
        self.difficolta = difficolta
        self.risposta_esatta = risposta_esatta
        self.opzioni = opzioni

    def getDomandaRisposte(self):
        print(f"Livello {self.difficolta}) {self.testo}")
        random.shuffle(self.opzioni)
        contatore = 1
        for o in self.opzioni:
            stringa = f"{contatore}. {o}"
            print(stringa)
            contatore += 1
