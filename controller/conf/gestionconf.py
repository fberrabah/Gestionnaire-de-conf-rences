from model.connection import *

class Createconf():

    def __init__(self):
        self.choice = connection()
        self.title = None
        self.resume = None
        self.date = None
        self.hour = None
        self.create_date = None
        self.speak_id = None 
        self.id = None

    def create(self,):
        self.choice.initialize_connection()
        self.title= input("Entrer un titre:").lower()
        self.resume = input("Entrer un résumé :").lower()
        self.date = input("Entrer une date :").lower()
        self.hour = input("Entrer une heur :").lower()
        self.speak_id = input("Entrer l'ID du conférencier :")
        
        self.choice.cursor.execute("INSERT INTO conf(title, resume, date, hour, speak_id) VALUES"
                                  "(%s, %s, %s, %s, %s)" ,(self.title, self.resume, self.date , self.hour, self.speak_id))
        self.choice.connection.commit()
        self.choice.close_connection()
        print("La conférence a était enregistré.")

    def delete(self,):
        """"method for delte user account after connect to bdd"""
        self.choice.initialize_connection()
        self.id =  input("Enter l'ID de la conference:")
        self.choice.cursor.execute("DELETE FROM conf WHERE id = %s;", (self.id,))
        self.choice.connection.commit()
        self.choice.close_connection()
        print("Le conférence a était supprimé.")   