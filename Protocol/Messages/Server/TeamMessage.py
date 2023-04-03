from ByteStream.Writer import Writer
from Utils.Helpers import Helpers

class TeamMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24124
        self.player = player

    def encode(self):
        #db = DBSQL()
        self.writeVInt(self.player.roomType)
        self.writeBoolean(False)
        self.writeVInt(1)
        
        self.writeInt(0)
        self.writeInt(Helpers().randomMapID())
        
        self.writeVInt(0)
        
        self.writeBoolean(False)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeDataReference(15, self.player.map_id)
        self.writeBoolean(False)
        
        self.writeVInt(1)

        #PlayerEntry
        self.writeBoolean(True) #Owner
        self.writeLong2(0, self.player.ID) 
        self.writeDataReference(16, self.player.home_brawler)
        self.writeDataReference(29, 0)
        
        self.writeVInt(self.player.brawlers_trophies[f"{self.player.brawl}"]) #t
        self.writeVInt(self.player.brawlers_high_trophies[f"{self.player.brawl}"]) #ht
        self.writeVInt(9)
        self.writeVInt(3) #State                               
        
        self.writeBoolean(False) # Is ready
        self.writeVInt(0) #Team
        self.writeVInt(52000000 + 69)
        self.writeVInt(52000000 + 69)
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeString(self.player.name) #name
        self.writeVInt(100)
        self.writeVInt(28000000 + self.player.profile_icon)  #  icon
        self.writeVInt(43000000 + self.player.name_color)    # name color
        self.writeVInt(-1)
        self.writeDataReference(23, self.player.starpower) if self.player.starpower != None else self.writeVInt(0)
        self.writeDataReference(23, self.player.gadget)    if self.player.gadget != None else self.writeVInt(0)
        self.writeVInt(self.player.pin)

        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(6)
        self.writeBoolean(False)
        self.writeVInt(0)