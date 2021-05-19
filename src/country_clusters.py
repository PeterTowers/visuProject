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


# Countries in the same cluster as Brazil on dimensional reduction
def dim_reduct():
    return df[df['iso_code'].isin(["ALB", "BIH", "BRA", "COL", "DZA", "ECU", "IDN",
                                   "LBN", "LKA", "MNG", "PER", "SRB", "TUN", "ZAF"])]


# Countries in the same cluster as Brazil on dimensional reduction
def dim_reduct_sickness():
    return df[df['iso_code'].isin(["QAT", "BRB", "BRA", "SLV", "TUR", "GRC", "MLT",
                                   "SVN", "FIN", "URY", "MEX", "DEU", "USA", "BHR",
                                   "AUT", "CYP"])]


# Countries in the same cluster as Brazil on TSNE-renda
def tsne_revenue():
    return df[df['iso_code'].isin(["LBN", "MKD", "SRB", "DZA", "BRA", "CHN", "DOM",
                                   "IRQ", "THA", "CRI", "BWA", "MNE", "GAB", "BLR",
                                   "MEX", "BGR", "ARG"])]


# Countries in the same cluster as Brazil on TSNE-comorbidades
def tsne_sickness():
    return df[df['iso_code'].isin(["GRC", "TUR", "CUB", "SLV", "BRA", "BRB", "QAT",
                                   "ETH", "CPV", "ARG", "LKA", "PRY", "ZAF", "BRN",
                                   "JAM", "MMR"])]


# General countries picked up from personal interest
def developed():
    return df[df['iso_code'].isin(["AUS", "BEL", "DEU", "ESP", "FRA", "GBR", "ITA", "JPN", "KOR", "NZL", "USA", "SWE"])]
