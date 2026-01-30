import fetchData
from teamsExtractor import teams_extract
from scoreDetailExtract import SD_extract
from tableUnion_M_SD import union_match_sd

def main():
    m_response = fetchData.getInfo("M", 2025, "MXTOQ")
    sd_response = fetchData.getInfo("SD", 2025, "MXTOQ")

    robots = teams_extract(m_response)
    red_sd_tabel, blue_sd_tabel = SD_extract(sd_response)

    print(union_match_sd(red_sd_tabel, blue_sd_tabel, robots))

if __name__ == "__main__":
    main()