from TV import TV
import pyfiglet
import time
import sys

# Creation of new objects:
def process():
    global tv
    tv = input("\033[1;30mPlease input a name for your TV: \033[4;30m")
# Get the name of the object
# Get the channel of the object
    while True:
        try:
            channel = int(input("\033[0m\033[1;31mInput the channel [1-120]: \033[4;31m"))
            if channel > 120:
                raise Exception("\033[0;101mSorry, channels are 1-120 only.\033[0m")
            else:
                break
        except ValueError:
            print("\033[0;101m\033[1;30m⚠️ Input error.\033[0m")
        except Exception as e:
            print("\033[0;101m\033[1;30m⚠️ Error:", e,"\033[0m")
            continue

# Get the volume level of the object
    while True:
        try:
            volume_level = int(input("\033[0m\033[1;36mInput the volume level [1-7]: \033[4;36m"))
            if volume_level > 7:
                raise Exception("\033[0;101m\033[1;30mSorry, volume level is only 1-7 only.\033[0m")
            else:
                break
        except ValueError:
            print("\033[0;101m\033[1;30m⚠️ Input error.\033[0m")
        except Exception as e:
            print("\033[0;101m\033[1;30m⚠️ Error:", e, "\033[0m")
            continue    
        except ValueError:
            print("\033[0;101m\033[1;30m⚠️ Input error.\033[0m")
            continue
# Ask the user whether the object is on or off
    while True:
        user_input = input("\033[0m\033[1;34mPlease type in True if the TV is on and False if the TV is off: \033[4;34m")
        if user_input.lower() == "true":
            on = True
            break
        elif user_input.lower() == "false":
            on = False
            break
        else:
            print("\033[0;101m\033[1;30m⚠️ Input Error, type in only True or False.\033[0m")
            continue

    tv = TV(channel, volume_level, on)

def methods():
    while True:
        method = (input("\n\033[0m\033[1;34m\033[47mPlease select a method to perform: \033[0m\n\033[1;30mA.Turn On\n\033[1;31mB.Turn Off\n\033[1;32mC.Get Channel\n\033[1;33mD.Set Channel\n\033[1;34mE.Get Volume\n\033[1;35mF.Set Volume\n\033[1;36mG.Channel Up\n\033[1;37mH.Channel Down\n\033[1;30mI.Volume Up\n\033[1;31mJ.Volume Down\n\033[1;32mK.End Program\n\n\033[0;90mType here: \033[4;37m"))
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
                    print("\033[0;101m\033[1;30m⚠️ Input error.\033[0m")
                except Exception as e:
                    print("\033[0;101m\033[1;30m⚠️ Error:", e, "\033[0m")
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
                    print("\033[0;101m\033[1;30m⚠️ Input error.\033[0m")
                except Exception as e:
                    print("\033[0;101m\033[1;30m⚠️ Error:", e, "\033[0m")
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
            print("\033[1;93mOkay, thank you for spending time with me.")
            print("   /\_/\     (\ __ /)      A__A".center(40))
            print("  ( ˶•o•˶)    ( •ω• )     ( •⤙•  )".center(40))
            print("ଘ(ა🍱)    (ა🍙૮)｡  (🍜٩  )੭".center(40))
            break

        else:
            print("\033[0;101m\033[1;30m⚠️ Invalid Input.\033[0m")
            continue



print("📺-🔌-🎮-"*10)
print("\033[0;34m")
banner = pyfiglet.figlet_format("TV OPERATIONS", font="slant", justify="center")
print(banner)
print("📺-🔌-🎮-"*10)
print("\033[0m")


