from API_KEY import FTC_KEY
from progresBar import progressBar
import pandas as pd
import numpy as np
import requests
import time
import os

def getInfo(what_see:str, season:int, eventCode:str) -> pd.DataFrame:
    '''
    Will call the FTC API to get a response, in case of an error there will be a retry

    ## Parameters
    - **what_see** *str*\n
    \tWhat data are we looking for SD: Score details, M: Match info["SD", "M"]
    - **season** *int*\n
    \tThe year of the start of the season that we are looking for
    - **eventCode**\n
    \tThe code of the event given by FIRST

    ## Returns
    **response_pd** *DataFrame*\n
    \tReturns a DataFrame of the response of the API
    '''

    os.system("cls")
    os.system("clear")
    print("Retreaving data...")

    # header = {
    #     "Authorization":f"Basic {FTC_KEY}"
    # }

    header = {
        "Authorization":f"Basic {os.environ["FTC_KEY"]}"
    }

    if(what_see == "SD"):
        response = requests.get(f"http://ftc-api.firstinspires.org/v2.0/{season}/scores/{eventCode}/qual", headers=header)
        if(response.status_code != 200):
            os.system("cls")
            os.system("clear")
            print(f"Failed API with code {response.status_code}...\nTrying again")
            time.sleep(5)
            response = requests.get(f"http://ftc-api.firstinspires.org/v2.0/{season}/scores/{eventCode}/qual", headers=header)
        return pd.DataFrame.from_dict(response.json())
    else:
        response = requests.get(f"http://ftc-api.firstinspires.org/v2.0/{season}/matches/{eventCode}?tournamentLevel=qual", headers=header)
        if(response.status_code != 200):
            os.system("cls")
            os.system("clear")
            print(f"Failed API with code {response.status_code}...\nTrying again")
            time.sleep(5)
            response = requests.get(f"http://ftc-api.firstinspires.org/v2.0/{season}/matches/{eventCode}?tournamentLevel=qual", headers=header)
        return pd.DataFrame.from_dict(response.json())
