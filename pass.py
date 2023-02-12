from time import sleep
from os import system
from colorama import Fore as f 
from random import *
import string
from time import sleep
import pyfiglet

blue = '\033[94m'
green =  '\033[92m'

print(f"""{blue}     __  __
    / / / /{f.RED}  Github > {f.YELLOW}https://github.com/Zrexer/PassGen{blue} 
   / /_/ /{f.BLUE}   PassGen version {green} 6.0.0{blue}
  / __  /{f.MAGENTA}    Creator >{f.CYAN} host1let{blue} 
 /_/ /_/
\n
""")


def cl():
    
    yt = str(input(f"{f.MAGENTA}Do You Want To Use Again?{f.BLUE}{f.GREEN} <yes-no> :{f.YELLOW} "))

    if yt == "yes":
        print("")
        y()
    
    elif yt == "clear":
        from os import system
        system("clear")    
        cl()
    
    elif yt == "no":
        print("")
    
   
    else:
        print(f"{f.RED}Invalid !!!")
        sleep(3)
        cl()    




def y():
    
    char = string.ascii_letters + string.punctuation + string.digits

    password = "".join(choice(char) for x in range(randint(8,16)))

    print(f"{f.RED}Your password >{f.CYAN} {password}")

    print("")

    yt = str(input(f"{f.MAGENTA}Do You Want To Use Again?{f.BLUE}{f.GREEN} <yes-no> :{f.YELLOW} "))

    if yt == "yes":
        print("")
        y()
    
    elif yt == "clear":
        from os import system
        system("clear")    
        cl()
    
    
    elif yt == "no":
        print("")
    
    else:
        print(f"{f.RED}Invalid !!!")
        sleep(3)
        cl()    




char = string.ascii_letters + string.punctuation + string.digits

password = "".join(choice(char) for x in range(randint(8,16)))

print(f"{f.RED}Your password >{f.CYAN} {password}")

print("")

yt = str(input(f"{f.MAGENTA}Do You Want To Use Again?{f.BLUE}{f.GREEN} <yes-no> :{f.YELLOW} "))

if yt == "yes":
    print("")
    y()
    
elif yt == "clear":
    from os import system
    system("clear")    
    cl()
    
    
elif yt == "no":
    print("")
    
else:
    print(f"{f.RED}Invalid !!!")
    sleep(3)
    cl()
