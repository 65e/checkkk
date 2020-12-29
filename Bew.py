from colored import fg
import requests
import sys as n
import os
import time as mm
import time
#================================================
color3 = fg(2)
color1 = fg(1)
color2 = fg(50)
colooor = fg(1)
print(color2+'''
      •••••••••••••••••••••••
[الاداة مطورة او مبرمجة من قبل YcYca@] 
          Rights : الحقوق
          𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 ~ تلجرام   
      CHANNEL : t.me/JailTweaks
       GROUP : t.me/sol4o
     Bot : t.me/jailtweaks_bot  
      •••••••••••••••••••••••
''')
print(color2+'Checker tiktok تشيكر تيك توك - Tybe Number  -> [1]')
print(color1+'===============================')
print(color2+'Checker SnapChat | تشيكر سناب شات - Tybe Number -> [2]')
print(color1+'===============================')
print(color2+'Checker Tellnyom | تشيكر تيلينيوم - Tybe Number -> [3]')
print(color1+'===============================')
print(color2+'List Maker | صانع لستات - Tybe Number -> [4]')
print(color1+'===============================')
print(color2+'CHECK BIN | تشيكر بين - Tybe Number -> [5]')
print(color1+'===============================')
what = input(color2+'Enter Number -> : ')
if what == '4':
    print('''
•••••••••••••••••••••••
[الاداة مطورة او مبرمجة من قبل YcYca@]
          Rights : الحقوق
          𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 ~ تلجرام   
      CHANNEL : t.me/JailTweaks
       GROUP : t.me/sol4o
     Bot : t.me/jailtweaks_bot  
      •••••••••••••••••••••••
    ''')
    print('')
    print('========================================')
    print('')
    default = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x',
               'c', 'v', 'b', 'n', 'm', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '_', 'q', 'w', 'e', 'r', 't',
               'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm',
               '_']
    only_letters = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z',
                    'x', 'c', 'v', 'b', 'n', 'm']
    only_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    more_ = ['_', '1', '2', '3', '_', '4', '5', 'q', 'w', 'e', '_', 'r', 't', 'y', 'u', 'i', '_', 'o', 'p', 'a', 's',
             '_', 'd', 'f', 'g', 'h', '_', 'j', 'k', '_', 'l', 'z', 'x', '_', 'c', 'v', '_', 'b', 'n', 'm', '6', '_',
             '7', '8', '_', '9', '0', '_']
    lett = ['w', 'e', 'u', 'i', 'o', 'a', 's', 'z', 'x', 'c', 'v', 'n', 'm']

    clear = lambda: os.system("cls")

    os.system("cls")

    color1 = ("""  _     _     _      ____                           _                     _____ """)
    color2 = (""" | |   (_)___| |_   / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __  __   _|___ / """)
    color3 = (""" | |   | / __| __| | |  _ / _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__| \ \ / / |_ \ """)
    color4 = (""" | |___| \__ \ |_  | |_| |  __/ | | |  __/ | | (_| | || (_) | |     \ V / ___) |""")
    color5 = (""" |_____|_|___/\__|  \____|\___|_| |_|\___|_|  \__,_|\__\___/|_|      \_/ |____/ """)
    print(color1)
    print(color2)
    print(color3)
    print(color4)
    print(color5)
    print('')
    print('                                  ')
    print('[choose a mode]')
    print('')
    print('1: default')
    print('2: only letters "a-z"')
    print('3: only numbers "0-9"')
    print('4: default with many "_"')
    print('5: letters on the line')
    print('6: from "a" to "z" (with "numbers" and "_")')
    print('')
    mode = input('mode: ')
    clear()

    print(color1)
    print(color2)
    print(color3)
    print(color4)
    print(color5)

    save = open('list.txt', 'w')


    def mode1():
        print('')
        mode1_length = input('length: ')
        mode1_count = input('count: ')
        print('')
        if mode1_length == '2':
            for i in range(0, int(mode1_count)):
                save.write(random.choice(default) + random.choice(default) + '\n')
                print('status: ' + str(i + 1))
        elif mode1_length == '3':
            for i in range(0, int(mode1_count)):
                save.write(random.choice(default) + random.choice(default) + random.choice(default) + '\n')
                print('status: ' + str(i + 1))
        elif mode1_length == '4':
            for i in range(0, int(mode1_count)):
                save.write(random.choice(default) + random.choice(default) + random.choice(default) + random.choice(
                    default) + '\n')
                print('status: ' + str(i + 1))
        elif mode1_length == '5':
            for i in range(0, int(mode1_count)):
                save.write(random.choice(default) + random.choice(default) + random.choice(default) + random.choice(
                    default) + random.choice(default) + '\n')
                print('status: ' + str(i + 1))
        elif mode1_length == '6':
            for i in range(0, int(mode1_count)):
                save.write(random.choice(default) + random.choice(default) + random.choice(default) + random.choice(
                    default) + random.choice(default) + random.choice(default) + '\n')
                print('status: ' + str(i + 1))
        elif mode1_length == '7':
            for i in range(0, int(mode1_count)):
                save.write(random.choice(default) + random.choice(default) + random.choice(default) + random.choice(
                    default) + random.choice(default) + random.choice(default) + random.choice(default) + '\n')
                print('status: ' + str(i + 1))
        elif mode1_length == '8':
            for i in range(0, int(mode1_count)):
                save.write(random.choice(default) + random.choice(default) + random.choice(default) + random.choice(
                    default) + random.choice(default) + random.choice(default) + random.choice(default) + random.choice(
                    default) + '\n')
                print('status: ' + str(i + 1))
        elif mode1_length == '9':
            for i in range(0, int(mode1_count)):
                save.write(random.choice(default) + random.choice(default) + random.choice(default) + random.choice(
                    default) + random.choice(default) + random.choice(default) + random.choice(default) + random.choice(
                    default) + random.choice(default) + '\n')
                print('status: ' + str(i + 1))
        elif mode1_length == '10':
            for i in range(0, int(mode1_count)):
                save.write(random.choice(default) + random.choice(default) + random.choice(default) + random.choice(
                    default) + random.choice(default) + random.choice(default) + random.choice(default) + random.choice(
                    default) + random.choice(default) + random.choice(default) + '\n')

        else:
            print('error')


    def mode2():
        print('')
        mode2_length = input('length: ')
        mode2_count = input('count: ')
        print('')
        if mode2_length == '2':
            for i in range(0, int(mode2_count)):
                save.write(random.choice(only_letters) + random.choice(only_letters) + '\n')
                print('status: ' + str(i + 1))
        elif mode2_length == '3':
            for i in range(0, int(mode2_count)):
                save.write(
                    random.choice(only_letters) + random.choice(only_letters) + random.choice(only_letters) + '\n')
                print('status: ' + str(i + 1))
        elif mode2_length == '4':
            for i in range(0, int(mode2_count)):
                save.write(
                    random.choice(only_letters) + random.choice(only_letters) + random.choice(
                        only_letters) + random.choice(
                        only_letters) + '\n')
                print('status: ' + str(i + 1))
        elif mode2_length == '5':
            for i in range(0, int(mode2_count)):
                save.write(
                    random.choice(only_letters) + random.choice(only_letters) + random.choice(
                        only_letters) + random.choice(
                        only_letters) + random.choice(only_letters) + '\n')
                print('status: ' + str(i + 1))
        elif mode2_length == '6':
            for i in range(0, int(mode2_count)):
                save.write(
                    random.choice(only_letters) + random.choice(only_letters) + random.choice(
                        only_letters) + random.choice(
                        only_letters) + random.choice(only_letters) + random.choice(only_letters) + '\n')
                print('status: ' + str(i + 1))
        elif mode2_length == '7':
            for i in range(0, int(mode2_count)):
                save.write(
                    random.choice(only_letters) + random.choice(only_letters) + random.choice(
                        only_letters) + random.choice(
                        only_letters) + random.choice(only_letters) + random.choice(only_letters) + random.choice(
                        only_letters) + '\n')
                print('status: ' + str(i + 1))
        elif mode2_length == '8':
            for i in range(0, int(mode2_count)):
                save.write(
                    random.choice(only_letters) + random.choice(only_letters) + random.choice(
                        only_letters) + random.choice(
                        only_letters) + random.choice(only_letters) + random.choice(only_letters) + random.choice(
                        only_letters) + random.choice(only_letters) + '\n')
                print('status: ' + str(i + 1))
        elif mode2_length == '9':
            for i in range(0, int(mode2_count)):
                save.write(
                    random.choice(only_letters) + random.choice(only_letters) + random.choice(
                        only_letters) + random.choice(
                        only_letters) + random.choice(only_letters) + random.choice(only_letters) + random.choice(
                        only_letters) + random.choice(
                        only_letters) + random.choice(only_letters) + '\n')
                print('status: ' + str(i + 1))
        elif mode2_length == '10':
            for i in range(0, int(mode2_count)):
                save.write(
                    random.choice(only_letters) + random.choice(only_letters) + random.choice(
                        only_letters) + random.choice(
                        only_letters) + random.choice(only_letters) + random.choice(only_letters) + random.choice(
                        only_letters) + random.choice(
                        only_letters) + random.choice(only_letters) + random.choice(only_letters) + '\n')
                print('status: ' + str(i + 1))
        else:
            print('error')


    def mode3():
        print('')
        mode3_length = input('length: ')
        mode3_count = input('count: ')
        print('')
        if mode3_length == '2':
            for i in range(0, int(mode3_count)):
                save.write(random.choice(only_numbers) + random.choice(only_numbers) + '\n')
                print('status: ' + str(i + 1))
        elif mode3_length == '3':
            for i in range(0, int(mode3_count)):
                save.write(
                    random.choice(only_numbers) + random.choice(only_numbers) + random.choice(only_numbers) + '\n')
                print('status: ' + str(i + 1))
        elif mode3_length == '4':
            for i in range(0, int(mode3_count)):
                save.write(
                    random.choice(only_numbers) + random.choice(only_numbers) + random.choice(
                        only_numbers) + random.choice(
                        only_numbers) + '\n')
                print('status: ' + str(i + 1))
        elif mode3_length == '5':
            for i in range(0, int(mode3_count)):
                save.write(
                    random.choice(only_numbers) + random.choice(only_numbers) + random.choice(
                        only_numbers) + random.choice(
                        only_numbers) + random.choice(only_numbers) + '\n')
                print('status: ' + str(i + 1))
        elif mode3_length == '6':
            for i in range(0, int(mode3_count)):
                save.write(
                    random.choice(only_numbers) + random.choice(only_numbers) + random.choice(
                        only_numbers) + random.choice(
                        only_numbers) + random.choice(only_numbers) + random.choice(only_numbers) + '\n')
                print('status: ' + str(i + 1))
        elif mode3_length == '7':
            for i in range(0, int(mode3_count)):
                save.write(
                    random.choice(only_numbers) + random.choice(only_numbers) + random.choice(
                        only_numbers) + random.choice(
                        only_numbers) + random.choice(only_numbers) + random.choice(only_numbers) + random.choice(
                        only_numbers) + '\n')
                print('status: ' + str(i + 1))
        elif mode3_length == '8':
            for i in range(0, int(mode3_count)):
                save.write(
                    random.choice(only_numbers) + random.choice(only_numbers) + random.choice(
                        only_numbers) + random.choice(
                        only_numbers) + random.choice(only_numbers) + random.choice(only_numbers) + random.choice(
                        only_numbers) + random.choice(only_numbers) + '\n')
                print('status: ' + str(i + 1))
        elif mode3_length == '9':
            for i in range(0, int(mode3_count)):
                save.write(
                    random.choice(only_numbers) + random.choice(only_numbers) + random.choice(
                        only_numbers) + random.choice(
                        only_numbers) + random.choice(only_numbers) + random.choice(only_numbers) + random.choice(
                        only_numbers) + random.choice(
                        only_numbers) + random.choice(only_numbers) + '\n')
                print('status: ' + str(i + 1))
        elif mode3_length == '10':
            for i in range(0, int(mode3_count)):
                save.write(
                    random.choice(only_numbers) + random.choice(only_numbers) + random.choice(
                        only_numbers) + random.choice(
                        only_numbers) + random.choice(only_numbers) + random.choice(only_numbers) + random.choice(
                        only_numbers) + random.choice(
                        only_numbers) + random.choice(only_numbers) + random.choice(only_numbers) + '\n')
                print('status: ' + str(i + 1))
        else:
            print('error')


    def mode4():
        print('')
        mode4_length = input('length: ')
        mode4_count = input('count: ')
        print('')
        if mode4_length == '2':
            for i in range(0, int(mode4_count)):
                save.write(random.choice(more_) + random.choice(more_) + '\n')
                print('status: ' + str(i + 1))
        elif mode4_length == '3':
            for i in range(0, int(mode4_count)):
                save.write(random.choice(more_) + random.choice(more_) + random.choice(more_) + '\n')
                print('status: ' + str(i + 1))
        elif mode4_length == '4':
            for i in range(0, int(mode4_count)):
                save.write(
                    random.choice(more_) + random.choice(more_) + random.choice(more_) + random.choice(
                        more_) + '\n')
                print('status: ' + str(i + 1))
        elif mode4_length == '5':
            for i in range(0, int(mode4_count)):
                save.write(
                    random.choice(more_) + random.choice(more_) + random.choice(more_) + random.choice(
                        more_) + random.choice(more_) + '\n')
                print('status: ' + str(i + 1))
        elif mode4_length == '6':
            for i in range(0, int(mode4_count)):
                save.write(
                    random.choice(more_) + random.choice(more_) + random.choice(more_) + random.choice(
                        more_) + random.choice(more_) + random.choice(more_) + '\n')
                print('status: ' + str(i + 1))
        elif mode4_length == '7':
            for i in range(0, int(mode4_count)):
                save.write(
                    random.choice(more_) + random.choice(more_) + random.choice(more_) + random.choice(
                        more_) + random.choice(more_) + random.choice(more_) + random.choice(
                        more_) + '\n')
                print('status: ' + str(i + 1))
        elif mode4_length == '8':
            for i in range(0, int(mode4_count)):
                save.write(
                    random.choice(more_) + random.choice(more_) + random.choice(more_) + random.choice(
                        more_) + random.choice(more_) + random.choice(more_) + random.choice(
                        more_) + random.choice(more_) + '\n')
                print('status: ' + str(i + 1))
        elif mode4_length == '9':
            for i in range(0, int(mode4_count)):
                save.write(
                    random.choice(more_) + random.choice(more_) + random.choice(more_) + random.choice(
                        more_) + random.choice(more_) + random.choice(more_) + random.choice(
                        more_) + random.choice(
                        more_) + random.choice(more_) + '\n')
                print('status: ' + str(i + 1))
        elif mode4_length == '10':
            for i in range(0, int(mode4_count)):
                save.write(
                    random.choice(more_) + random.choice(more_) + random.choice(more_) + random.choice(
                        more_) + random.choice(more_) + random.choice(more_) + random.choice(
                        more_) + random.choice(
                        more_) + random.choice(more_) + random.choice(more_) + '\n')
                print('status: ' + str(i + 1))
        else:
            print('error')


    def mode5():
        print('')
        mode5_length = input('length: ')
        mode5_count = input('count: ')
        print('')
        if mode5_length == '2':
            for i in range(0, int(mode5_count)):
                save.write(random.choice(lett) + random.choice(lett) + '\n')
                print('status: ' + str(i + 1))
        elif mode5_length == '3':
            for i in range(0, int(mode5_count)):
                save.write(random.choice(lett) + random.choice(lett) + random.choice(lett) + '\n')
                print('status: ' + str(i + 1))
        elif mode5_length == '4':
            for i in range(0, int(mode5_count)):
                save.write(
                    random.choice(lett) + random.choice(lett) + random.choice(lett) + random.choice(
                        lett) + '\n')
                print('status: ' + str(i + 1))
        elif mode5_length == '5':
            for i in range(0, int(mode5_count)):
                save.write(
                    random.choice(lett) + random.choice(lett) + random.choice(lett) + random.choice(
                        lett) + random.choice(lett) + '\n')
                print('status: ' + str(i + 1))
        elif mode5_length == '6':
            for i in range(0, int(mode5_count)):
                save.write(
                    random.choice(lett) + random.choice(lett) + random.choice(lett) + random.choice(
                        lett) + random.choice(lett) + random.choice(lett) + '\n')
                print('status: ' + str(i + 1))
        elif mode5_length == '7':
            for i in range(0, int(mode5_count)):
                save.write(
                    random.choice(lett) + random.choice(lett) + random.choice(lett) + random.choice(
                        lett) + random.choice(lett) + random.choice(lett) + random.choice(
                        lett) + '\n')
                print('status: ' + str(i + 1))
        elif mode5_length == '8':
            for i in range(0, int(mode5_count)):
                save.write(
                    random.choice(lett) + random.choice(lett) + random.choice(lett) + random.choice(
                        lett) + random.choice(lett) + random.choice(lett) + random.choice(
                        lett) + random.choice(lett) + '\n')
                print('status: ' + str(i + 1))
        elif mode5_length == '9':
            for i in range(0, int(mode5_count)):
                save.write(
                    random.choice(lett) + random.choice(lett) + random.choice(lett) + random.choice(
                        lett) + random.choice(lett) + random.choice(lett) + random.choice(
                        lett) + random.choice(
                        lett) + random.choice(lett) + '\n')
                print('status: ' + str(i + 1))
        elif mode5_length == '10':
            for i in range(0, int(mode5_count)):
                save.write(
                    random.choice(lett) + random.choice(lett) + random.choice(lett) + random.choice(
                        lett) + random.choice(lett) + random.choice(lett) + random.choice(
                        lett) + random.choice(
                        lett) + random.choice(lett) + random.choice(lett) + '\n')
                print('status: ' + str(i + 1))
        else:
            print('error')


    def mode6():
        let1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '_']
        let2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '_']
        let3 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '_']
        let4 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '_']
        print('')
        user = str(input('length: '))

        i = 1
        if user == '1':
            filename = input('input file name : ')
            sta1 = time.asctime()
            for a in let1:
                omar = a
                oo1 = str(i)
                print('status: ' + oo1)
                ra = open(filename + '.txt', 'a')
                ra.writelines(omar + '\n')
                i += 1
            end1 = time.asctime()
            ra.close()
            print('count: ' + oo1 + '\n' + 'start in: ' + sta1 + '\n' + 'end in: ' + end1)
        o = 1
        if user == '2':
            filename = input('input file name : ')
            sta2 = time.asctime()
            for a in let1:
                for b in let2:
                    omar = a + b
                    oo2 = str(o)
                    print('status: ' + oo2)
                    ra = open(filename + '.txt', 'a')
                    ra.writelines(omar + '\n')
                    o += 1
            end2 = time.asctime()
            ra.close()
            print('')
            print('count: ' + oo1 + '\n' + 'start in: ' + sta1 + '\n' + 'end in: ' + end1)
        if user == '3':
            filename = input('input file name : ')
            sta3 = time.asctime()
            for a in let1:
                for b in let2:
                    for c in let3:
                        omar = a + b + c
                        oo3 = str(i)
                        print('status: ' + oo3)
                        ra = open(filename + '.txt', 'a')
                        ra.writelines(omar + '\n')
                        i += 1
            end3 = time.asctime()
            ra.close()
            print('')
            print('count: ' + oo1 + '\n' + 'start in: ' + sta1 + '\n' + 'end in: ' + end1)
        if user == '4':
            filename = input('input file name : ')
            sta4 = time.asctime()
            for a in let1:
                for b in let2:
                    for c in let3:
                        for d in let4:
                            omar = a + b + c + d
                            oo4 = str(i)
                            print('status: ' + oo4)
                            ra = open(filename + '.txt', 'a')
                            ra.writelines(omar + '\n')
                            i += 1
            end4 = time.asctime()
            ra.close()
            print('')
            print('count: ' + oo1 + '\n' + 'start in: ' + sta1 + '\n' + 'end in: ' + end1)


    if mode == '1':
        mode1()
    elif mode == '2':
        mode2()
    elif mode == '3':
        mode3()
    elif mode == '4':
        mode4()
    elif mode == '5':
        mode5()
    elif mode == '6':
        mode6()
    else:
        print('error')

    save.close()
    print('')
    input("saved, press enter to close the program.")

