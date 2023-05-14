import pyfiglet
print("📺-🔌-🎮-"*10)
print("\033[0;34m")
banner = pyfiglet.figlet_format("TV OPERATIONS", font="slant", justify="center")
print(banner)
print("\033[0m")
print("📺-🔌-🎮-"*10)

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
        self.channel = 0
        self.volume_level = 0
        print("\n\033[0;31mThe television is currently \033[4;30mturned off.\n\033[0;31m \nChannel: \033[4;30m",self.channel, "\n\n\033[0;31mVolume Level: \033[4;30m", self.volume_level, "\033[0m")
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



# Creating of 2 objects TV_1 and TV_2
tv_1 = TV(30, 3, True)
tv_2 = TV(3, 2, True)

# Print the necessary data.
print()
print("\033[0;32mThe \033[1;30m\033[41mTV 1's\033[0;32m \033[1;33mchannel \033[0;32mis\033[4;35m", tv_1.channel, "\033[0;32mand \033[1;36mvolume level\033[4;35m", tv_1.volume_level, ".")
print("\033[0;32mThe \033[1;30m\033[41mTV 2's\033[0;32m \033[1;33mchannel \033[0;32mis\033[4;35m", tv_2.channel, "\033[0;32mand \033[1;36mvolume level\033[4;35m", tv_2.volume_level,".")
print()

# Test Driver
test = input("\033[0m\033[1;94mPlease press any key to continue to Test Drive: \033[4;35m")

import time
import sys
print("\033[0;100mLoading:\033[0m".center(90))
 # Make a loading animation.
animation = ["🎥 . . . . . . .".center(70),"🎥 🎞 . . . . . .".center(70), "🎥 🎞 📽 . . . . .".center(70), "🎥 🎞 📽 📺 . . . .".center(70), "🎥 🎞 📽 📺 📷 . . .".center(70), "🎥 🎞 📽 📺 📷 📸 . .".center(70), "🎥 🎞 📽 📺 📷 📸 📹 .".center(70), "🎥 🎞 📽 📺 📷 📸 📹 📼".center(70)]
for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
print("\n")


print()
print("\033[1;32m📺-🔌-🎮-"*10)
banner = pyfiglet.figlet_format("Test Drivers", font="slant", justify="center")
print(banner)
print("📺-🔌-🎮-"*10,"\033[0m")
print()
tv_1 = TV(30, 3, True)
tv_2 = TV(3, 2, True)


print("\n"+"\033[1;32m*"*90)
print("\033[0m\033[1;35mWhen the TV is Turned on: ")
tv_1.TurnOn()

print("\033[1;32m*"*90)
print("\033[0m\033[1;35mGet the channel: ")
tv_1.GetChannel()

print("\n"+"\033[1;32m*"*90)
print("\033[0m\033[1;35mSet the channel: (In this test, to channel 4)")
tv_1.SetChannel(4)

print("\n"+"\033[1;32m*"*90)
print("\033[0m\033[1;35mGet the volume level: ")
tv_1.GetVolume()

print("\n"+"\033[1;32m*"*90)
print("\033[0m\033[1;35mSet the volume level: (In this test, to 7)")
tv_1.SetVolume(7)

print("\n"+"\033[1;32m*"*90)
print("\033[0m\033[1;35mChannel up: ")
tv_1.ChannelUp()

print("\n"+"\033[1;32m*"*90)
print("\033[0m\033[1;35mChannel down: ")
tv_1.ChannelDown()

print("\n"+"\033[1;32m*"*90)
print("\033[0m\033[1;35mIncrease volume level: ")
tv_1.VolumeUp()

print("\n"+"\033[1;32m*"*90)
print("\033[0m\033[1;35mDecrease volume level: ")
tv_1.VolumeDown()

print("\n"+"\033[1;32m*"*90)
print("\033[0m\033[1;35mWhen the TV is turned off:")
tv_1.TurnOff()
print("\n"+"*\033[1;32m"*90)




create = input("\033[1;34mPlease press any key to continue to object creation: \033[4;35m")
import time
import sys
print("\033[0m\033[0;100mLoading:\033[0m".center(90))
 # Make a loading animation.
animation = ["🎥 . . . . . . .".center(70),"🎥 🎞 . . . . . .".center(70), "🎥 🎞 📽 . . . . .".center(70), "🎥 🎞 📽 📺 . . . .".center(70), "🎥 🎞 📽 📺 📷 . . .".center(70), "🎥 🎞 📽 📺 📷 📸 . .".center(70), "🎥 🎞 📽 📺 📷 📸 📹 .".center(70), "🎥 🎞 📽 📺 📷 📸 📹 📼".center(70)]
for i in range(len(animation)):
    time.sleep(0.2)
    sys.stdout.write("\r" + animation[i % len(animation)])
    sys.stdout.flush()
