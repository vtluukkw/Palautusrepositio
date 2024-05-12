class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 += 1
        else:
            self.m_score2 += 1

    def tarkista(self, pisteet):
        if pisteet == 0:
            return "Love"
        elif pisteet == 1:
            return "Fifteen"
        elif pisteet == 2:
            return "Thirty"
        else:
            return "Forty"

    def get_score(self):
        score1 = ""
        score2 = ""

        if self.m_score1 >= 4 or self.m_score2 >= 4:
            minus_result = self.m_score1 - self. m_score2
            if minus_result == 1: return "Advantage player1"
            if minus_result == -1: return "Advantage player2"
            if minus_result >= 2: return "Win for player1"
            if minus_result <= -2: return "Win for player2"
            
        if self.m_score1 == self.m_score2:
            if self.m_score1 == 0: return "Love-All"
            if self.m_score1 == 1: return "Fifteen-All"
            if self.m_score1 == 2: return "Thirty-All"
            if self.m_score1 >= 3: return "Deuce"
        
        score1 = self.tarkista(self.m_score1)
        score2 = self.tarkista(self.m_score2)

        return score1 + "-" + score2
    
    # selitystä mitä tein    
    ''' 
    En tiedä miten halusit että refaktoroin koodia kun se on jo aika helppo
    lukea.
    
    Muutin ton erikoistapaus tarkistimen eteen ja sitten tein apu ohjelman 
    (tarkistaja), joka tarkistaa pelaajien pisteet ja palauttaa
    oikean termin pisteelle. Vähensin myös elif ja else lauseita koska niitä
    ei tarvita minun muuttamissa kohdissa. Otin myös temp:scoren pois, koska
    en tykkää käyttää temp muuttujia jos ei tarvitse, ja se tuntui aika
    turhalta muuttujalta.
    '''
