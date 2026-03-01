import pandas as pd

def teams_involved_FRC(response_teams):
    df_md = pd.DataFrame.from_dict(response_teams.json())
    df_md = df_md["Matches"].apply(pd.Series)
    df_teams = df_md["teams"].apply(pd.Series)
    red1 = df_teams[0].apply(pd.Series)
    red2 = df_teams[1].apply(pd.Series)
    red3 = df_teams[2].apply(pd.Series)
    blue1 = df_teams[3].apply(pd.Series)
    blue2 = df_teams[4].apply(pd.Series)
    blue3 = df_teams[5].apply(pd.Series)
    robots_dict = {"Red1":[], "Red2":[], "Red3":[], "Blue1":[], "Blue2":[], "Blue3":[]}
    for r1,r2,r3,r4,r5,r6 in zip(red1.values, red2.values, red3.values, blue1.values, blue2.values, blue3.values):
        robots_dict[r1[1]].append(r1[0])
        robots_dict[r2[1]].append(r2[0])
        robots_dict[r3[1]].append(r3[0])
        robots_dict[r4[1]].append(r4[0])
        robots_dict[r5[1]].append(r5[0])
        robots_dict[r6[1]].append(r6[0])
    robots_FRC = pd.DataFrame.from_dict(robots_dict)
    return robots_FRC