from TV import TV
import pyfiglet
import time
import sys

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
            print("⚠️ Input error.")
        except Exception as e:
            print("⚠️ Error:", e)
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
            print("⚠️ Input error.")
        except Exception as e:
            print("⚠️ Error:", e)
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
            print("⚠️ Input Error, type in only True or False.")
            continue

    tv = TV(channel, volume_level, on)



print("📺-🔌-🎮-"*10)
print("\033[0;34m")
banner = pyfiglet.figlet_format("TV OPERATIONS", font="slant", justify="center")
print(banner)
print("\033[0m")
print("📺-🔌-🎮-"*10)


while True:
    option = (input("Press 1 to continue to test drive and press 2 to skip the test: "))
    if option == "2":
        process()

        # Ask the user to perform methods
        while True:
            print("="*80)
            decision = input("Do you want to create new obejct for TV? Type Yes or No: ")

            # If yes, repeat the process.
            if decision.lower() == "yes":
                process()
                while True:
                    method = (input("\nPlease select a method to perform: \033[0m\n\033[1;30mA.Turn On\n\033[1;31mB.Turn Off\n\033[1;32mC.Get Channel\n\033[1;33mD.Set Channel\n\033[1;34mE.Get Volume\n\033[1;35mF.Set Volume\n\033[1;36mG.Channel Up\n\033[1;37mH.Channel Down\n\033[1;30mI.Volume Up\n\033[1;31mJ.Volume Down\n\033[1;32mK.End Program\n\033[4;35m"))
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
                                print("⚠️ Input error.")
                            except Exception as e:
                                print("⚠️ Error:", e)
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
                                print("⚠️ Input error.")
                            except Exception as e:
                                print("⚠️ Error:", e)
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
                        break

                    else:
                        print("⚠️ Invalid Input.")
                        continue

            elif decision.lower() == "no":
                print("\033[0;34m="*80)
                print("\n\033[1;93mOkay, thank you for spending time with me.\n")
                print("\033[0;34m="*80)
                break
            else:
                print("⚠️ Please type in only Yes or No.")
                continue
        break
        
    if option == "1":
        # Test Driver
        print()
        print("📺-🔌-🎮-"*10)
        banner = pyfiglet.figlet_format("Test Drivers", font="slant", justify="center")
        print(banner)
        print("📺-🔌-🎮-"*10)
        print()
        tv_1 = TV(30, 3, True)
        tv_2 = TV(3, 2, True)
        print("TV 1 is in channel 30 with volume level of 3 and is currently on.")
        print("TV 2 is in channel 2 with volume level of 2 and is currently on.")
        print()
        print("Loading: ".center(90))
        # Make a loading animation.
        animation = ["🎥 . . . . . . .".center(70),"🎥 🎞 . . . . . .".center(70), "🎥 🎞 📽 . . . . .".center(70), "🎥 🎞 📽 📺 . . . .".center(70), "🎥 🎞 📽 📺 📷 . . .".center(70), "🎥 🎞 📽 📺 📷 📸 . .".center(70), "🎥 🎞 📽 📺 📷 📸 📹 .".center(70), "🎥 🎞 📽 📺 📷 📸 📹 📼".center(70)]
        for i in range(len(animation)):
            time.sleep(0.2)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        print("\n")

        print("\n"+"*"*90)
        print("When the TV is Turned on: ")
        print("For TV 1:")
        tv_1.TurnOn()
        print("\nFor TV 2:")
        tv_2.TurnOn()

        print("*"*90)
        print("Get the channel: ")
        print("For TV 1:")
        tv_1.GetChannel()
        print("\nFor TV 2:")
        tv_2.GetChannel()

        print("\n"+"*"*90)
        print("Set the channel: (In this test, to channel 4)")
        print("For TV 1:")
        tv_1.SetChannel(4)
        print("\nFor TV 2:")
        tv_2.SetChannel(4)

        print("\n"+"*"*90)
        print("Get the volume level: ")
        print("For TV 1:")
        tv_1.GetVolume()
        print("\nFor TV 2:")
        tv_2.GetVolume()

        print("\n"+"*"*90)
        print("Set the volume level: (In this test, to 7)")
        print("For TV 1:")
        tv_1.SetVolume(7)
        print("\nFor TV 2:")
        tv_2.SetVolume(7)

        print("\n"+"*"*90)
        print("Channel up: ")
        print("For TV 1:")
        tv_1.ChannelUp()
        print("\nFor TV 2:")
        tv_2.ChannelUp()

        print("\n"+"*"*90)
        print("\Channel down: ")
        print("For TV 1:")
        tv_1.ChannelDown()
        print("\nFor TV 2:")
        tv_2.ChannelDown()

        print("\n"+"*"*90)
        print("Increase volume level: ")
        print("For TV 1:")
        tv_1.VolumeUp()
        print("\nFor TV 2:")
        tv_2.VolumeUp()

        print("\n"+"*"*90)
        print("Decrease volume level: ")
        print("For TV 1:")
        tv_1.VolumeDown()
        print("\nFor TV 2:")
        tv_2.VolumeDown()

        print("\n"+"*"*90)
        print("When the TV is turned off:")
        print("For TV 1:")
        tv_1.TurnOff()
        print("\nFor TV 2:")
        tv_2.TurnOff()

        print("\n"+"*"*90)

        create = input("Do you want to create a new TV object? Type yes or No :")
        print("Loading:\033[0m".center(90))
    # Make a loading animation.
        animation = ["🎥 . . . . . . .".center(70),"🎥 🎞 . . . . . .".center(70), "🎥 🎞 📽 . . . . .".center(70), "🎥 🎞 📽 📺 . . . .".center(70), "🎥 🎞 📽 📺 📷 . . .".center(70), "🎥 🎞 📽 📺 📷 📸 . .".center(70), "🎥 🎞 📽 📺 📷 📸 📹 .".center(70), "🎥 🎞 📽 📺 📷 📸 📹 📼".center(70)]
        for i in range(len(animation)):

            time.sleep(0.2)
            sys.stdout.write("\r" + animation[i % len(animation)])
            sys.stdout.flush()
        print("\n")
        if create.lower() == "yes":
            process()
        if create.lower() == "no":
            print("\033[1;93mOkay, thank you for spending time with me.")
            break
    else:
        print("⚠️ Please type in only Yes or No.")
        continue


