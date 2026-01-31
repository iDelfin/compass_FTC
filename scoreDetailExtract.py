import pandas as pd
import requests
import os

def SD_extract(SD_response):

    os.system("cls")
    os.system("clear")
    print("Getting score details...")

    response_SD_pd = SD_response.copy()
    response_SD_pd = response_SD_pd["matchScores"].apply(pd.Series)
    alliance_SD_pd = response_SD_pd["alliances"].apply(pd.Series)
    blue_SD_pd = alliance_SD_pd[0].apply(pd.Series)
    red_SD_pd = alliance_SD_pd[1].apply(pd.Series)

    return(red_SD_pd, blue_SD_pd)