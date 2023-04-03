from ByteStream.Writer import Writer
from Files.CsvLogic.Regions import Regions

class AllianceDataMessage(Writer):

    def __init__(self, client, player, club_data):
        super().__init__(client)
        self.id = 24301
        self.player = player
        self.club_data = club_data

    def encode(self):
        if self.club_data['ID'] != 0:
        	
        	self.writeBoolean(False)
        	self.writeLong2(0, self.club_data["ID"]) #hlid
        	self.writeString(self.club_data["Name"]) #name
        	self.writeDataReference(8, self.club_data["BadgeID"]) #badge
        	self.writeVInt(self.club_data["Type"]) # Type
        	self.writeVInt(len(self.club_data["Members"]))  # Total Members
        	self.writeVInt(self.club_data["Trophies"])  # Total Trophies
        	self.writeVInt(self.club_data["RequiredTrophies"])  # Trophies Required
        	self.writeDataReference(0, 0)
        self.writeString(Regions().get_region_string(self.club_data["Region"]))  # Region
        self.writeVInt(0)
        self.writeBoolean(self.club_data["FamilyFriendly"])  # Family Friendly

        self.writeString(self.club_data["Description"]) # Description
        #online = self.player.ClientDict["Clients"]
        self.writeVInt(len(self.club_data["Members"])) # Members Count
        
        for member in self.club_data["Members"]:
        	
        	self.writeLong(member['ID'])
        	self.writeVInt(member["Role"])
        	self.writeVInt(member["Trophies"]) # Trophies
        self.writeVInt(2)
        self.writeVInt(0) # State Timer
        self.writeVInt(0)
        self.writeBoolean(False) #DND
        self.writeString(member["Name"])
        self.writeVInt(100)
        self.writeVInt(28000000 + member["ProfileIcon"]) # Player Thumbnail
        self.writeVInt(43000000 + member["NameColor"]) # Player Name Color
        self.writeVInt(42000000) # Color Gradients

        self.writeVInt(0)