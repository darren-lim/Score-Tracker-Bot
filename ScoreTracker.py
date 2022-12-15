# Discord bot that keeps track of player statistics in Valorant, CSGO, etc.
# Database: AWS DynamoDB
# Excel parser: Pandas

# Start of file
import pandas as pd
import numpy as np
import json

NUM_OF_PLAYERS = 10

class ImportData:
    
    def __init__(self, fileName):
        self.fileName = fileName
        self.excelData = None
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
        df = pd.read_excel(self.fileName)
        self.excelData = df

        # Print the first few rows of the dataframe
        #print(df.head(21))

    def createTeamStats(self):
        # games = list(filter(lambda x: x == True, df['Games'].notnull().tolist()))
        pass
    
    def createPlayerStats(self):
        for index, row in self.excelData.iterrows():
            player = row['Player']
            if player not in self.playerStats:
                self.playerStats[player] = {
                    'team': row['Team']
                }
            
            self.playerStats[player]['games_played'] = self.playerStats[player].get('games_played', 0) + 1
            self.playerStats[player]['combat_score'] = self.playerStats[player].get('combat_scoere', 0) + row['Combat Score']
            self.playerStats[player]['kills'] = self.playerStats[player].get('kills', 0) + row['Kills']
            self.playerStats[player]['deaths'] = self.playerStats[player].get('deaths', 0) + row['Deaths']
            self.playerStats[player]['assists'] = self.playerStats[player].get('assists', 0) + row['Assists']
        
        print(json.dumps(self.playerStats, indent = 4))



if __name__ == "__main__":
    file = "scores_example.xlsx"
    importData = ImportData(file)
    importData.readExcel()
    importData.createPlayerStats()