# # Creation of new objects:
# def process():
#     global tv
#     tv = input("Please input a name for your TV: ")
# # Get the name of the object
# # Get the channel of the object
#     while True:
#         try:
#             channel = int(input("Input the channel [1-120]: "))
#             if channel > 120:
#                 raise Exception("Sorry, channels are 1-120 only.")
#             else:
#                 break
#         except ValueError:
#             print("⚠️ Input error.")
#         except Exception as e:
#             print("⚠️ Error:", e)
#             continue

# # Get the volume level of the object
#     while True:
#         try:
#             volume_level = int(input("Input the volume level [1-7]: "))
#             if volume_level > 7:
#                 raise Exception("Sorry, volume level is only 1-7 only.")
#             else:
#                 break
#         except ValueError:
#             print("⚠️ Input error.")
#         except Exception as e:
#             print("⚠️ Error:", e)
#             continue    
#         except ValueError:
#             print("Input error.")
#             continue
# # Ask the user whether the object is on or off
#     while True:
#         user_input = input("Please type in True if the TV is on and False if the TV is off: ")
#         if user_input.lower() == "true":
#             on = True
#             break
#         elif user_input.lower() == "false":
#             on = False
#             break
#         else:
#             print("⚠️ Input Error, type in only True or False.")
#             continue

#     tv = TV(channel, volume_level, on)

# # Ask the user to perform methods
# while True:
#     print("="*80)
#     decision = input("Do you want to create new obejct for TV? Type Yes or No: ")

#     # If yes, repeat the process.
#     if decision.lower() == "yes":
#         process()
#         while True:
#             method = (input("\nPlease select a method to perform: \033[0m\n\033[1;30mA.Turn On\n\033[1;31mB.Turn Off\n\033[1;32mC.Get Channel\n\033[1;33mD.Set Channel\n\033[1;34mE.Get Volume\n\033[1;35mF.Set Volume\n\033[1;36mG.Channel Up\n\033[1;37mH.Channel Down\n\033[1;30mI.Volume Up\n\033[1;31mJ.Volume Down\n\033[1;32mK.End Program\n\033[4;35m"))
#             print("\033[0m")
#             print("\033[0;100mLoading:\033[0m".center(90))
#             # Make a loading animation.
#             animation = ["🎥 . . . . . . .".center(70),"🎥 🎞 . . . . . .".center(70), "🎥 🎞 📽 . . . . .".center(70), "🎥 🎞 📽 📺 . . . .".center(70), "🎥 🎞 📽 📺 📷 . . .".center(70), "🎥 🎞 📽 📺 📷 📸 . .".center(70), "🎥 🎞 📽 📺 📷 📸 📹 .".center(70), "🎥 🎞 📽 📺 📷 📸 📹 📼".center(70)]
#             for i in range(len(animation)):
#                 time.sleep(0.2)
#                 sys.stdout.write("\r" + animation[i % len(animation)])
#                 sys.stdout.flush()
#             print("\n")
#             method == method.lower()
#             if method == "a":
#                 tv.TurnOn()
#                 break

#             if method == "b":
#                 tv.TurnOff()
#                 break

#             if method == "c":
#                 tv.GetChannel()
#                 break
                
#             if method == "d":
#                 while True:
#                     try:
#                         input_channel = int(input("\033[0;34mInput the new channel [1-120]: "))
#                         if input_channel > 120:
#                             raise Exception("Sorry, channels are 1-120 only.")
#                         else:
#                             break
#                     except ValueError:
#                         print("⚠️ Input error.")
#                     except Exception as e:
#                         print("⚠️ Error:", e)
#                         continue
#                 tv.SetChannel(input_channel)
#                 break

#             if method == "e":
#                 tv.GetVolume()
#                 break

#             if method == "f":
#                 while True:
#                     try:
#                         input_volume = int(input("\033[0;34mInput the new volume level [1-7]: "))
#                         if input_volume > 7:
#                             raise Exception("Sorry, volume level is 1-7 only.")
#                         else:
#                             break
#                     except ValueError:
#                         print("⚠️ Input error.")
#                     except Exception as e:
#                         print("⚠️ Error:", e)
#                         continue
#                 tv.SetVolume(input_volume)
#                 break

#             if method == "g":
#                 tv.ChannelUp()
#                 break

#             if method == "h":
#                 tv.ChannelDown()
#                 break

#             if method == "i":
#                 tv.VolumeUp()
#                 break

#             if method == "j":
#                 tv.VolumeDown()
#                 break

#             if method == "k":
#                 print("\033[1;93mOkay, thank you for using this program.")
#                 break

#             else:
#                 print("⚠️ Invalid Input.")
#                 continue

#     elif decision.lower() == "no":
#         print("\033[0;34m="*80)
#         print("\n\033[1;93mOkay, thank you for using this program.\n")
#         print("\033[0;34m="*80)
#         break
#     else:
#         print("⚠️ Please type in only Yes or No.")
#         continue
