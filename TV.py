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
        print("\033[0;30mThe television is currently turned on. \n\033[0;30mChannel: \033[4;31m",self.channel, "\n\033[0;30mVolume Level: \033[4;31m", self.volume_level, "\033[0m\n")
# TurnOff()
    def TurnOff(self):
        self.on = False
        self.channel = None
        self.volume_level = None
        print("\033[0;31mThe television is currently turned off.\n\033[0;31mChannel: \033[4;30m",self.channel, "\n\033[0;31mVolume Level: \033[4;30m", self.volume_level, "\033[0m")
# GetChannel()
    def GetChannel(self):
        print("\033[0;32mThe channel is: \033[4;33m", self.channel,"\033[0m")
# SetChannel()
    def SetChannel(self, new_channel):
        self.channel = new_channel 
        print("\033[0;33mThe new channel is: \033[4;32m", new_channel,"\033[0m")
# GetVolume()
    def GetVolume(self):
        print("\033[0;34mThe current volume level is: \033[4;35m", self.volume_level,"\033[0m")    
# SetVolume()
    def SetVolume(self, new_volume_level):
        self.volume_level = new_volume_level
        print("\033[0;35mThe new volume level is: \033[4;34m", new_volume_level,"\033[0m")
# ChannelUp()
    def ChannelUp(self):
        self.channel = self.channel + 1
        print("\033[0;36mThe channel is: \033[4;37m", self.channel,"\033[0m")
# ChannelDown()
    def ChannelDown(self):
        self.channel = self.channel - 1
        print("\033[0;37mThe channel is: \033[4;36m", self.channel,"\033[0m")
# VolumeUp()
    def VolumeUp(self):
        self.volume_level = self.volume_level + 1
        print("\033[0;31mThe volume is: \033[4;30m", self.volume_level,"\033[0m")
# VolumeDown()
    def VolumeDown(self):
        self.volume_level = self.volume_level - 1
        print("\033[0;32mThe volume is: \033[4;31m", self.volume_level,"\033[0m")

