import pandas as pd
from teamExtractorFRC import teams_involved_FRC
from scoreDetailExtractFRC import SD_extractor_FRC
from requestDataFRC import teams_request, scoreDetail_request

def data_resume_FRC(region_code):
    station_number = {
        "Red1" : "Robot1",
        "Red2" : "Robot2",
        "Red3" : "Robot3",
        "Blue1" : "Robot1",
        "Blue2" : "Robot2",
        "Blue3" : "Robot3",
    }

    robots_info_df = []

    robots_FRC = teams_involved_FRC(teams_request(region_code))
    df_red_score, df_blue_score = SD_extractor_FRC(scoreDetail_request(region_code))

    for station in robots_FRC.columns:
        if (station.find("Red") != -1):
            specific_robot = df_red_score[[f'autoTower{station_number[station]}', f'endGameTower{station_number[station]}', 'energizedAchieved', 'superchargedAchieved', 'traversalAchieved', 'rp', 'totalPoints']]
            robot_info_colomn_name_station = pd.concat([robots_FRC[station], specific_robot], axis=1)
            robot_info_colomn_name_station.rename(columns={station:"team", f'autoTower{station_number[station]}':'autoTower', f'endGameTower{station_number[station]}':'endGameTower'}, inplace=True)
            robots_info_df.append(robot_info_colomn_name_station)
        else:
            specific_robot = df_blue_score[[f'autoTower{station_number[station]}', f'endGameTower{station_number[station]}', 'energizedAchieved', 'superchargedAchieved', 'traversalAchieved', 'rp', 'totalPoints']]
            robot_info_colomn_name_station = pd.concat([robots_FRC[station], specific_robot], axis=1)
            robot_info_colomn_name_station.rename(
                columns={
                    station:"team", 
                    f'autoTower{station_number[station]}':'autoTower', 
                    f'endGameTower{station_number[station]}':'endGameTower'}, 
                inplace=True)
            robots_info_df.append(robot_info_colomn_name_station)
    final_specific_data_teams = pd.concat(robots_info_df, axis=0)
    return final_specific_data_teams