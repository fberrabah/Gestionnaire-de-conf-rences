from model.connection import *
from controller.conf.gestionconf import *


class Gestionconf():
    def menuconf(self):


        info=""    
        
        print("\033[38m\n----------------------------------------\n\033[0m")
        print('\033[38mBienvenue dans votre gestionnaire de conférence.\033[0m')
        print("\033[38m\n----------------------------------------\n\033[0m")
        while info != "q":
            
            info = input("\033[34m\n(v) Pour voir toute les conferences programmées.\n(c) Pour créer une conférence.\n(s) Pour supprimer une conférennce.\n(q) Pour quitter.\nVotre choix :\033[0m").lower()
            if info == "s":
                ajout = Createconf()
                ajout.delete()
                
            if info == "c":  
                ajout = Createconf()
                ajout.create()

            if info == "v":  
                pass
                     
                    

            if info == "q":
                print("A bientôt.")
                    