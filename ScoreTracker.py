# Discord bot that keeps track of player statistics in Valorant, CSGO, etc.
# Database: AWS DynamoDB
# Excel parser: Pandas

# Start of file
import pandas as pd
import numpy as np
import json
import os
from dotenv import load_dotenv
from pymongo import MongoClient

def getDatabase():
    # Provide the mongodb atlas url to connect python to mongodb using pymongo
    password = os.getenv('MONGODB_PASSWORD')
    CONNECTION_STRING = f"mongodb+srv://burger:{password}@burgerinvitational.vmpfooj.mongodb.net/?retryWrites=true&w=majority"

    # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Create the database for our example (we will use the same database throughout the tutorial
    return client['BurgerInvitational']


# https://www.mongodb.com/languages/python

class ImportData:
    
    def __init__(self, fileName, databaseConnection):
        self.db = databaseConnection
        self.fileName = fileName
        self.playerExcelData = None
        self.gamesExcelData = None
        self.playerStats = {}

        # add team stats
        self.teamStats = {}
        
        '''
        player stats example
        {
            Burger: {
                games_played: 1,
                team: 'GAC',
                combat_score: 174,
                kills: 11,
                deaths: 15,
                assists: 4
            }
        }
        '''

    def readExcel(self):
        # Read the Excel file and create pandas dataframe
        self.playerExcelData = pd.read_excel(self.fileName, usecols="B:G")
        self.gamesExcelData = pd.read_excel(self.fileName, usecols="A")
        # Print the first few rows of the dataframe
        #print(df.head(21))

    def createTeamStats(self):
        for index, row in self.gamesExcelData.iterrows():
            games = row['Games']
            print(games)

        '''
        example:
        "GAC": {
                "wins": "1",
                "losses": 2,
                "total_played": 3,

            }
        '''
    
    def createPlayerStats(self):
        for index, row in self.playerExcelData.iterrows():
            player = row['Player']
            if player not in self.playerStats:
                self.playerStats[player] = {
                    'team': row['Team']
                }
            
            self.playerStats[player]['games_played'] = self.playerStats[player].get('games_played', 0) + 1
            self.playerStats[player]['total_combat_score'] = self.playerStats[player].get('total_combat_score', 0) + row['Combat Score']
            self.playerStats[player]['total_kills'] = self.playerStats[player].get('kills', 0) + row['Kills']
            self.playerStats[player]['total_deaths'] = self.playerStats[player].get('deaths', 0) + row['Deaths']
            self.playerStats[player]['total_assists'] = self.playerStats[player].get('assists', 0) + row['Assists']
            self.playerStats[player]['avg_combat_score'] = self.playerStats[player].get('total_combat_score', 0) // self.playerStats[player].get('games_played', 1)
            self.playerStats[player]['avg_kills_per_game'] = self.playerStats[player].get('total_kills', 0) // self.playerStats[player].get('games_played', 1)
            self.playerStats[player]['avg_deaths_per_game'] = self.playerStats[player].get('total_deaths', 0) // self.playerStats[player].get('games_played', 1)
            self.playerStats[player]['avg_assists_per_game'] = self.playerStats[player].get('total_assists', 0) // self.playerStats[player].get('games_played', 1)
        
        print(json.dumps(self.playerStats, indent = 4))

        '''
        example:
        "Burger": {
            "team": "GAC",
            "games_played": 2,
            "combined_combat_score": 459,
            "kills": 30,
            "deaths": 29,
            "assists": 4,
            "avg_combat_score": 229 
            }
        '''

if __name__ == "__main__":
    database = getDatabase()
    print(database)
    file = "scores_example.xlsx"
    importData = ImportData(file, database)
    importData.readExcel()
    # importData.createPlayerStats()
    # importData.createTeamStats()
