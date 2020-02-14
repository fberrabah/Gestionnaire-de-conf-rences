from model.connection import *
from controller.conferencier.displayspeaker import *
from controller.conf.displayconf import *




if __name__=='__main__':

    choix=""     
    print("\033[32m\n----------------------------------------\n\033[0m")
    print('\033[32mBienvenue dans votre application.\033[0m')
    print("\033[32m\n----------------------------------------\n\033[0m")
    while choix != "q":
       
        choix = input("\033[33m\n(s) Pour gerer les conférences.\n(c) Pour gerer les conférenciers.\n(q) Pour quitter.\nVotre choix :\033[0m").lower()
        if choix == "s":          
            gestionconf = Displayconf()
            gestionconf.menuconf()
        
        if choix == "c":
            gestionspeaker = Displayspeaker()    
            gestionspeaker.menu()   


        if choix == "q":
            print("A bientôt.")
            