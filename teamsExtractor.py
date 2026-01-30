import pandas as pd
import requests

def teams_extract(matches_respons):
    '''
    From the json of the match response of the FIRST API this function will return a DataFrame of all teams with the colummns of Red2, Red2, Blue1 and Blue2
    and the rows of each match. This only analizes the quals
    
    ## Parameters
    - **matches_respons** *json*\n
    \tThe json of the response of the FIRST API match info

    ## Returns
    - **teams_df** *DataFrame*\n
    \tA dataframe that will contains the 4 columns with their station
    '''
    response_pd = matches_respons.copy()
    response_pd = response_pd["matches"].apply(pd.Series)
    teams = response_pd["teams"].apply(pd.Series)

    robot1 = teams[0].apply(pd.Series)
    robot2 = teams[1].apply(pd.Series)
    robot3 = teams[2].apply(pd.Series)
    robot4 = teams[3].apply(pd.Series)
    robots_dict = {"Red1":[],"Red2":[], "Blue1":[], "Blue2":[]}

    for r1,r2,r3,r4 in zip(robot1.values, robot2.values, robot3.values, robot4.values):
        robots_dict[r1[1]].append(r1[0])
        robots_dict[r2[1]].append(r2[0])
        robots_dict[r3[1]].append(r3[0])
        robots_dict[r4[1]].append(r4[0])
    return(pd.DataFrame.from_dict(robots_dict))