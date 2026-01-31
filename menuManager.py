import pandas as pd
import os

import fetchData
from teamsExtractor import teams_extract
from scoreDetailExtract import SD_extract
from tableUnion_M_SD import union_match_sd

def column_input_dict(user_input:str) -> str:
    column_dict ={
        "a":"autoClassifiedArtifacts",
        "b":"autoOverflowArtifacts",
        "c":"Leave",
        "d":"teleopClassifiedArtifacts",
        "e":"teleopOverflowArtifacts",
        "f":"Base",
        "g":"movementRP",
        "h":"goalRP",
        "i":"patternRP"
    }
    return column_dict[user_input.lower()]

def data_retreval(season: int, region_code: str) -> pd.DataFrame:
    m_response = fetchData.getInfo("M", season, region_code)
    sd_response = fetchData.getInfo("SD", season, region_code)

    robots = teams_extract(m_response)
    
    red_sd_tabel, blue_sd_tabel = SD_extract(sd_response)

    return union_match_sd(red_sd_tabel, blue_sd_tabel, robots)

def grouping_by_input(table:pd.DataFrame, column:str) -> pd.DataFrame:
    return table.groupby("Team", as_index=False, sort=True).mean().sort_values(column, ascending=False)

def main_menu():

    # Regional toluca: MXTOQ

    latest_season = 2025
    print(f"{'=' * 30}\nFTC data retreval by 6606\n{'=' * 30}")
    season_in = int(input(f"Please entre the season to retreve data from\nNote: Use the first year of the season Ex. for season 2025-2026 enter 2025\n> "))
    while(season_in > latest_season):
        season_in = int(input(f"{'!' * 10}Invalid year{'!' * 10}\nPlease entre the season to retreve data from\nNote: Use the first year of the season Ex. for season 2025-2026 enter 2025\nError note: remember that the latest season is {latest_season}\n> "))
    region_code_in = input(f"Please entre the region code\nNote: You can find this code af FTC Web event\n> ")

    os.system("cls")
    os.system("clear")
    all_teams_table = data_retreval(season_in, region_code_in)
    while True:
        group_input = input(f"""
How would you like to filter?
--- AUTO ---
A) autoClassifiedArtifacts
B) autoOverflowArtifacts
C) Leave
--- Teleop ---
D) teleopClassifiedArtifacts
E) teleopOverflowArtifacts
F) Endgame
--- Extra ---
G) movementRP
H) goalRP
I) patternRP
--- Exit ---
X) Terminate code

Please write the letter
> """)
        if(group_input == "X"):
            exit()
        print(all_teams_table.columns)
        print(grouping_by_input(all_teams_table, column_input_dict(group_input)).head())

    
