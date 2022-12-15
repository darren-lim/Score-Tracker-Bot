# Discord bot that keeps track of player statistics in Valorant, CSGO, etc.
# Database: AWS DynamoDB
# Excel parser: Pandas

# Start of file
import pandas as pd
import numpy as np

NUM_OF_PLAYERS = 10

class ImportData:
    
    def __init__(self, fileName):
        self.gameCount = 0
        self.fileName = fileName
        self.excelData = None
        self.playerStats = {}
        
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

        # most likely dont need this
        # gameCount = len(list(filter(lambda x: x == True, df['Games'].notnull().tolist())))
        # self.gameCount = gameCount
        # print(gameCount)
    
    def createPlayerStats(self):
        for index, row in self.excelData.iterrows():
            print(row)


if __name__ == "__main__":
    file = "scores_example.xlsx"
    importData = ImportData(file)
    importData.readExcel()
    importData.createPlayerStats()
