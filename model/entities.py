from model.connection import *
from model.hydra import *

class Read():
    """class for user read this account"""
    def __init__(self):
        self.choice = connection()


    def read(self):
        
        sql="""SELECT speaker_id, firstname, name, description, job FROM speaker"""
        self.choice.initialize_connection()
        self.choice.cursor.execute(sql)
        test = self.choice.cursor.fetchall()
        self.choice.close_connection()
        for key, value in enumerate(test):
            test[key]= Hydra(value)
        return test


