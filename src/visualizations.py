import pandas as pd
import plotly.express as px


# Total covid cases
def total_cases(data):
    return px.line(data, x='date', y='total_cases', color='location')


# Total covid cases per million inhabitants
def total_cases_mil(data):
    return px.line(data, x='date', y='total_cases_per_million', color='location')


# 7 days moving average of new covid cases
def new_cases_smooth_mil(data):
    return px.line(data, x='date', y='new_cases_smoothed_per_million', color='location')


# Total deaths
def total_deaths(data):
    return px.line(data, x='date', y='total_deaths', color='location')


# Total deaths per million inhabitants
def total_deaths_mil(data):
    return px.line(data, x='date', y='total_deaths_per_million', color='location')


# 7 days moving avg. of new deaths
def new_deaths_smooth_mil(data):
    return px.line(data, x='date', y='new_deaths_smoothed_per_million', color='location')


# COVID-19 virus' reproduction rate (R)
def r_rate(data):
    return px.line(data, x='date', y='reproduction_rate', color='location')


# Stringency index as calculated in Oxford COVID-19 Government Response Tracker, Blavatnik School of Government.
# Interval is from 0 to 100, where 100 is the strictest response
def stringency_index(data):
    return px.line(data, x='date', y='stringency_index', color='location')


# Human development index from UNDP
def hdi(data):
    df_hdi = data.drop_duplicates(subset='location')
    df_hdi = df_hdi.dropna(subset=['human_development_index'])

    return px.bar(df_hdi, x='location', y='human_development_index', color='location')


# Gini index from World Bank Open Data
def gini(data):
    df_gini = data.drop_duplicates(subset='location')
    df_gini = df_gini.dropna(subset=['gini'])

    return px.bar(df_gini, x='location', y='gini', color='location')