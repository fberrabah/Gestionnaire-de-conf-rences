class Hydra():
    def __init__(self, i=False ): #add constructor with value none
        self.title = None
        self.resume = None
        self.date = None
        self.hour = None
        self.speak_id = None
        self.id = None
        self.name = None
        self.firstname = None
        if i:
            self.hydrat(i)


    def hydrat(self, i): 
        for key, value in i.items():
            if hasattr(self, key):
                setattr(self, key, value)


    def __str__(self):
        return"""\033[36m L'ID : {} \n Le titre : {}\n Le résumé : {}\n La date : {}\n L'heure : {}\n ID du conférencier : {}\n Nom du conférencier : {}\n Prénom du conférencier : {}\n~~~~~~~~~~~~~~~~~~~~\033[0m""".format(self.id, self.title, self.resume, self.date, self.hour, self.speak_id, self.name, self.firstname)