import pandas as pd
import requests
import os

def union_match_sd(red_SD_pd, blue_SD_pd, robots):

    os.system("cls")
    os.system("clear")
    print("Creating final table...")

    red_concat = pd.concat([robots[["Red1", "Red2"]], red_SD_pd], axis=1)
    blue_concat = pd.concat([robots[["Blue1", "Blue2"]], blue_SD_pd], axis=1)
    red_concat.replace({"PARTIAL":5, "FULL":10, "NONE":0}, inplace=True)
    blue_concat.replace({"PARTIAL":5, "FULL":10, "NONE":0}, inplace=True)

    Red1_pd = red_concat[["Red1", "autoClassifiedArtifacts", "autoOverflowArtifacts", "robot1Auto", "teleopClassifiedArtifacts", "teleopOverflowArtifacts", "robot1Teleop", "foulPointsCommitted", "movementRP", "goalRP", "patternRP"]]
    Red1_pd.rename({"Red1":"Team", "robot1Auto":"Leave", "robot1Teleop":"Base"}, axis=1, inplace=True)

    Red2_pd = red_concat[["Red2", "autoClassifiedArtifacts", "autoOverflowArtifacts", "robot2Auto", "teleopClassifiedArtifacts", "teleopOverflowArtifacts", "robot2Teleop", "foulPointsCommitted", "movementRP", "goalRP", "patternRP"]]
    Red2_pd.rename({"Red2":"Team", "robot2Auto":"Leave", "robot2Teleop":"Base"}, axis=1, inplace=True)

    Blue1_pd = blue_concat[["Blue1", "autoClassifiedArtifacts", "autoOverflowArtifacts", "robot1Auto", "teleopClassifiedArtifacts", "teleopOverflowArtifacts", "robot1Teleop", "foulPointsCommitted", "movementRP", "goalRP", "patternRP"]]
    Blue1_pd.rename({"Blue1":"Team", "robot1Auto":"Leave", "robot1Teleop":"Base"}, axis=1, inplace=True)

    Blue2_pd = blue_concat[["Blue2", "autoClassifiedArtifacts", "autoOverflowArtifacts", "robot2Auto", "teleopClassifiedArtifacts", "teleopOverflowArtifacts", "robot2Teleop", "foulPointsCommitted", "movementRP", "goalRP", "patternRP"]]
    Blue2_pd.rename({"Blue2":"Team", "robot1Auto":"Leave", "robot1Teleop":"Base"}, axis=1, inplace=True)
    
    allteams = pd.concat([Red1_pd, Red2_pd, Blue1_pd, Blue2_pd], axis=0)
    return (allteams)
    