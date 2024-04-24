
import numpy as np
import pymysql

class Game:
    def __init__(self):
        self.name = ""
        self.map = np.array([[" "," "," "],[" "," "," "],[" "," "," "]])
        self.ai_row = 0
        self.ai_col = 0
        self.rowplayer = 0
        self.colplayer = 0
    
    def __del__(self):
        print("Game has been deleted. ")

class Player_record(Game):

    def insert_score_database(self, winner):
        myconnection = pymysql.connect(host="localhost", user="root", password="", db="TicTacToe")
        mycursor = myconnection.cursor()
        insert_query = "INSERT INTO GameScore (Name, Score) VALUES ('{}'{}')".format(winner, '1')
        mycursor.execute(insert_query)
        myconnection.commit()
        myconnection.close()
    
    def Show_player_record():
        myconnection = pymysql.connect(host= "localhost", user='root',password='', db="TicTacToe")
        mycursor = myconnection.cursor()
        select_query = "SELECT * FROM GameScore"
        mycursor.execute(select_query)
        results = mycursor.fetchall()
        print(results)
        mycursor.close()