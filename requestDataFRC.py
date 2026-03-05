from API_KEY import FRC_KEY
import pandas as pd
import requests

def teams_request(region_code):
    header_FRC = {
        "Authorization":f"Basic {FRC_KEY}"
    }
    
    response_teams = requests.get(f"https://frc-api.firstinspires.org/v3.0/2026/matches/{region_code}?tournamentLevel=Qualification", headers=header_FRC)
    if(response_teams.status_code == 401):
        raise PermissionError("API kry having problems")
    else:
        return response_teams
    
def scoreDetail_request(region_code):
    header_FRC = {
        "Authorization":f"Basic {FRC_KEY}"
    }
    
    response_SD = requests.get(f"https://frc-api.firstinspires.org/v3.0/2026/scores/{region_code}/Qualification", headers=header_FRC)
    if(response_SD.status_code == 401):
        raise PermissionError("API kry having problems")
    else:
        return response_SD