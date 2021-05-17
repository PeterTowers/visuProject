import pandas as pd

df = pd.read_csv('data/owid_ginada.csv')


# General countries picked up from personal interest
def general():
    return df[df['iso_code'].isin(["BRA", "MEX", "USA", "VNM", "KOR", "CHN", "IND",
                                   "ZAF", "GBR", "NZL", "AUS", "DEU", "FRA", "SWE"])]


# Nordic countries, as defined by Wikipedia's page (Denmark, Finland, Iceland, Norway and Sweden)
def nordic():
    return df[df['iso_code'].isin(["DNK", "FIN", "ISL", "NOR", "SWE"])]


# Countries from the south american continent
def south_america():
    return df[df['continent'].isin(['South America'])]
