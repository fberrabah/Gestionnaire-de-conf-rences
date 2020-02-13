from model.connection import *
from model.entities import *
import datetime

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
        self.date = input("Entrer une date :")
        self.hour = input("Entrer une heur :")
        self.speak_id = input("Entrer l'ID du conférencier :")
        actual_date = datetime.datetime.today()
        
        self.choice.cursor.execute("INSERT INTO conf(title, resume, date, hour, speak_id, creation_date) VALUES"
                                  "(%s, %s, %s, %s, %s, %s)" ,(self.title, self.resume, self.date , self.hour, self.speak_id, actual_date))
        self.choice.connection.commit()
        self.choice.close_connection()
        print("La conférence est enregistrée.")

    def delete(self,):
        """"method for delte user account after connect to bdd"""
        self.choice.initialize_connection()
        self.id =  input("Entrer l'ID de la conférence:")
        self.choice.cursor.execute("DELETE FROM conf WHERE id = %s;", (self.id,))
        self.choice.connection.commit()
        self.choice.close_connection()
        print("La conférence est supprimée.")   

    def show(self):

        
        sql="""SELECT * FROM conf, speaker WHERE speaker.speaker_id = conf.speak_id ORDER BY date """
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

    def update_conf(self):
        """"method for delte user account after connect to bdd"""
        column = ""
        while column not in ['title','resume', 'date', 'hour', 'speak_id']:
            self.id = input("\033[32mEntrer l'ID de la conférence :\033[0m")
            column = input("\033[35mQuelle information voulez vous modifier \n title, resume, date, hour, speak_id :\033[0m")
            datta = input("\033[35mEntrer la nouvelle information:\033[0m")
            self.choice.initialize_connection()
            self.choice.cursor.execute("UPDATE conf set " + column + " = %s WHERE id = %s ;", (datta, self.id))
            self.choice.connection.commit()
            self.choice.close_connection()
            print("Information enregistrée")
