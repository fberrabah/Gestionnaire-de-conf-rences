from model.connection import *
from model.hydra import *

class Createspeaker():

    def __init__(self):
        self.choice = connection()
        self.firstname = None
        self.name = None
        self.description = None
        self.job = None
        self.speaker_id = None

    def create(self,):
        self.choice.initialize_connection()
        self.firstname= input("Entrer votre prénom:").lower()
        self.name = input("Entrer votre nom :").lower()
        self.description = input("Entrer une description :").lower()
        self.job = input("Entrer votre métier :").lower()
        self.choice.cursor.execute("INSERT INTO speaker(firstname, name, description, job) VALUES"
                                  "(%s, %s, %s, %s)" ,(self.firstname, self.name, self.description , self.job))
        self.choice.connection.commit()
        self.choice.close_connection()
        print("Le conférencier a était enregistré.")
    
    def delete(self,):
        """"method for delte user account after connect to bdd"""
        self.choice.initialize_connection()
        self.speaker_id =  input("Enter le speaker_id :")
        self.choice.cursor.execute("DELETE FROM speaker WHERE speaker_id = %s;", (self.speaker_id,))
        self.choice.connection.commit()
        self.choice.close_connection()
        print("Le conférencier a était supprimé.")


    def show(self):
        
        sql="""SELECT * FROM speaker"""
        self.choice.initialize_connection()
        self.choice.cursor.execute(sql)
        test = self.choice.cursor.fetchall()
        self.choice.close_connection()
        for key, value in enumerate(test):
            test[key]= Hydra(value)
        return test
    
    def show_conf(self):

        test = self.show()
        if test :
            for i in test :
                print(i)
