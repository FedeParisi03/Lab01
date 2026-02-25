import random

from game import Gioco  # Assicurati che il file della classe si chiami game.py


def main():
    partita = Gioco([], 0, 0)
    continuaAGiocare = True
    print("!!!! BENVENUTO AL TRIVIA GAME !!!!\n")
    print("Pronto a cominciare? Fa attenzione a scrivere bene le risposte\n"
          "Ogni minimo sbaglio verrà segnalato come errore!!!\n")

    while continuaAGiocare:
        domanda = partita.fornisciDomandaLivello()
        print(domanda.fornisciDomanda())
        continuaAGiocare = partita.controlloRisposta(domanda, input("Fornisci qui la tua risposta: "))

        print("\n")

if __name__ == '__main__':
    main()