# ================================================
color3 = fg(2)
color1 = fg(1)
color2 = fg(50)
colooor = fg(1)
green_color = "\033[1;93m"
O = '\033[33m'  # orange
detect_color = "\033[m"
red_color = "\033[m"
end_banner_color = "\33[00m"
C = "\033[0m"
W = "\033[96m"
BRed = "\033[1;31m"
Green = "\033[0;36m"
Yellow = "\033[0;33m"
os.system('pip install time')
os.system('pip install requests')
count = 0


def slow(M):
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 200)

if what == '1':
    print(green_color + '''
    ••••••••••••••••••••••
    Rights : الحقوق
    𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 ~ تلجرام   
    CHANNEL : t.me/JailTweaks
    GROUP : t.me/sol4o
    Bot : t.me/jailtweaks_bot  
    •••••••••••••••••••••••
    ''')
    slow('''
    
    ████████╗██╗██╗  ██╗████████╗ ██████╗ ██╗  ██╗
     ╚═██╔══╝██║██║ ██╔╝╚══██╔══╝██╔═══██╗██║ ██╔╝
       ██║   ██║█████╔╝    ██║   ██║   ██║█████╔╝ 
       ██║   ██║██╔═██╗    ██║   ██║   ██║██╔═██╗ 
       ██║   ██║██║  ██╗   ██║   ╚██████╔╝██║  ██╗
       ╚═╝   ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝
    
                Coded By | jailtweaks
    
    ''')
    print("""
    •••••••••••••••••••••••                                                              
    Rights : الحقوق
    𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 ~ تلجرام   
    CHANNEL : t.me/JailTweaks
    GROUP : t.me/sol4o
    bot : t.me/jailtweaks_bot
    khalid   
    •••••••••••••••••••••••""")

    print(" ")
    time.sleep(1)
    slow("CHECKER TIKTOK VERSION 1.02 ♣️")
    time.sleep(1)

    time.sleep(1)
    print('')
    dd = 'list.txt'

    slow('[1] EnTer SessionID Manually ')
    print(" ")
    slow('[2] RaNdom SessionID')
    print('')
    t788 = input('[?] CHOOSE NUMBER :')
    if t788 == '1':
        print('''
    =========================
    id M3GON -> : 958306236
    id berlin -> : 452297375
    =========================
        ''')
        ID = input("Enter id account you here -> : ")
        print('sessionid -> : bdb93d31ef1db420d010915fd8b5081f ')
        sw = input('Enter SessionId => : ')
        tokan = ('1316607340:AAEVQUBpR0OnPRs6THQFYrCoQBlBfvNsuxU')
        if dd == "1" or " ":
            dd = dd
            password = open(dd).read().splitlines()

            # Back up one character, print a space to erase the spinner, then a newline
            # so that the prompt after the program exits isn't on the same line as our
            # message

            for password in password:
                url = "https://www.tiktok.com/api/uniqueid/check/?region=SA&aid=1233&unique_id=" + password + "&app_language=ar"
                payload = ""
                headers = {
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36",
                    "Connection": "close",
                    "Host": "www.tiktok.com",
                    "Accept-Encoding": "gzip, deflate",
                    "Cache-Control": "max-age=0"
                }
                cookies = {'sessionid': sw}
                response = requests.request("GET", url, data=payload, headers=headers, cookies=cookies)
                post = str(response.json()["status_msg"])
                if post == "" or "":
                    count += 1
                    print(Green + "{}: {}".format(count, password.strip()) + " | ✅ متوفر  ")
                    tele = (
                        f'https://api.telegram.org/bot{tokan}/sendMessage?chat_id={ID}&text=𝙷𝚄𝙽𝚃𝙴𝚁 𝙱𝙾𝚃 ☯️␈\n ♡————————-♡\n   𝙸 𝙵𝚄𝙲𝙺𝙴𝙳 𝙽𝙴𝚆 𝚄𝚂𝙴𝚁 ☠️ \n♡––––––––––––––——♡\n 𖡃 𝚄𝚂𝙴𝚁 : {password}\n𖡃 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 : @jailtweaks\n𖡃 𝙶𝚁𝙾𝚄𝙿 : @sol4o\n𖡃 INSTAGTRAM\n ♡––––––––––––––––♡ ')
                    r = requests.post(tele)
                    with open('accountfound.txt', 'a') as x:
                        x.write(password + '\n')
                else:
                    count += 1
                    print(BRed + "{}: {}".format(count, password.strip()) + " | ❌ غير متوفر  ")
    if t788 == '2':
        print(" ")
        ID = input("[!] Enter id account you here -> : ")
        tokan = ('1316607340:AAEVQUBpR0OnPRs6THQFYrCoQBlBfvNsuxU')
        print(" ")

        time.sleep(2)

        use = 'user.txt'
        headers = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36",
            "Connection": "close",
            "Host": "www.tiktok.com",
            "Accept-Encoding": "gzip, deflate",
            "Cache-Control": "max-age=0"
        }
        file = open(use, "r")

        while True:
            Check = file.readline().split('\n')[0]
            tiklog = f'https://www.tiktok.com/@{Check}'
            rq = requests.get(tiklog, headers=headers)
            if rq.status_code == 404:

                print("[√] Available -> : " + Check)
                tele = (
                    f'https://api.telegram.org/bot{tokan}/sendMessage?chat_id={ID}&text=𝙷𝚄𝙽𝚃𝙴𝚁 𝙱𝙾𝚃 ☯︎︎␈\n♡︎––––––––––––––——♡︎\n   𝙸 𝙵𝚄𝙲𝙺𝙴𝙳 𝙽𝙴𝚆 𝚄𝚂𝙴𝚁 ☠︎︎ \n♡︎––––––––––––––——♡︎\n𖡃 𝚄𝚂𝙴𝚁 : {Check}\n𖡃 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 : @jailtweaks\n𖡃 𝙶𝚁𝙾𝚄𝙿 : @sol4o\n𖡃 𝙴𝙽𝙹𝙾𝚈\n♡︎––––––––––––––——♡︎')
                r = requests.post(tele)

            elif rq.status_code == 200:
                print("[!] NoT Available -> : " + Check)
                if (Check == ""):
                    break

