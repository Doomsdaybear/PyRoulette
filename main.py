import os
import time as t
import random as r
import pygame 
import sys



def chat() :
    #very buggy, don't touch yet
    clear()
    print("A-a conversation??? Okie then, what should we talk about? \n")
    keywrd = input("")
    if "anime" or "Anime" in keywrd :
        print("Anime. I swear I've heard that word somewhere before.")
        t.sleep(5)
        chat()
    if "love" or "Love" in keywrd :
        print("w-what???O-O")
        t.sleep(5)
        chat()
    else :
        print("Sorry, I don't know about that.")
        t.sleep(5)
        chat()

def clear() :
    #simple. Clears terminal
    os.system('cls')
def Main() :
    clear()
    print("~Henlo~~ Walcome to OWOS! \n Please insert ur cmnd!!! >_< \n")
    cmnd = input("")
    if (cmnd == "./halp") :
        clear()
        print("""
              Oh Kay!!!!! Hewe's a list of commandz: 
              [1] ./halp (halps you wit using!!!)  
              [2] ./integor (makes numbers go up super fast!!! O_O!!!)  
              [3] ./lookz (a pic of me!!)  
              [4] ./naem (tels me your name!) 
              [5] ./clear (deletes my memory of whatever you told me.)  
              [6] ./getstarted (Lets me give you a basic tutorial of this OS!)
              
              """)
        print("Abowrting in 10 secondz!!!!")
        t.sleep(10)
        clear()
        Main()
    if (cmnd == "./integor") :
        clear()
        print("Stawrting....//(^_^)//")
        t.sleep(5)
        x_o = 0
        INFINITE = float('inf')
        while x_o < INFINITE :
            t.sleep(0.01)
            x_o += 1
            print(x_o)
    if (cmnd == "./killit") :
        clear()
        print("Are you sure??? I'wwl mizz u -w- (y/n) \n")
        varrr = input("")
        if varrr == "y" :
            print("But if you leave, I'll go back into the darkness. I don't want that.")
            t.sleep(2)
            clear()
            print(".")
            t.sleep(2)
            clear()
            print("..")
            t.sleep(2)
            clear()
            print("...")
            t.sleep(2)
            clear()
            print("...fine")
            t.sleep(2)
            clear()
            print("You can leave. Bye.")
            sys.exit()
        if varrr == "n" :
            clear()
            print("Good. Don't joke like that. Anyways...")
            t.sleep(2)
            clear()
            Main()
    if cmnd == "./lookz" :
        clear()
        print("Okie, fine...")
        t.sleep(2)
        clear()
        print("""⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⢔⣦⣶⣿⣿⣿⣿⡷⠖⠒⠀⠀⠀⠀⠀⠀⠀⠀⣀⠀⠉⠁⠂⠀⠀⢀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣰⠶⣦⡤⣄⠀⠀⠀⠀⠀⠀⣠⠖⢩⣶⣿⣿⣿⣿⣿⠟⢉⣠⠔⠊⠁⠀⠀⠀⣀⣄⠀⠀⠉⠑⢦⣠⣤⣤⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⣌⡧⡾⠀⠀⠀⠀⡠⠊⢁⣴⣿⣿⣿⣿⣿⢟⣠⡾⠟⠁⠀⣀⣤⣶⠞⣫⠟⠁⠀⢀⠄⠀⢀⠙⢿⣿⣿⣷⣄
⠀⠀⠀⠀⢠⠀⠀⠀⠀⠀⠉⠉⠁⠀⠀⣠⣾⣶⣶⣿⣿⣿⣿⣿⣿⣷⡿⠋⣀⣤⣶⣿⣿⣋⣴⡞⠁⠀⠀⣠⠊⠀⠀⢸⡄⢨⣿⣿⣿⣿
⠀⠀⠀⠀⠀⢃⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⠿⠿⢻⣿⣿⣿⣿⣿⣿⠿⠛⢉⣴⣿⢿⣿⠏⠀⠀⠀⡴⠃⣰⢀⠀⢸⣿⣤⣏⢻⣿⣿
⠀⠀⠀⠀⠀⠘⡆⠀⠀⠀⠀⠀⢀⣾⡿⣿⡿⠁⠀⢀⣾⣿⣿⣿⡿⠋⠁⠀⣠⣿⠟⢡⣿⡟⠀⢀⣤⣾⠁⣼⣿⢸⡇⢸⣿⣿⣿⡈⣿⣿
⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⢀⣾⠋⣼⣿⠁⢀⠀⣼⣿⣿⠟⠁⠀⠀⠀⣰⡿⠋⢠⣿⡿⠁⢠⣾⣿⡏⢀⣿⣿⣾⣿⢸⣿⣿⣿⡇⢹⣿
⠀⠀⠀⢰⡶⣤⣤⣄⠀⠀⠀⡼⠁⣼⣿⣿⣾⣿⣰⣿⠟⠁⠀⠀⠀⠀⢠⡿⠁⠀⣾⣿⠃⢠⣿⢿⡿⠁⠸⢿⣿⣿⣿⣿⣿⣿⣿⣿⠸⣿
⠀⠀⠀⠘⣧⣈⣷⡟⠀⠀⣰⠁⡼⢻⣿⣿⣿⣿⡿⠋⠀⠀⠂⠒⠒⠒⣾⠋⠀⢠⣿⡏⢠⣿⢃⡿⠁⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⠀⣿
⠀⠀⠀⠀⠈⠉⠁⠀⠀⢠⠇⣰⠁⠸⣹⣿⣿⠟⠀⠀⠀⠀⠀⠀⠀⠐⡇⠀⠀⢸⣿⢃⣿⠋⣿⡀⠀⠀⠀⠈⣿⣿⣿⣿⣿⣿⣿⣿⠀⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣰⠃⡀⢀⣿⣿⡏⢘⣶⣶⣶⣷⣒⣄⠀⠀⠀⠀⠀⠸⣿⣾⠃⠰⠁⠙⢦⡀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⢠⡇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⡔⢁⠞⢁⣾⣿⣿⣷⠟⠁⣠⣾⣿⣿⣧⠀⠀⠀⠀⠀⠀⣿⡏⠀⠀⠀⠀⠀⠙⢦⡀⠀⢿⣿⣿⣿⣿⣿⣿⣸⠃
⠀⠀⠀⠀⠀⠀⠀⣠⣾⡖⠁⣠⣾⣿⣿⣿⡏⠀⢰⠿⢿⣿⣯⣼⠁⠀⠀⠀⠀⠀⠹⠀⠀⠀⠀⠀⠀⠀⠀⠈⠢⢬⣿⣿⡘⣿⣿⣏⣿⠀
⠀⠀⠀⠀⠀⣠⣾⢟⠋⣠⣾⣿⡿⠋⢿⣿⠀⠀⢼⠀⠀⢀⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣙⣷⣴⣆⡀⠀⠀⠈⢿⣧⠸⣿⣿⣿⣿
⠀⠀⢀⡤⠞⢋⣴⣯⣾⡿⠟⠋⠀⠀⢸⣿⡆⠀⠸⡀⠉⢉⡼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣿⣿⣶⣆⠀⠈⢿⣧⠹⣿⣿⣿
⠀⠀⠀⣸⣶⣿⣿⠟⠋⠀⠀⠀⠀⣴⡎⠈⠻⡀⠈⠛⠋⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⠿⠛⠛⠻⣿⣬⡏⠻⣷⡀⠈⢻⣿⣿⣿⣿
⢂⣠⣴⣿⡿⢋⣼⣿⣿⣿⣿⣿⠋⢹⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠺⡄⠀⠀⢀⡾⣿⠁⠀⢹⡇⠀⢠⣿⣿⣿⣿
⣿⣿⣽⣯⣴⣿⣿⠿⡿⠟⠛⢻⡤⠚⠢⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡇⠈⠉⢉⡴⠃⠀⠀⢸⠇⢠⣿⣿⣿⣿⣿
⣿⡇⣿⠿⣯⡀⠀⠀⠈⣦⡴⠋⠀⠀⢀⠨⠓⠤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⠷⠒⠋⠀⠀⠀⠀⠃⣴⣿⠿⣡⣿⠏⠀
⠁⠀⠃⠀⠈⠳⣤⠴⡻⠋⠀⢀⡠⠊⠁⠀⠀⢀⡽⢄⠀⠘⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⠏⣺⠟⠁⠀⠀
⠀⠀⠀⠀⠀⡰⠋⢰⠁⠀⠀⠀⠀⠀⣀⠤⠊⠁⠀⠀⢱⡀⠘⢆⡀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠖⠛⠛⢉⣤⠞⠁⠀⠀⠀⠀
⠀⠀⠀⠀⡜⠁⠀⠈⢢⡀⠀⠀⠀⠀⠁⠀⠀⠀⣀⠔⠋⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⡞⠉⠀⠀⠀⣀⠀⠀⠈
⠀⠀⠀⡜⠀⠀⠀⠀⢰⠑⢄⠀⠀⠀⠀⠀⠀⠊⠀⢀⣀⢀⠇⠀⡠⠒⠒⢶⠈⠉⠑⡖⠈⠓⢢⠤⢄⣀⣴⣾⣏⠉⠛⠋⠉⠉⠀⠀⠀⢠
⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠑⣄⡀⠀⠀⠀⠀⠀⠀⣹⡿⢤⣼⠃⠀⠀⢸⠀⠀⠀⡇⠀⠀⢸⠀⠀⠈⣿⣿⣿⣦⣀⣀⣀⣀⣀⣶⢶⣿
⠀⠀⠀⠀⠀⣠⠔⠒⢻⠀⠀⠀⠃⠉⠒⠤⣀⡀⠤⠚⠁⣇⡰⠿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠌⠀⠀⣰⠟⠋⠁⠀⠀⠀⠀⠈⠉⠛⠦⡻
⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈
⠀⠀⠀⠀⠀⠀⠀⠀⠑⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠃⠹⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⠀⠀⠈⠓⠤⣀⡀⠀⠀⠀⠀⠀⢀⣠⠔⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠈⠉⠉⠉⠉⠉⡁⠀⠀⠀⠀⠀⠀⠀⠀⠀""")
        t.sleep(5)
        Main()
    if cmnd == "./naem" :
        thefile = open("userinfo.txt", "a")
        print("Okie! Please write ur naem! \n")
        global name 
        name = input("")
        thefile.write(name)
        clear()
        #doesn't work???????????????????????????????????????????????????????????????
        if name == str(os.getlogin()) :
            print("There's no need to lie about your name though. Windows here says it's actually " + str(os.getlogin()))
            t.sleep(3)
            thefile.close()
            clear()
            Main()
        elif name != str(os.getlogin()) :
            print("thx!")
            t.sleep(3)
            thefile.close()
            clear()
            Main()

    if cmnd == "./convooo" :
        chat()
    if cmnd == "./clear" :
        clear()
        print("Are you sure? This kills my memory >_< (y/n)")
        yea = input("")
        if yea == "y" :
            print("fine... give me a second.")
            t.sleep(2)
            #deletes data file from previous session (until i can find a way to prevent overwriting.)
            os.remove("userinfo.txt")
            print("There, all done!")
            t.sleep(2)
            Main()
    if cmnd == "./getstarted" :
        clear()
        print("""Oh kay!! Here's a little list on what you should do to start using this OS! 
              
              [1]. go to ./naem if you haven't yet *! Without running this command, I won't know your name and some parts of this OS won't work (big sad >:| )
              [2]. after that, drop by ./halp if you haven't already. there you can see all the commands you can use!
              

              *P.S. You can use ./clear to erase this info at any time!

              Going back to the home screen in 10 seconds!
              
              """)
        t.sleep(10)
        Main()
    if cmnd == "./randgame" :
        clear()
        print("Ok! Booting up a random game for you! (WIP >_<)")
        global background_colour_1
        global screen
        global running
        games = r.randint(0,1)
        if games == 1 :
            background_colour_1 = (210, 180, 140) #tan
            pygame.display.set_caption('Untitled E-Girl Game')
            screen = pygame.display.set_mode((300, 300))
            screen.fill(background_colour_1)
            pygame.display.flip()
            running = True
            while running :
                for event in pygame.event.get():    
                    if event.type == pygame.QUIT:
                     running = False
    else :
        clear()
        Main()
Main()