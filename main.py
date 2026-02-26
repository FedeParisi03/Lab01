from utente import Utente
from game import Gioco


def main():
    partita = Gioco([], 0, 0)
    continuaAGiocare = True
    print("!!!! BENVENUTO AL TRIVIA GAME !!!!\n")
    print("Pronto a cominciare? Fa attenzione a scrivere bene le risposte\n"
          "Ogni minimo sbaglio verrà segnalato come errore!!!\n")

    while continuaAGiocare:
        domanda = partita.fornisciDomandaLivello()
        domanda.getDomandaRisposte()
        continuaAGiocare = partita.controlloRisposta(domanda, int(input("Fornisci qui la tua risposta: ")))

    nickname = input("Inserisci il tuo nickname: ")
    punteggio = partita.punteggio
    x = Utente(nickname, punteggio)
    x.aggiornaPunteggio(x)

if __name__ == '__main__':
    main()