if what == '2':
    print('''
      •••••••••••••••••••••••
[الاداة مطورة او مبرمجة من قبل YcYca@] 
          Rights : الحقوق
          𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 ~ تلجرام   
      CHANNEL : t.me/JailTweaks
       GROUP : t.me/sol4o
     Bot : t.me/jailtweaks_bot  
      •••••••••••••••••••••••
    ''')
    print('''
███████╗███╗   ██╗ █████╗ ██████╗               
██╔════╝████╗  ██║██╔══██╗██╔══██╗              
███████╗██╔██╗ ██║███████║██████╔╝              
╚════██║██║╚██╗██║██╔══██║██╔═══╝               
███████║██║ ╚████║██║  ██║██║                   
╚══════╝╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝                   
                                                
 ██████╗██╗  ██╗███████╗ ██████╗██╗  ██╗    
██╔════╝██║  ██║██╔════╝██╔════╝██║ ██╔╝    
██║     ███████║█████╗  ██║     █████╔╝     @JailTweaks
██║     ██╔══██║██╔══╝  ██║     ██╔═██╗     
╚██████╗██║  ██║███████╗╚██████╗██║  ██╗    
 ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝╚═╝  ╚═╝
    ''')
    print('')
    print('====================================')
    print('')
    print(" \n ")

    username = input("ادخل اسم الملف -> : ")
    use = username


    def getUser(use):
        url = "https://app.snapchat.com:443/loq/suggest_username_v2"
        headers = {"Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
                   "Accept": "application/json", "Accept-Locale": "en_SA", "Connection": "close",
                   "X-Snapchat-UUID": "",
                   "x-snapchat-att": "CgsYACAAFaiThEQIChK4AXyUc_6dfBtKSeUR7bYZn0xI3IaxCqocThfdZ4fCFeoM8mrMEximQTGWrkzcyg1sjaRpG4u1K0n7-Next7xsXOUxyVojGVG1gu6BZ8_cFt0q-JMVpYEUrN6IIab-cKS9_5WiHel0tW6U04TmiXOac9dHtkIgbvF0w9J6vq3XxA8_IEF6ibfu2qkBZxvaRuCrEzZh-4GFEo_0BM6m2dJmTZTxTw5xxKwlGBIXq_yqQ7Ba-v8lfOEEzdw=",
                   "User-Agent": "Snapchat/10.87.0.69 (Twitter XcodeOn1; iOS 13.5.1; gzip)",
                   "Accept-Language": "en-SA;q=1, ar-SA;q=0.9, en-US;q=0.8, bn-SA;q=0.7, pa-SA;q=0.6",
                   "Accept-Encoding": "gzip, deflate"}
        web_data = {"req_token": "9307955c05e1ab886e3a9eeff7a501f40deb4d8219ac0a87f9b4f214dfc518eb",
                    "requested_username": use, "timestamp": "1595566579397"}
        response = requests.post(url, headers=headers, data=web_data)
        if (response.status_code == 200):
            data = response.json()
            # print(type(data))
            # print("status_code is ")
            if (data["status_code"] == "OK"):
                print(color3 + f"متاح يمكنك اخذه -> : {use}")
                with open('UserFound.txt', 'a') as x:
                    x.write(use + '\n')
            else:
                print(color1+f"غير متاح لايمكنك اخذه -> : {use}")


    file = open(use, "r")
    lines = file.readlines()
    # print(type(lines))
    # print(lines)
    for line in lines:
        line = str(line).strip()
        getUser(line)
