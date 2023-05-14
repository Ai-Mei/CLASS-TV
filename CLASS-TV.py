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



# Creating of 2 objects TV_1 and TV_2
TV_1 = TV(30, 3, True)
TV_2 = TV(3, 2, True)

# Print the necessary data.
print("The TV 1's channel is", TV_1.channel, "and volume level", TV_1.volume_level, ".")
print("The TV 2's channel is", TV_2.channel, "and volume level", TV_2.volume_level,".")


# Test Driver
print()
print("📺-🔌-🎮-"*10)
print("Test Driver".center(90))
print("📺-🔌-🎮-"*10)
print()
TV_1 = TV(30, 3, True)
TV_2 = TV(3, 2, True)


print("\n"+"*"*90)
print("When the TV is Turned on: ")
TV_1.TurnOn()

print("*"*90)
print("Get the channel: ")
TV_1.GetChannel()

print("\n"+"*"*90)
print("Set the channel: (In this test, to channel 4)")
TV_1.SetChannel(4)

print("\n"+"*"*90)
print("Get the volume level: ")
TV_1.GetVolume()

print("\n"+"*"*90)
print("Set the volume level: (In this test, to 7)")
TV_1.SetVolume(7)

print("\n"+"*"*90)
print("Channel up: ")
TV_1.ChannelUp()

print("\n"+"*"*90)
print("Channel down: ")
TV_1.ChannelDown()

print("\n"+"*"*90)
print("Increase volume level: ")
TV_1.VolumeUp()

print("\n"+"*"*90)
print("Decrease volume level: ")
TV_1.VolumeDown()

print("\n"+"*"*90)
print("When the TV is turned off:")
TV_1.TurnOff()
print("\n"+"*"*90)


# Creation of new objects:
# Get the name of the object
# Get the channel of the object
# Get the volume level of the object
# Ask the user whether the object is on or off
# Make the object.