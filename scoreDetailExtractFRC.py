import pandas as pd

def SD_extractor_FRC(response_sd):
    df = pd.DataFrame.from_dict(response_sd.json())
    df_sd = df["MatchScores"].apply(pd.Series)
    temp_sd = df_sd["alliances"].apply(pd.Series)
    df_blue_score = temp_sd[0].apply(pd.Series)
    df_red_score = temp_sd[1].apply(pd.Series)
    return df_red_score, df_blue_score