if what == '7':
    print("""
      •••••••••••••••••••••••
 [الاداة مطورة او مبرمجة من قبل YcYca@]
          Rights : الحقوق
          𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 ~ تلجرام   
      CHANNEL : t.me/JailTweaks
       GROUP : t.me/sol4o
     Bot : t.me/jailtweaks_bot  
      •••••••••••••••••••••••
    """)
    time.sleep(2)
    print("الاداه مجانيه بالكامل انتبه من المحتالين ✖️")

    time.sleep(1)
    print("اداه استخراج فيزا 💳")
    print("                                           ")

    import random

    time.sleep(1)
    bin = input('ادخل البن الذي تريده : ')


    def cc(gen):
        ll = 10
        lst = ''
        while len(lst) != ll:
            rr = random.choice(gen)
            lst += rr

        return lst


    def dt(cvv):
        cvl = 3
        ccv = ''
        while len(ccv) != cvl:
            cvg = random.choice(cvv)
            ccv += cvg
        return ccv


    def da(nn):
        pop = 2
        das = '0'
        while len(das) != pop:
            deo = random.choice(nn)
            das += deo
        return das


    def tte(ewe):
        ttp = 4
        fdd = '202'
        while len(fdd) != ttp:
            rweh = random.choice(ewe)
            fdd += rweh
        return fdd


    ewe = '123456'
    cvv = '1234567890'
    gen = '1234567890'
    nn = '123456789'
    if len(bin) > 6:
        print('The Bin Most Be Less Than 7 Numbers')
        exit()
    while len(bin) < 6:
        bin += random.choice(cvv)
    for i in range(55):
        print(bin + cc(gen) + '|' + da(nn) + '|' + tte(ewe) + '|' + dt(cvv))

    print('تم الانتهاء بنجاح')