print("\n")

# Creation of new objects:
def process():
    global tv
    tv = input("\033[0;30mPlease input a name for your TV: \033[4;35m")
# Get the name of the object
# Get the channel of the object
    while True:
        try:
            channel = int(input("\033[0m\033[1;32mInput the channel [1-120]: \033[4;35m"))
            if channel > 120:
                raise Exception("Sorry, channels are 1-120 only.")
            else:
                break
        except ValueError:
            print("\033[0m\033[1;30m⚠️ Input error.")
        except Exception as e:
            print("\033[0m\033[1;30m⚠️ Error:", e)
            continue

# Get the volume level of the object
    while True:
        try:
            volume_level = int(input("\033[0m\033[0;36mInput the volume level [1-7]: \033[4;35m"))
            if volume_level > 7:
                raise Exception("Sorry, volume level is only 1-7 only.")
            else:
                break
        except ValueError:
            print("\033[0m\033[1;30m\033[0;91m⚠️ Input error.")
        except Exception as e:
            print("\033[0m\033[1;30m\033[0;91m⚠️ Error:", e)
            continue    
        except ValueError:
            print("Input error.")
            continue
# Ask the user whether the object is on or off
    while True:
        user_input = input("\033[0m\033[1;32mPlease type in True if the TV is on and False if the TV is off: \033[4;35m")
        if user_input.lower() == "true":
            on = True
            break
        elif user_input.lower() == "false":
            on = False
            break
        else:
            print("\033[0m\033[1;30m\033[0;91m⚠️ Input Error, type in only True or False.")
            continue

    tv = TV(channel, volume_level, on)


# Ask the user to perform methods
while True:
    print("\033[0;34m="*80)
    decision = input("\033[0;35mDo you want to create new obejct for TV? Type Yes or No: \033[4;31m")
    print("\033[0m")
    # If yes, repeat the process.
    if decision.lower() == "yes":
        process()
        while True:
            method = (input("\n\033[0m\033[42mPlease select a method to perform: \033[0m\n\033[1;30mA.Turn On\n\033[1;31mB.Turn Off\n\033[1;32mC.Get Channel\n\033[1;33mD.Set Channel\n\033[1;34mE.Get Volume\n\033[1;35mF.Set Volume\n\033[1;36mG.Channel Up\n\033[1;37mH.Channel Down\n\033[1;30mI.Volume Up\n\033[1;31mJ.Volume Down\n\033[1;32mK.End Program\n\033[4;35m"))
            print("\033[0m")
            print("\033[0;100mLoading:\033[0m".center(90))
            # Make a loading animation.
            animation = ["🎥 . . . . . . .".center(70),"🎥 🎞 . . . . . .".center(70), "🎥 🎞 📽 . . . . .".center(70), "🎥 🎞 📽 📺 . . . .".center(70), "🎥 🎞 📽 📺 📷 . . .".center(70), "🎥 🎞 📽 📺 📷 📸 . .".center(70), "🎥 🎞 📽 📺 📷 📸 📹 .".center(70), "🎥 🎞 📽 📺 📷 📸 📹 📼".center(70)]
            for i in range(len(animation)):
                time.sleep(0.2)
                sys.stdout.write("\r" + animation[i % len(animation)])
                sys.stdout.flush()
            print("\n")
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
                        input_channel = int(input("\033[0;34mInput the new channel [1-120]: "))
                        if input_channel > 120:
                            raise Exception("Sorry, channels are 1-120 only.")
                        else:
                            break
                    except ValueError:
                        print("\033[1;30m\033[0;91m⚠️ Input error.")
                    except Exception as e:
                        print("\033[1;30m\033[0;91m⚠️ Error:", e)
                        continue
                tv.SetChannel(input_channel)
                break

            if method == "e":
                tv.GetVolume()
                break

            if method == "f":
                while True:
                    try:
                        input_volume = int(input("\033[0;34mInput the new volume level [1-7]: "))
                        if input_volume > 7:
                            raise Exception("Sorry, volume level is 1-7 only.")
                        else:
                            break
                    except ValueError:
                        print("\033[1;30m\033[0;91m⚠️ Input error.")
                    except Exception as e:
                        print("\033[1;30m\033[0;91m⚠️ Error:", e)
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
                print("\033[1;93mOkay, thank you for using this program.")
                break

            else:
                print("\033[1;30m\033[0;91m⚠️ Invalid Input.")
                continue

    elif decision.lower() == "no":
        print("\033[0;34m="*80)
        print("\n\033[1;93mOkay, thank you for using this program.\n")
        print("\033[0;34m="*80)
        break
    else:
        print("\033[1;30m\033[0;91m⚠️ Please type in only Yes or No.")
        continue








