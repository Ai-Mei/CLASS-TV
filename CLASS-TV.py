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
tv_1 = TV(30, 3, True)
tv_2 = TV(3, 2, True)

# Print the necessary data.
print()
print("The TV 1's channel is", tv_1.channel, "and volume level", tv_1.volume_level, ".")
print("The TV 2's channel is", tv_2.channel, "and volume level", tv_2.volume_level,".")


# Test Driver
print()
print("📺-🔌-🎮-"*10)
print("Test Driver".center(90))
print("📺-🔌-🎮-"*10)
print()
tv_1 = TV(30, 3, True)
tv_2 = TV(3, 2, True)


print("\n"+"*"*90)
print("When the TV is Turned on: ")
tv_1.TurnOn()

print("*"*90)
print("Get the channel: ")
tv_1.GetChannel()

print("\n"+"*"*90)
print("Set the channel: (In this test, to channel 4)")
tv_1.SetChannel(4)

print("\n"+"*"*90)
print("Get the volume level: ")
tv_1.GetVolume()

print("\n"+"*"*90)
print("Set the volume level: (In this test, to 7)")
tv_1.SetVolume(7)

print("\n"+"*"*90)
print("Channel up: ")
tv_1.ChannelUp()

print("\n"+"*"*90)
print("Channel down: ")
tv_1.ChannelDown()

print("\n"+"*"*90)
print("Increase volume level: ")
tv_1.VolumeUp()

print("\n"+"*"*90)
print("Decrease volume level: ")
tv_1.VolumeDown()

print("\n"+"*"*90)
print("When the TV is turned off:")
tv_1.TurnOff()
print("\n"+"*"*90)


# Creation of new objects:
def process():
    global tv
    tv = input("Please input a name for your TV: ")
# Get the name of the object
# Get the channel of the object
    while True:
        try:
            channel = int(input("Input the channel [1-120]: "))
            if channel > 120:
                raise Exception("Sorry, channels are 1-120 only.")
            else:
                break
        except ValueError:
            print("Input error.")
        except Exception as e:
            print("Error:", e)
            continue    
        except ValueError:
            print("Input error.")
            continue

# Get the volume level of the object
    while True:
        try:
            volume_level = int(input("Input the volume level [1-7]: "))
            if volume_level > 7:
                raise Exception("Sorry, volume level is only 1-7 only.")
            else:
                break
        except ValueError:
            print("Input error.")
        except Exception as e:
            print("Error:", e)
            continue    
        except ValueError:
            print("Input error.")
            continue
# Ask the user whether the object is on or off
    while True:
        user_input = input("Please type in True if the TV is on and False if the TV is off: ")
        if user_input.lower() == "true":
            on = True
            break
        elif user_input.lower() == "false":
            on = False
            break
        else:
            print("Input Error, type in only True or False.")
            continue

    tv = TV(channel, volume_level, on)


# Ask the user to perform methods
while True:
    decision = input("Do you want to create new obejct for TV? Type Yes or No: ")
    # If yes, repeat the process.
    if decision.lower() == "yes":
        process()
        while True:
            method = (input("\nPlease select a method to perform: \nA.Turn On\nB.Turn Off\nC.Get Channel\nD.Set Channel\nE.Get Volume\nF.Set Volume\nG.Channel Up\nH.Channel Down\nI.Volume Up\nJ.Volume Down\nK.End Program\n"))
            method == method.lower()
            if method == "a":
                tv.TurnOn()
                break

            if method == "b":
                tv.TurnOff()
                break

            if method == "c":
                tv.GetChannel()
                break
                
            if method == "d":
                while True:
                    try:
                        input_channel = int(input("Input the new channel [1-120]: "))
                        if input_channel > 120:
                            raise Exception("Sorry, channels are 1-120 only.")
                        else:
                            break
                    except ValueError:
                        print("Input error.")
                    except Exception as e:
                        print("Error:", e)
                        continue    
                    except ValueError:
                        print("Input error.")
                        continue
                tv.SetChannel(input_channel)
                break

            if method == "e":
                tv.GetVolume()
                break

            if method == "f":
                while True:
                    try:
                        input_volume = int(input("Input the new volume level [1-7]: "))
                        if input_volume > 7:
                            raise Exception("Sorry, volume level is 1-7 only.")
                        else:
                            break
                    except ValueError:
                        print("Input error.")
                    except Exception as e:
                        print("Error:", e)
                        continue    
                    except ValueError:
                        print("Input error.")
                        continue
                tv.SetVolume(input_volume)
                break

            if method == "g":
                tv.ChannelUp()
                break

            if method == "h":
                tv.ChannelDown()
                break

            if method == "i":
                tv.VolumeUp()
                break

            if method == "j":
                tv.VolumeDown()
                break

            if method == "k":
                print("Okay, thank you for using this program.")
                break

            else:
                print("Invalid Input.")
                continue

    elif decision.lower() == "no":
        print("Okay, thank you for using this program.")
        break
    else:
        print("Please type in only Yes or No.")
        continue








