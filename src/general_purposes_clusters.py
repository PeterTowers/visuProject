import pandas as pd

df = pd.read_csv('data/owid_ginada.csv')


def revenue():
    df_renda = df[['date', 'location', 'continent', 'gdp_per_capita',
                   'life_expectancy', 'hospital_beds_per_thousand',
                   'human_development_index', 'gini']]
    df_renda = df_renda.dropna()
    df_renda = df_renda.drop_duplicates(subset=['location'], keep='last')
    return df_renda


def sickness():
    df_comorb = df[['date', 'location', 'continent', 'cardiovasc_death_rate',
                    'diabetes_prevalence', 'female_smokers', 'male_smokers',
                    'hospital_beds_per_thousand']]
    df_comorb = df_comorb.dropna()
    df_comorb = df_comorb.drop_duplicates(subset=['location'], keep='last')
    return df_comorb

