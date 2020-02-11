from model.connection import *
from controller.conferencier.create import *


class Gestionpeaker():
    def menu(self):

        info=""    
        
        print("\033[35m\n----------------------------------------\n\033[0m")
        print('\033[35mBienvenue dans votre application.\033[0m')
        print("\033[35m\n----------------------------------------\n\033[0m")
        while info != "q":
            
            info = input("\033[34m\n(c) Pour créer un conférencier.\n(s) Pour supprimer les conférenciers.\n(q) Pour quitter.\nVotre choix :\033[0m").lower()
            if info == "s":
                log = Createspeaker()
                log.delete()     
                
            if info == "c":  
                log = Createspeaker()
                log.create()        
                    

            if info == "q":
                print("A bientôt.")
                    