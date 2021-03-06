from model.connection import *
from controller.conferencier.gestionspeaker import *

class Displayspeaker():
    def menu(self):

        info=""    
        
        print("\033[35m\n----------------------------------------\n\033[0m")
        print('\033[35mBienvenue dans votre gestionnaire de conférencier.\033[0m')
        print("\033[35m\n----------------------------------------\n\033[0m")
        while info != "q":
            
            info = input("\033[34m\n(v) Pour voir la liste des conférenciers.\n(c) Pour créer un conférencier.\n(m) Pour modifier les informations d'un conférencier.\n(s) Pour supprimer les conférenciers.\n(q) Pour quitter.\nVotre choix :\033[0m").lower()
            if info == "s":
                log = Gestionspeaker()
                log.delete()     
                
            if info == "c":  
                log = Gestionspeaker()
                log.create()    

            if info == "m":  
                log = Gestionspeaker()
                log.update_speaker()   

            if info == "v":  
                log = Gestionspeaker()
                log.show_conf()        
                     
                    

            if info == "q":
                print("A bientôt.")
                    