if what == '3':
    import requests
    import os
    from colored import fg
    import time

    os.system("pip install colored")
    color1 = fg(50)
    color2 = fg(1)

    print(" ")

    time.sleep(1)
    print("""

    ██████╗ ██╗  ██╗███████╗ ██████╗ ██╗  ██╗    
    ██╔════╝██║  ██║██╔════╝██╔════╝ ██║ ██╔╝    
    ██║     ███████║█████╗  ██║      █████╔╝       @JailTweaks
    ██║     ██╔══██║██╔══╝  ██║      ██╔═██╗     
    ╚██████╗██║  ██║███████╗╚██████╗ ██║  ██╗    
     ╚═════╝╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚═╝  ╚═╝ """)

    time.sleep(1)
    print("""
    ████████╗ ███████╗  ██╗     ██╗         
    ╚══██╔══╝ ██╔════╝  ██║     ██║         
       ██║    █████╗    ██║     ██║         
       ██║    ██╔══╝    ██║     ██║         
       ██║    ███████╗  ███████╗███████╗    
       ╚═╝    ╚══════╝  ╚══════╝╚══════╝ """)

    time.sleep(2)
    print("""
        •••••••••••••••••••••••
    [الاداة مطورة او مبرمجة من قبل YcYca@] 
              Rights : الحقوق
              𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 ~ تلجرام   
          CHANNEL : t.me/JailTweaks
           GROUP : t.me/sol4o
         Bot : t.me/jailtweaks_bot  
    """)
    print("==================================")
    time.sleep(1)
    print("💎 الاداه مجانيه بالكامل 💎 ")
    print("==================================")
    time.sleep(1)
    print("اداه تشيكر تيلينيوم اصدار 1.01 ♦")
    print("==================================")
    time.sleep(1)
    print("CHECKER TELLYNEOM VERSION 1.01 exir♦")
    time.sleep(1)
    print('==================================')
    us = input('ادخل اسم الملف الي فيه اليوزرات -> : ')
    print('')
    print('==========================================')
    print('')
    print('If you want to send you the available algorithms on your account on Telegram Act [yes] and if you do not want write [no]?')
    print('')
    print('==========================================')
    print('')
    print('إذا كنت تريد أن ارسلك اليوزرات المتاحه على حسابك في التليجرام اكتب [نعم] واذا كنت لاتريد اكتب [لا]؟')
    print('')
    t7gg = input('Enter -> : ')
    if t7gg == 'yes':
        ID = input(" : <- ضع ايدي حسابك في التيليقرام 📱 :")
        time.sleep(1)
        print("سيتم ارسال المتاحات في التيليقرام 📥")
        tokan = ('1316607340:AAG22NmS8MQSeWHHAIXZQk3C2GAn14NBblw')
        use = us
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': '__cfduid=d0ffc45fa1efa9e0d736b1c14bb6c594a1605979176; _ga=GA1.2.821290333.1605979177; G_ENABLED_IDPS=google; __gads=ID=c7705da3c1f492a3:T=1606880061:S=ALNI_MZomN5KxOkG_i59jEZaJOEsiBQi6g; _gid=GA1.2.725225671.1606979880; cf_clearance=dcd41d1895597ca22ffa90136382f60ddea9e6e2-1606979881-0-150; __rtgt_sid=ki8ibzq4bp1k2d; _gat=1',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
        }
        file = open(use, "r")
        while True:
            Check = file.readline().split('\n')[0]
            tiillog = f'https://tellonym.me/{Check}'
            rq = requests.get(tiillog, headers=headers)
            if rq.status_code == 404:
                print(color3+"[√] اليوزر متوفر -> : " + Check)
                tele = (f'https://api.telegram.org/bot{tokan}/sendMessage?chat_id={ID}&text={done} {Check}')
                r = requests.post(tele)
            elif rq.status_code == 200:
                print(colooor+"[!] اليوزر غير متوفر -> :" + Check)
                if (Check == ""):
                    break
    if t7gg == 'no':
        use = us
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': '__cfduid=d0ffc45fa1efa9e0d736b1c14bb6c594a1605979176; _ga=GA1.2.821290333.1605979177; G_ENABLED_IDPS=google; __gads=ID=c7705da3c1f492a3:T=1606880061:S=ALNI_MZomN5KxOkG_i59jEZaJOEsiBQi6g; _gid=GA1.2.725225671.1606979880; cf_clearance=dcd41d1895597ca22ffa90136382f60ddea9e6e2-1606979881-0-150; __rtgt_sid=ki8ibzq4bp1k2d; _gat=1',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
        }
        file = open(use, "r")
        while True:
            Check = file.readline().split('\n')[0]
            tiillog = f'https://tellonym.me/{Check}'
            rq = requests.get(tiillog, headers=headers)
            if rq.status_code == 404:
                print(color3+"[√] اليوزر متوفر -> : " + Check)
            elif rq.status_code == 200:
                print(colooor+"[!] اليوزر غير متوفر -> :" + Check)
                if (Check == ""):
                    break
    if t7gg == 'نعم':
        ID = input(" : <- ضع ايدي حسابك في التيليقرام 📱 :")
        time.sleep(1)
        print("سيتم ارسال المتاحات في التيليقرام 📥")
        tokan = ('1316607340:AAG22NmS8MQSeWHHAIXZQk3C2GAn14NBblw')
        use = us
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': '__cfduid=d0ffc45fa1efa9e0d736b1c14bb6c594a1605979176; _ga=GA1.2.821290333.1605979177; G_ENABLED_IDPS=google; __gads=ID=c7705da3c1f492a3:T=1606880061:S=ALNI_MZomN5KxOkG_i59jEZaJOEsiBQi6g; _gid=GA1.2.725225671.1606979880; cf_clearance=dcd41d1895597ca22ffa90136382f60ddea9e6e2-1606979881-0-150; __rtgt_sid=ki8ibzq4bp1k2d; _gat=1',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
        }
        file = open(use, "r")
        while True:
            Check = file.readline().split('\n')[0]
            tiillog = f'https://tellonym.me/{Check}'
            rq = requests.get(tiillog, headers=headers)
            if rq.status_code == 404:
                print(color3+"[√] اليوزر متوفر -> : " + Check)
                tele = (f'https://api.telegram.org/bot{tokan}/sendMessage?chat_id={ID}&text={done} {Check}')
                r = requests.post(tele)
            elif rq.status_code == 200:
                print(colooor+"[!] اليوزر غير متوفر -> :" + Check)
                if (Check == ""):
                    break
    if t7gg == 'لا':
        use = us
        headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar-AE,ar;q=0.9,en-US;q=0.8,en;q=0.7',
            'cookie': '__cfduid=d0ffc45fa1efa9e0d736b1c14bb6c594a1605979176; _ga=GA1.2.821290333.1605979177; G_ENABLED_IDPS=google; __gads=ID=c7705da3c1f492a3:T=1606880061:S=ALNI_MZomN5KxOkG_i59jEZaJOEsiBQi6g; _gid=GA1.2.725225671.1606979880; cf_clearance=dcd41d1895597ca22ffa90136382f60ddea9e6e2-1606979881-0-150; __rtgt_sid=ki8ibzq4bp1k2d; _gat=1',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
        }
        file = open(use, "r")
        while True:
            Check = file.readline().split('\n')[0]
            tiillog = f'https://tellonym.me/{Check}'
            rq = requests.get(tiillog, headers=headers)
            if rq.status_code == 404:
                print(color3+"[√] اليوزر متوفر -> : " + Check)
            elif rq.status_code == 200:
                print(colooor+"[!] اليوزر غير متوفر -> :" + Check)
                if (Check == ""):
                    break





