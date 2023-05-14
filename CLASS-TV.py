# Create a TV class
class TV:
# Set the object's channel(integer), volume_level(integer), and if it is on or off(boolean).
    def __init__(self, channel, volume_level, on):
        self.channel = channel
        self.volume_level = volume_level
        self.on = on

# Create methods.

# TurnOn()
    def TurnOn(self):
        self.on = True
        print("The television is currently turned on. \nChannel: ",self.channel, "\nVolume Level: ", self.volume_level, "\n")

# TurnOff()
    def TurnOff(self):
        self.on = False
        self.channel = 0
        self.volume_level = 0
        print("\nThe television is currently turned off. \nChannel: ",self.channel, "\nVolume Level: ", self.volume_level)

# GetChannel()
    def GetChannel(self):
        print("The channel is: ", self.channel)

# SetChannel()
    def SetChannel(self, new_channel):
        self.channel = new_channel 
        print("The new channel is: ", new_channel)

# GetVolume()
    def GetVolume(self):
        print("The current volume level is: ", self.volume_level) 
        
# SetVolume()
    def SetVolume(self, new_volume_level):
        self.volume_level = new_volume_level
        print("The new volume level is: ", new_volume_level)

# ChannelUp()
    def ChannelUp(self):
        self.channel = self.channel + 1
        print("The channel is: ", self.channel)

# ChannelDown()
    def ChannelDown(self):
        self.channel = self.channel - 1
        print("The channel is: ", self.channel)

# VolumeUp()
    def VolumeUp(self):
        self.volume_level = self.volume_level + 1
        print("The volume is: ", self.volume_level)

# VolumeDown()
    def VolumeDown(self):
        self.volume_level = self.volume_level - 1
        print("The volume is: ", self.volume_level)