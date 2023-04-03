from ByteStream.Writer import Writer
from DataBase.DBManager import DB


class BattleEndMessage(Writer):

    def __init__(self, client, player, type, result, players, db: DB):
        super().__init__(client)
        self.id = 23456
        self.player  = player
        self.type    = type
        self.result  = result
        self.players = players
        db = db

    def encode(self):
        brawler_trophies = self.player.brawlers_trophies[str(self.player.home_brawler)]
#        old_tr = self.player.trophies


#        if 0 <= brawler_trophies <= 49:
#            win_val = 8
#            lose_val = 0

#        else:
#            if 50 <= brawler_trophies <= 99:
#                win_val = 8
#                lose_val = -1

#            if 100 <= brawler_trophies <= 199:
#                win_val = 8
#                lose_val = -2

#            if 200 <= brawler_trophies <= 299:
#                win_val = 8
#                lose_val = -3

#            if 300 <= brawler_trophies <= 399:
#                win_val = 8
#                lose_val = -4

#            if 400 <= brawler_trophies <= 499:
#                win_val = 8
#                lose_val = -5

#            if 500 <= brawler_trophies <= 599:
#                win_val = 8
#                lose_val = -6

#            if 600 <= brawler_trophies <= 699:
#                win_val = 8
#                lose_val = -7

#            if 700 <= brawler_trophies <= 799:
#                win_val = 8
#                lose_val = -8

#            if 800 <= brawler_trophies <= 899:
#                win_val = 7
#                lose_val = -9

#            if 900 <= brawler_trophies <= 999:
#                win_val = 6
#                lose_val = -10

#            if 1000 <= brawler_trophies <= 1099:
#                win_val = 5
#                lose_val = -11

#            if 1100 <= brawler_trophies <= 1199:
#                win_val = 4
#                lose_val = -12

#            if brawler_trophies >= 1200:
#                win_val = 3
#                lose_val = -12

#        if self.result == 0:
#            trop = win_val
#            self.player.trophies += win_val
#            pon = 1
#            self.player.brawlers_high_trophies[str(self.player.home_brawler)] = brawler_trophies + win_val
#            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + win_val
#            
#            self.db.update_player_account(self.player.token, 'BrawlersTrophies', self.player.brawlers_trophies)
#            self.db.update_player_account(self.player.token, 'BrawlersHighestTrophies', self.player.brawlers_high_trophies)

#            self.db.update_player_account(self.player.token, 'Trophies', self.player.trophies)
#            
#            self.db.update_player_account(self.player.token, 'HighestTrophies', self.player.trophies)
#        else:
#            trop = lose_val
#            self.player.trophies += lose_val
#            self.player.brawlers_trophies[str(self.player.home_brawler)] = brawler_trophies + lose_val
#            
#            self.db.update_player_account(self.player.token, 'BrawlersTrophies', self.player.brawlers_trophies)
#            self.db.update_player_account(self.player.token, 'Trophies', self.player.trophies)
        self.writeLong(self.player.ID)
        self.writeLong(1)

        self.writeVInt(0)#Game Mode Type
        self.writeVInt(0)#Result
        self.writeVInt(100)
        self.writeVInt(228)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(1)

        self.writeVInt(0)
        self.writeVInt(16)
        self.writeVInt(-64)
        self.writeBoolean(False)

        self.writeVInt(2) # Battle End Screen Players
        self.writeVInt(1) # Player Team and Star Player Type
        self.writeDataReference(16, self.player.home_brawler) # Player Brawler
        self.writeDataReference(29, self.player.selected_skins[str(self.player.home_brawler)]) # Player Skin
        self.writeVInt(self.player.brawlers_trophies[str(self.player.home_brawler)]) # Brawler Trophies
        self.writeVInt(0) # Player Power Play Points
        self.writeVInt(10) # Brawler Power Level
        self.writeBoolean(True) # Player HighID and LowID Array
        self.writeInt(0) # HighID
        self.writeInt(1) # LowID
        self.writeString(self.player.name) # Player Name
        self.writeVInt(0) # Player Experience Level
        self.writeVInt(28000000) # Player Profile Icon
        self.writeVInt(43000000 + self.player.name_color) # Player Name Color
        self.writeVInt(0) # Null VInt
        
       
        self.writeVInt(2) # Player Team and Star Player Type
        self.writeDataReference(16, 0) # Player Brawler
        self.writeDataReference(29, 52) # Player Skin
        self.writeVInt(1250) # Brawler Trophies
        self.writeVInt(0) # Player Power Play Points
        self.writeVInt(10) # Brawler Power Level
        self.writeBoolean(True) # Player HighID and LowID Array
        self.writeInt(0) # HighID
        self.writeInt(1) # LowID
        self.writeString("Bot") # Player Name
        self.writeVInt(0) # Player Experience Level
        self.writeVInt(28000000) # Player Profile Icon
        self.writeVInt(43000000) # Player Name Color
        self.writeVInt(0) # Null VInt
 

        # Experience Array
        self.writeVInt(2) # Count
        self.writeVInt(0) # Normal Experience ID
        self.writeVInt(0) # Normal Experience Gained
        self.writeVInt(8) # Star Player Experience ID
        self.writeVInt(0) # Star Player Experience Gained

        # Rank Up and Level Up Bonus Array
        self.writeVInt(0) # Count

        # Trophies and Experience Bars Array
        self.writeVInt(2) # Count
        self.writeVInt(1) # Trophies Bar Milestone ID
        self.writeVInt(self.player.brawlers_trophies[str(self.player.home_brawler)]) # Brawler Trophies
        self.writeVInt(self.player.brawlers_high_trophies[str(self.player.home_brawler)]) # Brawler Trophies for Rank
        self.writeVInt(5) # Experience Bar Milestone ID
        self.writeVInt(0) # Player Experience
        self.writeVInt(0) # Player Experience for Level
        
        self.writeDataReference(28, 0)  # Player Profile Icon
        self.writeBoolean(True)  # Play Again


