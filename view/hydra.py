class Hydra():
    def __init__(self, i=False ): #add constructor with value none
        self.firstname = None
        self.name = None
        self.job = None
        self.description = None
        self.speaker_id = None
        if i:
            self.hydrat(i)


    def hydrat(self, i): 
        for key, value in i.items():
            if hasattr(self, key):
                setattr(self, key, value)


    def __str__(self):
        return"""\033[36m L'ID : {} \n Le prénom : {}\n Le nom : {}\n Métier : {}\n Description : {}\n~~~~~~~~~~~~~~~~~~~~\033[0m""".format(self.speaker_id, self.firstname, self.name, self.job, self.description)