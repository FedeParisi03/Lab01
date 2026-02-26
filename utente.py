class Utente:

    def __init__(self, nickname, punteggioAttuale):
        self.nickname = nickname
        self.punteggioAttuale = punteggioAttuale

    def fornisciUtente(self):
        return self.nickname + " " + str(self.punteggioAttuale)

    def aggiornaPunteggio(self, nuovoGiocatore):
        recordClassifica = []
        with open("punti.txt", "r", encoding="utf-8") as file:
            for riga in file:
                nickname, punti = riga.strip().split(" ")
                vecchioGiocatore = Utente(nickname, punti)
                recordClassifica.append(vecchioGiocatore)

        recordClassifica.append(nuovoGiocatore)
        recordClassifica.sort(key=lambda x: int(x.punteggioAttuale), reverse=True)

        with open("punti.txt", "w", encoding="utf-8") as file:
            for u in recordClassifica:
                file.write(u.fornisciUtente() + "\n")
