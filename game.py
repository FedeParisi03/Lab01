from domanda import Domanda
import random

class Gioco:
    def __init__(self,listaDomande: list[Domanda], livelloAttuale: int, punteggio: int):
            self.listaDomande = listaDomande
            self.livelloAttuale = livelloAttuale
            self.punteggio = punteggio
            self.aggiungiDomanda()


    def aggiungiDomanda(self):
        with open("domande.txt", "r", encoding="utf-8") as file:
            righe = file.readlines()

        for i in range(0, len(righe), 7):
            nuovadomanda = Domanda(righe[i].strip(), int(righe[i + 1].strip()), righe[i + 2].strip(),
                              [righe[i + 2].strip(), righe[i + 3].strip(), righe[i + 4].strip(), righe[i + 5].strip()])
            self.listaDomande.append(nuovadomanda)

    def fornisciDomandaLivello(self):
        domandeLivello = [d for d in self.listaDomande if d.difficolta == self.livelloAttuale]
        domandaFornita = random.choice(domandeLivello)
        return domandaFornita

    def controlloRisposta (self, domandaEstratta, rispostaData):
        if domandaEstratta.difficolta == 4:
            if rispostaData == domandaEstratta.risposta_esatta:
                self.punteggio += 1
                print ("COMPLIMENTI!!!! Hai finito il gioco con successo.")
                return False
            if rispostaData != domandaEstratta.risposta_esatta:
                print("HAI SBAGLIATO!!!! Ritenta e sarai più fortunato.")
                return False
        else:
            if domandaEstratta.risposta_esatta == rispostaData:
                self.punteggio += 1
                self.livelloAttuale += 1
                return True
            elif domandaEstratta.risposta_esatta != rispostaData:
                print("HAI SBAGLIATO!!!! Ritenta e sarai più fortunato.")
                return False



