while True:
    option = (input("\033[0m\033[1;34mPress 1 to continue to test drive and press 2 to skip the test: \033[4;35m"))
    if option == "2":
        print("\n")
        print("\033[0mLoading: ".center(90))
        # Make a loading animation.
        animation = ["🎥 . . . . . . .".center(70),"🎥 🎞 . . . . . .".center(70), "🎥 🎞 📽 . . . . .".center(70), "🎥 🎞 📽 📺 . . . .".center(70), "🎥 🎞 📽 📺 📷 . . .".center(70), "🎥 🎞 📽 📺 📷 📸 . .".center(70), "🎥 🎞 📽 📺 📷 📸 📹 .".center(70), "🎥 🎞 📽 📺 📷 📸 📹 📼".center(70)]
        for i in range(len(animation)):
            time.sleep(0.2)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        print("\n")
        process()
        methods()

        # Ask the user to perform methods
        while True:
            print("")
            print("="*80)
            decision = input("\033[1;34mDo you want to create new obejct for TV? Type Yes or No: \033[4;35m")
            print("\033[0m")

            # If yes, repeat the process.
            if decision.lower() == "yes":
                process()
                methods()
                

            elif decision.lower() == "no":
                print("\033[0;34m="*80)
                print("\n\033[1;93mOkay, thank you for spending time with me.\n")
                print("   /\_/\     (\ __ /)      A__A".center(40))
                print("  ( ˶•o•˶)    ( •ω• )     ( •⤙•  )".center(40))
                print("ଘ(ა🍱)    (ა🍙૮)｡  (🍜٩  )੭".center(40))
                print("\033[0;34m="*80)
                break
            else:
                print("\033[0;101m\033[1;30m⚠️ Please type in only Yes or No.\033[0m")
                continue
        break
        
    if option == "1":
        print("\n")
        print("\033[0m\033[0;94mLoading: ".center(90))
        # Make a loading animation.
        animation = ["🎥 . . . . . . .".center(70),"🎥 🎞 . . . . . .".center(90), "🎥 🎞 📽 . . . . .".center(90), "🎥 🎞 📽 📺 . . . .".center(90), "🎥 🎞 📽 📺 📷 . . .".center(70), "🎥 🎞 📽 📺 📷 📸 . .".center(70), "🎥 🎞 📽 📺 📷 📸 📹 .".center(70), "🎥 🎞 📽 📺 📷 📸 📹 📼".center(70)]
        for i in range(len(animation)):
            time.sleep(0.2)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        print("\n\033[40m")
        # Test Driver
        print("\033[0m")
        print("📺-🔌-🎮-"*10)
        print("\033[0m\033[1;31m")
        banner = pyfiglet.figlet_format("Test Drivers", font="slant", justify="center")
        print(banner)
        print("\033[0m"+"📺-🔌-🎮-"*10)
        print()
        tv_1 = TV(30, 3, True)
        tv_2 = TV(3, 2, True)
        print("\033[1;36mTV 1 \033[0;32mis in \033[1;31mchannel 30 \033[0m\033[0;32mwith \033[1;36mvolume level of 3 \033[0m\033[0;32mand is currently \033[1;34mon.\033[0m")
        print("\033[1;36mTV 2 \033[0;32mis in \033[1;31mchannel 2 \033[0m\033[0;32mwith \033[1;36mvolume level of 2 \033[0m\033[0;32mand is currently \033[1;34mon.\033[0m")


        print("\n"+"\033[1;97m /ᐠ. .ᐟ\ฅ\033[0;31m ♡\033[0m"*9)
        print("\n\033[0;100mWhen the TV is Turned on: \033[0m")
        print("\033[1;92mFor TV 1:\033[0m")
        tv_1.TurnOn()
        print("\033[1;96mFor TV 2:")
        tv_2.TurnOn()

        print("\033[1;97m /ᐠ. .ᐟ\ฅ\033[0;31m ♡\033[0m"*9)
        print("\n\033[0;102mGet the channel: \033[0m")
        print("\033[1;92mFor TV 1:\033[0m")
        tv_1.GetChannel()
        print("\n\033[1;96mFor TV 2:")
        tv_2.GetChannel()

        print("\n"+"\033[1;97m /ᐠ. .ᐟ\ฅ\033[0;31m ♡\033[0m"*9)
        print("\n\033[0;103mSet the channel: (In this test, to channel 4)\033[0m")
        print("\033[1;92mFor TV 1:\033[0m")
        tv_1.SetChannel(4)
        print("\n\033[1;96mFor TV 2:")
        tv_2.SetChannel(4)

        print("\n"+"\033[1;97m /ᐠ. .ᐟ\ฅ\033[0;31m ♡\033[0m"*9)
        print("\n\033[0;104mGet the volume level: \033[0m")
        print("\033[1;92mFor TV 1:\033[0m")
        tv_1.GetVolume()
        print("\n\033[1;96mFor TV 2:")
        tv_2.GetVolume()

        print("\n"+"\033[1;97m /ᐠ. .ᐟ\ฅ\033[0;31m ♡\033[0m"*9)
        print("\n\033[45mSet the volume level: (In this test, to 7)\033[0m")
        print("\033[1;92mFor TV 1:\033[0m")
        tv_1.SetVolume(7)
        print("\n\033[1;96mFor TV 2:")
        tv_2.SetVolume(7)

        print("\n"+"\033[1;97m /ᐠ. .ᐟ\ฅ\033[0;31m ♡\033[0m"*9)
        print("\n\033[0;106mChannel up: \033[0m")
        print("\033[1;92mFor TV 1:\033[0m")
        tv_1.ChannelUp()
        print("\n\033[1;96mFor TV 2:")
        tv_2.ChannelUp()

        print("\n"+"\033[1;97m /ᐠ. .ᐟ\ฅ\033[0;31m ♡\033[0m"*9)
        print("\n\033[0;107mChannel down: \033[0m")
        print("\033[1;92mFor TV 1:\033[0m")
        tv_1.ChannelDown()
        print("\n\033[1;96mFor TV 2:")
        tv_2.ChannelDown()

        print("\n"+"\033[1;97m /ᐠ. .ᐟ\ฅ\033[0;31m ♡\033[0m"*9)
        print("\n\033[0;100mIncrease volume level: \033[0m")
        print("\033[1;92mFor TV 1:\033[0m")
        tv_1.VolumeUp()
        print("\n\033[1;96mFor TV 2:")
        tv_2.VolumeUp()

        print("\n"+"\033[1;97m /ᐠ. .ᐟ\ฅ\033[0;31m ♡\033[0m"*9)
        print("\n\033[0;101mDecrease volume level: \033[0m")
        print("\033[1;92mFor TV 1:\033[0m")
        tv_1.VolumeDown()
        print("\n\033[1;96mFor TV 2:")
        tv_2.VolumeDown()

        print("\n"+"\033[1;97m /ᐠ. .ᐟ\ฅ\033[0;31m ♡\033[0m"*9)
        print("\n\033[0;101mWhen the TV is turned off:\033[0m")
        print("\033[1;92mFor TV 1:\033[0m")
        tv_1.TurnOff()
        print("\n\033[1;96mFor TV 2:")
        tv_2.TurnOff()

        print("\n"+"\033[1;97m /ᐠ. .ᐟ\ฅ\033[0;31m ♡\033[0m"*9)
        print()

        while True:
            print("")
            print("="*80)
            decision = input("\033[1;34mDo you want to create new obejct for TV? Type Yes or No: \033[4;35m")
            print("\033[0m")

            # If yes, repeat the process.
            if decision.lower() == "yes":
                process()
                methods()
                

            elif decision.lower() == "no":
                print("\033[0;34m="*80)
                print("\n\033[1;93mOkay, thank you for spending time with me.\n")
                print("   /\_/\     (\ __ /)      A__A".center(40))
                print("  ( ˶•o•˶)    ( •ω• )     ( •⤙•  )".center(40))
                print("ଘ(ა🍱)    (ა🍙૮)｡  (🍜٩  )੭".center(40))
                print("\033[0;34m="*80)
                break
            else:
                print("\033[0;101m\033[1;30m⚠️ Please type in only Yes or No.\033[0m")
                continue
        break


