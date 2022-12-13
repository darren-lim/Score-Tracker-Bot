# Discord bot that keeps track of player statistics in Valorant, CSGO, etc.
# Database: AWS DynamoDB
# Excel parser: Pandas

# Start of file
import pandas as pd

def readExcel():
    # Read the Excel file
    df = pd.read_excel("scores_example.xlsx")

    # Print the first few rows of the dataframe
    print(df.head())

if __name__ == "__main__":
    readExcel()
