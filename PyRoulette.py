import os
import time as t
import colorama
import random as r
colorama.init()
global numer
global let
global Red 
global Black 

def clear() :
    os.system('cls')
def Main(cash) :
    clear()
    print(colorama.Fore.WHITE, "Welcome to PyRoulette! Please enter wager: \n")
    print(colorama.Fore.GREEN, "Current Cash: ", cash)
    wager = input("")
    wagero = int(wager)
    if wagero > cash :
        clear()
        print(colorama.Fore.RED, "DON'T FUCK WITH ME ON THIS.")
        t.sleep(5)
        Main()
    clear()
    print(colorama.Fore.WHITE, "Alright! Now please select a number between 0 and 36! Or, bet on Red or Black by typing R or B respectively. \n") #IM SO SORRY I DONT WANT TO CODE AMERICAN ROULETTE WITH 00
    num = input("")
    
    if num == "R" or "G" :
        let = str(num)
        numer = r.randint(0,37)
        clear()
        print(colorama.Fore.WHITE, "All bets off the table! Rolling now...")
        Red = [3,12,7,18,9,14,1,16,5,23,30,36,27,34,25,19,21,32]
        Black = [26,35,28,29,32,21,20,33,24,10,8,11,13,6,17,2,4,15]
        if let == "R":
            if numer in Red :
                print(colorama.Fore.RED, numer, "\n")
                print(colorama.Fore.GREEN, "You win! Your wager has been multiplied by 1.5! Current cash: ", cash + wagero*1.5)
                cash = cash + wagero * 1.5
                t.sleep(5)
                Main(cash)
            if numer in Black :
                print(colorama.Fore.BLACK, numer, "\n")
                print(colorama.Fore.RED, "You lost! Your wager has been subtracted from your account. Current cash: ", cash - wagero)
                cash = cash - wagero
                t.sleep(5)
                Main(cash)
        if let == "B" :
            if numer in Red :
                print(colorama.Fore.BLACK, numer, "\n")
                print(colorama.Fore.RED, "You lost! Your wager has been subtracted from your account. Current cash: ", cash - wagero)
                cash = cash - wagero
                t.sleep(5)
                Main(cash)

            if numer in Black :
                print(colorama.Fore.RED, numer, "\n")
                print(colorama.Fore.GREEN, "You win! Your wager has been multiplied by 1.5! Current cash: ", cash + wagero*1.5)
                cash = cash + wagero * 1.5
                t.sleep(5)
                Main(cash)
    if num.isdigit() == True :
        numo = int(num)
        if numo > 36 :
            print(colorama.Fore.RED, "Once again...")
            Main(cash)
        if numo < 0 :
            print(colorama.Fore.RED, "Once again...")
            Main(cash)
        clear()
        print(colorama.Fore.WHITE, "All bets off the table! Rolling now....")
        numer = r.randint(0,37)
        if numer == numo :
            print(colorama.Fore.GREEN, numer, "\n")
            print(colorama.Fore.GREEN, "You win! Your wager has been doubled! Current cash: ", cash + wagero*2)
            cash = cash + wagero*2
            t.sleep(5)
            Main(cash)
        if numer != numo :
            print(colorama.Fore.BLACK, numer, "\n")
            print(colorama.Fore.RED, "You have lost! Your wager has been subtracted from your account. Current cash: ", cash - wagero)
            cash = cash-wagero
            t.sleep(5)
            Main(cash)

Main(cash=100)